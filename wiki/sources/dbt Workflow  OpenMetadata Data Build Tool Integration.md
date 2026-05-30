---
type: source
title: "dbt Workflow | OpenMetadata Data Build Tool Integration"
created: 2026-05-14
updated: 2026-05-14
tags: [dbt, ingestion, lineage, data-quality, metadata]
related: [dbt-integration, dbt-artifacts, dbt-lineage-ingestion, dbt-artifact-storage, data-lineage, data-quality, openmetadata-connectors, metadata-ingestion-workflow]
sources: ["dbt Workflow  OpenMetadata Data Build Tool Integration.md"]
authors: []
year: 2026
url: "https://docs.open-metadata.org/v1.12.x/connectors/database/dbt"
venue: "OpenMetadata Official Documentation"
---
# dbt Workflow | OpenMetadata Data Build Tool Integration

Official documentation for integrating dbt (Data Build Tool) workflows with OpenMetadata. This source covers the complete dbt ingestion workflow, including artifact requirements, storage configuration for dbt Core, dbt Cloud API integration, and the ten categories of metadata ingested from dbt projects.

## Key Points

- dbt integration is **PROD stage** and supports dbt Core versions v1.2 through v1.9.
- Three artifact files drive the integration: **manifest.json** (required), **catalog.json** (recommended), **run_results.json** (recommended).
- dbt Core requires external artifact storage (S3, GCS, Azure, HTTP, Local) because OpenMetadata cannot access the dbt execution environment's local filesystem.
- dbt Cloud eliminates storage complexity by using API-based integration.
- Lineage capture requires the `compiled_code` field in manifest.json; without it, lineage is silently absent.
- Ten metadata categories are ingested: Queries, Lineage, Tags, Owner, Descriptions, Tests, Tiers, Glossary, Domain, Custom Properties.
- dbt Exposures are listed but not yet supported.