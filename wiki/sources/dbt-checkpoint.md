---
type: source
title: dbt-checkpoint
created: 2026-04-07
updated: 2026-04-07
tags: [dbt, ci-cd, data-quality, pre-commit]
related: [dbt-checkpoint, ci-cd-for-data-pipelines, dbt-slim-ci, dbt-data-contract-implementation, dbt-testing-patterns, dbt-observability-implementation, datacoves, pre-commit]
sources: ["dbt-checkpoint.md"]
---
# dbt-checkpoint

## Source Overview

**dbt-checkpoint** is an open-source tool providing a comprehensive set of [pre-commit](https://pre-commit.com/) hooks to ensure the quality of [dbt](https://www.getdbt.com/) projects. It is maintained by [Datacoves](https://datacoves.com/), a managed DataOps platform for dbt and Airflow.

The tool addresses the challenge of maintaining consistent quality across dbt projects as they grow in complexity. Without automation, reviewers face increased workload and unintentional errors may be missed. dbt-checkpoint allows organizations to add automated validations that run before code is committed, improving the code review and release process.

## Key Features

- **40+ pre-built hooks** organized by category: model, source, script, macro, exposure, seed, snapshot, and test checks
- **Modifiers** that can auto-generate missing sources, model properties files, and unify column descriptions
- **dbt command hooks** for running `dbt parse`, `dbt compile`, `dbt test`, and other commands as pre-commit steps
- **Configurable** via `.dbt-checkpoint.yaml` for project root and telemetry settings
- **CI/CD integration** via GitHub Actions (or similar) for teams using dbt Cloud

## Hook Categories

| Category | Example Hooks |
|----------|---------------|
| Model checks | `check-model-has-contract`, `check-model-has-tests`, `check-column-name-contract`, `check-model-has-description` |
| Source checks | `check-source-has-description`, `check-source-has-freshness`, `check-source-has-tests` |
| Script checks | `check-script-semicolon`, `check-script-has-no-table-name`, `check-script-ref-and-source` |
| Macro checks | `check-macro-has-description`, `check-macro-arguments-have-desc` |
| Exposure checks | `check-exposure-has-meta-keys` |
| Seed checks | `check-seed-has-meta-keys` |
| Snapshot checks | `check-snapshot-has-meta-keys` |
| Test checks | `check-test-has-meta-keys` |
| Modifiers | `generate-missing-sources`, `generate-model-properties-file`, `unify-column-description` |
| dbt commands | `dbt-parse`, `dbt-compile`, `dbt-docs-generate`, `dbt-test` |

## Limitations

- **dbt Cloud incompatibility**: Cannot be used natively with dbt Cloud; requires a workaround running checks after push via GitHub Actions
- **Manifest dependency**: Most hooks require `manifest.json`, meaning they effectively run after `dbt parse` in CI, not truly at commit time for local development without a database connection
- **Telemetry**: Built-in anonymous usage tracking (opt-out via `.dbt-checkpoint.yaml`)

## Connections to Existing Wiki

- [[ci-cd-for-data-pipelines]] — dbt-checkpoint is a concrete implementation of CI/CD practices for dbt workflows
- [[dbt-slim-ci]] — Complementary: dbt-checkpoint operates at commit time, Slim CI at PR time
- [[dbt-data-contract-implementation]] — Hooks like `check-model-has-contract` and `check-column-name-contract` enforce contract patterns
- [[dbt-testing-patterns]] — Hooks enforce testing coverage requirements
- [[dbt-observability-implementation]] — Both are dbt-native quality mechanisms, but dbt-checkpoint is pre-commit while observability is post-run