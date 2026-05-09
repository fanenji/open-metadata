---
type: concept
title: dbt Incremental Strategy Guide
created: 2026-04-04
updated: 2026-04-04
tags: [dbt, incremental-models, performance, best-practices]
related: [dbt-anti-patterns, dbt-materialization-strategy-matrix, dbt-insert-by-period, dbt-testing-patterns]
sources: ["Top 5 Advanced dbt Anti-Patterns That Nearly Killed Our Analytics Team.md"]
---
# dbt Incremental Strategy Guide

A decision framework for choosing and implementing dbt incremental strategies, based on production experience with 340 models and 47M+ rows.

## Strategy Selection

| Strategy | When to Use | Key Behavior |
|----------|-------------|--------------|
| `append` | Append-only data, no updates to existing rows | Ignores `unique_key` — inserts all new rows |
| `merge` | Data with updates to existing rows | Respects `unique_key` — inserts new, updates existing |
| `insert_overwrite` | Large partitions that need full replacement | Replaces entire partitions |

## Critical Anti-Pattern: Append + Unique Key

Using `append` strategy with `unique_key` is a common mistake. The `append` strategy ignores `unique_key`, creating duplicate rows on every run. This silently corrupts aggregations and metrics.

## The Lookback Window Pattern

For incremental models that need to catch late-arriving data updates, use a lookback window:

```sql
{% if is_incremental() %}
  WHERE order_date >= (SELECT DATE_SUB(MAX(last_updated), 7) FROM {{ this }})
{% endif %}
```

This re-processes the last 7 days of data on each run, capturing delayed updates. The window size (7 days) should be tuned based on your maximum expected data delay.

## When NOT to Use Incremental

- Tables with <10M rows (use Table materialization instead)
- Dimension/lookup tables that change infrequently
- Tables where historical data is frequently updated (use merge + lookback or full refresh)
- Small tables where rebuild time is negligible

## Best Practices

1. Always use `on_schema_change='fail'` to catch upstream schema changes immediately
2. Add a `last_updated` column for debugging and freshness tracking
3. Use `merge` strategy when you specify `unique_key`
4. Test incremental models with a `--full-refresh` in staging before production deployment
5. Monitor incremental model failure rates — frequent failures indicate wrong strategy choice