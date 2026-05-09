---
type: concept
title: Hidden Partitioning
created: 2026-04-04
updated: 2026-04-04
tags: [apache-iceberg, partitioning, performance, data-lake]
related: [apache-iceberg, partition-evolution, metadata-driven-pruning]
sources: ["Is Apache Iceberg Melting?.md"]
---
# Hidden Partitioning

A key Iceberg feature where partition transforms (e.g., `day(event_time)`) are defined declaratively, and Iceberg tracks the relationship between source columns and partition values in metadata rather than physical paths.

## Benefits

- Queries don't have to encode physical partition paths to be efficient — Iceberg prunes files based on metadata
- Enables partition evolution without rewriting the table
- Different partition layouts can coexist within the same table (e.g., month partitions for older data, day partitions for newer data)

## Enterprise Value

This is one of the most underappreciated enterprise benefits. Partition schemes change because businesses change. Iceberg reduces the cost of adapting to those changes.
