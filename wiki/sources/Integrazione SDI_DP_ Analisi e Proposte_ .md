---
type: source
title: "Integrazione SDI_DP_ Analisi e Proposte_"
created: 2026-02-13
updated: 2026-02-13
tags: [sdi, data-platform, integration, geospatial, etl]
related: [legacy-geospatial-etl-pipeline, oracle-to-postgresql-gdal-etl, geospatial-etl-pipeline-iceberg, geoparquet-vs-iceberg-metadata, dremio-geospatial-limitations, geoscript-modernization-plan, sdi-dp-integration-strategy, raster-ingestion-pipeline, postgis-to-dp-ingestion]
sources: ["Integrazione SDI_DP_ Analisi e Proposte_ .md"]
---
# Integrazione SDI_DP_ Analisi e Proposte_

This document is a detailed analysis and proposal for integrating the existing Spatial Data Infrastructure (SDI) of Regione Liguria with the new Data Platform (DP) under construction. It describes the current SDI ETL system (Geoscript), its criticalities, and proposes two main hypotheses for vector data ingestion (two-phase via PostGIS vs. direct from Geoscript) and a separate approach for raster data ingestion. The document also outlines a plan for modernizing the Geoscript system from Windows/Groovy to Ubuntu/Python.

## Key Topics

- **SDI-DP Integration Strategy**: Analysis of overlapping functions between the existing SDI and the new DP, with two proposed integration hypotheses.
- **Geoscript System**: Description of the legacy ETL system using Groovy scripts and GDAL/OGR on Windows Server 2019, including its criticalities.
- **Geoscript Modernization**: Proposal to migrate to Ubuntu/Python with updated GDAL/OGR.
- **Vector Data Ingestion**: Two hypotheses: (1) two-phase ingestion via PostGIS, (2) direct ingestion from Geoscript.
- **Raster Data Ingestion**: COG-based approach using gdalwarp and gdal_translate.
- **CRS Transformation**: Target coordinate reference system EPSG:7791 for vector data.

## Connections

This source provides concrete context for the [[legacy-geospatial-etl-pipeline]] and validates the [[geospatial-etl-pipeline-iceberg]] pattern with a real-world use case. It extends the [[Formati e Standard]] page by adding COG as a raster format. The analysis of Dremio's geospatial limitations ([[dremio-geospatial-limitations]]) is relevant if Dremio is used to query the ingested data.