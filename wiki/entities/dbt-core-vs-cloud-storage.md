---
type: entity
title: dbt Core vs. dbt Cloud Storage
created: 2026-05-14
updated: 2026-05-14
tags: [dbt, artifact-storage, comparison]
related: [dbt, dbt-artifacts, dbt-artifact-storage, dbt-integration, dbt-lineage-ingestion]
sources: ["dbt-artifact-configuration-guide-openmetadata---op-20260514.md"]
---

# dbt Core vs. dbt Cloud Storage

This page clarifies the critical distinction between dbt Core and dbt Cloud regarding artifact storage configuration for OpenMetadata ingestion.

## dbt Core

- **Requires storage configuration**: You must make dbt-generated artifacts (manifest.json, catalog.json, run_results.json) accessible to OpenMetadata via one of five supported storage backends.
- **Artifacts are local**: dbt Core runs within your infrastructure and produces artifacts in the `target/` directory.
- **Manual upload or automation**: You must upload artifacts to S3, GCS, Azure, HTTP server, or shared filesystem, either manually or via automated workflows (Airflow DAG, Cloud Composer, etc.).
- **Command sequence required**: `dbt run` → `dbt test` → `dbt docs generate` must be executed in order to produce all artifacts.

## dbt Cloud

- **No storage configuration needed**: dbt Cloud handles artifact storage automatically.
- **Uses Cloud API directly**: OpenMetadata connects to the dbt Cloud API to retrieve metadata, lineage, and test results.
- **Simpler setup**: Go directly to the dbt Cloud API guide for configuration.

## Decision Matrix

| Factor | dbt Core | dbt Cloud |
|--------|----------|-----------|
| Storage Configuration | Required | Not needed |
| Artifact Location | Local `target/` directory | Managed by dbt Cloud |
| Upload Automation | Manual or custom (Airflow, etc.) | Built-in |
| OpenMetadata Connection | Via storage backend | Via Cloud API |
| Setup Complexity | Higher | Lower |

## Common Misconception

Users often assume storage configuration is always required. This is only true for dbt Core. If using dbt Cloud, skip the storage configuration guides entirely and proceed directly to the dbt Cloud API integration.