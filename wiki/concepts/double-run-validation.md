type: concept
title: Double-Run Validation
created: 2026-04-04
updated: 2026-04-04
tags: [dbt, migration, data-quality, testing]
related: [dbt-testing-patterns, dbt-dry-run, blablacar, dbt-scaling-patterns]
sources: ["One Thousands and One dbt Models How BlaBlaCar Moved to dbt in 12 months - Summary.md"]
---
# Double-Run Validation

**Double-run validation** is a migration-specific testing pattern used by [[blablacar]] to ensure data quality when migrating SQL transformation pipelines to dbt.

## Process

When migrating a model from legacy SQL to dbt:

1. **Run the old query** against production and materialize results to a temporary table
2. **Run the new dbt model** against the same inputs and materialize results
3. **Compare outputs**: row counts, key column distributions, spot-check sample rows
4. **Proceed with cutover** only when outputs are identical (or documented differences are intentional)

## Automation

BlaBlaCar formalized this into an internal **data quality module** — a tool that automates steps 1–3 and produces a diff report. This enabled the team to maintain zero-tolerance for data quality regressions during their 12-month migration of ~1,200 models.

## When to Use

- **Migration projects**: When replacing legacy SQL with dbt models
- **High-risk pipelines**: Complex models with deep dependency chains (e.g., BlaBlaCar's 120-model "spaghetti" pipeline)
- **Zero-tolerance environments**: Where any data quality regression is unacceptable

## Related Concepts

- [[dbt-testing-patterns]] — Broader categorization of dbt testing strategies
- [[dbt-dry-run]] — CI gate technique for pre-execution validation
- [[dbt-scaling-patterns]] — Collection of practices for scaling dbt adoption