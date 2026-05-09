---
type: concept
title: dbt Snapshots
created: 2026-04-29
updated: 2026-04-29
tags: [dbt, slowly-changing-dimensions, historical-tracking]
related: [dbt-core, dbt-incremental-models]
sources: ["How to get started with dbt.md"]
---
# dbt Snapshots

Snapshots in [[dbt Core]] implement slowly changing dimensions (SCD), a methodology designed over 20 years ago to track historical changes in dimension data while optimizing storage. Snapshots capture the state of a source table at each point in time, recording when a record was valid and when it changed.

dbt supports SCD Type 2 by default, creating new rows for each change with `valid_from` and `valid_to` timestamps. This enables point-in-time analysis and historical reporting. The dbt snapshot documentation is considered one of the best illustrations of SCD implementation.