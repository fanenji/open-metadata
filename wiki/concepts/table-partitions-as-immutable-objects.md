---
type: concept
title: Table Partitions as Immutable Objects
created: 2026-04-29
updated: 2026-04-29
tags: [data-engineering, immutability, partitioning, functional-programming]
related: [functional-data-engineering, pure-task, persistent-immutable-staging-area, dimension-snapshots, event-processing-time-partitioning]
sources: ["Functional Data Engineering — a modern paradigm for batch data processing.md"]
---
# Table Partitions as Immutable Objects

Table partitions as immutable objects is a core enforcement mechanism of [[functional-data-engineering]]. It treats table partitions as immutable blocks that are always fully overwritten, never mutated via UPDATE, APPEND, or DELETE operations.

## Principle

While databases may allow row-level mutations, the functional approach prohibits them. A [[pure-task]] should always fully overwrite a partition as its output. This ensures determinism and idempotence: re-running the task with the same input produces the same partition.

## Implementation Strategies

1. **Native partition support**: Use the database's physical partition mechanism and TRUNCATE PARTITION + INSERT OVERWRITE.
2. **Logical partitioning with separate tables**: Use different physical tables as outputs, UNIONed ALL into views that act as logical tables.
3. **DELETE + INSERT**: For databases without partition support, systematically DELETE prior to INSERT using a partitioning key. Note that DELETE may be expensive compared to TRUNCATE PARTITION.

## Benefits

- **Reproducibility**: Any partition can be recomputed independently.
- **Safe re-runs**: Re-executing a task overwrites the previous output, preventing double-counting.
- **Clear lineage**: Each partition maps to a specific task instance.
- **Parallelization**: Partitions can be computed independently.

## Relationship to Modern Tools

Modern data lakehouses ([[iceberg-table-versioning]], Delta Lake) natively support this pattern through their immutable file formats and partition-level operations. The [[write-audit-publish-pattern]] is a practical implementation for Iceberg tables.