---
type: source
title: "How to Ingest Custom Properties from dbt into OpenMetadata"
created: 2026-05-25
updated: 2026-05-25
tags: [dbt, custom-properties, ingestion, metadata]
related: [dbt-integration, dbt-artifacts, custom-properties, dbt-lineage-ingestion]
sources: ["thinkwe-need-to-answer-how-can-i-ingest-custom-pro-2026-05-25-140121.md"]
---
# How to Ingest Custom Properties from dbt into OpenMetadata

This source documents the procedure for populating pre-defined OpenMetadata custom properties with values declared in dbt model YAML files. It covers the prerequisite that properties must already exist in OpenMetadata, the YAML syntax for declaring values at the table (model) level only, the 14 supported custom property types, artifact generation via `manifest.json`, and the ingestion workflow. The source also describes the validation and graceful degradation behavior: invalid values are skipped with warnings, and undefined properties are ignored.

> **⚠️ CORREZIONE (giugno 2026):** Column-level custom properties NON sono supportate. La precedente affermazione "at both table and column levels" era errata.

## Key Points

- Custom properties **must be pre-defined** in OpenMetadata (Settings → Custom Properties → Tables) before ingestion; dbt cannot create new property definitions.
- Values are declared under `meta.openmetadata.customProperties` in `schema.yml` at the table (model) level only. Column-level is NOT supported.
- 14 custom property types are supported, including complex types like entity references, time intervals, and tables.
- Values are embedded into `manifest.json` under `config.meta.openmetadata.customProperties`.
- Ingestion validates values against their defined types; invalid or undefined properties are silently skipped with warnings.
- This extends the standard [[dbt-integration]] by adding custom properties as an additional metadata category alongside descriptions, tags, ownership, and lineage.