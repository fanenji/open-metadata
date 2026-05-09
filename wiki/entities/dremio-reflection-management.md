type: entity
title: Dremio Reflection Management
created: 2026-05-07
updated: 2026-05-07
tags: [dremio, reflections, performance, materialization]
related: [dremio, dremio-semantic-layer-ci-cd, dremio-dbt-connector-configuration, dbt-dremio-adapter]
sources: ["semantic-layer-ci-cd-with-dremio-and-dbt.pdf"]
---
# Dremio Reflection Management

Reflections are Dremio's hybrid materialization mechanism, sitting between traditional ETL-style materializations and virtualized views. They accelerate query performance by pre-computing and caching data.

## Reflection Types

- **Aggregate reflections**: Pre-compute aggregations on specified dimensions and measures
- **Raw reflections**: Cache raw data for faster scans
- **Dimension reflections**: Optimize for dimension-based filtering

## Deployment via dbt

Reflections can be defined in dbt models using the `reflection` materialization type:

```sql
{{ config(
    materialized='reflection',
    reflection_type='aggregate',
    dimensions=['passenger_count'],
    measures=['trip_distance_mi'],
    computations=['COUNT,SUM']
) }}
-- depends_on: {{ ref('nyc_taxi_trips') }}
```

## Deployment Trade-offs

**Arguments FOR including reflections in CI/CD:**
- Changes to transformation logic may affect materialized data downstream
- Consistent deployment of views and their reflections
- Single source of truth for the semantic layer

**Arguments AGAINST including reflections in CI/CD:**
- Reflection creation can be expensive (long-running jobs)
- May slow down frequent CI/CD pipelines
- Better governed by separate ETL-style batch workflows

## Best Practices

- Use the dbt connector's built-in reflection materialization type, not raw SQL via post-hooks
- Enable reflections via `dremio:reflections_enabled: true` in `dbt_project.yml`
- Consider separate deployment pipelines for reflections vs. views/tables
- Monitor reflection creation time and resource usage
