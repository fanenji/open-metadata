---
type: concept
title: dbt Analyses
created: 2026-04-29
updated: 2026-04-29
tags: [dbt, sql, exploration]
related: [dbt-core, dbt-project-scaffolding]
sources: ["How to get started with dbt.md"]
---
# dbt Analyses

Analyses in [[dbt Core]] are SQL queries stored in the `analyses/` directory of a dbt project. Unlike models, analyses are not materialized as tables or views. They serve as a place to store:
- Queries that are not yet ready to become models
- Exploratory or ad-hoc queries
- Queries that should not be part of the main data model

Analyses provide a way to keep SQL queries version-controlled and organized alongside the rest of the dbt project without materializing them in the warehouse.