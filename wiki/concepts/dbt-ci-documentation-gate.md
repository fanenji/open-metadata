---
type: concept
title: dbt CI/CD Documentation Gate
created: 2026-01-15
updated: 2026-01-15
tags: [dbt, ci-cd, documentation, quality-gate]
related: [dbt-checkpoint, dbt-pre-commit-patterns, ci-cd-for-data-pipelines, dbt-osmosis, dbt-workflow]
sources: ["SCRIPT ESECUZIONE DBT.md"]
---
# dbt CI/CD Documentation Gate

A pattern for enforcing documentation quality in dbt projects at the CI/CD boundary, rather than during development. This addresses the constraint that [[dbt-osmosis]] requires prior `dbt build` execution, making it impractical to block builds during development for documentation reasons.

## Rationale

- `dbt-osmosis yaml refactor` requires a completed `dbt build` to function.
- Blocking the build during development would prevent developers from iterating.
- Documentation enforcement is deferred to the CI/CD pipeline, where it can block merge requests.

## Implementation

- **Tool**: [[dbt-checkpoint]] provides pre-commit hooks for CI/CD.
- **Behavior**: If documentation standards are not met, the merge request is blocked.
- **Effect**: Prevents deployment of undocumented or poorly documented models to staging/production environments.

## Workflow

1. **Development**: Developer runs `dbt build` → `dbt-osmosis yaml refactor` → `dbt docs generate` → `pre-commit` (non-blocking).
2. **CI/CD**: On commit/push, dbt-checkpoint runs as a blocking pre-commit hook.
3. **Gate**: If dbt-checkpoint fails, the merge request is rejected.

## Related

- [[dbt-checkpoint]] — the tool that implements this gate
- [[dbt-pre-commit-patterns]] — broader pre-commit patterns in dbt
- [[CI-CD-for-data-pipelines]] — general CI/CD practices for data pipelines
- [[dbt-osmosis]] — the tool that creates the constraint this pattern addresses