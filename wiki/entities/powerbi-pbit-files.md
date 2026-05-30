---
type: entity
title: PowerBI pbit Files
created: 2026-05-14
updated: 2026-05-14
tags: [powerbi, pbit, files, lineage, connectors]
related: [pbit-lineage, powerbi-connector, dashboard-lineage]
sources: ["lineage-from-pbit-files---openmetadata-documentati-20260514.md"]
---

# PowerBI pbit Files

.pbit files are PowerBI Desktop project files that contain report definitions, visual layouts, and data source references. They are the input format used by the [[pbit-lineage]] feature of the [[powerbi-connector]] to generate dashboard-to-table lineage.

## Generation

.pbit files are exported from PowerBI Desktop. Each .pbit file corresponds to a single PowerBI report. The export process is documented in the official PowerBI documentation.

## Storage Options

.pbit files can be stored in any of the following locations for ingestion by the PowerBI connector:

- **Local filesystem** — Requires the ingestion process to run on the same machine.
- **Azure Data Lake** — Requires Azure storage credentials.
- **Amazon S3** — Requires AWS access credentials.
- **Google Cloud Storage** — Requires GCP service account credentials.

## Permissions

- The `pbitFilesExtractDir` (the local directory where files are extracted) must have write permissions.
- Sufficient disk space must be available for extraction.
- For cloud storage backends, appropriate read permissions on the bucket/container are required.

## Relationship to Lineage

The PowerBI connector parses .pbit files to extract references to data source tables. These references are matched against the database services listed in `lineageInformation.dbServiceNames` to create lineage links between the underlying tables and the PowerBI datasets/reports.