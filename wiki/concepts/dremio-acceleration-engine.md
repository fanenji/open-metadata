---
type: concept
title: Dremio Acceleration Engine
created: 2026-04-29
updated: 2026-04-29
tags: [dremio, performance, caching, materialized-views]
related: [dremio, dremio-semantic-layer, data-lakehouse, data-virtualization-pattern]
sources: ["Dremio.md"]
---
# Dremio Acceleration Engine

The Dremio Acceleration Engine is a caching and optimization layer that automatically accelerates query performance through Data Reflections — a combination of materialized views and indexes maintained transparently by Dremio.

## Data Reflections

Data Reflections are the core mechanism of the Acceleration Engine. They are pre-computed, optimized representations of data that Dremio creates and maintains automatically based on query patterns.

### Types of Reflections

- **Raw Reflections** — Optimized columnar storage of raw data, similar to a materialized view.
- **Aggregate Reflections** — Pre-computed aggregations for common GROUP BY patterns.
- **Partition Reflections** — Optimized storage for partitioned data access patterns.

### Key Characteristics

- **Automatic Maintenance** — Dremio updates Reflections incrementally as source data changes.
- **Transparent Routing** — Queries are automatically routed to the most efficient Reflection without user intervention.
- **No Manual Tuning** — Dremio's optimizer determines which Reflections to create and use.
- **Storage Efficiency** — Reflections are stored in columnar format with compression.

## Performance Benefits

- Sub-second query response on petabyte-scale data lakes
- Elimination of separate ETL for performance optimization
- Reduced query latency for BI and reporting workloads
- Support for concurrent query workloads without degradation

## Relationship to Semantic Layer

The Acceleration Engine works closely with [[dremio-semantic-layer]]. When a Virtual Dataset (VDS) is queried, Dremio can transparently route the query to underlying Reflections, providing semantic abstraction without sacrificing performance.

## Use Cases

- Accelerating BI dashboard queries on large datasets
- Enabling interactive exploration of data lake content
- Supporting real-time analytics on historical data
- Reducing infrastructure costs by eliminating separate performance optimization layers

## Related Pages

- [[dremio]] — Primary Dremio entity page
- [[dremio-semantic-layer]] — Semantic abstraction layer
- [[data-lakehouse]] — Architectural pattern
- [[data-virtualization-pattern]] — Broader virtualization context