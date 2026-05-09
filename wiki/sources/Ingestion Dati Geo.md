---
type: source
title: "Ingestion Dati Geo: SDI/DP Integration Strategy"
created: 2026-01-15
updated: 2026-04-29
tags: [geospatial, ingestion, sdi, etl, migration]
related: [regione-liguria-sdi, geoscript-etl-system, postgis-staging-environment, ingestion-dati-geo-strategy, raster-ingestion-cog, catalogo-sit-metadata, legacy-geospatial-etl-pipeline, geospatial-etl-pipeline-iceberg, etl-attuale]
sources: ["Ingestion Dati Geo.md"]
---
# Ingestion Dati Geo: SDI/DP Integration Strategy

This document outlines the integration strategy between the existing Spatial Data Infrastructure (SDI) of Regione Liguria and the new Data Platform (DP) under construction. It analyzes the functional overlap between the two systems and proposes concrete ETL patterns for ingesting geospatial vector and raster data into the DP.

## Key Topics

- **Boundary Definition**: Clarifying the functional overlap between SDI and DP to prevent duplication and define integration points.
- **Geoscript Migration**: Moving the ETL system from Windows Server 2019 / Groovy / GDAL to Ubuntu / Python / GDAL with containerization options.
- **Two-Phase Ingestion (Hypothesis 1)**: Oracle → PostGIS (viscarto) → DP, leveraging PostGIS as a staging environment for validation, coordinate transformation, and performance.
- **Single-Phase Ingestion (Hypothesis 2)**: Oracle → DP directly, simpler but losing PostGIS capabilities.
- **Raster Ingestion**: Using COG (Cloud Optimized GeoTIFF) format with gdalwarp and gdal_translate.
- **Metadata Extension**: Proposing to extend the Catalogo SIT to manage DP data copy metadata.

## Recommended Approach

The document favors the two-phase ingestion approach (Hypothesis 1) due to:
- Existing and functioning data copy procedures within the SDI
- PostGIS's robust spatial validation and coordinate transformation capabilities
- Performance benefits of using PostGIS as a staging environment
- Native grid-shift file support for high-precision CRS transformations

## Related Pages

- [[regione-liguria-sdi]] — The Spatial Data Infrastructure of Regione Liguria
- [[geoscript-etl-system]] — The current ETL system and migration plan
- [[postgis-staging-environment]] — The proposed PostGIS staging environment
- [[ingestion-dati-geo-strategy]] — The ingestion strategy decision
- [[raster-ingestion-cog]] — Raster ingestion using COG format
- [[catalogo-sit-metadata]] — The metadata system guiding ETL configuration
- [[legacy-geospatial-etl-pipeline]] — The legacy ETL pipeline
- [[geospatial-etl-pipeline-iceberg]] — Geospatial ETL patterns for Iceberg
- [[ETL ATTUALE]] — Current ETL pipeline description