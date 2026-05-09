---
type: concept
title: dbt Metrics
created: 2026-04-29
updated: 2026-04-29
tags: [dbt, metrics, data-modeling]
related: [dbt-core, dbt-exposures, analytics-engineering-role]
sources: ["How to get started with dbt.md"]
---
# dbt Metrics

Metrics in [[dbt Core]] are a way to define measures grouped by dimensions within a dbt project. After creating dimensions and measures in data models, users can define metrics that represent aggregated business calculations. The purpose of metrics is to enable downstream consumption without materializing every possible aggregation. Metrics are defined in YAML files and can be used by BI tools and other consumers to query pre-defined business calculations.