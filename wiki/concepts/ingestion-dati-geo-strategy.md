---
type: concept
title: Ingestion Dati Geo Strategy
created: 2026-04-29
updated: 2026-04-29
tags: [geospatial, ingestion, etl, strategy]
related: [regione-liguria-sdi, geoscript-etl-system, postgis-staging-environment, catalogo-sit-metadata, legacy-geospatial-etl-pipeline, geospatial-etl-pipeline-iceberg, raster-ingestion-cog]
sources: ["Ingestion Dati Geo.md"]
---
# Ingestion Dati Geo Strategy

The ingestion strategy for geospatial data into the Data Platform (DP) involves two main hypotheses for vector data and a separate approach for raster data. The document favors the two-phase ingestion approach.

## Vector Ingestion Hypotheses

### Hypothesis 1: Two-Phase Ingestion (Oracle → PostGIS → DP)

**Phase 1 (Oracle → PostGIS)**: Data is copied from Oracle to PostGIS (viscarto) using Geoscript/GDAL scripts. The configuration is read from the Catalogo SIT. Updates are scheduled daily, monthly, or on-demand. Orchestration can be via cron on Geoscript or via Airflow.

**Phase 2 (PostGIS → DP)**: Data is read from PostGIS and written to S3 Object Storage in GeoParquet format (optionally Iceberg/GeoIceberg). Data is transformed to EPSG:7791 (RDN2008 / UTM zone 32N). Orchestration is via Airflow.

**Advantages**: Existing procedures, PostGIS performance and spatial functions, geometry validation, native CRS transformations with grid-shift files.

**Disadvantages**: Two-phase ETL requires synchronization and error handling.

### Hypothesis 2: Single-Phase Ingestion (Oracle → DP)

Data is ingested directly from Oracle to the DP within the Geoscript system, parallel to the PostGIS feed.

**Advantages**: Single process avoids cascading synchronization.

**Disadvantages**: Loses PostGIS spatial validation and transformation capabilities.

## Raster Ingestion

Raster data is ingested using Python scripts with:
- **gdalwarp**: Coordinate system transformation
- **gdal_translate**: Format transformation
- **COG (Cloud Optimized GeoTIFF)**: Target format
- **S3 Object Storage**: Target storage

## Metadata

The Catalogo SIT is proposed to be extended to manage DP data copy metadata, enabling a unified metadata-driven approach.

## Related Pages

- [[regione-liguria-sdi]] — The Spatial Data Infrastructure
- [[geoscript-etl-system]] — The current ETL system
- [[postgis-staging-environment]] — The proposed PostGIS staging environment
- [[catalogo-sit-metadata]] — The metadata system
- [[raster-ingestion-cog]] — Raster ingestion using COG
- [[legacy-geospatial-etl-pipeline]] — The legacy ETL pipeline
- [[geospatial-etl-pipeline-iceberg]] — Geospatial ETL patterns for Iceberg