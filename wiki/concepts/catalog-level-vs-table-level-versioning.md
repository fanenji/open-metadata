---
type: concept
title: Catalog-Level vs Table-Level Versioning
created: 2026-02-13
updated: 2026-02-13
tags: [iceberg, versioning, catalog, branching, time-travel]
related: [nessie-catalog-versioning, iceberg-table-versioning, lakekeeper, apache-polaris, data-lakehouse-versioning-strategies, lakefs-file-versioning]
sources: ["Nessie vs LakeKeeper.md"]
---
# Catalog-Level vs Table-Level Versioning

A distinction between two approaches to versioning in data lakehouses, particularly relevant when choosing an Iceberg catalog.

## Table-Level Versioning

- **Scope**: Individual tables
- **Mechanism**: Iceberg snapshots — every change creates a new immutable snapshot of the table's metadata
- **Capabilities**: Time travel to any historical snapshot, schema evolution, table-level branching and tagging
- **Supported by**: All Iceberg catalogs (Nessie, LakeKeeper, Polaris) via the Iceberg REST API
- **Limitations**: Cannot atomically version changes across multiple tables; each table's history is independent

## Catalog-Level Versioning

- **Scope**: Entire catalog (all tables)
- **Mechanism**: Git-like commits, branches, and tags applied to the catalog's metadata pointers
- **Capabilities**: Multi-table atomic transactions, consistent cross-table time travel, zero-copy branching of the entire lakehouse
- **Supported by**: Project Nessie (currently the only option)
- **Limitations**: Additional service to manage, learning curve for Git-like workflows

## Decision Framework

| Priority | Recommended Approach |
|----------|---------------------|
| Multi-table atomic workflows | Catalog-level (Nessie) |
| Single-table development | Table-level (any catalog) |
| Centralized governance | Table-level (Polaris) |
| Performance & security | Table-level (LakeKeeper) |

## Related Pages

- [[nessie-catalog-versioning]] — Catalog-level versioning in detail
- [[iceberg-table-versioning]] — Table-level versioning in detail
- [[lakekeeper]] — Table-level implementation
- [[apache-polaris]] — Table-level implementation with governance
- [[data-lakehouse-versioning-strategies]] — Broader versioning comparison
- [[lakefs-file-versioning]] — File-level versioning alternative
