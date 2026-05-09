---
type: concept
title: Event Processing Time Partitioning
created: 2026-04-29
updated: 2026-04-29
tags: [data-engineering, partitioning, late-arriving-data, immutability]
related: [functional-data-engineering, table-partitions-as-immutable-objects]
sources: ["Functional Data Engineering — a modern paradigm for batch data processing.md"]
---
# Event Processing Time Partitioning

Event processing time partitioning is a strategy for handling late-arriving facts in [[functional-data-engineering]]. Instead of partitioning data on the event's occurrence time (event time), partitioning is done on the time the event was received or processed (processing time).

## Motivation

Late-arriving facts are common, especially with mobile devices and unstable networks. If partitioning is done on event time, late-arriving data would require mutating existing partitions (violating immutability) or creating new partitions for old data (breaking the partition scheme). Processing-time partitioning allows immutable blocks to land without delays, in a predictable fashion.

## Benefits

- **Immutability**: Partitions are created on a predictable schedule and never need to be modified.
- **Time machine analysis**: Enables analysis like "total sales in February as of today" vs. "total sales in February as of March 1st", providing a view of reality at any point in time.

## Tradeoff: Loss of Partition Pruning

The major cost is that queries with predicates on event time cannot benefit from partition pruning. Mitigation strategies include:

1. **Dual partitioning**: Partition on both time dimensions, though this increases model complexity.
2. **Wider processing-time windows**: Apply predicates on both event time and a relatively wide processing-time window.
3. **Read-optimized formats**: With columnar formats like ORC or Parquet, execution engines can skip files by reading only headers, reducing the impact of missing partition pruning.

## Pragmatic Compromise

In some cases, strict immutability can be traded for earlier SLAs. For example, joining to the latest available dimension partition (even if not the correct one for the event time) can allow aggregates to land earlier, at the cost of potential inaccuracy.