---
type: concept
title: Metadata Mart
created: 2026-04-04
updated: 2026-04-04
tags: [metadata, observability, data-engineering]
related: [elementary, dbt, data-observability]
sources: ["Are You Using Elementary for DBT?.md"]
---
# Metadata Mart

A **Metadata Mart** is a structured database or schema (typically composed of dimension tables) that stores historical metadata about data transformation processes. 

In the context of tools like [[elementary]], a metadata mart is automatically populated with dbt artifacts, including:
- `dbt_run_results`
- `dbt_models`
- `dbt_tests`
- `dbt_sources`
- `dbt_exposures`
- `dbt_metrics`

## Purpose and Utility

The primary goal of a metadata mart is to enable **Operational Intelligence**. By transforming ephemeral dbt artifacts into persistent, queryable tables, engineers can:
1. **Perform Anomaly Detection**: Use SQL window functions to detect significant deviations in model execution time or data volume.
2. **Track Data Quality Trends**: Monitor test failure rates over time.
3. **Audit Pipeline Performance**: Analyze the impact of changes on downstream dependencies.