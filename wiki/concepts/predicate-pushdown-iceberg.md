---
type: concept
title: Predicate Pushdown for Iceberg
created: 2025-02-10
updated: 2025-02-10
tags: [duckdb, iceberg, query-optimization, performance]
related: [duckdb, iceberg, duckdb-iceberg-limitations, duckdb-iceberg-sufficiency]
sources: ["Quando duckdb e iceberg sono sufficienti?.md"]
---
# Predicate Pushdown for Iceberg

The mechanism by which a query engine pushes filter conditions (WHERE clauses) down to the storage layer to minimize the amount of data read. For [[iceberg]] tables, this involves using Iceberg's manifest files and partition metadata to skip irrelevant data files.

## DuckDB's Current Limitation

[[duckdb]] has poor predicate pushdown for Iceberg files. When querying Iceberg tables on S3, DuckDB may scan all data files in a partition rather than using Iceberg's metadata to skip irrelevant files. This leads to:

- Higher S3 request costs (more GET requests).
- Slower query performance (more data read).
- Inefficient use of DuckDB's in-memory processing.

## Why It Matters

Without efficient predicate pushdown, the main advantage of Iceberg — fast metadata-driven pruning — is lost. Queries that should scan only a few files may scan hundreds, making the stack impractical for large datasets.

## Comparison with Other Engines

- **Spark/Trino:** Full predicate pushdown support for Iceberg, including partition pruning and min/max statistics.
- **Snowflake/Databricks:** Native Iceberg integration with optimized pushdown.
- **DuckDB:** Limited pushdown; relies on file-level statistics but does not fully leverage Iceberg's manifest metadata.

## Workarounds

- Use [[PyIceberg]] to handle metadata filtering before passing data to DuckDB.
- Pre-filter data at the storage layer (e.g., using S3 bucket policies or partitioning strategies).
- Limit DuckDB to small datasets where full scans are acceptable.

## Related Concepts

- [[duckdb-iceberg-limitations]] — Broader context of DuckDB's Iceberg limitations.
- [[duckdb-iceberg-sufficiency]] — The architecture where this limitation is a key constraint.