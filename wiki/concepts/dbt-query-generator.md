---
type: concept
title: dbt Query Generator
created: 2026-05-06
updated: 2026-05-06
tags: [dbt, migration, tooling, sql]
related: [dbt-migration-strategy, blablacar, tushar-bhasin]
sources: ["One Thousands and One dbt Models How BlaBlaCar Moved to dbt in 12 months.md"]
---
# dbt Query Generator

An internal script built by [[BlaBlaCar]] to accelerate migration by converting standard BigQuery SQL to dbt format. Key transformations include:

- Converting table references to `{{ ref() }}` and `{{ source() }}` syntax
- Adding tests to preserve schema definitions (since dbt does not use DDL for schema specification)
- Conserving column types and constraints

Part of the [[dbt-migration-strategy]] tooling to increase migration speed and consistency across 1,000+ models.