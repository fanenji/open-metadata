---
type: concept
title: dbt Integration
created: 2026-05-14
updated: 2026-05-15
tags: [dbt, ingestion, metadata, integration, metadata-ingestion]
related: [dbt, dbt-artifacts, dbt-lineage-ingestion, dbt-artifact-storage, metadata-ingestion-workflow, openmetadata-connectors, data-lineage, data-quality, openmetadata]
sources: ["dbt Workflow  OpenMetadata Data Build Tool Integration.md", "dbt-workflow-openmetadata-data-build-tool-integrat-20260514.md"]
---

# dbt Integration

The dbt integration is a production-ready (PROD stage) connector that ingests transformation metadata from dbt projects into OpenMetadata. Unlike typical database connectors that connect to live data sources, the dbt integration reads pre-generated JSON artifact files — `manifest.json`, `catalog.json`, and `run_results.json` — to extract metadata about data models, lineage, tests, and governance attributes. It supports both [[dbt]] Core (open-source) and dbt Cloud (SaaS) deployment models.

## Deployment Models

### dbt Core Integration
For self-hosted dbt, artifacts must be placed in cloud storage accessible to OpenMetadata. Five storage backends are supported: Amazon S3, Google Cloud Storage, Azure Blob Storage, HTTP/HTTPS servers, and local/shared filesystems. See [[dbt-artifact-storage]] for configuration details.

### dbt Cloud Integration
For SaaS dbt, OpenMetadata integrates directly via dbt Cloud APIs, eliminating storage requirements. Requires an active dbt Cloud account, configured jobs, and a valid API token.

## Prerequisites and Artifact Generation

To generate the required artifacts, run the following commands after your dbt models execute:

- `dbt run` — Generates `manifest.json`
- `dbt test` — Updates `run_results.json` with test outcomes
- `dbt docs generate` — Creates `catalog.json`
- `dbt compile` — Required to populate `compiled_code` in `manifest.json` for lineage; run before `dbt docs generate`

**Critical Requirements:**
- `manifest.json` is mandatory — without it, no metadata is ingested.
- `compiled_code` is required for lineage — run `dbt compile` before `dbt docs generate`. If missing, lineage is silently absent.
- `run_results.json` is required for test results — run `dbt test` before ingestion to capture the latest test outcomes.

## Ingested Metadata Categories

The integration imports the following metadata from dbt:

1. **dbt Queries** — SQL used to create dbt models, viewable in the dbt tab.
2. **dbt Lineage** — Transformation lineage from `ref()` and `source()` dependencies. Requires `compiled_code` in `manifest.json`. See [[dbt-lineage-ingestion]].
3. **dbt Tags** — Table and column-level classification tags from dbt.
4. **dbt Owner** — Model ownership assignments.
5. **dbt Descriptions** — Table and column descriptions from `manifest.json` and `catalog.json`.
6. **dbt Tests and Test Results** — Data quality test cases with pass/fail results, imported when `run_results.json` is provided.
7. **dbt Tiers** — Table and column-level tier classifications.
8. **dbt Glossary** — Glossary term assignments.
9. **dbt Domain** — Table-level domain assignments.
10. **dbt Custom Properties** — Organization-specific custom attributes.

> **Note:** dbt Exposures are listed in the feature table but are **not yet supported**.

## Related

- [[dbt]]
- [[dbt-artifacts]]
- [[dbt-lineage-ingestion]]
- [[dbt-artifact-storage]]
- [[openmetadata]]