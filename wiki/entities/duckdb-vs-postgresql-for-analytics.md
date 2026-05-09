type: entity
title: DuckDB vs PostgreSQL for Analytics
created: 2026-05-07
updated: 2026-05-07
tags: [duckdb, postgresql, comparison, analytics, performance]
related: [duckdb, duckdb-production-deployment, duckdb-migration-strategy, duckdb-performance-benchmarks, elt-pattern]
sources: ["why-duckdb-crushed-our-500gb-data-pipeline-and-how-itll-crush-yours-too.md"]
---
# DuckDB vs PostgreSQL for Analytics

A decision framework for choosing between DuckDB and PostgreSQL for analytical workloads, based on the production migration documented in "Why DuckDB Crushed Our 500GB Data Pipeline."

## Performance Comparison

| Query Type | PostgreSQL (RDS r5.4xlarge) | DuckDB (m5.2xlarge) | Speedup |
|---|---|---|---|
| GROUP BY + JOIN (100M rows) | 127s | 3.8s | 33.4x |
| Full table scan (50GB Parquet) | 89s | 4.2s | 21.2x |
| Window functions (200M rows) | 256s | 11.3s | 22.7x |

## Cost Comparison

| Component | PostgreSQL RDS | DuckDB + S3 |
|---|---|---|
| Compute | $9,200/month (r5.4xlarge) | $380/month (EC2 m5.2xlarge) |
| Storage | $2,400/month (4TB EBS) | $400/month (4TB S3) |
| Backup | $800/month | Included in S3 |
| **Total** | **$12,400/month** | **$780/month** |

## When to Use DuckDB

- Analytical workloads (aggregations, window functions, joins)
- ETL/ELT pipelines
- Embedded analytics (in-process database)
- Data lake queries (direct S3/Parquet access)
- Single-node deployments

## When to Use PostgreSQL

- High-frequency writes (OLTP)
- Multi-user concurrent writes
- Server-based access from multiple applications
- Real-time streaming analytics
- Distributed queries across datacenters
- ACID transactions with row-level locking

## Migration Strategy

1. Identify slow analytical queries using `pg_stat_statements`
2. Export tables to Parquet format
3. Load into DuckDB
4. Validate row counts and sample data
5. Update application code (minimal changes needed)

## Caveats

- Benchmarks are from a single source and may not be representative
- Cost comparison is apples-to-oranges (managed RDS vs self-managed EC2)
- DuckDB is not a full PostgreSQL replacement — only for analytics workloads