---
type: concept
title: System Metrics
created: 2026-05-14
updated: 2026-05-14
tags: [profiler, metrics, data-freshness, dml, snowflake, redshift, bigquery]
related: [profiler-metrics, data-profiling, data-quality, snowflake]
sources: ["metrics-openmetadata-profiler-metrics-guide---open-20260514.md"]
---
# System Metrics

System Metrics are a category of [[profiler-metrics]] that provide information about DML operations (INSERT, UPDATE, DELETE) performed on a table. They offer a concise view of **data freshness** — monitoring when specific operations were last performed and how many rows they affected.

## Available Metrics

- **DML Operations** — Timeseries of all DML operations (INSERT, UPDATE, DELETE) performed against the table.
- **Rows Affected by the DML Operation** — Number of rows affected by each DML operation over time.

## Supported Database Engines

System Metrics are available **only** for the following engines:

- **Snowflake** — Uses `QUERY_HISTORY_BY_WAREHOUSE` view and `RESULT_SCAN` function. Looks at the past 24 hours.
- **Redshift** — Uses `SVV_TABLE_INFO`, `STL_INSERT`, `STL_DELETE`, `STL_QUERYTEXT` (Provisioned Cluster) or `SYS_QUERY_DETAIL` (Serverless). Looks at the previous day.
- **BigQuery** — Uses `INFORMATION_SCHEMA.JOBS` table. Looks at the previous day, filtering on `creation_time` partition.

For all other database engines, system metric computation is **skipped**.

## Grant Access Requirements

Each engine requires specific permissions on system tables/views. See the [[profiler-metrics]] page for detailed grant instructions.

## Relationship to Data Profiling

System Metrics extend [[data-profiling]] by adding operational context to profile data. While column and table metrics describe the static state of data, system metrics describe how data changes over time, enabling freshness monitoring and operational observability.

## Open Questions

- Are there plans to support System Metrics for other database engines (e.g., PostgreSQL, Oracle)?
- How do System Metrics interact with [[data-observability-alerts]] for freshness monitoring?