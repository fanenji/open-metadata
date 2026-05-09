---
type: entity
title: dbt Command Reference
created: 2026-04-04
updated: 2026-04-04
tags: [dbt, commands, reference]
related: [dbt-core, dbt-core-cheat-sheet, dbt-testing-patterns, dbt-macros, dbt-project-scaffolding]
sources: ["The Ultimate dbt Core Cheat Sheet.md"]
---
# dbt Command Reference

A structured listing of all [[dbt Core]] commands with descriptions and use cases, derived from [[The Ultimate dbt Core Cheat Sheet]].

## Build & Run Commands

- **`dbt run`** — Executes compiled SQL models against the warehouse. Supports `--select`, `--exclude`, `--full-refresh`, and `--dry-run` flags.
- **`dbt build`** — Runs models and tests in a single command. Preferred workflow for CI/CD.
- **`dbt compile`** — Compiles SQL to `target/compiled/` without executing. Used for debugging generated SQL.
- **`dbt retry`** — Re-runs only models that failed in the previous `dbt run` or `dbt build`.

## Testing Commands

- **`dbt test`** — Executes all defined tests. Supports `--select` and `--exclude` flags.
- **`dbt test --select source:*`** — Tests all sources for freshness and column constraints.
- **`dbt test --exclude test_type:schema`** — Runs only data tests, excluding schema tests.

## Data Loading Commands

- **`dbt seed`** — Loads CSV files from the `data/` directory into the warehouse.
- **`dbt seed --select seed_name`** — Loads a specific seed file.
- **`dbt seed --full-refresh`** — Drops and recreates seed tables.

## Documentation Commands

- **`dbt docs generate`** — Generates documentation site from project metadata.
- **`dbt docs serve`** — Serves the documentation site locally in a browser.

## Maintenance Commands

- **`dbt deps`** — Installs dependencies defined in `packages.yml`.
- **`dbt clean`** — Removes `target/` and `dbt_packages/` directories.
- **`dbt debug`** — Verifies warehouse connection and project configuration.