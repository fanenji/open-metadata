---
type: concept
title: CSV Import Fields Reference
created: 2026-05-14
updated: 2026-05-14
tags: [csv-import, reference, data-discovery, bulk-operations]
related: [bulk-import-csv, data-discovery, classification-tags, glossary-terms, tiers, domain, data-asset-ownership]
sources: ["bulk-import-data-assets-via-csv-in-openmetadata----20260514.md"]
---

# CSV Import Fields Reference

This page provides a consolidated reference of all CSV fields available for bulk importing data assets into OpenMetadata. Fields are grouped by asset type. Required fields are indicated.

## Database Service CSV Fields

| Field | Required | Description |
|-------|----------|-------------|
| `name` | Yes | Name of the database |
| `fullyQualifiedName` | Yes | Fully Qualified Name of the database service |
| `displayName` | No | Display name of the database |
| `description` | No | Detailed description or information about the database |
| `owner` | No | Owner of the database |
| `tags` | No | Tags associated with the database |
| `glossaryTerms` | No | Glossary terms linked to the database |
| `tiers` | No | Tiers associated with the database service |
| `domain` | No | Domain assigned to the data asset |

## Database CSV Fields

| Field | Required | Description |
|-------|----------|-------------|
| `name` | Yes | Name of the database |
| `fullyQualifiedName` | Yes | Fully Qualified Name of the database |
| `displayName` | No | Display name of the database |
| `description` | No | Detailed description or information about the database |
| `owner` | No | Owner of the database |
| `tags` | No | Tags associated with the database |
| `glossaryTerms` | No | Glossary terms linked to the database |
| `tiers` | No | Tiers associated with the database |
| `sourceUrl` | No | Source URL of the data asset (e.g., Snowflake console link) |
| `retentionPeriod` | No | Retention period expressed as an ISO 8601 duration (e.g., `P23DT23H`) |
| `domain` | No | Domain assigned to the data asset |

## Database Schema CSV Fields

| Field | Required | Description |
|-------|----------|-------------|
| `name` | Yes | Name of the database schema |
| `fullyQualifiedName` | Yes | Fully Qualified Name of the database schema |
| `displayName` | No | Display name of the database schema |
| `description` | No | Detailed description or information about the database schema |
| `owner` | No | Owner of the database schema |
| `tags` | No | Tags associated with the database schema |
| `glossaryTerms` | No | Glossary terms linked to the database schema |
| `tiers` | No | Tiers associated with the database schema |
| `sourceUrl` | No | Source URL of the data asset (e.g., Snowflake schema link) |
| `retentionPeriod` | No | Retention period expressed as an ISO 8601 duration (e.g., `P23DT23H`) |

## Table CSV Fields

| Field | Required | Description |
|-------|----------|-------------|
| `name` | No | Name of the table |
| `fullyQualifiedName` | Yes | Fully Qualified Name of the table |
| `displayName` | No | Display name of the table |
| `description` | No | Detailed description or information about the table |
| `owner` | No | Owner of the table |
| `tags` | No | Tags associated with the table |
| `glossaryTerms` | No | Glossary terms linked to the table |
| `tiers` | No | Tiers associated with the table |
| `sourceUrl` | No | Source URL of the data asset (e.g., Snowflake table link) |
| `retentionPeriod` | No | Retention period expressed as an ISO 8601 duration (e.g., `P23DT23H`) |
| `column.fullyQualifiedName` | Yes | Fully Qualified Name of the column |
| `column.displayName` | No | Display name of the column |
| `column.description` | No | Detailed description or information about the column |
| `column.dataTypeDisplay` | No | Data type for display purposes |
| `column.dataType` | No | Data type of the column (e.g., VARCHAR, INT, BOOLEAN) |
| `column.arrayDataType` | No | Data type of array elements (if column is an array) |
| `column.dataLength` | No | Length or size of the data |
| `column.tags` | No | Tags associated with the column |
| `column.glossaryTerms` | No | Glossary terms linked to the column |

## Notes

- The `fullyQualifiedName` field serves as the unique identifier for each asset and is used in the API endpoints for programmatic import.
- The `retentionPeriod` field uses ISO 8601 duration format (e.g., `P23DT23H` for 23 days and 23 hours).
- Column-level fields enable bulk metadata enrichment at the column granularity, including data types, tags, and glossary terms.