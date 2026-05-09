---
type: source
title: "Quando duckdb e iceberg sono sufficienti?"
created: 2025-02-10
updated: 2025-02-10
tags: [reddit, duckdb, iceberg, data-architecture, discussion]
related: [duckdb, iceberg, duckdb-iceberg-sufficiency, duckdb-iceberg-limitations, single-user-database-limitation, medium-scale-data-architecture, vendor-lock-in-tradeoff, embedded-query-engine-for-bi]
sources: ["Quando duckdb e iceberg sono sufficienti?.md"]
authors: [haragoshi]
year: 2025
url: "https://www.reddit.com/r/dataengineering/comments/1im5kgl/when_is_duckdb_and_iceberg_enough/"
venue: Reddit r/dataengineering
---
# Quando duckdb e iceberg sono sufficienti?

A Reddit discussion exploring the viability of using [[duckdb]] as a lightweight, in-process compute engine combined with [[iceberg]] as a file-based storage format on object storage (e.g., S3) as an alternative to traditional data warehouses for medium-scale workloads.

## Summary

The original poster ([[haragoshi]]) proposes that DuckDB + Iceberg on S3 could simplify architecture, reduce vendor lock-in, and lower costs for teams processing a few TB of data per year. The discussion reveals a nuanced consensus: the stack is viable for small-to-medium workloads and technical consumers, but has significant limitations including DuckDB's single-user design, lack of Iceberg catalog read support, lack of native Iceberg write support, poor predicate pushdown, and absence of RBAC/column-level security.

## Key Points

- **Core proposition:** DuckDB for in-process ETL/transformation + Iceberg on S3 for ACID-compliant storage can replace full data warehouses for many teams.
- **Single-user limitation:** DuckDB is designed for single-user, local use. Multiple concurrent users require workarounds.
- **Iceberg integration gaps:** DuckDB cannot read Iceberg Catalogs, cannot write to Iceberg natively, and has poor predicate pushdown for Iceberg files.
- **Scale threshold:** Commenters suggest the stack works well for datasets under 1-2 TB. Beyond that, dedicated warehouses or distributed systems become necessary.
- **Consumer type matters:** The architecture is sufficient when consumers are technical (data scientists, analysts who can run DuckDB locally) and can manage shared views via git (dbt, sqlmesh).
- **Future direction:** BI tools embedding DuckDB-like engines (e.g., [[Rill]]) could make this architecture mainstream, eliminating the need for dedicated warehouses for most organizations.
- **Historical caution:** A commenter draws a parallel to Hadoop's overpromise, warning that "storage is cheap, storage performance is not" and that avoiding vendor lock-in means losing vendor-specific optimizations.

## Notable Comments

- [[caksters]] highlights DuckDB's single-user design as a fundamental limitation for team sharing.
- [[patate_volante]] clarifies that OP refers to Iceberg files on shared S3 storage, not local DuckDB files.
- [[unexpectedreboots]] notes DuckDB does not yet support writing to Iceberg.
- [[pknpkn21]] notes DuckDB lacks Iceberg Catalog read support.
- [[pescennius]] suggests the architecture is sufficient when consumers are technical and can run DuckDB locally.
- [[LargeSale8354]] warns about historical parallels with Hadoop and the trade-off of losing vendor advantages.
- [[aacreans]] criticizes DuckDB's poor Iceberg support (no catalog, no predicate pushdown).
- [[mertertrern]] recommends PyIceberg + DuckDB for better Iceberg compatibility.
- [[turbolytics]] notes DuckDB lacks RBAC/column-level security.
- [[Mythozz2020]] reports a successful PoC using DuckDB to execute PySpark code on Parquet files.

## Relevance

This source provides a practical, community-driven perspective on the limits of lightweight data architectures. It challenges the implicit assumption that a full data warehouse is always necessary, while also tempering enthusiasm with concrete technical limitations. It connects to the wiki's existing coverage of [[duckdb]], [[iceberg]], [[data-lakehouse]], and [[elt-pattern]].