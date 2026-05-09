---
type: entity
title: Catalogo SIT Metadata
created: 2026-04-29
updated: 2026-04-29
tags: [geospatial, metadata, catalog, sdi]
related: [regione-liguria-sdi, geoscript-etl-system, ingestion-dati-geo-strategy]
sources: ["Ingestion Dati Geo.md"]
---
# Catalogo SIT Metadata

The Catalogo SIT is the metadata catalog within the Regione Liguria SDI that guides ETL configuration. It contains the list of layers to convert and the information needed by ETL scripts to retrieve data from the source.

## Current Usage

The Geoscript ETL system uses Catalogo SIT metadata to:
- Read layer configuration
- Build appropriate OGR configuration
- Execute ogr2ogr commands

## Proposed Extension

The document proposes extending the Catalogo SIT to also manage metadata for data copy operations to the Data Platform (DP), enabling a unified metadata-driven approach for both SDI and DP ingestion pipelines.

## Related Pages

- [[regione-liguria-sdi]] — The Spatial Data Infrastructure
- [[geoscript-etl-system]] — The current ETL system
- [[ingestion-dati-geo-strategy]] — The ingestion strategy decision