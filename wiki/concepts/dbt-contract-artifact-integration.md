---
type: concept
title: dbt Contract Artifact Integration
created: 2026-05-07
updated: 2026-05-07
tags: [dbt, data-contracts, metadata, artifacts, API]
related: [dbt-data-contract-implementation, data-contract-observability, data-contract-platform, datahub, openmetadata]
sources: ["dbt and Data Contracts Enabling Reliable, API-Driven Analytics.md"]
---
# dbt Contract Artifact Integration

dbt embeds full contract metadata in its build artifacts — specifically `manifest.json` and `catalog.json`. This enables downstream tools, APIs, and data catalogs to automatically pull schema and contract definitions for observability, validation, and self-serve discovery.

## Key Capabilities

- **Automated Schema Sync:** Data catalogs (e.g., [[openmetadata]], [[datahub]]) can consume contract metadata to keep schema definitions up to date.
- **API-Driven Consumption:** Contract definitions can be exposed via custom APIs for integration with BI tools, semantic layers, and consumer applications.
- **Lineage and Impact Analysis:** Contracts are traced across dbt's graph, enabling impact analysis when contracts change.
- **Change Communication:** Contract changes can be tracked and alerted on to avoid uncoordinated schema drift.

## Integration Patterns

- Syndicate contract metadata via APIs, dashboards, and data catalogs.
- Leverage manifest and semantic artifacts for automated contract API endpoints.
- Sync with orchestration tools (Airflow, Dagster) so downstream jobs depend on contract pass/fail status.