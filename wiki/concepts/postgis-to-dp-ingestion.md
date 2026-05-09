---
type: concept
title: PostGIS to DP Ingestion
created: 2026-02-13
updated: 2026-02-13
tags: [sdi, data-platform, ingestion, geospatial, postgis]
related: [postgis-viscarto, sdi-dp-integration-strategy, geospatial-etl-pipeline-iceberg, geoparquet-vs-iceberg-metadata, epsg-7791]
sources: ["Integrazione SDI_DP_ Analisi e Proposte_ .md"]
---
# PostGIS to DP Ingestion

This is Phase 2 of Hypothesis 1 for vector data ingestion in the SDI-DP integration. Data is read from the PostGIS database (Viscarto) and written to the Data Platform's object storage.

## Process

1. Read data from PostGIS database.
2. Transform coordinates to EPSG:7791 (RDN2008 / UTM zone 32N).
3. Write to MinIO object storage as GeoParquet files.
4. Register as Iceberg/GeoIceberg tables.

## Orchestration

The orchestration is handled by the DP's orchestration system (Airflow or equivalent), not by the Geoscript system.

## Format Decisions

- **File Format**: GeoParquet
- **Table Format**: Iceberg / GeoIceberg
- **CRS**: EPSG:7791

## Connections to Existing Wiki

This phase directly aligns with the [[geospatial-etl-pipeline-iceberg]] pattern documented in the wiki. The format decisions relate to the [[geoparquet-vs-iceberg-metadata]] analysis.