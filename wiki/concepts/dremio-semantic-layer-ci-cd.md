---
type: concept
title: Dremio Semantic Layer CI/CD
created: 2026-05-06
updated: 2026-05-06
tags: [dremio, dbt, ci-cd, semantic-layer, data-engineering]
related: [dremio, dbt-dremio-adapter, dremio-reflections, dremio-dataset-promotion, dremio-twin-strategy, CI-CD-for-data-pipelines, iceberg-table-versioning, dbt-macros, data-lakehouse]
sources: ["Semantic Layer CI-CD with Dremio and dbt.md"]
---
# Dremio Semantic Layer CI/CD

The Dremio semantic layer is a virtual data layer defined via views, spaces, folders, UDFs, and security policies in Dremio. This concept covers how to define, version, and deploy this semantic layer using dbt in a CI/CD pipeline.

## Core Principles

1. **Separation of Concerns**: Physical tables (Iceberg) live in object storage; views live in Dremio spaces. They follow different rules and are managed separately.
2. **Idempotent Creation**: Dremio objects that support `CREATE OR REPLACE` syntax are compatible with dbt's SQL-first approach.
3. **Version Control**: All semantic layer definitions are stored in git, enabling automated deployment across environments.

## Dremio Objects in dbt

### Objects creatable via SQL in dbt:
- Views
- Tables (promoting existing datasets)
- Iceberg tables (creating or updating datasets)
- Spaces & folders
- User-defined functions (UDFs)
- Row- & column-level security (using UDFs)
- RBAC privileges (grants)

### Objects creatable via dbt connector:
- Reflections

### Objects NOT creatable via dbt:
- Sources (recommended separate workflow due to secrets)
- Wikis & tags (not supported via SQL as of Dremio 24.3)

## Materialization Strategies

- **View**: Default materialization for semantic layer definitions
- **Table**: Creates Iceberg tables in object storage with corresponding views in Dremio spaces
- **Incremental**: Appends new records to existing Iceberg tables
- **Reflection**: Dremio-specific acceleration objects

## CI/CD Workflow

The typical workflow involves:
1. Define Dremio objects in dbt models within a git repository
2. Use dbt's on-run-start and on-run-end hooks for UDF creation and RBAC grants
3. Run `dbt run` to deploy changes to the target environment
4. Run `dbt test` to validate data quality after deployment

## Required Privileges

The service user account requires:
- Read access to INFORMATION_SCHEMA tables
- Read access to reflection system table
- Read/write access to data sources and target spaces/folders