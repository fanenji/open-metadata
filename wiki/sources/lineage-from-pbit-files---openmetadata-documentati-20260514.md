---
type: source
title: "Lineage from pbit files - OpenMetadata Documentation"
created: 2026-05-14
updated: 2026-05-14
tags: [powerbi, lineage, pbit, connectors, dashboard]
related: [pbit-lineage, powerbi-connector, dashboard-lineage, data-lineage, powerbi-pbit-files]
sources: ["lineage-from-pbit-files---openmetadata-documentati-20260514.md"]
---

# Lineage from pbit files - OpenMetadata Documentation

This source is the official OpenMetadata documentation page for generating lineage between data source tables, PowerBI datasets, and PowerBI reports by parsing .pbit files exported from PowerBI Desktop. It covers the complete 4-step workflow: generating .pbit files, selecting a storage backend (local, Azure, S3, GCS), configuring the source with the PowerBI connector, and running the connector. The page provides YAML configuration examples for all four storage backends and emphasizes the critical `dbServiceNames` parameter under `lineageInformation` for linking PowerBI datasets to underlying database tables.

## Key Points

- .pbit files are PowerBI Desktop project files that contain report definitions and data source references.
- The connector parses .pbit files to create lineage: DataSource Tables ↔ PowerBI Datasets ↔ PowerBI Reports.
- Four storage backends are supported: local, Azure, S3, GCS.
- The `pbitFilesExtractDir` parameter specifies a local directory for extraction; it is created automatically if missing and must have write permissions.
- The `dbServiceNames` parameter under `lineageInformation` lists database services (e.g., `snowflake_service`, `redshift_service`) to match table references.
- For the `local` source type, the ingestion must run on the same system as the .pbit files.