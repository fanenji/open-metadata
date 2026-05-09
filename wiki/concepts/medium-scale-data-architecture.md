---
type: concept
title: Medium-Scale Data Architecture
created: 2025-02-10
updated: 2025-02-10
tags: [data-architecture, scale, lightweight-stack]
related: [duckdb-iceberg-sufficiency, duckdb, iceberg, vendor-lock-in-tradeoff, data-lakehouse, elt-pattern]
sources: ["Quando duckdb e iceberg sono sufficienti?.md"]
---
# Medium-Scale Data Architecture

The category of data architectures designed for teams processing a few TB of data per year, where full distributed systems (Spark, Snowflake, Databricks) are overkill but a simple database is insufficient.

## Characteristics

- **Data volume:** 1-10 TB/year, fitting comfortably on a single server or laptop.
- **Team size:** Small teams (1-10 people) with technical skills.
- **Workload type:** Batch processing, aggregations, joins, reporting.
- **Complexity tolerance:** Low — teams want simplicity over maximum performance.
- **Budget:** Limited — cloud warehouse costs are a significant concern.

## Typical Stack

- **Storage:** Object storage (S3, GCS) with an open table format ([[iceberg]], Delta Lake).
- **Compute:** Lightweight, single-node engines ([[duckdb]], [[pyarrow]]) for transformations and queries.
- **Orchestration:** Simple schedulers ([[kestra]], Airflow) or embedded in application code.
- **Ingestion:** Lightweight ELT frameworks ([[dlthub]]) or custom scripts.
- **Consumption:** Technical users running local DuckDB instances, or BI tools with embedded query engines ([[Rill]]).

## When to Consider

- Your data fits on a single machine.
- Your team has strong SQL/Python skills and can manage their own compute.
- You want to minimize vendor lock-in and operational complexity.
- Your consumers are technical and can use programmatic interfaces.

## When to Upgrade

- Data volume exceeds 2-3 TB and performance degrades.
- You need multi-user concurrent write access.
- You require RBAC, column-level security, or audit logging.
- Non-technical consumers need direct BI tool access.
- Query complexity requires distributed processing.

## Related Concepts

- [[duckdb-iceberg-sufficiency]] — A specific instantiation of this architecture.
- [[vendor-lock-in-tradeoff]] — The trade-off of avoiding vendor lock-in.
- [[data-lakehouse]] — A related but more enterprise-oriented architecture.