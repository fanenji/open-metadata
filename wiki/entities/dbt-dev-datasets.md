type: entity
title: dbt Dev Datasets
created: 2026-04-04
updated: 2026-04-04
tags: [dbt, development, bigquery, isolation]
related: [blablacar, dbt-cloud-environments, dbt-scaling-patterns]
sources: ["One Thousands and One dbt Models How BlaBlaCar Moved to dbt in 12 months - Summary.md"]
---
# dbt Dev Datasets

**Dev datasets** are personal BigQuery datasets used by each engineer at [[blablacar]] for safe parallel development during their dbt migration.

## How It Works

- Each engineer works in a personal dev dataset (e.g., `dev_thibault.my_model`)
- The `target` in `profiles.yml` is set to the developer's personal dataset by default
- Production runs target the shared production dataset
- No risk of breaking production tables during development
- No interference between engineers working in parallel

## Key Requirements

- Explicit setup in the CLI setup script so every engineer has it correctly configured from day one
- dbt's `target` and `project` configuration makes this straightforward

## Benefits

- Enables 6+ engineers to work on the same pipeline simultaneously (as BlaBlaCar did with their 120-model "spaghetti" pipeline)
- Eliminates the risk of accidental production table overwrites during development
- Provides a clean isolation boundary for testing

## Related Concepts

- [[dbt-cloud-environments]] — Broader pattern for environment isolation in dbt
- [[dbt-scaling-patterns]] — Collection of practices for scaling dbt adoption