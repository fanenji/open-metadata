type: entity
title: Dremio dbt Connector Configuration
created: 2026-05-07
updated: 2026-05-07
tags: [dremio, dbt, configuration, connector]
related: [dremio, dbt-dremio-adapter, dremio-semantic-layer-ci-cd, dremio-reflection-management]
sources: ["semantic-layer-ci-cd-with-dremio-and-dbt.pdf"]
---
# Dremio dbt Connector Configuration

The Dremio dbt connector provides several configuration options that control how dbt interacts with Dremio. These are set in the `dbt_project.yml` file or in model-level config blocks.

## Key Configuration Parameters

### `twin_strategy`
Controls whether tables and views can have identical paths and names in the same Dremio environment. Can prevent or enforce this behavior.

### `reflections_enabled`
Boolean variable (`dremio:reflections_enabled`) that enables the reflection materialization type in dbt models. When `true`, models with `materialized='reflection'` can be created.

### `object_storage_source`
Specifies the object storage source (e.g., S3, ADLS) where Iceberg tables will be created. Required for table and incremental materializations.

### `object_storage_path`
Path within the object storage source where Iceberg tables will be stored.

### `database` and `schema`
Override the default Dremio space and folder path for view creation. The `database` parameter maps to the Dremio space, and `schema` maps to the folder/subfolder path.

### `alias`
Overrides the view or table name in Dremio.

## Required Privileges

The dbt service user requires:
- Read access to `INFORMATION_SCHEMA` tables
- Read access to `sys.reflections` system table
- Read access to data sources (`SELECT`, `ALTER`)
- Write access to target data sources (`SELECT`, `ALTER`, `CREATE TABLE`, `DROP`, `INSERT`)
- Write access to target spaces/folders (`SELECT`, `ALTER`, `VIEW REFLECTION`, `ALTER REFLECTION`)
