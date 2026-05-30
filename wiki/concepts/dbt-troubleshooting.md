---
type: concept
title: dbt Troubleshooting
created: 2026-05-14
updated: 2026-05-14
tags: [dbt, troubleshooting, openmetadata, ingestion]
related: [dbt-troubleshooting, dbt-artifacts, dbt-lineage-ingestion, dbt-artifact-storage, dbt-integration]
sources: ["dbt-troubleshooting-openmetadata-integration-suppo-20260514.md"]
---

# dbt Troubleshooting

This concept page documents the common failure modes and resolution strategies for the [[dbt]]-[[openmetadata|OpenMetadata]] integration. The three primary troubleshooting scenarios are:

1. **dbt tab not displaying** — Caused by missing required keys in `manifest.json` or `catalog.json`, or by name/schema/database mismatches between dbt artifacts and OpenMetadata ingested tables.
2. **Lineage not displaying** — Caused by tables not being ingested *before* dbt ingestion, or by missing `depends_on`/`compiled_code` keys in `manifest.json`.
3. **S3 AccessDenied** — Caused by insufficient IAM policy scope; both the bucket and its contents must be in the Resource ARN.

The most common root cause across all scenarios is the **name/alias/schema/database matching requirement**: values in `manifest.json` must exactly match the corresponding table/view metadata already ingested in OpenMetadata. If names don't match, dbt processing is skipped entirely.

For detailed procedures and examples, see the [[dbt-troubleshooting]] entity page.