---
type: concept
title: dbt Slim CI Strategy
created: 2026-05-06
updated: 2026-05-06
tags: [dbt, cicd, optimization]
related: [dbt-advanced-patterns, infrastructure-architecture]
sources: ["Beyond Basics 7 Advanced dbt Patterns for Production-Grade Pipelines.md"]
---
# dbt Slim CI Strategy

**Slim CI** is an advanced dbt pattern used within CI/CD pipelines to optimize the testing and deployment process.

## Mechanism
Instead of running the entire dbt project for every Pull Request, Slim CI utilizes the `state:modified` flag. By comparing the current state of the code against a "state" manifest from a previous production run, dbt identifies only the models that have been changed or are downstream of changed models.

## Benefits
*   **Reduced Compute Costs**: Minimizes the amount of data processed during the CI phase.
*    **Faster Feedback Loops**: Significantly reduces the time engineers wait for CI pipelines to complete.
* **Efficiency**: Prevents redundant testing of stable, unchanged models.

## Implementation Requirements
*   **State Manifest**: Access to the `manifest.json` from the last successful production run.
*   **CI/CD Integration**: A robust orchestration layer (e.g., GitLab CI, Kestra) capable of downloading the production artifacts and executing the `dbt test --select state:modified+` command.
