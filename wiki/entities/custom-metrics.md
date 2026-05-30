---
type: entity
title: Custom Metrics
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, data-profiling, data-quality, custom-metrics]
related: [data-profiling, data-quality, profiler-agent, metadata-agent, data-observability-alerts, ingestion-framework]
sources: ["custom-metrics---openmetadata-documentation-20260514.md"]
---
# Custom Metrics

**Custom Metrics** is a feature in [[OpenMetadata]] that enables users to define and compute business-specific metrics using custom SQL queries during the profiling workflow. They extend the built-in profiler metrics and are displayed alongside system metrics in table and column profiles.

## Overview

Custom metrics provide a flexible way to track specific data insights tailored to organizational needs. They are defined at either the table level or column level and are executed by the [[profiler-agent]] as part of the profiling pipeline. Once computed, their values appear in the Table Profile and Column Profile UI views.

## Types

### Table-Level Custom Metrics
- SQL queries that aggregate over an entire table.
- Defined via the Table Profile UI in the Data Observability tab.
- Example: Row count for a specific condition, sum of values in a filtered set.

### Column-Level Custom Metrics
- SQL queries scoped to a single column.
- Defined via the Column Profile UI with column selection.
- Example: Percentage of nulls in a specific category, distinct count for a filtered subset.

## Workflow

1. **Define:** Navigate to the Database → Data Observability tab → Table Profile or Column Profile → Add → Custom Metric. Provide a name and SQL query.
2. **Execute:** Run the Profiler Agent in the Database Services.
3. **View:** Return to the same dataset to see the computed custom metric in the profile.

## Operational Considerations

- The Profiler Agent must be run after defining a custom metric to compute its value.
- SQL syntax support is not explicitly documented; standard SQL compatible with the target database is recommended.
- Performance implications of complex queries are not documented; users should test queries for efficiency.
- Error handling for invalid SQL queries is not specified; validation is assumed to occur at execution time.

## Open Questions

- What SQL syntax is supported? (Standard SQL? Dialect-specific?)
- Are there performance or security guardrails for custom SQL queries?
- Can custom metrics be reused across multiple tables/columns or shared between users?
- How are custom metrics handled during re-profiling or schema changes?

## Related Pages

- [[data-profiling]] — Core profiling concepts and built-in metrics.
- [[data-quality]] — Data quality testing and domain-specific checks.
- [[profiler-agent]] — The execution engine for profiling workflows.
- [[metadata-agent]] — Configurable pipelines for metadata extraction.
- [[data-observability-alerts]] — Alerts for data quality and schema changes.