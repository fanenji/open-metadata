type: entity
title: DuckDB Production Deployment
created: 2026-05-07
updated: 2026-05-07
tags: [duckdb, deployment, production, docker, s3]
related: [duckdb, duckdb-performance-benchmarks, duckdb-vs-postgresql-for-analytics, duckdb-migration-strategy, fastapi, elt-pattern, data-lakehouse]
sources: ["why-duckdb-crushed-our-500gb-data-pipeline-and-how-itll-crush-yours-too.md"]
---
# DuckDB Production Deployment

A production deployment pattern for DuckDB documented in the article "Why DuckDB Crushed Our 500GB Data Pipeline." The architecture uses an EC2 instance running DuckDB as an embedded analytical engine, with data stored in AWS S3 as Parquet files. A FastAPI application provides REST endpoints for dashboards, scheduled ETL jobs, and data export.

## Architecture

- **Compute**: EC2 m5.2xlarge (or similar) running DuckDB engine
- **Storage**: AWS S3 data lake with Parquet files (Hive-partitioned)
- **API Layer**: FastAPI application serving REST endpoints
- **Hot Data**: Local DuckDB database file (analytics.duckdb) for recent 30 days
- **Cold Data**: Direct S3 queries for historical data
- **Orchestration**: Scheduled ETL jobs via cron or scheduler

## Key Components

- **DuckDBManager**: A production-grade connection manager class that handles connection lifecycle, performance configuration (memory limits, threads, temp directory), S3 configuration, and extension loading (httpfs, parquet)
- **UserEventsPipeline**: Example ETL pipeline that extracts from S3, transforms into analytics tables (user sessions, conversion funnels), and exports to Parquet
- **PerformanceMonitor**: Tracks query execution time, stores metrics in DuckDB itself, and provides slow query analysis
- **Docker Deployment**: Dockerfile and docker-compose.yml for containerized deployment with health checks and resource limits

## Configuration

- Memory limit: 16GB (configurable via environment variable)
- Threads: 8 (configurable)
- Temp directory for large operations
- S3 region and bucket configuration
- Extensions: httpfs, parquet

## Limitations

- Single-node architecture (no distributed query capability)
- Concurrent reads require separate connections per thread
- Not suitable for high-frequency writes, multi-user concurrent writes, or real-time streaming