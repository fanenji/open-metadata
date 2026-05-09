---
type: concept
title: dbt Materialization Strategy Matrix
created: 2026-04-04
updated: 2026-04-04
tags: [dbt, materialization, performance, best-practices]
related: [dbt-anti-patterns, dbt-incremental-strategy-guide, dbt-3-layer-architecture]
sources: ["Top 5 Advanced dbt Anti-Patterns That Nearly Killed Our Analytics Team.md"]
---
# dbt Materialization Strategy Matrix

A decision framework for choosing the right dbt materialization strategy based on data volume and access patterns. Prevents the "everything incremental" anti-pattern.

## The Matrix

| Materialization | Row Count | Use Case | Trade-offs |
|-----------------|-----------|----------|------------|
| **View** | < 1M rows | Fast queries, needs real-time data, simple transformations | No performance gain, re-computes on every query |
| **Table** | < 10M rows | Slow queries, dimension tables, lookup tables | Rebuilds on every run, simple and reliable |
| **Incremental** | > 10M rows AND mostly append-only | Large fact tables, event data, time-series | Complex logic, needs careful strategy selection |
| **External** | Any | Reference data that changes outside dbt | No dbt control over refresh timing |

## Decision Rules

1. **Start with View** — If the model is fast enough as a view, keep it as a view.
2. **Promote to Table** — Only when query performance becomes an issue or the model is used as a dimension.
3. **Use Incremental** — Only when the table has >10M rows AND the data is mostly append-only with infrequent updates.
4. **Never Incremental for Small Tables** — A 15-row lookup table should never be incremental. The incremental logic overhead (45 seconds) exceeds the rebuild time (0.1 seconds).

## The "Everything Incremental" Anti-Pattern

Symptoms:
- Small dimension tables (15-365 rows) using incremental materialization
- Frequent `--full-refresh` runs needed when incremental logic breaks
- Debugging time spent on incremental issues for tables that could be rebuilt in seconds
- Complex merge logic for tables that change monthly

## Results of Applying the Matrix

- Total dbt run time: 23 min → 8 min (-65%)
- Models requiring `--full-refresh`: 12/month → 0-1/month
- 60% reduction in incremental-related issues