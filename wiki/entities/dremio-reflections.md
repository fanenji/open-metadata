---
type: entity
title: Dremio Reflections
created: 2026-05-06
updated: 2026-05-06
tags: [dremio, reflections, materialization, performance]
related: [dremio, dremio-semantic-layer-ci-cd, dbt-dremio-adapter, CI-CD-for-data-pipelines]
sources: ["Semantic Layer CI-CD with Dremio and dbt.md"]
---
# Dremio Reflections

Reflections are Dremio-specific materialized acceleration objects that serve as a hybrid between traditional ETL-style materialization and the virtualized, view-centric approach at the heart of Dremio's semantic layer philosophy. They enable fast query response times on data lake queries.

## Management in dbt

Reflections can be managed via the Dremio dbt connector's built-in materialization type. To enable reflections in dbt, set the following variable in `dbt_project.yml`:

```yaml
vars:
  dremio:reflections_enabled: true
```

Reflections are defined in dbt models using the `materialized='reflection'` configuration, with parameters for reflection type (aggregate, raw), dimensions, measures, and computations.

## CI/CD Trade-offs

There are arguments for and against including reflections in CI/CD pipelines:

- **For**: Creating reflections goes hand-in-hand with view definitions; changes to transformation logic can impact materialized data downstream.
- **Against**: Reflection creation can be expensive and may be more economical to govern via a separate ETL-style batch workflow rather than slowing down frequent CI/CD deployments.

The document recommends using the dbt connector's built-in reflection materialization type rather than raw SQL via post-hooks when including reflections in dbt models.