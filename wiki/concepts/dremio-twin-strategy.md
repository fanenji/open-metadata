---
type: concept
title: Dremio Twin Strategy
created: 2026-05-06
updated: 2026-05-06
tags: [dremio, dbt, configuration, materialization]
related: [dremio, dbt-dremio-adapter, dremio-semantic-layer-ci-cd]
sources: ["Semantic Layer CI-CD with Dremio and dbt.md"]
---
# Dremio Twin Strategy

The twin strategy is a configuration setting in the Dremio dbt connector that prevents or enforces having tables and views with identical paths and names inside the same Dremio environment.

## Purpose

Dremio has a strict separation of tables and views unless using Dremio's lakehouse management service or the Nessie catalog. Object storage sources only allow Iceberg table creation, while Dremio spaces and folders only allow view creation. The twin strategy setting manages the relationship between these two object types when they share the same logical path.

## Usage

The `twin_strategy` setting is configured in the dbt project's YAML configuration. It can be set to:
- Prevent identical table/view paths
- Enforce identical table/view paths

This ensures consistency between the physical data materialization (Iceberg tables in object storage) and the virtual semantic layer (views in Dremio spaces).