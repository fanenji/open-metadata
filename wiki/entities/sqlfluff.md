---
type: entity
title: SQLFluff
created: 2026-04-29
updated: 2026-05-07
tags: ["tool", "sql", "linting", "dbt", "ci-cd"]
related: ["sqlfluff-dbt-linting", "dbt-ci-cd-github-actions", "implementing-cicd-for-dbt-first-steps", "blablacar", "dev-containers-for-dbt", "ci-cd-for-data-pipelines"]
sources: ["Implementing CICD for dbt First Steps.md", "Scaling Success The dbt Ecosystem at BlaBlaCar.md"]
---
# SQLFluff

SQLFluff is a popular open-source SQL linter and formatter optimized for data workflows. It integrates with [[dbt]] by supporting a dbt templater that understands dbt's Jinja syntax. SQLFluff can check for issues such as improper indentation, non‑descriptive naming, overly complex SQL logic, and unoptimized join patterns. Configuration is done via a `.sqlfluff` file in the project root, and a `.sqlfluffignore` file can exclude folders like `analysis/`, `macros/`, `dbt_packages/`, and `target/`.

At [[BlaBlaCar]], SQLFluff is included in the [[dev-containers-for-dbt]] configuration and used as part of the CI/CD pipeline for automated code quality checks on every pull request. It enforces SQL style and formatting standards across all dbt projects in their mono‑repo.

## Basic Configuration

```ini
[sqlfluff]
templater = dbt
dialect = snowflake
```

## Usage in CI/CD

SQLFluff is typically run as a job in a [[GitHub Actions]] workflow to enforce code quality. In a mono‑repo setup (as at BlaBlaCar), it can be configured to run against all dbt projects, ensuring consistent formatting across the entire codebase.