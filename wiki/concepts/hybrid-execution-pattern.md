---
type: concept
title: Hybrid Execution Pattern
created: 2026-04-08
updated: 2026-04-08
tags: [architecture, cloud, duckdb, motherduck]
related: [motherduck, duckdb, aws-s3]
sources: ["Beyond Sturing Data How to Use DuckDB, MotherDuck and Kestra for ETL.md"]
---
# Hybrid Execution Pattern

The [[hybrid-execution-pattern]] is a specialized architectural capability provided by [[motherduck]] that allows a single SQL session to transparently query data across different environments.

### How it Works
In a hybrid execution model, the engine intelligently decides where to process a query based on the location of the data and the available compute resources. A user can execute a single query that:
1. Joins a local CSV file on their laptop.
2. With a Parquet file stored in [[aws-s3]].
3. With a large, persistent table residing in the [[motherduck]] cloud instance.

### Benefits
- **Seamless Scalability**: Users can start with local datasets and transition to cloud-scale datasets without changing their SQL logic.
- **Reduced Data Movement**: By processing queries where the data resides (or moving only necessary subsets), the pattern minimizes egress costs and latency.
- **Unified Interface**: Provides a single point of access for fragmented data landscapes.
