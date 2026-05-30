---
type: concept
title: Bulk Import via CSV
created: 2026-05-14
updated: 2026-05-14
tags: [csv-import, data-discovery, bulk-operations, metadata-ingestion]
related: [csv-import-fields-reference, data-discovery, bottom-up-top-down-enrichment, metadata-ingestion-workflow, service-connection, data-asset-ownership, classification-tags, glossary-terms, tiers, domain, snowflake]
sources: ["bulk-import-data-assets-via-csv-in-openmetadata----20260514.md"]
---

# Bulk Import via CSV

The Bulk Import via CSV feature in OpenMetadata allows users to create or update multiple data assets — Database Services, Databases, Database Schemas, and Tables — by uploading a CSV file. This provides an efficient alternative to manual UI entry for populating business metadata such as descriptions, owners, tags, glossary terms, tiers, and domains.

## Workflow

The general workflow for bulk importing data assets consists of the following steps:

1. **Navigate** to the parent asset (e.g., a Database Service for importing Databases).
2. **Click the ⋮ icon** and select **Import**.
3. **Upload or drop** a CSV file. Alternatively, export an existing asset's CSV as a template, edit it, and re-upload.
4. **Preview and edit** the CSV data using the inline editor.
5. **Validate** the changes. A success or failure message is displayed.
6. **Confirm** the changes to commit them.

## Asset Types and CSV Fields

Each asset type has a specific set of CSV fields. Required fields are marked.

### Database Service CSV Fields
- `name` (required)
- `fullyQualifiedName` (required)
- `displayName`
- `description`
- `owner`
- `tags`
- `glossaryTerms`
- `tiers`
- `domain`

### Database CSV Fields
- `name` (required)
- `fullyQualifiedName` (required)
- `displayName`
- `description`
- `owner`
- `tags`
- `glossaryTerms`
- `tiers`
- `sourceUrl`
- `retentionPeriod` (ISO 8601 duration)
- `domain`

### Database Schema CSV Fields
- `name` (required)
- `fullyQualifiedName` (required)
- `displayName`
- `description`
- `owner`
- `tags`
- `glossaryTerms`
- `tiers`
- `sourceUrl`
- `retentionPeriod` (ISO 8601 duration)

### Table CSV Fields
- `name`
- `fullyQualifiedName` (required)
- `displayName`
- `description`
- `owner`
- `tags`
- `glossaryTerms`
- `tiers`
- `sourceUrl`
- `retentionPeriod` (ISO 8601 duration)
- `column.fullyQualifiedName` (required)
- `column.displayName`
- `column.description`
- `column.dataTypeDisplay`
- `column.dataType`
- `column.arrayDataType`
- `column.dataLength`
- `column.tags`
- `column.glossaryTerms`

## API Endpoints

Each asset type can also be imported programmatically via a dedicated API endpoint:

- **Database Service:** `POST /api/v1/services/databaseServices/name/{name}/import`
- **Database:** `POST /api/v1/databases/name/{name}/import`
- **Database Schema:** `POST /api/v1/databaseSchemas/name/{name}/import`
- **Table:** `POST /api/v1/tables/name/{name}/import`

Replace `{name}` with the Fully Qualified Name (FQN) of the asset.

## Relationship to Other Metadata Population Methods

The CSV bulk import is a **top-down enrichment** method, complementing the **bottom-up** metadata ingestion from infrastructure via [[metadata-ingestion-workflow|ingestion pipelines]]. While ingestion pipelines discover schema structure and technical metadata automatically, CSV import allows users to efficiently add business context (descriptions, ownership, classification, domains) to existing assets.

## Open Questions

- Whether CSV import supports **updates** to existing assets or only creation of new ones. The export-as-template workflow suggests updates are possible, but this is not explicitly documented.
- Error handling behavior for **partial failures** (some rows succeed, others fail).
- **Maximum file size** or row limit for CSV uploads.
- Interaction with **RBAC/ABAC permissions** — whether non-Admin users can import assets into services they do not own.
- How CSV import interacts with **owner propagation** and **tag inheritance** mechanisms.