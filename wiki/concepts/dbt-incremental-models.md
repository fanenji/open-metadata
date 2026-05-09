---
type: concept
title: dbt Incremental Models
created: 2026-04-04
updated: 2026-05-07
tags: ["dbt", "performance", "optimization", "incremental-loading"]
related: ["dbt", "dbt-core", "dbt-adapters", "dbt-project-scaffolding"]
sources: ["10 Game-Changing dbt Tips Iwh I Knew Before My First Production Model 1.md", "How to get started with dbt.md"]
---
# dbt Incremental Models

**Incremental models** in [[dbt]] are a powerful pattern used to optimize compute costs and performance by processing only new or changed data rather than reprocessing the entire dataset on each run. They use Jinja conditional syntax (typically `is_incremental()`) to define different SQL for the initial full load versus subsequent incremental runs.

## Implementation

The core mechanism involves the `is_incremental()` macro, which filters for records newer than the maximum date currently in the target table. A common example is:

```sql
where updated_at > (select max(updated_at) from {{ this }})
```

In the SQL definition of the model, the `is_incremental()` block wraps the incremental logic so that it applies only after the first run. This allows the initial full load to process all data while subsequent runs process only new or updated records.

## Incremental Strategies

The incremental strategy depends on the [[dbt-adapters|adapter]] and warehouse capabilities. Common strategies include:

- **`merge`** — upsert logic based on a unique key
- **`insert_overwrite`** — replace partitions (common on BigQuery)
- **`append`** — add new rows without deduplication

Choosing the right strategy is essential for handling late-arriving data, deduplication, and maintaining data integrity.

## Advantages

- **Compute Efficiency**: Incremental models significantly reduce the amount of data processed during each run, which is critical for large-scale datasets.
- **Scalability**: They enable the processing of massive tables that would be too expensive or slow to rebuild completely on every run.
- **Performance Optimization**: Incremental models are a critical performance optimization for large datasets where full refreshes would be prohibitively expensive or slow.

## Challenges and Risks

- **Complexity**: Requires careful management of logic to ensure data integrity between full and incremental loads.
- **Deduplication**: Developers must implement logic to handle late-arriving data or updates to existing rows to prevent duplicates.
- **Schema Evolution**: Changes to the underlying table schema can break incremental logic if not handled via appropriate dbt configurations (e.g., using `on_schema_change`).