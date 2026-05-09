type: concept
title: Dremio Reflection Deployment Trade-offs
created: 2026-05-07
updated: 2026-05-07
tags: [dremio, reflections, deployment, ci-cd, performance]
related: [dremio, dremio-reflection-management, dremio-semantic-layer-ci-cd, CI-CD-for-data-pipelines]
sources: ["semantic-layer-ci-cd-with-dremio-and-dbt.pdf"]
---
# Dremio Reflection Deployment Trade-offs

Reflections are a hybrid materialization mechanism in Dremio that accelerate query performance. Their deployment in a CI/CD pipeline involves significant trade-offs.

## Arguments for Including Reflections in CI/CD

- **Consistency**: Changes to transformation logic may affect materialized data downstream
- **Single source of truth**: Views and their reflections are deployed together
- **Automated coordination**: DAG ordering ensures reflections are created after dependent views

## Arguments Against Including Reflections in CI/CD

- **Expensive creation**: Reflection creation can be a very resource-intensive job
- **Pipeline slowdown**: Frequent CI/CD deployments may be slowed by reflection creation
- **Separate governance**: Reflections may be better governed by a separate ETL-style batch workflow

## Recommendation

The document does not take a definitive stance but presents both perspectives. The choice depends on:
- Frequency of deployments
- Cost of reflection creation
- Tolerance for pipeline latency
- Organizational separation of concerns

If reflections are included in the main dbt model, use the dbt connector's built-in reflection materialization type rather than raw SQL via post-hooks.
