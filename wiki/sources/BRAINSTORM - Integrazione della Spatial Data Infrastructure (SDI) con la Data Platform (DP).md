---
type: source
title: "BRAINSTORM - Integrazione della Spatial Data Infrastructure (SDI) con la Data Platform (DP)"
created: 2026-05-06
updated: 2026-05-06
tags: [gis, ingestion, architecture, brainstorming]
related: [geospatial-data-stack, data-lakehouse-on-premise-architecture, apache-sedona]
authors: []
year: 2026
url: ""
venue: ""
---
# BRAINSTORM - Integrazione della Spatial Data Infrastructure (SDI) con la Data Platform (DP)

This document outlines the architectural strategies for integrating the existing Regional Spatial Data Infrastructure (SDI) with the new Data Platform (DP).

## Context
The integration aims to ingest geospatial data from the SDI into the DP to expand analytical capabilities. The SDI currently uses a legacy ETL system called **Geoscript** (Windows/Groovy) and a **PostGIS** database (`viscarto`) for spatial validation and transformations.

## Proposed Architectures

### Alternative B: Hybrid Optimized Architecture (Recommended)
**Flow:** Oracle $\rightarrow$ PostGIS (via Evolved Geoscript) $\rightarrow$ DP (via Spark)

This approach leverages PostGIS for complex spatial tasks (CRS transformations using regional grids) and Spark for the final ingestion into the Iceberg/MinIO Lakehouse.

**Phase 1: Oracle $\rightarrow$ PostGIS (SDI Side)**
- **Process:** Evolved Geoscript (Ubuntu/Python) reads from Oracle and writes to PostGIS.
- **Role:** Maintains existing business logic and uses PostGIS for geometry validation and initial transformations.

**Phase 2: PostGIS $\rightarrow$ DP Storage (DP Side)**
- **Process:** A Spark job (orchestrated by Airflow/Mage) connects to PostGIS via JDBC.
- **Transformation:** The Spark query uses `ST_Transform(geometry, 7791)` via the JDBC driver, delegating the heavy computational lifting (using regional grids) to the PostGIS engine.
- **Output:** Data is converted to **GeoParquet** and written to **MinIO** as **Apache Iceberg** tables (managed by **Nessie**).

**Advantages:**
- **Robustness:** Uses PostGIS's superior capability for handling regional coordinate grids.
- **Separation of Concerns:** SDI team manages Oracle $\rightarrow$ PostGIS; DP team manages PostGIS $\rightarrow$ DP.
- **Simplified DP Logic:** The Spark job focuses on format conversion rather than complex CRS math.

**Critical Risks:**
- **PostGIS Bottleneck:** The `ST_Transform` operation performed on-the-fly during JDBC reads can place a massive CPU/RAM load on the PostGIS server.
- **Mitigation:** Use **Materialized Views** in PostGIS to pre-calculate transformations or optimize Spark JDBC partitioning.

### Alternative A: Native DP Ingestion
**Flow:** Oracle $\rightarrow$ DP (via DP Tools)

**Concept:** Using DP components (Kafka Connect or Spark) to ingest directly from Oracle.

**Advantages:**
- **Architectural Consistency:** Uses only DP-native tools (Kafka, Spark, Air/Mage).
- **Lower Latency:** Eliminates the intermediate PostGIS hop.

**Disadvantages:**
- **Complexity:** Requires replicating complex spatial transformation logic (including regional grids) within the Spark/Python environment.

### Raster Data Strategy
**Flow:** Evolved Geoscript $\rightarrow$ COG on MinIO S3

**Concept:** Using Python/GDAL (`gdalwarp`, `gdal_translate`) to transform raster sources into **Cloud Optimized GeoTIFF (COG)** format and saving them directly to the DP object storage. This is considered a highly valid and recommended approach.

## Summary of Recommendations
1. **Modernize Geoscript:** Transition from Windows/Groovy to Ubuntu/Python/GDAL.
2. **Adopt Alternative B:** Use the hybrid approach to balance robustness and modern standards.
3. **Centralized Orchestration:** Use **Airflow** or **Mage** to orchestrate both phases of the ingestion pipeline.
4. **Automated Cataloging:** Ensure all new GeoParquet and COG files are automatically registered in the **Data Catalog** (OpenMetadata/DataHub).
