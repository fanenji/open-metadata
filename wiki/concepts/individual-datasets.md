---
type: concept
title: Individual Datasets
created: 2026-05-06
updated: 2026-05-06
tags: [dbt, bigquery, development, safety]
related: [dbt-developer-experience, blablacar, dbt-migration-strategy]
sources: ["One Thousands and One dbt Models How BlaBlaCar Moved to dbt in 12 months.md"]
---
# Individual Datasets

A safety mechanism used by [[BlaBlaCar]] where each developer gets a personal BigQuery dataset. When running `dbt run` locally, models are materialized in the developer's personal dataset rather than production. This allows safe testing of code changes without affecting production data or other developers. Part of the [[dbt-developer-experience]] strategy to enable safe code releases.