---
type: entity
title: dbt-dry-run
created: 2026-04-04
updated: 2026-05-07
tags: ["package", "dbt", "ci-cd", "bigquery", "testing", "production-readiness"]
related: ["dbt-migration-strategy", "dbt-developer-experience", "blablacar", "dbt-preflight-validation", "dbt-slim-ci", "bigquery", "ci-cd-for-data-pipelines", "dbt-project-scaffolding"]
sources: ["One Thousands and One dbt Models How BlaBlaCar Moved to dbt in 12 months.md", "One Thousands and One dbt Models How BlaBlaCar Moved to dbt in 12 months - Summary.md", "Scaling Success The dbt Ecosystem at BlaBlaCar.md"]
---
# dbt-dry-run

`dbt-dry-run` is an open-source dbt package and CI gate technique used by [[blablacar]] to validate dbt models before execution. It sends compiled SQL to BigQuery's dry-run API, which returns estimated bytes processed and validates syntax, reference resolution, column existence, and permissions without actually running the query. It forms part of the [[dbt-developer-experience]] tooling, enabling safe and efficient code releases.

## Key Characteristics

- **Zero cost**: The BigQuery dry-run API is free.
- **Catches errors early**: Syntax errors, missing references, missing columns, insufficient permissions, and expensive queries are identified before deployment.
- **Mandatory CI gate**: No model merges to production without a successful dry-run.

## CI/CD Integration

At [[BlaBlaCar]], `dbt-dry-run` is integrated into the CI/CD pipeline as a mandatory pre-deployment check before any dbt model can be merged to production. It validates:

- SQL syntax correctness
- Reference resolution (all `ref()` and `source()` calls resolve correctly)
- Column existence
- Permissions
- Estimated query cost (bytes processed)

This approach catches common mistakes such as missing commas and other syntax errors, providing rapid feedback to developers. It is part of a broader set of [[ci-cd-for-data-pipelines]] checks that also include linting, tag enforcement, and DAG load validation.

## Related Concepts

- [[dbt-preflight-validation]] — Broader category of pre-execution validation techniques.
- [[dbt-slim-ci]] — CI/CD strategy for running only changed models.
- [[double-run-validation]] — Migration-specific validation pattern that complements dry-run.
- [[dbt-migration-strategy]] — Overall approach for moving to dbt, where dry-run plays a key role.
- [[ci-cd-for-data-pipelines]] — Broader CI/CD pipeline for data.
- [[dbt-project-scaffolding]] — Project structure and organization.