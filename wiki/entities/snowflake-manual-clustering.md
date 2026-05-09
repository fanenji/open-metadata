---
type: entity
title: Snowflake Manual Clustering
created: 2026-05-07
updated: 2026-05-07
tags: [snowflake, performance, clustering, dbt]
related: [geospatial-analytics-with-dbt, snowflake-zero-copy-clone, dbt-insert-by-period]
sources: ["Complex geospatial analytics with dbt - Summary-20260507.md"]
---
# Snowflake Manual Clustering

Snowflake Manual Clustering allows explicit definition of clustering keys to optimize partition pruning for large tables with predictable query patterns.

## Usage in dbt

```sql
{{ config(
    materialized='incremental',
    cluster_by=['operating_system', 'DATE(ride_start_at)']
) }}
```

## When to Use

- Query patterns are highly predictable (consistent filter columns)
- Table is very large and filter pruning is impactful

## When to Avoid

- Ad-hoc, unpredictable query patterns — manual clustering can hurt performance in those cases

> Manual clustering pairs extremely well with incremental materialization.