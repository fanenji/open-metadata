---
type: source
title: "dbt Troubleshooting | OpenMetadata Integration Support"
created: 2026-05-14
updated: 2026-05-14
tags: [dbt, troubleshooting, openmetadata, ingestion]
related: [dbt-troubleshooting, dbt-artifacts, dbt-lineage-ingestion, dbt-artifact-storage, dbt-integration]
sources: ["dbt-troubleshooting-openmetadata-integration-suppo-20260514.md"]
authors: [OpenMetadata]
year: 2026
url: "https://docs.open-metadata.org/v1.12.x/connectors/database/dbt/dbt-troubleshooting"
venue: "OpenMetadata Documentation"
---

# dbt Troubleshooting | OpenMetadata Integration Support

Official troubleshooting guide for the dbt integration in OpenMetadata v1.12.x. Covers three common failure scenarios: the dbt tab not displaying in the UI, lineage not appearing from dbt, and S3 AccessDenied errors when retrieving dbt artifacts.

## Key Content

- **Required manifest.json keys**: Enumerates the specific keys (`resource_type`, `alias`/`name`, `schema`, `description`, `compiled_code`/`compiled_sql`, `depends_on`, `columns`) that must be present in each node for the dbt workflow to succeed. Missing keys cause the dbt tab to not display.
- **Name/alias/schema/database matching**: Values in manifest.json must exactly match the corresponding table/view metadata already ingested in OpenMetadata. If names don't match, dbt processing is skipped entirely.
- **Lineage prerequisite ordering**: Tables must be ingested *before* dbt ingestion runs. Lineage is drawn from model dependencies in manifest.json. The log search string `Processing dbt lineage for` is provided for debugging.
- **S3 IAM policy requirements**: The `s3:ListBucket` action on the bucket *and* `s3:GetObject` on contents are required. Pointing only to the bucket ARN is insufficient. Includes a concrete JSON policy example.

## Connections

This source strengthens [[dbt-integration]] and [[dbt-artifacts]] by adding concrete troubleshooting procedures and required key specifications. It extends [[dbt-lineage-ingestion]] by clarifying the prerequisite ordering and adding a log search string. It extends [[dbt-artifact-storage]] by adding specific S3 IAM policy requirements.