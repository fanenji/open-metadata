---
type: concept
title: dbt Artifact Query History Join
created: 2026-04-07
updated: 2026-04-07
tags: [dbt, observability, performance, snowflake]
related: [dbt-artifacts, dbt-observability-implementation, dbt-domain-alerting-pattern, dbt-jinja-variables]
sources: ["Observability within dbt.md"]
---
# dbt Artifact Query History Join

The dbt Artifact Query History Join is a pattern for combining dbt artifact metadata (from run_results.json and manifest.json) with data warehouse query history to gain deeper performance insights than artifacts alone can provide.

## How It Works

1. **Artifact Loading**: dbt artifacts are loaded into the data warehouse using a dbt macro (PUT → COPY → REMOVE pattern) executed via a run operation after every dbt command.
2. **Modeling**: dbt models parse the nested JSON artifacts into structured tables.
3. **Join**: The parsed artifact tables are joined with the warehouse's query history table (e.g., Snowflake's `QUERY_HISTORY` view) using query IDs or timestamps.
4. **Insights**: The combined view surfaces metrics such as:
   - Credit usage per model
   - Bytes spilled to disk
   - Warehouse sizing per model
   - Percentage of partition scan
   - Bytes sent over the network

## Applications

- **Materialization decisions**: Long-running models may benefit from incremental or insert strategies.
- **Clustering optimization**: High partition scan percentages suggest clustering improvements.
- **Warehouse sizing**: Frequent spillage indicates a need for larger warehouses.
- **Time-series performance tracking**: Monitor model execution growth over time to identify degradation.

## Relationship to Other Patterns

This pattern complements [[dbt-observability-implementation]] (which focuses on on-run-end hooks and Jinja variables) by providing a richer data source for performance analysis. It was pioneered by [[Kevin Chan]] and [[Jonathan Talmi]] at [[Snapcommerce]] and presented at Coalesce 2021.