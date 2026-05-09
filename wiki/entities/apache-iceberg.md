---
type: entity
title: Apache Iceberg
tags: [table-format, storage, governance, lakehouse, iceberg, data-lakehouse, open-source]
related: [duckdb, low-ops-lakehouse, data-governance, minio, nessie, data-lakehouse-on-premise-pattern, project-nessie, data-lakehouse, iceberg-table-versioning, iceberg-hidden-partitioning, iceberg-partition-evolution, dremio]
sources: ["10 DuckDB + Iceberg Patterns for Low-Ops Lakehouses.md", "Architetture Open Source Simili_ -20260506.md", "Open Source and the Data Lakehouse Iceberg and Project Nessie.md"]
created: 2026-04-04
updated: 2026-05-07
---
# Apache Iceberg

[[apache-iceberg]] is an open-source table format for managing huge analytical datasets on a data lake. It introduces a metadata layer between tools and data files that enables intelligent scanning and provides the structural layer for warehouse-like features, acting as the storage, governance, and contract layer in a modern lakehouse architecture.

## Key Features

- **ACID Transactions**: Ensures atomicity, consistency, isolation, and durability for concurrent read/write scenarios, preventing data corruption.
- **Schema Evolution**: Allows safe changes to table structures (e.g., adding, renaming, or dropping columns, or widening types) without rewriting datasets or breaking downstream consumers.
- **Partition Evolution**: Enables changing the partitioning strategy (e.g., bucketing, truncating) as data grows to match query patterns, without requiring a full rewrite.
- **Time Travel (Snapshot Isolation)**: Provides access to previous table states by querying historical snapshots, enabling stable data views during ongoing writes.
- **Hidden Partitioning**: Exposes partitioning benefits without burdening end users; query engines automatically perform partition pruning.
- **Equality Deletes**: Supports bulk removal of rows (e.g., for GDPR compliance) and upsert replacements.
- **Position Deletes**: Allows surgical, precise deletion of specific rows.

## Role in Lakehouse Architecture

Apache Iceberg provides the "Single Source of Truth" by managing table semantics and data governance. It acts as an enforceable contract for schema and versioning, enabling reliable data operations in a low-ops environment.

In a complete Lakehouse stack, Iceberg works in conjunction with [[minio]] for storage and [[nessie]] for cataloging and versioning. Iceberg is complementary to [[Project Nessie]]: Iceberg provides table-level versioning, while Nessie provides catalog-level versioning. Together they form a unified, vendor-independent data lakehouse stack.