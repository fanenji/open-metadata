---
type: concept
title: pbit-based Lineage
created: 2026-05-14
updated: 2026-05-14
tags: [powerbi, lineage, pbit, dashboard, connectors]
related: [pbit-lineage, powerbi-connector, dashboard-lineage, data-lineage, powerbi-pbit-files]
sources: ["lineage-from-pbit-files---openmetadata-documentati-20260514.md"]
---

# pbit-based Lineage

pbit-based lineage is a method for generating traceability between data source tables, PowerBI datasets, and PowerBI reports by parsing .pbit files exported from PowerBI Desktop. It is a concrete implementation of [[dashboard-lineage]] specific to Microsoft PowerBI.

## How It Works

1. .pbit files are generated from PowerBI Desktop for each report.
2. The files are stored in a supported backend (local, Azure, S3, GCS).
3. The [[powerbi-connector]] retrieves the files, extracts them to a local directory (`pbitFilesExtractDir`), and parses their contents.
4. Table references found in the .pbit files are matched against the database services listed in `lineageInformation.dbServiceNames`.
5. Lineage edges are created: DataSource Tables ↔ PowerBI Datasets ↔ PowerBI Reports.

## Key Parameters

- **pbitFilesSource** — Specifies the storage backend and its configuration.
- **pbitFilesExtractDir** — Local directory for temporary extraction; must have write permissions.
- **dbServiceNames** — Critical parameter; without it, no table-level lineage will be created.

## Importance

This is the primary mechanism for capturing PowerBI lineage in OpenMetadata. Without it, PowerBI reports would appear as isolated assets with no connection to the underlying data sources. It bridges the gap between business-facing dashboards and the data infrastructure.

## Limitations

- The `local` source type requires the ingestion to run on the same machine as the .pbit files.
- Tables not listed in `dbServiceNames` will not produce lineage.
- Failure conditions (corrupted files, insufficient disk space) are not documented.