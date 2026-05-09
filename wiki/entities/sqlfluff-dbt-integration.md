---
type: entity
title: SQLFluff dbt Integration
created: 2026-04-29
updated: 2026-04-29
tags: [sqlfluff, dbt, linting, ci-cd]
related: [dbt-core-slim-ci-implementation, dbt-ci-testing-strategy, dbt-pre-commit-patterns]
sources: ["How to Create CI-CD Pipelines for dbt Core.md"]
---
# SQLFluff dbt Integration

SQLFluff is a SQL linter that can be integrated with dbt projects in CI/CD pipelines. The `diff-quality` command enables linting only on modified models, making it suitable for incremental CI/CD workflows.

## Key Features

- `diff-quality --violations sqlfluff --compare-branch origin/master --fail-under 100` — lints only changed SQL files.
- Works well with the Slim CI pattern by targeting only modified dbt models.
- Can be used as a pre-commit hook or CI/CD step.

## Warning

If SQLFluff is not already in use across the codebase, introducing it in CI/CD will flag legacy code issues, potentially blocking pipelines. Teams should uplift existing SQL code first or use a phased adoption approach.

## Related

- [[dbt-core-slim-ci-implementation]] — The CI/CD pattern where SQLFluff is a recommended enhancement.
- [[dbt-pre-commit-patterns]] — Broader pattern of pre-commit hooks in dbt workflows.