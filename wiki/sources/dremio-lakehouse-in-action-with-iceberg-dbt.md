type: source
title: "Dremio Lakehouse in Action with Iceberg & dbt"
created: 2026-04-22
updated: 2026-04-22
tags: [dremio, nessie, iceberg, dbt, data-lakehouse, data-as-code, hands-on]
related: [alex-merced, dremio, nessie-catalog-versioning, iceberg-table-versioning, dbt, data-lakehouse, write-audit-publish-pattern, dremio-reflections, dbt-dremio, apache-superset, minio, postgresql, mongodb]
sources: ["dremio-lakehouse-in-action-with-iceberg-dbt.md"]
---
# Dremio Lakehouse in Action with Iceberg & dbt

A hands-on tutorial by Alex Merced (Dremio Developer Advocate) demonstrating the complete Dremio Lakehouse lifecycle — from data ingestion to BI dashboards — using Dremio, Nessie, Apache Iceberg, dbt, and Apache Superset in a local Docker environment.

## Summary

The guide walks through setting up a full data lakehouse stack locally via Docker Compose, including Nessie (catalog), Minio (object storage), Dremio (query engine), PostgreSQL and MongoDB (source databases), and Apache Superset (BI). It covers:

1. **Data Ingestion** — Using Dremio SQL (`CREATE TABLE AS`, `INSERT INTO`) to move data from PostgreSQL and MongoDB into Iceberg tables cataloged by Nessie and stored in Minio.
2. **Data-as-Code with Nessie** — Creating branches for isolated data ingestion, validating on the branch, then merging to main. Demonstrates the [[write-audit-publish-pattern]] at the catalog level.
3. **Semantic Layer Curation with dbt** — Using dbt-dremio to define and materialize views (raw tables, curated views, production views) organized in a three-layer folder structure (raw/curated/production).
4. **Query Acceleration with Reflections** — Enabling Dremio Reflections (managed materialized Iceberg tables) to accelerate BI queries without vendor lock-in.
5. **BI Dashboarding** — Connecting Apache Superset to Dremio via Arrow Flight and building dashboards.

## Key Takeaways

- The Dremio + Nessie + Iceberg + dbt stack provides a complete, performant, and easy-to-maintain data lakehouse lifecycle.
- Nessie's catalog-level versioning enables isolated data ingestion and validation before publishing, implementing the Write-Audit-Publish pattern naturally.
- dbt provides a second layer of observability (via Git) alongside Nessie's catalog commits.
- Dremio Reflections accelerate BI queries across any tool without traditional BI cubes/extracts.

## Caveats

- The guide uses small, static datasets — production scaling considerations are not addressed.
- The incremental ingestion pattern (`INSERT INTO ... WHERE product_id > (SELECT MAX(...))`) is simplified and assumes append-only data with monotonically increasing IDs.
- The local Docker setup is a learning tool, not a production deployment pattern.
- The gap between Dremio OSS (used here) and Dremio Cloud (Text-to-SQL, AI Wiki, autoscaling) is not explored.

## Author

- [[alex-merced]] — Dremio Developer Advocate

## Published

2024-04-25

## URL

https://www.dremio.com/blog/experience-the-dremio-lakehouse-hands-on-with-dremio-nessie-iceberg-data-as-code-and-dbt/