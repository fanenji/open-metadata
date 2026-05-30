---
type: source
title: "Run the PowerBI Connector Externally - OpenMetadata Documentation"
created: 2026-05-14
updated: 2026-05-14
tags: [powerbi, connector, ingestion, yaml, cli]
related: [powerbi-connector, metadata-ingestion-workflow, cli-ingestion-with-basic-auth, dashboard-lineage, dashboard-connectors, soft-deletion, pbit-file-lineage-extraction, powerbi-admin-vs-non-admin-apis]
sources: ["run-the-powerbi-connector-externally---openmetadat-20260514.md"]
---
# Run the PowerBI Connector Externally - OpenMetadata Documentation

This source is the official OpenMetadata v1.12.x documentation for running the PowerBI connector externally via YAML configuration and the CLI. It covers the complete setup, including Azure AD authentication, Admin vs. Non-Admin API modes, pbit file lineage extraction, and all configurable parameters.

## Key Topics

- **Authentication:** OAuth 2.0 Service Principal flow with Azure AD (Client ID, Client Secret, Tenant ID).
- **Admin vs. Non-Admin APIs:** Toggle controlling workspace scope and lineage capabilities.
- **pbit File Lineage:** Extraction of lineage from PowerBI template files stored in local, Azure, GCS, or S3 backends.
- **YAML Configuration:** Complete reference for all source, sourceConfig, sink, and workflowConfig parameters.
- **CLI Execution:** Running ingestion via `metadata ingest -c <path-to-yaml>`.
- **Limitations:** Usage API not supported (Service Principal incompatibility); dataflows not yet supported.
- **Soft Deletion:** `markDeletedDashboards` and `markDeletedDataModels` toggles.
- **Override Metadata/Lineage:** Toggles for controlling whether fetched data overwrites existing records.

## Connections

- Extends the [[powerbi-connector]] page with external/YAML execution details.
- Complements the [[metadata-ingestion-workflow]] UI-driven process with a CLI alternative.
- Relates to [[cli-ingestion-with-basic-auth]] via the `metadata ingest` command pattern.
- Documents PowerBI-specific lineage considerations for [[dashboard-lineage]].
- Fits within the broader [[dashboard-connectors]] category.
- References [[soft-deletion]] for dashboards and data models.