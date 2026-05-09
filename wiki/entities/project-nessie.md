---
type: entity
title: Project Nessie
created: 2026-04-04
updated: 2026-04-04
tags: [nessie, catalog, versioning, data-lakehouse, open-source]
related: [apache-iceberg, data-lakehouse, nessie-catalog-versioning, nessie-branch-merge-workflow, nessie-multi-table-transactions, dremio]
sources: ["Open Source and the Data Lakehouse Iceberg and Project Nessie.md"]
---
# Project Nessie

Project Nessie is an open-source, versioned, and transactional catalog for data lakehouses. It is often described as "Git for metadata" — it allows managing and tracking changes to the metadata of tables stored in [[Apache Iceberg]] format across an entire catalog, not just individual tables.

Key capabilities include:
- **Ingestion Isolation:** Create a branch of the catalog, ingest data, run quality checks, then merge into the default branch.
- **Zero Copy Environment Generation:** Create isolated environments for different analytical tasks without duplicating data; each environment references the same underlying data with its own metadata snapshot.
- **Disaster Recovery:** Rollback the catalog to historical commits to recover from failures.
- **Multi-Table Transactions:** Group multiple table changes in a single transaction at the catalog level.
- **Reproducibility:** Tag catalog commits to run queries on the catalog as it existed at a specific point in time.

Nessie complements Iceberg's table-level versioning with catalog-level versioning, forming a unified stack.