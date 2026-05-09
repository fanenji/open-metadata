---
type: concept
title: DuckDB Execution Model
created: 2026-04-29
updated: 2026-04-29
tags: ["duckdb", "execution", "vectorized", "architecture", "performance"]
related: ["duckdb", "duckdb-spatial-extension", "duckdb-python-integration", "duckdb-spatial-architecture", "graceful-degradation"]
sources: ["DuckDB Spatial Supercharged Geospatial SQL - Summary.md", "DuckDB Spatial Supercharged Geospatial SQL.md"]
---
# DuckDB Execution Model

DuckDB uses a **vector-at-a-time** execution model, which balances the tradeoffs between row-at-a-time and column-at-a-time approaches. This model processes rows in chunks (vectors) sized to fit into CPU cache, avoiding the high CPU overhead of row-at-a-time processing while maintaining a lower memory footprint than column-at-a-time processing.

## Key Characteristics

- **Vector size optimization:** Vectors are sized so that the current working set fits in CPU cache, minimizing memory access latency.
- **Multi-threaded parallelism:** DuckDB is multi-threaded, and the vectorized model synergizes well with parallelism because synchronization overhead can be amortized over vectors.
- **Order-preserving option:** DuckDB optionally preserves input row order, providing dataframe-like semantics where slicing rows on the vertical axis maintains correlation between input and output rows.

## Comparison with Other Models

| Model | Memory Footprint | CPU Efficiency | Examples |
|-------|-----------------|----------------|----------|
| Row-at-a-time | Low | Low (high overhead) | SQLite, PostgreSQL, SQL Server |
| Column-at-a-time | High | High (SIMD-friendly) | Pandas, Polars |
| Vector-at-a-time | Medium | High | DuckDB |

## Graceful Degradation

When DuckDB runs out of RAM, it spills intermediate results to disk rather than crashing. This provides a smooth performance degradation curve rather than a sharp wall, making DuckDB suitable for larger-than-memory workloads on resource-constrained machines.

## Related

- [[duckdb]] — The database engine implementing this model
- [[duckdb-spatial-architecture]] — How spatial operations interact with the vectorized model