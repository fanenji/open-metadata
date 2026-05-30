---
type: entity
title: Profiler Metrics
created: 2026-05-14
updated: 2026-05-14
tags: [profiler, metrics, data-quality, data-profiling, sqlalchemy]
related: [data-profiling, data-quality, system-metrics, profiler-workflow, jsonschemas, snowflake, openmetadata]
sources: ["metrics-openmetadata-profiler-metrics-guide---open-20260514.md"]
---
# Profiler Metrics

Profiler Metrics are the fundamental building blocks of OpenMetadata's [[data-profiling]] system. A **Metric** is a computation on a Table or Column that returns a value. Metrics are defined generically via SQLAlchemy expressions for cross-database portability, not as database-specific queries.

A **Profiler** is the binding between a set of metrics and the external world — it contains the Table and Session information and is responsible for executing the metrics.

## Metric Categories

### Table Metrics

Computed at the table level:

- **Row Count** — The number of rows in the table.
- **Column Count** — The number of columns in the table.

### System Metrics

System metrics provide information about DML operations (INSERT, UPDATE, DELETE) performed on a table, offering a concise view of data freshness. These metrics are available **only** for Snowflake, Redshift, and BigQuery. For other database engines, system metric computation is skipped.

- **DML Operations** — Timeseries of all DML operations performed against the table.
- **Rows Affected by the DML Operation** — Number of rows affected by each DML operation over time.

OpenMetadata looks at the past 24 hours (Snowflake) or the previous day (Redshift, BigQuery) to fetch operations.

### Column Metrics

List of metrics run for all columns. Complex types such as ARRAY and STRUCT are **not supported** (future implementation noted).

| Metric | Description | Type Support |
|--------|-------------|--------------|
| Values Count | Total count of non-null values | All |
| Values Percentage | Percentage of non-null values vs. Row Count | All |
| Duplicate Count | `count(col) - count(distinct(col))` | All |
| Null Count | Number of null values | All |
| Null Proportion | Ratio of null values vs. total values | All |
| Unique Count | Number of values appearing only once | All |
| Unique Proportion | Unique Count / Values Count | All |
| Distinct Count | Number of different items | All |
| Distinct Proportion | Distinct Count / Values Count | All |
| Min | Minimum value | Numerical only |
| Max | Maximum value | Numerical only |
| Min Length | Minimum length of values | Concatenable only |
| Max Length | Maximum length of values | Concatenable only |
| Mean | Average of values (numerical) or average length (concatenable) | Numerical, Concatenable |
| Median | Middle value | Numerical only (not supported in MySQL) |
| Sum | Sum of all values | Numerical only |
| Standard Deviation | Standard deviation of values | Numerical only |
| Histogram | Dictionary of bins and counts; requires Inter Quartile Range | Numerical only |
| First Quartile | Middle number between smallest value and median | Numerical only |
| Third Quartile | Middle number between median and greatest value | Numerical only |
| Inter Quartile Range | Third Quartile - First Quartile | Numerical only |
| Nonparametric Skew | Skewness: `(mean - median) / standard deviation` | Numerical only |

## JSON Schema Definition

The metric definitions are based on the `columnProfile` JSON Schema. See the [columnProfile definition](https://github.com/open-metadata/OpenMetadata/blob/main/openmetadata-spec/src/main/resources/json/schema/dataInsight/type/columnProfile.json) and the [metric implementations](https://github.com/open-metadata/OpenMetadata/tree/main/ingestion/src/metadata/profiler/metrics).

## Grant Access for System Metrics

### Snowflake
- Uses `QUERY_HISTORY_BY_WAREHOUSE` view of `INFORMATION_SCHEMA` and `RESULT_SCAN` function.
- The DDL query must include database, schema, and table name for matching.

### Redshift
- Provisioned Cluster: `SVV_TABLE_INFO`, `STL_INSERT`, `STL_DELETE`, `STL_QUERYTEXT`.
- Serverless: `SYS_QUERY_DETAIL`.

### BigQuery
- Uses `INFORMATION_SCHEMA.JOBS` table.
- Data location must be properly set in the BigQuery service connection.

## Related Pages

- [[data-profiling]] — High-level concept of data profiling in OpenMetadata.
- [[data-quality]] — Data quality tests built on top of profiler metrics.
- [[system-metrics]] — Detailed page on System Metrics (DML operations, freshness monitoring).
- [[profiler-workflow]] — How the Profiler binds metrics to tables and executes them.
- [[jsonschemas]] — JSON Schema definitions for metadata entities.