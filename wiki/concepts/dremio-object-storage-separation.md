type: concept
title: Dremio Object Storage Separation
created: 2026-05-07
updated: 2026-05-07
tags: [dremio, architecture, object-storage, iceberg]
related: [dremio, dremio-semantic-layer, dremio-dbt-connector-configuration, iceberg-table-versioning]
sources: ["semantic-layer-ci-cd-with-dremio-and-dbt.pdf"]
---
# Dremio Object Storage Separation

A critical architectural constraint in Dremio is the strict separation between object storage sources and Dremio spaces. Object storage sources (like S3 or ADLS) only allow the creation of Iceberg tables, while traditional Dremio spaces and folders only allow the creation of views.

## Implications

- **Table materializations**: Iceberg tables are created in object storage sources, not in Dremio spaces
- **View materializations**: Views are created in Dremio spaces, referencing tables in object storage
- **Incremental materializations**: Follow the same pattern — Iceberg table in object storage + view in Dremio space
- **Twin strategy**: The Dremio dbt connector can prevent or enforce having tables and views with identical paths and names

## Workflow

When a dbt model with `materialized='table'` is run:
1. An Iceberg table is created in the specified object storage source
2. A corresponding view is automatically created in the Dremio space
3. The view references the physical table in object storage

This separation ensures that the semantic layer (views) remains virtual and governed, while physical data resides in scalable object storage.
