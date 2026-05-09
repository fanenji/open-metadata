---
type: concept
title: Nessie Multi-Table Transactions
created: 2026-04-04
updated: 2026-05-07
tags: [nessie, transactions, data-lakehouse, catalog, atomicity, multi-table, data-lake]
related: [project-nessie, nessie-branch-merge-workflow, nessie-catalog-versioning, apache-iceberg, iceberg-table-versioning, data-lakehouse-versioning-strategies]
sources: ["Open Source and the Data Lakehouse Iceberg and Project Nessie.md", "Project Nessie Transactional Catalog for Data Lakes with Git-like semantics.md"]
---

# Nessie Multi-Table Transactions

[[Project Nessie]] extends [[Apache Iceberg]]'s (and other table formats') single-table ACID transactions to the catalog level, allowing multiple table changes to be grouped together in a single atomic transaction. This ensures consistency across multiple table modifications — for example, updating a fact table and its associated dimension tables atomically. This capability is critical for maintaining data integrity in complex data pipelines where changes to multiple tables must be coordinated. It is a key differentiator from Iceberg's native table-level transactions, providing an additional layer of consistency at the catalog level.

## Problem

Traditional table formats such as Apache Iceberg and Delta Lake provide atomic operations only at the **single-table level**. This means:
- Data loaded into a temporary table risks exposure to production until explicitly promoted.
- Related changes to multiple tables (e.g., a fact and its dimensions) are disconnected and not committed together.
- There is no atomic "all-or-nothing" commit across a set of tables.
- Rolling back multi-table changes is difficult or impossible without external coordination.

## Solution

Nessie extends the catalog layer to support multi-table atomic transactions. Using Nessie's Git-like branching model, changes to multiple tables can be made on a development branch. When that branch is merged into `main`, all table changes (creations, updates, schema modifications) are committed atomically. Either all changes appear, or none appear. This multi-table atomicity is achieved by version-controlling the metadata pointers for all tables involved in a transaction at the catalog level.

## Practical Impact

- **ETL workflows**: Load data into multiple related tables on a dev branch, validate correctness, then merge atomically into production.
- **Schema evolution**: Change schemas across multiple tables in one atomic operation, avoiding version mismatches.
- **Incremental ETL**: Apply updates to multiple tables on a branch, then merge to keep the warehouse consistent.
- **Rollback**: Undo a merge to revert multiple tables to a previous consistent state, simplifying recovery.

## Relationship to Iceberg and Delta Lake

Nessie does not replace Apache Iceberg or Delta Lake — it builds on top of them. Iceberg and Delta Lake handle single-table atomic operations (e.g., file-level commits). Nessie coordinates multi-table atomicity at the catalog level by version-controlling the metadata pointers for all tables involved in a transaction. Together, they provide both fine-grained table-level transactions and coarse-grained catalog-level multi-table transactions.

## Open Questions

- How does Nessie handle merge conflicts when two branches modify the same table?
- What is the performance overhead of Nessie's multi-table transactions compared to sequential single-table operations?