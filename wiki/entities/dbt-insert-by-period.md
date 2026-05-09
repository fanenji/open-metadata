---
type: entity
title: dbt Insert By Period
created: 2026-05-07
updated: 2026-05-07
tags: [dbt, incremental, materialization, dbt-utils]
related: [geospatial-analytics-with-dbt, snowflake-zero-copy-clone, snowflake-manual-clustering]
sources: ["Complex geospatial analytics with dbt - Summary-20260507.md"]
---
# dbt Insert By Period

Insert by period is an advanced incremental strategy from the `dbt_utils` package. It is best suited for data that is cleanly partitioned by time and bulk-updated once per day with no late-arriving data.

## How It Works

This strategy chunks the source data into time periods and processes one chunk at a time. Key benefits:
- Avoids memory/resource limits for very large backfills
- Can be paused and resumed mid-backfill

## Trade-offs

**Sensitive to late-arriving data:** If records can arrive after their processing window, reprocessing is needed.

> Recommendation: start with standard incremental materialization. If performance is poor, consider insert_by_period.