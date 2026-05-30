---
type: source
title: Bulk Import Data Assets via CSV in OpenMetadata
created: 2026-05-14
updated: 2026-05-14
tags: [csv-import, data-discovery, bulk-operations, metadata-ingestion]
related: [bulk-import-csv, csv-import-fields-reference, data-discovery, bottom-up-top-down-enrichment, metadata-ingestion-workflow, snowflake]
sources: ["bulk-import-data-assets-via-csv-in-openmetadata----20260514.md"]
authors: [OpenMetadata Documentation Team]
year: 2026
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/data-discovery/import"
venue: "OpenMetadata Documentation"
---

# Bulk Import Data Assets via CSV in OpenMetadata

Official documentation (v1.12.x) describing how to bulk import data assets — Database Services, Databases, Database Schemas, and Tables — into OpenMetadata using CSV files. The guide covers the step-by-step UI workflow for each asset type, including the export-as-template pattern, inline editing, validation, and confirmation. It also provides the corresponding API endpoints for programmatic import. The source uses Snowflake as the reference example throughout.

Key topics covered:
- Bulk import of Database Services, Databases, Database Schemas, and Tables
- CSV field specifications for each asset type, including column-level fields for Tables
- Export-as-template workflow for reducing manual formatting errors
- Inline editor for previewing and modifying CSV data before validation
- Two-step validation and confirmation process
- API endpoints for programmatic import using Fully Qualified Names (FQNs)
- Column-level import with fields for data types, tags, and glossary terms

This source establishes the CSV bulk import as a complementary "top-down" enrichment method alongside the existing ingestion pipelines, enabling efficient population of business metadata (descriptions, owners, tags, glossary terms, tiers, domains) without manual UI entry.