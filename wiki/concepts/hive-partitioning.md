type: concept
title: Hive Partitioning
created: 2026-05-07
updated: 2026-05-07
tags: [duckdb, partitioning, parquet, s3, performance]
related: [duckdb, duckdb-production-deployment, duckdb-performance-benchmarks, cloud-native-geospatial-workflow, data-lakehouse]
sources: ["why-duckdb-crushed-our-500gb-data-pipeline-and-how-itll-crush-yours-too.md"]
---
# Hive Partitioning

Hive partitioning is a directory-based partition scheme for organizing data in object storage (S3, GCS, Azure Blob). Data is stored in nested directories following a key=value pattern, enabling partition pruning — only reading the relevant directories for a query.

## Directory Structure

```
s3://bucket/events/year=2024/month=01/day=15/data.parquet
s3://bucket/events/year=2024/month=01/day=16/data.parquet
```

## How It Works

- Each partition level corresponds to a column (year, month, day)
- DuckDB reads only the directories matching the query's WHERE clause
- Partition pruning eliminates unnecessary file reads, dramatically reducing I/O

## DuckDB Integration

DuckDB supports Hive partitioning natively via the `hive_partitioning=1` option in `read_parquet()`:

```sql
SELECT * FROM read_parquet(
    's3://bucket/events/**/*.parquet',
    hive_partitioning=1
)
WHERE year = 2024 AND month = 1 AND day = 15
```

## Benefits

- Dramatically reduces data scanned for time-range queries
- Works with any object storage (S3, MinIO, GCS)
- Standard format supported by many tools (Spark, Presto, Hive)
- No separate partition metadata management needed

## Limitations

- Requires careful partition key selection (high cardinality = too many directories)
- Small file problem if partitions are too granular
- Schema evolution across partitions can be complex

## Relevance

Hive partitioning is a key technique for making DuckDB + S3 architectures performant at scale. The article demonstrates partitioning by date (year/month/day) for event data, enabling fast time-range queries on 500GB datasets.