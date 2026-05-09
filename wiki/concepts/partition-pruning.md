type: concept
title: Partition Pruning
created: 2026-05-07
updated: 2026-05-07
tags: [duckdb, performance, partitioning, optimization]
related: [duckdb, duckdb-performance-benchmarks, hive-partitioning, duckdb-performance-guide]
sources: ["why-duckdb-crushed-our-500gb-data-pipeline-and-how-itll-crush-yours-too.md"]
---
# Partition Pruning

Partition pruning is a query optimization technique where the database engine reads only the relevant partition directories (or files) based on the query's WHERE clause, rather than scanning the entire dataset. This is critical for performance on partitioned data stored in object storage.

## How It Works

When data is organized using [[hive-partitioning]] (e.g., `year=2024/month=01/day=15/`), DuckDB can determine which directories contain data matching the query's filter conditions. It then reads only those directories, skipping all others.

## Example

```sql
-- DuckDB reads only the directory for 2024-01-15
SELECT COUNT(*)
FROM read_parquet(
    's3://bucket/events/**/*.parquet',
    hive_partitioning=1
)
WHERE year = 2024 AND month = 1 AND day = 15
```

## Benefits

- Dramatically reduces I/O for time-range queries
- Enables fast queries on petabyte-scale datasets
- Works with any object storage (S3, MinIO, GCS)
- No index maintenance required

## Limitations

- Requires careful partition key selection
- Queries without partition filters still scan all data
- Over-partitioning can lead to the small file problem

## Relevance

Partition pruning is the key performance enabler for the DuckDB + S3 architecture described in the article. By organizing data with Hive partitioning and relying on DuckDB's automatic partition pruning, the system achieves sub-second query times on 500GB datasets.