---
type: entity
title: dbt Core Cheat Sheet
created: 2026-04-04
updated: 2026-04-04
tags: [dbt, cheat-sheet, reference]
related: [dbt-core, dbt-command-reference, dbt-testing-patterns, dbt-macros, dbt-project-scaffolding, dbt-cloud-environments, dbt-slim-ci]
sources: ["The Ultimate dbt Core Cheat Sheet.md"]
---
# dbt Core Cheat Sheet

A quick-reference summary of the most useful commands and patterns from [[The Ultimate dbt Core Cheat Sheet]] by [[Mihir Samant]]. Designed as a practical reference for the team.

## Essential Commands

| Command | Description |
|---------|-------------|
| `dbt init my_project` | Scaffold a new dbt project |
| `dbt debug` | Verify warehouse connection |
| `dbt run` | Build all models |
| `dbt test` | Run all tests |
| `dbt build` | Run + test everything |
| `dbt compile` | Compile SQL without running (debugging) |
| `dbt retry` | Re-run only failed models |
| `dbt seed` | Load CSV files into warehouse |
| `dbt docs generate` | Generate documentation site |
| `dbt docs serve` | Serve documentation locally |
| `dbt clean` | Remove compiled artifacts |

## Selection Patterns

- `dbt run --select model_name` — Single model
- `dbt run --select +model_name` — Model + upstream dependencies
- `dbt run --select model_name+` — Model + downstream dependents
- `dbt run --select @model_name` — Model + both directions
- `dbt run --select tag:daily` — Models with a specific tag
- `dbt run --select models/staging` — All models in a folder
- `dbt run --exclude tag:slow` — Exclude tagged models

## Model Organization

```
models/
├── staging/          # Raw data cleanup (stg_ prefix)
├── intermediate/     # Business logic (int_ prefix)
└── marts/           # Final output (fct_ / dim_ prefix)
```

## Testing

- **Built-in**: `unique`, `not_null`, `accepted_values`, `relationships`
- **Custom generic**: Define in `tests/generic/` (e.g., `valid_email`)
- **Singular**: Define in `tests/` (e.g., `assert_positive_revenue`)

## Performance Tips

- Views for staging, tables for marts
- Incremental models for large append-only data
- Snapshots for SCD Type 2 change tracking
- Proper indexing in post-hooks
- Partition large tables by date