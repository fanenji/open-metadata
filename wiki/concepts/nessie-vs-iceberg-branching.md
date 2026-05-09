---
type: concept
title: Nessie vs Iceberg Branching
created: 2026-05-07
updated: 2026-05-07
tags: [nessie, iceberg, branching, versioning, comparison]
related: [nessie-catalog-versioning, iceberg-table-versioning, data-lakehouse-versioning-strategies]
sources: ["Project Nessie Transactional Catalog for Data Lakes with Git-like semantics.md"]
---
# Nessie vs Iceberg Branching

Both Nessie and Apache Iceberg support branching and versioning, but at different levels of the stack and with different capabilities.

## Iceberg Native Branching (since v1.5.0)

- **Level**: Table-level
- **Scope**: Single table
- **Operations**: Branch, tag, merge within a single table
- **Atomicity**: Single-table atomic operations
- **Use case**: Time travel, experiment with a single table

## Nessie Catalog-Level Branching

- **Level**: Catalog-level
- **Scope**: Multiple tables across the entire catalog
- **Operations**: Branch, tag, merge, cherry-pick across tables
- **Atomicity**: Multi-table atomic commits
- **Use case**: ETL workflows involving multiple related tables, CI/CD for data pipelines

## Key Differences

| Feature | Iceberg Branching | Nessie Branching |
|---------|------------------|------------------|
| Scope | Single table | Multiple tables |
| Atomic commits | Single table | Multi-table |
| Merge conflicts | Table-level | Catalog-level (less documented) |
| Integration | Native to Iceberg | Requires Nessie catalog |
| Maturity | Since v1.5.0 (2023) | Since 2021 |

## When to Use Which

- **Use Iceberg branching** when working with a single table and needing time travel or isolated experiments on that table.
- **Use Nessie branching** when working with ETL pipelines that update multiple related tables and need atomic multi-table commits.

## Nuance

Since Iceberg v1.5.0 introduced native branching, Nessie's primary differentiator is no longer branching itself but **multi-table atomic transactions**. The "Git-like" analogy is useful but imprecise — Nessie's concrete value is in coordinating changes across tables, not just versioning a single table.