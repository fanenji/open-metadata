---
type: concept
title: Single-User Database Limitation
created: 2025-02-10
updated: 2025-02-10
tags: [duckdb, database-design, concurrency, limitation]
related: [duckdb, duckdb-iceberg-sufficiency, duckdb-iceberg-limitations]
sources: ["Quando duckdb e iceberg sono sufficienti?.md"]
---
# Single-User Database Limitation

The design constraint of [[duckdb]] (and similar in-process databases) that limits it to a single concurrent user or process. This is a fundamental architectural choice, not a bug.

## How It Manifests

- DuckDB creates a lock file when a database is opened. A second user or application cannot open the same database file without unsafe workarounds.
- Concurrent writes are not supported. Multiple processes cannot safely write to the same DuckDB instance.
- The database is designed for local, single-user use — ideal for data exploration, development, and embedded transformations.

## Workarounds

- **Shared storage pattern:** Store data in [[iceberg]] tables on S3. Multiple users can read the same data using their own DuckDB instances. Writes must be coordinated (e.g., using Iceberg's optimistic concurrency).
- **Orchestration:** Use a scheduler (e.g., [[kestra]]) to ensure only one DuckDB process writes at a time.
- **Stateless mode:** Use DuckDB in-memory for transformations, reading from and writing to shared storage without persisting a DuckDB database file.

## When It Matters

- **Team collaboration:** Multiple analysts cannot share a single DuckDB database. Each must have their own instance.
- **Production pipelines:** A service cannot rely on DuckDB as a multi-user query engine. It must be used as an embedded transformation step.
- **Concurrent writes:** High-frequency or concurrent write workloads require external coordination.

## Related Concepts

- [[duckdb-iceberg-sufficiency]] — The broader architecture where this limitation is managed.
- [[duckdb-iceberg-limitations]] — Other DuckDB limitations with Iceberg.