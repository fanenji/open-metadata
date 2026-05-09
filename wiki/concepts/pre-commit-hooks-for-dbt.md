---
type: concept
title: Pre-commit Hooks for dbt
created: 2026-04-07
updated: 2026-04-07
tags: [dbt, pre-commit, data-quality, automation, ci-cd]
related: [dbt-checkpoint, pre-commit, ci-cd-for-data-pipelines, dbt-slim-ci, dbt-data-contract-implementation, dbt-testing-patterns]
sources: ["dbt-checkpoint.md"]
---
# Pre-commit Hooks for dbt

**Pre-commit hooks for dbt** are automated validations that run before code is committed to version control, checking the quality and consistency of dbt projects. They are implemented primarily through the [[dbt-checkpoint]] tool, which provides 40+ pre-built hooks.

## Purpose

As dbt projects grow, maintaining consistent quality across models, sources, macros, and tests becomes challenging. Pre-commit hooks catch mistakes at commit time, reducing reviewer workload and preventing errors from reaching production.

## Categories of Validation

- **Documentation completeness**: Ensuring models, columns, sources, and macros have descriptions
- **Testing coverage**: Enforcing minimum test counts by name, type, or group
- **Contract enforcement**: Checking that models have contracts, constraints, and column name conventions
- **Structural integrity**: Verifying all columns are documented in properties files, scripts use `ref()` and `source()` macros
- **Naming conventions**: Enforcing model and column name contracts
- **Metadata completeness**: Checking meta keys and labels on models, sources, macros, exposures, seeds, snapshots, and tests
- **Source freshness**: Ensuring sources have freshness configured
- **Lineage validation**: Checking parent/child relationships and database/schema consistency

## Integration Patterns

### Local Development (Pre-commit)
Hooks run automatically on `git commit` after installing via `pre-commit install`. This provides immediate feedback to developers.

### CI/CD Pipeline
For teams using [[dbt-cloud]], dbt-checkpoint cannot run natively. Instead, hooks run after push via GitHub Actions (or similar CI). This requires:
1. Generating `manifest.json` via `dbt parse`
2. Providing database credentials via GitHub Secrets
3. Configuring a workflow that runs hooks against changed files

## Relationship to Other Quality Mechanisms

- **[[dbt-slim-ci]]**: Complementary — pre-commit hooks run at commit time, Slim CI runs at PR time
- **[[dbt-data-contract-implementation]]**: Several hooks directly enforce contract patterns
- **[[dbt-testing-patterns]]**: Hooks enforce testing coverage requirements
- **[[dbt-observability-implementation]]**: Pre-commit is pre-run, observability is post-run — together they form a complete quality lifecycle

## Limitations

- **dbt Cloud incompatibility**: Cannot run natively with dbt Cloud
- **Manifest dependency**: Most hooks require `manifest.json`, requiring a database connection
- **False sense of security**: Hooks that run in CI (not truly at commit time) may give developers a false sense of local validation