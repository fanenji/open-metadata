type: concept
title: Vectorized Execution
created: 2026-05-07
updated: 2026-05-07
tags: [duckdb, performance, execution, simd]
related: [duckdb, duckdb-performance-benchmarks, columnar-storage]
sources: ["why-duckdb-crushed-our-500gb-data-pipeline-and-how-itll-crush-yours-too.md"]
---
# Vectorized Execution

Vectorized execution is a query processing technique where the database engine processes data in batches (vectors) rather than row-by-row, using SIMD (Single Instruction, Multiple Data) CPU instructions. This is a key performance differentiator for DuckDB compared to traditional row-based databases.

## How It Works

- **Traditional (row-based)**: Each operator processes one row at a time, calling functions for each row. High overhead from function calls and branch mispredictions.
- **Vectorized (batch-based)**: Each operator processes a batch of rows (typically 1024-4096) at a time. Operations are applied to entire vectors using SIMD instructions.

## Benefits

- **CPU efficiency**: SIMD instructions process multiple values with a single instruction
- **Cache locality**: Processing batches keeps data in CPU cache
- **Reduced overhead**: Fewer function calls per row
- **Amortized interpretation**: Loop overhead is spread across many rows

## DuckDB's Implementation

DuckDB uses a vectorized execution engine where all operators (scan, filter, aggregate, join) operate on columnar vectors. This is why DuckDB can process 100M rows with GROUP BY and JOIN in 3.8 seconds — the vectorized engine efficiently utilizes modern CPU capabilities.

## Comparison

| Aspect | Row-based (PostgreSQL) | Vectorized (DuckDB) |
|---|---|---|
| Processing unit | Single row | Batch (vector) |
| CPU utilization | Low | High (SIMD) |
| Cache efficiency | Poor | Good |
| Analytical queries | Slow | Fast |
| OLTP queries | Fast | Slow |

## Limitations

- Less effective for transactional workloads with many small queries
- Higher memory usage per query (batches need memory)
- More complex implementation

## Relevance

Vectorized execution, combined with [[columnar-storage]], is the primary reason DuckDB achieves 20-30x speedups over PostgreSQL for analytical workloads. The article's benchmarks demonstrate the practical impact of this architectural choice.