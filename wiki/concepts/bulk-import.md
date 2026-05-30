---
type: concept
title: Bulk Import
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, data-discovery, import, csv]
related: [bulk-export, openmetadata-features, openmetadata-administration]
sources: ["bulk-export-data-assets-via-csv-in-openmetadata----20260514.md"]
---

# Bulk Import

The bulk import feature in OpenMetadata allows users to upload metadata for data assets via CSV files. This feature is referenced in the OpenMetadata navigation under "Bulk Upload Data Assets" alongside [[bulk-export]], but its detailed documentation is not covered in the current source material.

## Relationship to Bulk Export

The navigation structure suggests that bulk import and bulk export are complementary features within the Data Discovery section. The export feature produces CSV files that may be compatible with the import workflow, but this relationship is not explicitly documented in the available sources.

## Open Questions

- What is the exact CSV format required for bulk import?
- Does bulk import support the same asset types as bulk export (Database Service, Database, Schema, Table)?
- Can exported CSV files be directly used as import input?
- Are there validation rules, error handling, or rollback mechanisms for import operations?
- What authentication and permissions are required for bulk import?

## See Also

- [[bulk-export]] — Bulk export of data assets via CSV
- [[openmetadata-features]] — Comprehensive overview of OpenMetadata features
- [[openmetadata-administration]] — Administrative capabilities