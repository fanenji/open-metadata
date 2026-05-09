---
type: concept
title: dbt Model Performance Triage
created: 2026-04-29
updated: 2026-04-29
tags: [dbt, performance, optimization, snowflake]
related: [dbt-observability-implementation, dbt-query-comment-pattern, dbt-artifact-upload-macro]
sources: ["How to add observability to your dbt deployment - Show and Tell.md"]
---
# dbt Model Performance Triage

A decision framework for optimizing slow dbt models based on performance metrics from Snowflake query history. Three main action items are identified from the data:

## Action Items

1. **Materialization Change** — If a model takes a long time to build, consider switching to an incremental or insert_by_period strategy
2. **Clustering Key Optimization** — If a model is slow and scans a high percentage of partitions, explore new cluster keys
3. **Warehouse Resize** — If a model has significant spillage or network bytes, increase warehouse size after exhausting other optimizations

## Metrics Used

- Total elapsed time
- Byte spillage
- Partitions scanned
- Bytes sent over network

## Context

This framework was part of the [[dbt-observability-implementation]] at Snapcommerce, enabled by joining dbt artifacts to Snowflake query history via the [[dbt-query-comment-pattern]].