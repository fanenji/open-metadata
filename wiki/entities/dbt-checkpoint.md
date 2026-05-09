---
type: entity
title: dbt-checkpoint
created: 2026-04-07
updated: 2026-05-07
tags: [dbt, pre-commit, data-quality, ci-cd, open-source, documentation]
related: [datacoves, pre-commit, ci-cd-for-data-pipelines, dbt-slim-ci, dbt-data-contract-implementation, dbt-testing-patterns, dbt-observability-implementation, dbt-core-slim-ci-implementation, dbt-ci-testing-strategy, dbt-pre-commit-patterns, dbt-ci-documentation-gate, dbt-workflow]
sources: ["dbt-checkpoint.md", "How to Create CI-CD Pipelines for dbt Core.md", "SCRIPT ESECUZIONE DBT.md"]
---
# dbt-checkpoint

**dbt-checkpoint** is an open-source tool that provides a comprehensive set of [pre-commit](https://pre-commit.com/) hooks for ensuring the quality of [dbt](https://www.getdbt.com/) projects. Maintained by [[Datacoves]], it serves as a CI/CD gatekeeper for both data quality test coverage and documentation standards, blocking merge requests when required tests or descriptions are missing and preventing untested or undocumented code from reaching production.

## Purpose

As dbt projects grow in size and complexity, maintaining consistent quality across models, sources, macros, and tests becomes challenging. dbt-checkpoint automates validation checks that run before code is committed, catching mistakes early and reducing reviewer burden. It enforces key data quality dimensions—uniqueness, completeness, validity, timeliness, and relevance—by ensuring appropriate generic tests (e.g., `unique`, `not_null`, `accepted_values`) are configured. Additionally, it enforces documentation quality by verifying that models, columns, and other project resources have proper descriptions and metadata.

## Hook Catalog

dbt-checkpoint offers 40+ hooks organized into the following categories:

- **Model checks**: Validate model descriptions, column descriptions, contracts, constraints, tests, naming conventions, tags, materialization, and parent/child relationships
- **Source checks**: Validate source descriptions, column descriptions, freshness, loader, tests, tags, and child relationships
- **Script checks**: Validate SQL scripts for semicolons, table name usage, and ref/source references
- **Macro checks**: Validate macro descriptions, argument descriptions, and meta keys
- **Exposure checks**: Validate exposure meta keys
- **Seed checks**: Validate seed meta keys
- **Snapshot checks**: Validate snapshot meta keys
- **Test checks**: Validate singular test meta keys
- **Modifiers**: Auto-generate missing sources, model properties files, unify column descriptions, replace table names with ref/source macros
- **dbt commands**: Run `dbt clean`, `dbt compile`, `dbt deps`, `dbt docs generate`, `dbt parse`, `dbt run`, `dbt test` as pre-commit steps

Many of the model and source hooks specifically verify that generic tests (such as `unique`, `not_null`, `accepted_values`) are defined, thereby enforcing data quality test coverage. Documentation hooks check that descriptions are present on models and columns.

## Usage in CI/CD

dbt-checkpoint can be used both as a local pre-commit hook and as a step in CI/CD pipelines. When integrated into CI/CD jobs, it acts as a blocking gate: if the checks fail, the merge request is blocked and deployment to staging/production is prevented. This enforces quality standards at the deployment boundary rather than during development.

- **Local development**: Pre-commit runs non-blocking checks (warnings only).
- **CI/CD**: dbt-checkpoint runs as a blocking gate, ensuring every modified model has the required data quality tests and documentation before code is merged. It is particularly recommended in patterns such as [[dbt-core-slim-ci-implementation]] as a means to enforce quality gates.

## Configuration

Hooks are configured in a `.pre-commit-config.yaml` file. Global settings (project root, telemetry opt-out) are set in `.dbt-checkpoint.yaml`.

## Relationship to Local Pre-commit

In local development, pre-commit hooks typically run non-blocking checks that warn but do not block commits. In CI/CD, dbt-checkpoint is configured as a blocking gate that prevents deployment if documentation or test standards are not met. This ensures that quality requirements are enforced at the point of merge, while allowing flexibility during development.

## Limitations

- **dbt Cloud incompatibility**: Cannot be used natively with dbt Cloud; requires running checks after push via GitHub Actions
- **Manifest dependency**: Most hooks require `manifest.json`, requiring `dbt parse` to run first
- **Telemetry**: Built-in anonymous usage tracking (opt-out available)

## Repository

- GitHub: [dbt-checkpoint/dbt-checkpoint](https://github.com/dbt-checkpoint/dbt-checkpoint/tree/main?tab=readme-ov-file#run-in-cicd)

## Related Concepts

- [[ci-cd-for-data-pipelines]] — dbt-checkpoint is a concrete implementation of CI/CD for dbt
- [[dbt-slim-ci]] — Complementary commit-time vs. PR-time validation
- [[dbt-data-contract-implementation]] — Hooks enforce contract patterns
- [[dbt-testing-patterns]] — Hooks enforce testing coverage
- [[dbt-observability-implementation]] — Relates to monitoring data quality
- [[dbt-core-slim-ci-implementation]] — CI/CD pattern where dbt-checkpoint is a recommended enhancement
- [[dbt-ci-testing-strategy]] — Broader strategy for testing in CI
- [[dbt-pre-commit-patterns]] — Broader pattern of pre-commit hooks in dbt workflows
- [[dbt-ci-documentation-gate]] — Pattern this tool implements for documentation quality gates
- [[dbt-workflow]] — Proposed orchestration tool that would precede this gate