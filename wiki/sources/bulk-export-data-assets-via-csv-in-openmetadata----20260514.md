---
type: source
title: Bulk Export Data Assets via CSV in OpenMetadata
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, data-discovery, export, csv, api]
related: [bulk-export, bulk-import, openmetadata-features, openmetadata-administration, snowflake]
sources: ["bulk-export-data-assets-via-csv-in-openmetadata----20260514.md"]
---

# Bulk Export Data Assets via CSV in OpenMetadata

Official documentation page (v1.12.x) covering the bulk export of data assets (Database Services, Databases, Schemas, and Tables) as CSV files via the UI and API. The source uses Snowflake as the reference example but the feature works for any database service.

## Key Content

- **Supported asset types**: Database Service, Database, Database Schema, Table
- **UI workflow**: Navigate to the asset, click the ⋮ icon, select Export
- **API endpoints**:
  - `/api/v1/services/databaseServices/name/{name}/export`
  - `/api/v1/databases/name/{name}/export`
  - `/api/v1/databaseSchemas/name/{name}/export`
  - `/api/v1/tables/name/{name}/export`
- **Authentication**: API calls require the Fully Qualified Name (FQN) of the asset

## Related Pages

- [[bulk-export]] — Concept page for the bulk export feature
- [[bulk-import]] — Related bulk import feature (referenced in navigation)
- [[openmetadata-features]] — Comprehensive feature overview
- [[openmetadata-administration]] — Administrative capabilities
- [[snowflake]] — Reference example for export operations