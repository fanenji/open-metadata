type: entity
title: DuckDB Performance Benchmarks
created: 2026-05-07
updated: 2026-05-07
tags: [duckdb, benchmarks, performance, analytics]
related: [duckdb, duckdb-production-deployment, duckdb-vs-postgresql-for-analytics, duckdb-migration-strategy, duckdb-performance-guide]
sources: ["why-duckdb-crushed-our-500gb-data-pipeline-and-how-itll-crush-yours-too.md"]
---
# DuckDB Performance Benchmarks

A collection of performance benchmarks from the article "Why DuckDB Crushed Our 500GB Data Pipeline," comparing DuckDB against PostgreSQL RDS for analytical workloads.

## Benchmark Results

| Query | PostgreSQL | DuckDB | Speedup |
|---|---|---|---|
| GROUP BY + JOIN (100M rows) | 127s | 3.8s | 33.4x |
| Full table scan (50GB Parquet) | 89s | 4.2s | 21.2x |
| Window functions (200M rows) | 256s | 11.3s | 22.7x |

## Production Metrics

- **Average query time**: 127s → 4.2s (30x faster)
- **Dashboard load time**: 45s → 1.8s
- **ETL pipeline**: 6 hours → 23 minutes
- **Scale**: 50M events/day, 200+ internal users

## Cost Impact

- **Infrastructure**: $12,400/month → $780/month (94% reduction)
- **Developer time**: 20 hours/week → 2 hours/week on database maintenance
- **ROI**: Migration paid for in 3 weeks

## Caveats

- Benchmarks are from a single source and may be cherry-picked
- No independent verification of results
- Dataset characteristics and query complexity not fully specified
- Cost comparison is apples-to-oranges (managed RDS vs self-managed EC2)
- AWS pricing changes over time

## Related

See [[duckdb-performance-guide]] for official DuckDB performance optimization documentation.