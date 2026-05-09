type: source
title: "Research: HEX_EGG Table"
created: 2026-05-08
updated: 2026-05-08
tags: [geospatial, dbt, h3, data-model, nexar, spatial-aggregation, research]
related: [hex-egg-table, h3-geospatial-indexing, geospatial-analytics-with-dbt, nexar, elt-pattern, data-lakehouse, dbt, iceberg-table-versioning, dremio-geospatial-limitations, dbt-osmosis, data-contract-implementation]
sources: ["research-hexegg-table-2026-05-08.md"]
---
# Research: HEX_EGG Table

A deep research synthesis on the **HEX_EGG Table** pattern — a spatial data model for large-scale geospatial analytics using [[h3-geospatial-indexing]] and [[dbt]]. The pattern is strongly associated with organizations processing massive telemetry streams, such as [[nexar]], which ingests data from approximately 500,000 dashcam devices.

The document synthesizes the HEX_EGG pattern from multiple sources, including Nexar's architecture, H3 literature, and dbt integration patterns. It proposes a hypothetical schema, data flow, and use cases, while explicitly flagging the "EGG" acronym as a knowledge gap.

Key findings:
- The HEX_EGG table serves as a critical intermediate/fact table converting raw geospatial events into H3 hexagon cells for scalable aggregation.
- The pattern integrates with [[dbt]] incremental models, [[data-lakehouse]] storage (e.g., [[iceberg-table-versioning]]), and analytics platforms like [[count-co]]'s Hex.
- The "EGG" acronym lacks a canonical definition; plausible expansions include "Event Geometry Grid" or "Entity Geographic Grid."
- The pattern is logically sound and consistent with known practices, but no single source explicitly names "HEX_EGG" — it is a synthesized pattern.

See the [[hex-egg-table]] synthesis page for the full documented pattern.