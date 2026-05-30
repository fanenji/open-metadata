---
type: source
title: "Source: ingest-descriptions-from-dbt-official-documentatio-20260514.md"
created: 2026-05-15
updated: 2026-05-15
sources: ["ingest-descriptions-from-dbt-official-documentatio-20260514.md"]
tags: []
related: []
---

# Source: ingest-descriptions-from-dbt-official-documentatio-20260514.md

## Analysis: Ingest Descriptions from dbt

### Key Entities

- **dbt (Data Build Tool)** — Central entity. Data transformation tool whose `manifest.json` and `catalog.json` artifacts are the source of descriptions.
- **OpenMetadata** — Central entity. Target platform where descriptions are ingested into tables and columns.
- **manifest.json** — dbt artifact; default source for descriptions. Descriptions from this file are imported by default.
- **catalog.json** — dbt artifact; secondary source. Descriptions from this file take precedence when both artifacts are passed.
- **Update Descriptions toggle** — Configuration option controlling overwrite behavior during dbt ingestion.

All entities likely already exist in the wiki (dbt, dbt-artifacts, dbt-integration).

### Key Concepts

- **Description Source Precedence** — When both `manifest.json` and `catalog.json` are provided, `catalog.json` descriptions override `manifest.json` descriptions. When only `manifest.json` is provided, its descriptions are used.
- **Update Descriptions Toggle** — Boolean configuration option:
    - **Enabled**: Existing OpenMetadata descriptions are overwritten with dbt descriptions (dbt as single source of truth).
    - **Disabled**: dbt descriptions are only applied to tables/columns that currently have no descriptions in OpenMetadata. Existing descriptions are preserved.
- **Single Source of Truth** — The architectural decision point: descriptions can be maintained centrally in dbt (with overwrite enabled) or in OpenMetadata (with overwrite disabled).

These concepts likely do not have dedicated wiki pages. They are specific to the dbt ingestion workflow.

### Main Arguments & Findings

- **Core claim**: Descriptions from dbt artifacts can be ingested into OpenMetadata tables and columns, with configurable overwrite behavior.
- **Evidence**: Official documentation from OpenMetadata v1.12.x.
- **Strength**: High — this is authoritative documentation from the platform vendor.

### Connections to Existing Wiki

- **dbt-integration** — This page is a sub-topic of the broader dbt integration. It extends the dbt integration documentation with specific details about description ingestion.
- **dbt-artifacts** — Directly relevant; describes the two artifact files (`manifest.json`, `catalog.json`) and their role.
- **metadata-ingestion-workflow** — This is a specific step within the broader ingestion workflow.
- **dbt-lineage-ingestion** — Parallel concept for lineage; this page is the equivalent for descriptions.

### Contradictions & Tensions

- **No contradictions** with existing wiki content.
- **Internal tension**: The documentation presents a binary choice (overwrite vs. preserve) without discussing hybrid approaches or conflict resolution strategies. This is a design limitation, not a contradiction.

### Recommendations

**Create new wiki pages:**
- **dbt-description-ingestion** — Dedicated page covering the description ingestion workflow, source precedence rules, and th
