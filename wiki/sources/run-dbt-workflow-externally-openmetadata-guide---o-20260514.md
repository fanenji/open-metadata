---
type: source
title: "Run dbt Workflow Externally | OpenMetadata Guide"
created: 2026-05-14
updated: 2026-05-14
tags: [dbt, ingestion, cli, metadata-ingestion, openmetadata]
related: [dbt, dbt-integration, dbt-artifact-storage, dbt-lineage-ingestion, cli-ingestion-with-basic-auth, run-dbt-workflow-externally, ingestion-framework, metadata-ingestion-workflow, filter-patterns]
sources: ["run-dbt-workflow-externally-openmetadata-guide---o-20260514.md"]
---

# Run dbt Workflow Externally | OpenMetadata Guide

Official OpenMetadata v1.12.x documentation providing a complete procedural guide for running the dbt metadata ingestion workflow outside the OpenMetadata UI, using a YAML configuration file executed via the `metadata ingest -c <path-to-yaml>` CLI command.

## Content Summary

The document covers:

- **Python Requirements**: `pip3 install "openmetadata-ingestion[dbt]"` (Python 3.9-3.11)
- **Six YAML Configuration Patterns** for different dbt artifact sources:
  1. **AWS S3 Buckets** — `dbtConfigType: s3` with AWS credentials (access key, session token, IAM role, profile, custom endpoint)
  2. **Google Cloud Storage Buckets** — `dbtConfigType: gcs` with service account credentials (file path or inline)
  3. **Azure Storage Buckets** — `dbtConfigType: azure` with Azure AD credentials (client ID, client secret, tenant ID, account name)
  4. **Local Storage** — `dbtConfigType: local` with file paths for catalog.json, manifest.json, run_results.json
  5. **File Server (HTTP)** — `dbtConfigType: http` with URLs for dbt artifacts
  6. **dbt Cloud API** — `dbtConfigType: cloud` with service token, account/project/job IDs
- **dbtPrefixConfig**: Optional bucket/prefix specification for cloud storage; if omitted, ingestion scans all buckets
- **Source Config Options**: `dbtUpdateDescriptions`, `dbtUpdateOwners`, `includeTags`, `dbtClassificationName`, `databaseFilterPattern`, `schemaFilterPattern`, `tableFilterPattern`
- **Sink Configuration**: `type: metadata-rest` for sending metadata to OpenMetadata
- **Workflow Configuration**: `openMetadataServerConfig` with JWT token authentication, `storeServiceConnection`, SSL configuration, `ingestionPipelineFQN`

## Key Insights

- The external CLI workflow is an alternative to the UI-driven 8-step [[metadata-ingestion-workflow]] process
- The `dbtPrefixConfig` is optional — if omitted, ingestion scans all buckets, which may be inefficient in multi-bucket environments
- The `dbtUpdateDescriptions` and `dbtUpdateOwners` flags control whether dbt metadata overrides existing OpenMetadata content, with significant governance implications
- The `storeServiceConnection` flag (default true) controls whether sensitive connection info is stored encrypted in the database or used only at runtime
- The YAML structure is consistent across all connectors; only the `dbtConfigSource` block varies by artifact source

## Connections

- Strengthens [[dbt-integration]] with the detailed external workflow procedure
- Expands [[dbt-artifact-storage]] with complete YAML configurations and authentication parameters
- Extends [[cli-ingestion-with-basic-auth]] with dbt-specific YAML structure
- Relates to [[filter-patterns]] for scoping dbt model ingestion
- Relates to [[dbt-lineage-ingestion]] as the mechanism for triggering lineage ingestion from dbt artifacts