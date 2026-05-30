---
type: source
title: "Ingest Custom Properties From Dbt Openmetadata Cus 20260514"
created: 2026-05-30
updated: 2026-05-30
tags: []
related: []
authors: []
year: 2026
url: ""
venue: ""
---

type: source
title: Ingest Custom Properties from dbt | OpenMetadata Custom Metadata Guide
created: 2026-05-14
updated: 2026-05-14
tags: [dbt, custom-properties, metadata-ingestion, openmetadata]
related: [dbt-custom-properties-ingestion, custom-properties, dbt-integration, dbt-artifacts, dbt-lineage-ingestion, dbt-artifact-storage]
sources: ["ingest-custom-properties-from-dbt-openmetadata-cus-20260514.md"]
---

# Ingest Custom Properties from dbt

Official OpenMetadata documentation (v1.12.x) describing how to ingest custom property values from dbt's `manifest.json` artifact to enrich table metadata with organization-specific attributes.

## Key Topics

- Pre-definition requirement: custom properties must be defined on the Table entity in OpenMetadata before ingestion
- `schema.yml` syntax for declaring custom properties under `meta.openmetadata.customProperties`
- 14 supported custom property types (string, integer, number, markdown, sqlQuery, email, date-cp, dateTime-cp, time-cp, timestamp, duration, enum, entityReference, entityReferenceList, timeInterval, table-cp)
- Advanced examples: entity references, entity reference lists, time intervals, table custom properties
- Validation and error handling: graceful degradation with warnings for invalid or undefined properties
- Complete example combining custom properties with domain, tier, and owner metadata

## Relevance

This source provides the concrete ingestion pathway for populating [[custom-properties]] via the [[dbt]] workflow, extending the standard metadata model with organization-specific attributes such as SLA hours, data classification levels, and refresh frequencies. It establishes a critical ordering constraint — custom properties must be pre-defined in OpenMetadata before dbt ingestion can apply values.