---
type: entity
title: Dremio Sonar
created: 2026-04-29
updated: 2026-04-29
tags: [dremio, query-engine, execution]
related: [dremio, dremio-arctic, dremio-semantic-layer, dremio-acceleration-engine, data-lakehouse]
sources: ["Dremio.md"]
---
# Dremio Sonar

Dremio Sonar is the core query engine component of the Dremio platform. It is responsible for executing SQL queries directly against data lake storage (e.g., Apache Iceberg tables, Parquet files, CSV files) without requiring a separate data warehouse.

## Key Capabilities

- **Direct Lake Access** — Queries data directly from object storage (S3, ADLS, GCS, MinIO) without data movement.
- **SQL Execution** — Full ANSI SQL support with advanced optimizations for data lake formats.
- **Distributed Processing** — Distributed query execution across multiple nodes for parallel processing.
- **Caching and Acceleration** — Integration with [[dremio-acceleration-engine]] for automatic performance optimization.

## Architecture

Sonar uses a distributed, columnar execution engine optimized for data lake storage patterns. It supports:

- **Pushdown Optimizations** — Pushes filtering and aggregation down to storage when possible.
- **Adaptive Query Execution** — Dynamically adjusts execution plans based on runtime statistics.
- **Concurrent Workload Support** — Handles multiple concurrent queries with resource isolation.

## Relationship to Other Components

- **Dremio Arctic** — Arctic is a managed service that includes Sonar as its query engine.
- **Semantic Layer** — Sonar executes queries against Virtual Datasets (VDS) defined in the semantic layer.
- **Acceleration Engine** — Sonar automatically routes queries to Data Reflections for performance.

## Related Pages

- [[dremio]] — Primary Dremio entity page
- [[dremio-arctic]] — Managed service offering
- [[dremio-semantic-layer]] — Semantic abstraction layer
- [[dremio-acceleration-engine]] — Performance optimization
- [[data-lakehouse]] — Architectural pattern