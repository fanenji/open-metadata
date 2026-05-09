type: source
title: "One Thousand and One dbt Models: How BlaBlaCar Moved to dbt in 12 Months"
created: 2026-04-04
updated: 2026-04-04
tags: [dbt, data-engineering, bigquery, airflow, migration, data-mesh]
related: [blablacar, dbt-dag-generator, double-run-validation, dbt-dry-run, dbt-dev-datasets, dbt-scaling-patterns, dbt-project-governance, dbt-dragons, data-mesh, dbt-testing-patterns, dbt-preflight-validation, dbt-cloud]
sources: ["One Thousands and One dbt Models How BlaBlaCar Moved to dbt in 12 months - Summary.md"]
---
# One Thousand and One dbt Models: How BlaBlaCar Moved to dbt in 12 Months

**Speakers:** Thibault Ambard & Tushar Bhasin, BlaBlaCar
**Event:** Forward Data Conference
**Video:** https://www.youtube.com/watch?v=JGkVDRrCHcs

## Summary

BlaBlaCar, a European ride-sharing platform with a ~50-person data team, migrated from Airflow-managed SQL transformation pipelines to dbt over 12 months. The migration moved ~1,200 models and was organized around a data mesh structure with domain teams and a central platform team.

The talk covers the decision to adopt dbt, the critical enablers built to integrate dbt with Airflow (DAG generator from manifest.json, PythonVirtualenvOperator, source freshness sensors), the migration process for a complex 120-model "spaghetti" pipeline, and the scaling practices used to onboard 50 engineers. Key practices include dev datasets, double-run validation, dbt-dry-run CI gates, DBT Dragons expert group, git training for analysts, node selectors in Airflow, and project governance lessons from 50+ project proliferation.

## Key Takeaways

- **DAG generator from manifest.json** is the single most important enabler for scaling dbt with Airflow
- **Double-run validation** (running old and new models in parallel) is essential for safe migration with zero-tolerance for data quality regressions
- **dbt-dry-run** as a mandatory CI gate validates syntax and cost without execution
- **Dev datasets** per engineer enable safe parallel development
- **DBT Dragons** (domain champions) scale dbt knowledge without central team bottleneck
- **Project governance** must be established early to prevent cross-project lineage and CI problems from project proliferation
- **Git training** is a necessary prerequisite for analysts new to version control workflows
- **Node selectors** in Airflow enable per-model scheduling and partial project runs