---
type: concept
title: Bulk Export
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, data-discovery, export, csv, api]
related: [bulk-import, openmetadata-features, openmetadata-administration, metadata-ingestion-workflow, service-connection, filter-patterns, soft-deletion]
sources: ["bulk-export-data-assets-via-csv-in-openmetadata----20260514.md"]
---

# Bulk Export

The bulk export feature in OpenMetadata allows users to download metadata for data assets as CSV files. This provides a simple way to extract metadata for offline analysis, documentation, or integration with external systems.

## Supported Asset Types

- **Database Service** — Export all metadata for a connected database service
- **Database** — Export metadata for a specific database within a service
- **Database Schema** — Export metadata for a specific schema within a database
- **Table** — Export metadata for a specific table within a schema

## UI Workflow

1. Navigate to the asset (e.g., Settings > Services > Database for a Database Service)
2. Click the ⋮ (ellipsis) icon on the asset row
3. Select **Export** from the dropdown menu
4. The CSV file is downloaded automatically

## API Endpoints

For programmatic export, the following REST API endpoints are available:

| Asset Type | Endpoint |
|---|---|
| Database Service | `/api/v1/services/databaseServices/name/{name}/export` |
| Database | `/api/v1/databases/name/{name}/export` |
| Database Schema | `/api/v1/databaseSchemas/name/{name}/export` |
| Table | `/api/v1/tables/name/{name}/export` |

Replace `{name}` with the [[Fully Qualified Name (FQN)]] of the asset.

## Relationship to Bulk Import

The OpenMetadata navigation includes a "Bulk Upload Data Assets" section with both "How to Bulk Import Data Asset" and "How to Export Data Asset" pages, suggesting that bulk import is a complementary feature. The relationship between export and import formats is not documented in this source.

## Open Questions

- What fields are included in the exported CSV?
- Are there limitations on export size or performance considerations for large datasets?
- Does the export include all metadata (tags, owners, descriptions, lineage) or just structural information?
- Can the exported CSV be used directly as input for bulk import?

## See Also

- [[bulk-import]] — Bulk import of data assets via CSV
- [[openmetadata-features]] — Comprehensive overview of OpenMetadata features
- [[openmetadata-administration]] — Administrative capabilities including export
- [[metadata-ingestion-workflow]] — The ingestion process (complementary to export)