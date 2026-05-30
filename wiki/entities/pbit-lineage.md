---
type: entity
title: pbit Lineage
created: 2026-05-14
updated: 2026-05-14
tags: [powerbi, lineage, pbit, connectors, dashboard]
related: [powerbi-connector, powerbi-pbit-files, dashboard-lineage, data-lineage, openmetadata-connectors]
sources: ["lineage-from-pbit-files---openmetadata-documentati-20260514.md"]
---

# pbit Lineage

pbit Lineage is a feature of the [[powerbi-connector]] that generates traceability from data source tables through PowerBI datasets to PowerBI reports by parsing .pbit files exported from PowerBI Desktop. It is the primary mechanism for capturing PowerBI dashboard lineage in OpenMetadata.

## Workflow

1. **Generate .pbit files** — Export .pbit files from PowerBI Desktop for each report.
2. **Select storage backend** — Choose one of four supported backends: local, Azure, S3, or GCS.
3. **Configure the source** — Add the `pbitFilesSource` configuration block to the PowerBI connector YAML, specifying the storage backend, credentials, and extraction directory.
4. **Run the connector** — The connector gathers .pbit files, extracts them to the `pbitFilesExtractDir`, and parses the contents to create lineage.

## Configuration Parameters

- **pbitFilesSource** — Configuration block specifying the storage backend and its credentials.
- **pbitFilesExtractDir** — Local directory path where .pbit files are extracted; created automatically if missing. Must have write permissions.
- **lineageInformation.dbServiceNames** — List of database service names (e.g., `snowflake_service`, `redshift_service`) used to match table references found in .pbit files. Without this, no table-level lineage will appear.

## Storage Backends

- **local** — Provide the full path to the folder containing .pbit files. The ingestion must run on the same system.
- **Azure** — Store files in an Azure Data Lake bucket; configure with `clientId`, `clientSecret`, `tenantId`, `accountName`.
- **S3** — Store files in an S3 bucket; configure with AWS credentials (`awsAccessKeyId`, `awsSecretAccessKey`, `awsRegion`).
- **GCS** — Store files in a GCS bucket; configure with GCP service account credentials.

## Limitations

- For the `local` source type, the ingestion process must run on the same machine as the .pbit files, which may conflict with containerized or remote ingestion setups.
- The `pbitFilesExtractDir` must have sufficient disk space and write permissions; failure conditions (corrupted files, insufficient space) are not documented.
- Tables referenced in .pbit files that are not listed in `dbServiceNames` will not produce lineage.