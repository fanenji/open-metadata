type: concept
title: Dremio Lakehouse Lifecycle
created: 2026-04-22
updated: 2026-04-22
tags: [dremio, lakehouse, architecture, workflow]
related: [dremio, nessie-catalog-versioning, iceberg-table-versioning, dbt, dremio-reflections, data-lakehouse, write-audit-publish-pattern, data-as-code]
sources: ["dremio-lakehouse-in-action-with-iceberg-dbt.md"]
---
# Dremio Lakehouse Lifecycle

The Dremio Lakehouse Lifecycle is an end-to-end workflow for building and managing a data lakehouse using Dremio, Nessie, Apache Iceberg, and dbt. It covers the full journey from data ingestion to BI dashboard delivery, emphasizing [[data-as-code]] principles and catalog-level versioning.

## Stages

1. **Environment Setup** — Deploying Dremio, Nessie (catalog), Minio (object storage), source databases (PostgreSQL, MongoDB), and BI tools (Apache Superset) — typically via Docker for development.
2. **Data Source Connection** — Connecting Dremio to source databases and the Nessie catalog (backed by Minio) through the Dremio UI or APIs.
3. **Data Ingestion into Iceberg** — Using Dremio SQL (`CREATE TABLE AS`, `INSERT INTO`, `MERGE INTO`, `COPY INTO`) to move data from source systems into Apache Iceberg tables cataloged by Nessie.
4. **Isolated Ingestion with Nessie Branches** — Creating Nessie branches for isolated data ingestion, running validation on the branch, and merging to main only after validation passes. This implements the [[write-audit-publish-pattern]] at the catalog level.
5. **Semantic Layer Curation with dbt** — Using dbt-dremio to define and materialize views organized in a three-layer structure (raw/curated/production). dbt provides SQL versioning via Git, adding a second layer of observability alongside Nessie's catalog commits.
6. **Query Acceleration with Reflections** — Enabling Dremio Reflections (managed materialized Iceberg tables) to accelerate BI queries without vendor lock-in.
7. **BI Dashboarding** — Connecting BI tools (e.g., Apache Superset) to Dremio via Arrow Flight and building dashboards on the curated views.

## Key Principles

- **Data-as-Code** — All transformations are managed through version-controlled code (dbt SQL + Git) and catalog-level versioning (Nessie).
- **Separation of Concerns** — Raw data ingestion is isolated from production via Nessie branches; the semantic layer is curated separately from raw storage.
- **Open Standards** — Apache Iceberg for table format, Arrow Flight for high-performance connectivity, and SQL for all operations.
- **Performance Without Lock-In** — Reflections accelerate queries across any BI tool, avoiding vendor-specific cubes or extracts.

## Relationship to Other Concepts

- Implements the [[write-audit-publish-pattern]] naturally through Nessie branching.
- Extends [[data-lakehouse-versioning-strategies]] by demonstrating Nessie's branch/merge workflow in action.
- Relates to [[data-ingestion-architectural-patterns]] (ELT pattern) and [[self-serve-data-platform]].
- The folder structure (raw/curated/production) hints at domain-oriented organization relevant to [[data-mesh]].