---
type: concept
title: dbt CI/CD with GitHub Actions
created: 2026-04-29
updated: 2026-04-29
tags: [dbt, ci-cd, github-actions, automation]
related: [ci-cd-for-data-pipelines, dbt-slim-ci, dbt-cloud-environments, dbt-testing-patterns, sqlfluff-dbt-linting, piperider-dbt-impact-analysis, dbt-staging-production-environments, github-actions, sqlfluff, piperider, implementing-cicd-for-dbt-first-steps]
sources: ["Implementing CICD for dbt First Steps.md"]
---
# dbt CI/CD with GitHub Actions

A practical pattern for setting up continuous integration and continuous delivery for [[dbt]] projects using [[GitHub Actions]]. This approach is recommended by [[Jens Wilms]] as a starting point for data teams, emphasizing a "start small" philosophy.

## Core Components

1. **CI/CD Platform**: [[GitHub Actions]] with workflow files in `.github/workflows/`.
2. **Environments**: Separate staging and production environments for validation vs. deployment.
3. **Linting**: [[SQLFluff]] for enforcing SQL code style and best practices.
4. **Testing**: dbt's built-in test framework (`dbt test`) for data validation.
5. **Impact Analysis**: [[PipeRider]] for automated downstream impact assessment.

## Basic Workflow Structure

```yaml
name: dbt CI/CD
on:
  pull_request:
    branches:
    - staging
jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Install SQLFluff
        run: pip install sqlfluff sqlfluff-templater-dbt
      - name: Run SQLFluff
        run: sqlfluff lint models/
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Run dbt tests
        run: dbt test
  piperider-compare:
    runs-on: ubuntu-latest
    permissions:
      pull-requests: write
    steps:
      - uses: actions/checkout@v3
      - name: PipeRider Compare
        uses: InfuseAI/piperider-compare-action@v1
```

## Relationship to Other Patterns

- **vs. [[dbt-slim-ci]]**: This pattern runs all tests on every PR, while Slim CI runs only changed models and their dependencies. The article acknowledges Slim CI as an optimization for later stages.
- **vs. [[dbt-cloud-environments]]**: This pattern uses GitHub Actions for environment management, while dbt Cloud provides native environment configuration.
- **vs. [[dbt-pre-commit-patterns]]**: This pattern moves linting to the CI pipeline rather than pre-commit hooks.