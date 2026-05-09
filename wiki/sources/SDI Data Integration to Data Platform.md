---
type: source
title: SDI Data Integration to Data Platform
created: 2026-02-13
updated: 2026-02-13
tags: [sdi, data-platform, integration, geospatial, etl]
related: [legacy-geospatial-etl-pipeline, oracle-to-postgresql-gdal-etl, geospatial-etl-pipeline-iceberg, postgis, postgis-crs-gridded-transformation, geoscript-modernization, sdi-data-platform-integration, crs-transformation-strategy, raster-ingestion-pattern]
sources: ["SDI Data Integration to Data Platform.md"]
---
# SDI Data Integration to Data Platform

This source documents the integration strategy between the existing Spatial Data Infrastructure (SDI) of Regione Liguria and the new Data Platform (DP) under construction. It analyzes multiple hypotheses for ingesting vector and raster geospatial data from the SDI into the DP's modern lakehouse architecture (MinIO/Iceberg/Nessie/Dremio).

## Key Topics

- **Geoscript Modernization**: Migration from Windows/Groovy/GDAL to Ubuntu/Python/GDAL as a prerequisite for any integration strategy.
- **Vector Ingestion Hypotheses**: Four approaches for vector data ingestion, ranging from two-phase (Oracle→PostGIS→DP) to direct ingestion and native DP tools.
- **Raster Ingestion**: COG (Cloud Optimized GeoTIFF) conversion via GDAL and direct S3 upload to MinIO.
- **CRS Transformation**: Critical challenge of coordinate system conversion using gridded data, with PostGIS ST_Transform as the recommended mechanism.
- **Recommended Approach**: Alternative B (Optimized Hybrid) — Oracle→PostGIS (CRS transform in Phase 1)→DP via DP tools (Spark/Python).

## Architecture Context

The source references the DP architecture: MinIO (object storage), Apache Iceberg (table format), Project Nessie (catalog), Dremio (query engine), Spark (processing), and Airflow/Mage (orchestration). The SDI includes Oracle (source), PostGIS/viscarto (analytical database), and Geoscript (ETL system).

## Key Decisions

- Alternative B is recommended as the best compromise between robustness, existing asset utilization, and architectural coherence.
- CRS transformation with gridded data should remain in PostGIS where natively supported.
- Raster approach (COG via GDAL) is sound and standard practice.
- Proof of Concept is required to validate PostGIS performance under load before final decision.