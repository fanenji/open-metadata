---
type: concept
title: Past Dependencies Avoidance
created: 2026-04-29
updated: 2026-04-29
tags: [data-engineering, dag, dependencies, backfill, parallelization]
related: [functional-data-engineering, pure-task, table-partitions-as-immutable-objects]
sources: ["Functional Data Engineering — a modern paradigm for batch data processing.md"]
---
# Past Dependencies Avoidance

Past dependencies avoidance is a principle in [[functional-data-engineering]] that discourages modeling tasks where a partition depends on a previous partition of the same table.

## Problem

When a partition depends on a previous partition of the same table (e.g., computing the latest user dimension snapshot from the previous snapshot), the DAG depth grows linearly over time. For a table with 3 years of daily snapshots, the dependency chain exceeds 1000 steps. This means:

- **Backfills require sequential processing**: To reprocess data from months back, hundreds of partitions must be recomputed in sequence.
- **No parallelization**: The linear dependency chain prevents concurrent execution.
- **Growing complexity**: The complexity of the graph increases linearly with time.

## Solution

Avoid modeling with past dependencies whenever possible. Instead, design tasks to be independent of previous partitions of the same table. For cumulative-type metrics (e.g., life-to-date customer spending), consider modeling them in a specialized framework optimized for that purpose, separate from the main functional pipeline.

## Benefits

- **Parallelizable backfills**: Partitions can be recomputed concurrently.
- **Constant complexity**: The DAG structure does not grow over time.
- **Simpler lineage**: Each partition's lineage is independent of previous partitions.