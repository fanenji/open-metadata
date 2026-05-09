type: entity
title: Dremio Semantic Layer CI/CD
created: 2026-05-07
updated: 2026-05-07
tags: [dremio, dbt, ci-cd, semantic-layer]
related: [dremio, dbt-dremio-adapter, dremio-dbt-connector-configuration, dremio-reflection-management, dremio-dataset-promotion, dremio-rbac-via-dbt, CI-CD-for-data-pipelines, iceberg-table-versioning]
sources: ["semantic-layer-ci-cd-with-dremio-and-dbt.pdf"]
---
# Dremio Semantic Layer CI/CD

The Dremio Semantic Layer CI/CD pattern defines a complete workflow for managing a Dremio semantic layer (views, tables, reflections, UDFs, RBAC, security policies) in a version-controlled repository and deploying it via dbt. This enables automated, coordinated, and reported deployments of Dremio objects across environments.

## Core Principles

- **SQL-first**: Most Dremio objects support idempotent SQL creation via dbt
- **Strict separation**: Iceberg tables live in object storage sources; views live in Dremio spaces
- **Idempotent deployment**: All objects can be recreated without side effects
- **CI/CD integration**: Full pipeline from code commit to production deployment

## Objects Managed

| Object | Method | Notes |
|--------|--------|-------|
| Views | SQL via dbt | Default materialization |
| Tables (Iceberg) | SQL via dbt | Object storage source required |
| Incremental tables | SQL via dbt | Uses Iceberg DML |
| Spaces & Folders | REST calls via dbt connector | Auto-created from folder structure |
| UDFs | SQL via dbt macros | Must be created before dependent views |
| Reflections | dbt connector materialization | Requires `reflections_enabled: true` |
| RBAC grants | SQL via dbt hooks | Folder/space level recommended |
| Row/Column security | SQL via dbt post-hooks | Uses UDFs for policies |

## Objects NOT Managed via dbt

- Sources (require REST API or manual setup)
- Wikis & Tags (no SQL support in Dremio)
- Users & Roles (recommended via IDP)

## Example Project Structure

```
dbt_cicd_demo/
├── dbt_project.yml
├── macros/
│   └── create_udf.sql
└── models/
    └── demo/
        ├── nyc_taxi_trips.sql
        ├── nyc_taxi_trips_refl.sql
        └── nyc_taxi_trips_rls.sql
```

## Key Configuration

- `twin_strategy`: Prevents/enforces identical table/view paths
- `reflections_enabled`: Enables reflection materialization type
- `object_storage_source`: Specifies the object storage source for Iceberg tables
- `object_storage_path`: Path within the object storage source

## Deployment Sequence

1. On-run-start hooks (UDF creation)
2. View/table model execution (DAG-ordered)
3. Reflection model execution
4. On-run-end hooks (RBAC grants)
5. Automated data quality tests
