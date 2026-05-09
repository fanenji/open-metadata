type: concept
title: Auto-materialization
created: 2024-03-13
updated: 2024-03-13
tags: [automation, dagster, data-engineering]
related: [dagster, software-defined-assets]
sources: ["Airflow vs Dagster vs Kestra.md"]
---
# Auto-materialization

**Auto-materialization** is an advanced automation feature, primarily associated with **Dagster**, that manages the lifecycle of data assets.

It allows developers to define rules that automatically trigger the re-computation of an asset based on:
- **Freshness Requirements**: e.g., "This table must be updated at least once every hour."
- **Upstream Changes**: Automatically re-running a downstream model when a parent table is updated.
- **Time-based Triggers**: e.g., "Ensure all yesterday's data is processed by 9 AM."

This is particularly powerful for managing large-scale [[dbt]] projects where manual scheduling of hundreds of interdependent models would be impossible.