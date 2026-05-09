---
type: concept
title: dbt-checkpoint Hooks
created: 2026-04-07
updated: 2026-04-07
tags: [dbt, pre-commit, hooks, validation, quality]
related: [dbt-checkpoint, pre-commit-hooks-for-dbt, ci-cd-for-data-pipelines, dbt-data-contract-implementation, dbt-testing-patterns]
sources: ["dbt-checkpoint.md"]
---
# dbt-checkpoint Hooks

**dbt-checkpoint hooks** are the individual validation rules provided by the [[dbt-checkpoint]] tool. They are organized into categories covering all aspects of dbt project quality.

## Hook Categories

### Model Checks
- `check-column-desc-are-same` — Column descriptions are consistent
- `check-column-name-contract` — Column names follow naming contract
- `check-model-columns-have-desc` — All columns have descriptions
- `check-model-columns-have-meta-keys` — Columns have required meta keys
- `check-model-has-all-columns` — Properties file documents all columns
- `check-model-has-contract` — Model has contract enforced
- `check-model-has-constraints` — Model has specific constraints
- `check-model-has-generic-constraints` — Model has generic constraints
- `check-model-has-description` — Model has a description
- `check-model-has-meta-keys` — Model has required meta keys
- `check-model-has-labels-keys` — Model has required labels
- `check-model-has-properties-file` — Model has a properties file
- `check-model-has-tests-by-name` — Model has tests by specific name
- `check-model-has-tests-by-type` — Model has tests by type (unique, not_null, etc.)
- `check-model-has-tests-by-group` — Model has tests from a group
- `check-model-has-tests` — Model has minimum number of tests
- `check-model-name-contract` — Model name follows naming contract
- `check-model-parents-and-childs` — Model has correct number of parents/children
- `check-model-parents-database` — Parent models use specific database
- `check-model-parents-name-prefix` — Parent models have specific name prefix
- `check-model-parents-schema` — Parent models use specific schema
- `check-model-tags` — Model has valid tags
- `check-model-materialization-by-childs` — Materialization based on child count

### Source Checks
- `check-source-columns-have-desc` — Source columns have descriptions
- `check-source-has-all-columns` — Properties file documents all source columns
- `check-source-has-description` — Source has description
- `check-source-table-has-description` — Source table has description
- `check-source-has-freshness` — Source has freshness configured
- `check-source-has-loader` — Source has loader specified
- `check-source-has-meta-keys` — Source has required meta keys
- `check-source-has-labels-keys` — Source has required labels
- `check-source-has-tests-by-name` — Source has tests by name
- `check-source-has-tests-by-type` — Source has tests by type
- `check-source-has-tests` — Source has minimum tests
- `check-source-has-tests-by-group` — Source has tests from a group
- `check-source-tags` — Source has valid tags
- `check-source-childs` — Source has correct number of children

### Script Checks
- `check-script-semicolon` — Script has no semicolons
- `check-script-has-no-table-name` — Script uses `ref()`/`source()` macros, not table names
- `check-script-ref-and-source` — Script references only existing refs and sources

### Macro Checks
- `check-macro-has-description` — Macro has description
- `check-macro-arguments-have-desc` — Macro arguments have descriptions
- `check-macro-has-meta-keys` — Macro has meta keys

### Exposure, Seed, Snapshot, Test Checks
- `check-exposure-has-meta-keys` — Exposure has meta keys
- `check-seed-has-meta-keys` — Seed has meta keys
- `check-snapshot-has-meta-keys` — Snapshot has meta keys
- `check-test-has-meta-keys` — Singular tests have meta keys

### Modifiers
- `generate-missing-sources` — Auto-create missing source definitions
- `generate-model-properties-file` — Auto-generate model properties file
- `unify-column-description` — Unify column descriptions across models
- `replace-script-table-names` — Replace table names with `ref()`/`source()` macros
- `remove-script-semicolon` — Remove trailing semicolons

### dbt Commands
- `dbt-clean`, `dbt-compile`, `dbt-deps`, `dbt-docs-generate`, `dbt-parse`, `dbt-run`, `dbt-test`

### Database Checks
- `check-database-casing-consistency` — Compare manifest and catalog for casing consistency

## Usage Patterns

Hooks are configured in `.pre-commit-config.yaml` with optional `files` patterns to scope them to specific directories. Multiple instances of the same hook can be configured with different scopes (e.g., `check-model-has-all-columns` for `models/core` and `models/mart` separately).