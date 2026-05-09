---
type: concept
title: Local Iceberg Development Stack
created: 2026-05-07
updated: 2026-05-07
tags: [iceberg, development, docker, lakehouse, prototyping]
related: [duckdb-iceberg-write-support, lakekeeper-catalog, duckdb-iceberg-extension, data-lakehouse]
sources: ["Writing Iceberg Tables with DuckDB 1.4.0 A Practical Starter Guide.md"]
---
# Local Iceberg Development Stack

A pattern for setting up a complete Apache Iceberg environment locally using Docker containers for prototyping and development. The stack typically includes:

## Components

- **REST Catalog Server** (e.g., Lakekeeper) — Manages Iceberg metadata and provides a REST API for catalog operations
- **Object Store** (optional, e.g., MinIO) — S3-compatible storage for Iceberg data files
- **Query Engine** (e.g., DuckDB) — Client that connects to the catalog and performs read/write operations

## Workflow

1. Start the Docker containers: `docker compose up -d`
2. Configure DuckDB with secrets and catalog connection
3. Execute SQL to create, write, and query Iceberg tables
4. Tables are immediately consumable by other Iceberg-compatible engines (Spark, Flink, Trino)

## Advantages

- No cloud dependencies required
- Fast iteration for schema and query prototyping
- Reproducible environment via Docker Compose
- Tables written locally can be promoted to production clusters

## Limitations

- Not suitable for production workloads
- Dummy authentication tokens are used
- Single-node performance only
- Catalog implementation specifics may vary

This pattern is particularly useful for teams exploring [[data-lakehouse]] architectures and wanting to experiment with Iceberg before committing to a full-scale deployment.