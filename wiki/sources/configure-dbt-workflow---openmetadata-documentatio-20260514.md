---
type: source
title: "Source: configure-dbt-workflow---openmetadata-documentatio-20260514.md"
created: 2026-05-15
updated: 2026-05-15
sources: ["configure-dbt-workflow---openmetadata-documentatio-20260514.md"]
tags: []
related: []
---

# Source: configure-dbt-workflow---openmetadata-documentatio-20260514.md

## Key Entities

- **dbt (Data Build Tool)** — Central entity. Data transformation tool whose artifacts (manifest.json, catalog.json, run_results.json) are ingested by OpenMetadata. Already exists in wiki.
- **OpenMetadata** — Central platform performing the ingestion. Already exists in wiki.
- **dbt Core** — Open-source dbt deployment model requiring manual artifact storage configuration. Already exists in wiki.
- **dbt Cloud** — SaaS dbt deployment model with automatic artifact management via API. Already exists in wiki.
- **AWS S3 Buckets** — Storage backend for dbt Core artifacts. Peripheral. Already exists in wiki (dbt-artifact-storage).
- **Google Cloud Storage Buckets** — Storage backend for dbt Core artifacts. Peripheral. Already exists in wiki.
- **Azure Storage Buckets** — Storage backend for dbt Core artifacts. Peripheral. Already exists in wiki.
- **Local Storage** — Storage backend for dbt Core artifacts (local filesystem or container). Peripheral. Already exists in wiki.
- **File Server** — Storage backend for dbt Core artifacts (HTTP file server). Peripheral. Already exists in wiki.
- **dbt Cloud v2 APIs** — API endpoints (/runs, /artifacts) used to retrieve dbt run artifacts. Peripheral. Not explicitly in wiki.

## Key Concepts

- **dbt Artifact Ingestion Workflow** — The UI-driven process for configuring dbt metadata ingestion. Core concept: defines the 3-step configuration flow (Add Ingestion → Configure Source → Schedule & Deploy). Not explicitly documented as a standalone concept in wiki.
- **dbt Artifact Storage Configuration** — Prerequisite for dbt Core: artifacts must be accessible to OpenMetadata via one of five backends. Already exists in wiki (dbt-artifact-storage).
- **dbt Cloud API Authentication** — Authentication via Authentication Token with minimum Account Viewer permission. Peripheral. Not in wiki.
- **dbt Cloud Run Filtering** — API filters by account_id, project_id, job_id to retrieve the most recent successful run. Peripheral. Not in wiki.
- **Automatic Metadata Association** — After successful dbt ingestion, metadata is automatically associated with corresponding data assets without manual UI configuration. Important design principle. Not explicitly in wiki.

## Main Arguments & Findings

- **Core claim**: Configuring a dbt workflow in OpenMetadata is a straightforward 3-step UI process (Add Ingestion → Configure Source → Schedule & Deploy).
- **Key finding**: Only manifest.json is required; catalog.json and run_results.json are optional.
- **Key finding**: dbt Cloud does not require artifact storage configuration — artifacts are managed automatically via API.
- **Key finding**: After successful ingestion, dbt metadata is automatically associated with data assets and no additional manual configuration is needed.
- **Evidence**: Official documentation from OpenMetadata v1.12.x. Strength: High (official source).

## Connections to Existing Wiki

- **Strengthens**: [[dbt-integration]], [[dbt-artifacts]], [[dbt-a
