---
type: concept
title: Double Run Migration
created: 2026-05-06
updated: 2026-05-06
tags: [migration, data-quality, dbt, risk-management]
related: [dbt-migration-strategy, blablacar, data-quality-dimensions]
sources: ["One Thousands and One dbt Models How BlaBlaCar Moved to dbt in 12 months.md"]
---
# Double Run Migration

A risk mitigation strategy used by [[BlaBlaCar]] during their dbt migration. The old and new pipelines run in parallel for 3-4 days, with automated data quality checks comparing outputs. Only after the new pipeline passes all checks for the validation period is the old pipeline decommissioned. This approach was implemented via a custom data quality module built as part of the [[dbt-migration-strategy]].