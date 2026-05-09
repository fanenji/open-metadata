---
type: entity
title: Paul Fry
created: 2026-04-29
updated: 2026-04-29
tags: [author, dbt, data-architecture]
related: [dbt-core-slim-ci-implementation, dbt-slim-ci, dbt-checkpoint, sqlfluff-dbt-integration, data-diff-dbt]
sources: ["How to Create CI-CD Pipelines for dbt Core.md"]
---
# Paul Fry

Welsh data architect based in Dublin, certified in dbt, Airflow, Snowflake, and AWS. Author of the practical guide "How to Create CI/CD Pipelines for dbt Core" which details replicating dbt Cloud's Slim CI pattern in dbt Core.

## Contributions

- Published a step-by-step guide on implementing Slim CI in dbt Core using `state:modified` and `defer` flags.
- Proposed enhancement candidates for dbt CI/CD pipelines: SQLFluff, Git standards enforcement, dbt-checkpoint, and data-diff.
- Highlighted operational challenges such as manifest storage strategy and the `defer` + `dbt ls` incompatibility.

## Related

- [[dbt-core-slim-ci-implementation]] — The dedicated page for the implementation pattern he described.
- [[dbt-slim-ci]] — The broader Slim CI concept he operationalized for dbt Core.