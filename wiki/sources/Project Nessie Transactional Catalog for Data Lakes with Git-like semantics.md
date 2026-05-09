---
type: source
title: "Project Nessie: Transactional Catalog for Data Lakes with Git-like semantics"
created: 2026-05-07
updated: 2026-05-07
tags: [nessie, data-lake, versioning, git-like, catalog]
related: [nessie-catalog-versioning, iceberg-table-versioning, data-lakehouse-versioning-strategies, dremio, nessie-multi-table-transactions, nessie-vs-iceberg-branching]
sources: ["Project Nessie Transactional Catalog for Data Lakes with Git-like semantics.md"]
---
# Project Nessie: Transactional Catalog for Data Lakes with Git-like semantics

**Author:** Dremio  
**Published:** 2021-09-27  
**URL:** https://www.dremio.com/blog/project-nessie-transactional-catalog-for-data-lakes-with-git-like-semantics/

This article introduces Project Nessie, an open-source transactional catalog that brings Git-like versioning semantics to data lakes built on table formats like Apache Iceberg and Delta Lake. It explains how Nessie extends the atomic single-table operations of Iceberg/Delta Lake to support multi-table atomic transactions, branching, merging, and tagging at the catalog level.

The article provides a technical walkthrough of Nessie's architecture: it manages versions of table metadata files (not data files), enabling efficient branch isolation for ETL workflows. Concrete code examples using PySpark and PyNessie demonstrate creating branches, creating tables on a dev branch, merging to main, and performing incremental ETL with schema evolution.

Key claims include: Nessie enables safe, isolated data development without copying data; multi-table atomic commits ensure consistency across related tables; and the Git-like model (commit, branch, tag, merge) aligns with how data engineers work. The article also clarifies that Nessie is "Git-like" — it uses similar concepts but is not built on Git itself, as that would be too slow.

This source strengthens the existing [[nessie-catalog-versioning]] page with detailed technical explanation and code examples, extends [[iceberg-table-versioning]] by showing how Nessie builds on Iceberg's snapshot model, and positions Nessie within the [[data-lakehouse-versioning-strategies]] framework as the catalog-level approach.