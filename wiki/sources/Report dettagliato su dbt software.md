---
type: source
title: "Report dettagliato su dbt software"
created: 2026-03-15
updated: 2026-03-15
tags: [dbt, analytics-engineering, data-lakehouse, duckdb, dremio, iceberg, medallion-architecture]
related: [dbt-core-vs-platform, dbt-duckdb-adapter, dbt-dremio-adapter, dbt-project-structure, dbt-local-first-development, dbt-iceberg-catalog-integration, dbt-naming-conventions, dbt-project-scaffolding, dbt-git-branching-strategies, dbt-testing-patterns, dbt-macros, dbt-cloud, dremio, duckdb, iceberg-table-versioning, elt-pattern, data-lakehouse]
sources: ["Report dettagliato su dbt software.md"]
---
# Report dettagliato su dbt software

A comprehensive guide to architecting a modern data lakehouse with dbt, covering the full spectrum from local development with DuckDB to production deployment with Dremio and Iceberg. The report positions dbt as an analytics engineering framework that applies software engineering best practices (version control, modularity, automated testing, CI/CD) to data transformation within the ELT paradigm.

## Key Topics

- **dbt Core vs. dbt Platform (Cloud):** Detailed comparison table covering development environment, job scheduling, CI/CD, documentation hosting, monitoring, cost, and management. Core is free and open-source but requires manual orchestration; Platform is a managed SaaS with integrated IDE, scheduler, and alerting.

- **Local-First Development Paradigm:** The combination of dbt-duckdb adapter with S3 access creates a "serverless, local-first lakehouse," disconnecting development workflow from expensive cloud compute. Developers can run entire ELT pipelines on their laptop, interacting with cloud only for storage I/O.

- **Medallion Architecture:** Bronze (raw data on S3), Silver (cleansed/conformed), Gold (curated/aggregated) layers mapped to dbt staging, intermediate, and marts model layers.

- **Apache Iceberg Integration:** Two approaches — legacy (table_format config) and modern recommended catalog integration that centralizes catalog configuration. dbt manages base_location automatically to prevent technical debt.

- **Dremio Adapter Configuration:** Detailed parameter table for dbt-dremio adapter covering Cloud and Software variants, including authentication via PAT, object storage source, and Dremio space configuration.

- **DuckDB Adapter Configuration:** Detailed parameter table for dbt-duckdb adapter with S3 integration via httpfs extension, including settings for s3_region, s3_access_key_id, and s3_secret_access_key.

- **Project Structure Best Practices:** Separation of concerns across staging (source interface), intermediate (business logic), and marts (presentation) layers. Naming conventions for models, columns, and sources.

- **Testing and Documentation:** Shift-left testing philosophy, generic tests (unique, not_null, accepted_values, relationships), singular custom tests, and YAML-based documentation.

- **Git Branching Strategies:** Direct Promotion (GitHub Flow) for small teams and rapid releases; Indirect Promotion (GitFlow) for larger teams with staging environments.

## Architecture Reference

The report presents a reference architecture for a lakehouse pipeline: S3 (Bronze Parquet files) → Query Engine (DuckDB for dev, Dremio for prod) → dbt (staging/intermediate/marts transformations) → S3 (Silver/Gold Iceberg/Parquet tables).

## Key Design Decisions

- Separation of `dbt_project.yml` (code configuration) and `profiles.yml` (credentials) is a deliberate security mechanism preventing accidental credential commits.
- DuckDB for local development, Dremio for production — dual-engine architecture requiring maintaining two configurations.
- Catalog integration is the recommended modern approach for Iceberg table management over legacy table_format configuration.

## Strengths

- Detailed, actionable configuration examples for both DuckDB and Dremio adapters
- Clear comparison table for Core vs. Platform decision
- Practical step-by-step tutorial for project initialization
- Strong emphasis on security patterns and best practices

## Limitations

- Assumes S3 as the only storage layer (no GCS, Azure Blob)
- No discussion of dbt Mesh or multi-project architectures
- DuckDB local-first paradigm requires developers to manage S3 credentials locally
- Does not address performance trade-offs between DuckDB and Dremio for production workloads