---
type: concept
title: Graceful Degradation
created: 2026-04-29
updated: 2026-04-29
tags: [duckdb, performance, memory-management]
related: [duckdb, duckdb-execution-model]
sources: ["DuckDB Spatial Supercharged Geospatial SQL.md"]
---
# Graceful Degradation

Graceful degradation is a design principle in [[DuckDB]] where the database spills intermediate results to disk when RAM is exhausted, rather than crashing or aborting the query. This ensures that DuckDB always makes progress, even on resource-constrained machines.

## How It Works

- Almost all operators (different parts of the query execution pipeline) can offload their intermediate results to temporary files on disk.
- The database then continues processing and reassembles the final result.
- The performance degradation is smooth rather than a sharp wall, as demonstrated in benchmarks comparing DuckDB with other database engines under memory limits.

## Importance

- Makes DuckDB suitable for larger-than-memory workloads on laptops and other resource-constrained environments.
- Differentiates DuckDB from other engines that may abort or time out when memory limits are reached.
- Aligns with DuckDB's philosophy of being a "good guest" that shares resources with other processes.

## Related

- [[duckdb-execution-model]] — The vectorized execution model that enables graceful degradation
- [[duckdb]] — The database engine implementing this feature