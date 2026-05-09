---
type: concept
title: Dimension Snapshots
created: 2026-04-29
updated: 2026-04-29
tags: [data-engineering, dimensions, scd, snapshots, reproducibility]
related: [functional-data-engineering, table-partitions-as-immutable-objects, persistent-immutable-staging-area]
sources: ["Functional Data Engineering — a modern paradigm for batch data processing.md"]
---
# Dimension Snapshots

Dimension snapshots are a methodology for handling slowly changing dimensions (SCD) in [[functional-data-engineering]]. Instead of using traditional SCD types (type-1, type-2, type-3) that mutate data, a new partition containing the full dimension as-of a point in time is appended at each ETL schedule.

## Principle

The dimension table becomes a collection of snapshots, where each partition contains the complete dimension state at a specific point in time. This replaces the traditional SCD approach of tracking changes through row-level mutations.

## Benefits

- **Simplicity**: No need for surrogate key management or complex lookup logic.
- **Reproducibility**: Any historical state can be reconstructed by reading the appropriate snapshot.
- **Immutability**: Aligns with the functional paradigm by avoiding mutations.
- **Cheap storage vs. expensive engineering**: Storage is cheap; engineering time is expensive. Duplicating data is acceptable.

## Tradeoffs

- **Storage overhead**: Data is duplicated across snapshots, though dimension tables are typically negligible in size compared to fact tables.
- **Query complexity**: Joining facts to time-relative dimension snapshots requires additional predicates on snapshot time.
- **Very large dimensions**: For dimensions with millions of members, a hybrid approach mixing snapshots with SCD methodology may be necessary.

## Alternative: Nested Data Types

An alternative to full snapshots is using complex/nested data types (e.g., a `state_history` column as a map with effective dates as keys). This tracks history without altering the table grain, and is more dynamic than type-3 SCD.