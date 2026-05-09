---
type: concept
title: Geospatial Data Stack
created: 2026-05-06
updated: 2026-05-06
tags: ["geospatial", "data-science", "architecture", "big-data", "gis", "spatial"]
related: ["duckdb", "geopandas", "apache-sedona", "spatial-pre-processing-pattern", "geoparquet", "data-lakehouse-on-premise-architecture", "geo-parquet"]
sources: ["Analisi Architettura.md", "Apache Sedona Coordinate Transform.md", "BRAINSTOR - Integrazione della Spatial Data Infrastructure (SDI) con la Data Platform (DP).md", "analyzing-real-estate-data-with-apache-sedona"]
---
# Geospatial Data Stack

The **Geospatial Data Stack** is a specialized extension of the regional Data Platform, designed to handle the ingestion, transformation, and distribution of vector and raster spatial datasets.

## Architecture Components

### Vector Data Pipeline
- **Source:** Oracle RDBMS.
- **Staging/Transformation:** **PostGIS** (`viscarto`) for complex CRS transformations using regional grids and geometry validation.
- **Processing:** **Apache Spark** (with **Apache Sedona**) for large-scale processing and format conversion.
- **Storage Format:** **GeoParquet** for efficient columnar storage and **Apache Iceberg** for ACID transactions and schema evolution.
- **Catalog:** **Project Nessie** for versioning and **OpenMetadata** for discovery.

### Raster Data Pipeline
- **Source:** Various regional raster sources.
- **Transformation:** **GDAL/OGR** (via Python/Geoscript) for reprojecting and converting to **Cloud Optimized GeoTIFF (COG)**.
- **Storage:** **MinIO** (S3-compatible object storage).

### Key Technologies
- **GDAL/OGR:** The core engine for format conversion and coordinate transformations.
- **Apache Sedona:** Distributed spatial computing engine for Apache Spark.
- **GeoParquet:** An optimized file format for geospatial vector data.
- **COG (Cloud Optimized GeoTIFF):** An optimized format for efficient cloud-native raster access.
