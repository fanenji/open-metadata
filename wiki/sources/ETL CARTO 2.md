---
type: source
title: ETL CARTO 2 - Geospatial ETL Migration Plan
created: 2026-04-29
updated: 2026-04-29
tags: [geospatial, etl, migration, gdal, docker, python]
related: [gdal-docker-image, geoscript-migration-plan, italian-datum-transformations, groovy-to-python-etl-migration, oracle-to-postgresql-gdal-etl, legacy-geospatial-etl-pipeline, kubernetes-etl-deployment-strategies, container-image-strategy-for-data-pipelines]
sources: ["ETL CARTO 2.md"]
---
# ETL CARTO 2 - Geospatial ETL Migration Plan

This document outlines the migration plan for the legacy Groovy-based geospatial ETL system (GeoScript) to a modern Python-based, containerized architecture. The plan covers the conversion of 18+ Groovy scripts to Python, the creation of a multi-stage GDAL Docker image with Oracle OCI, ECW, and GSB grid support, and a three-phase migration roadmap (script conversion → container testing → Airflow scheduling).

## Key Content

- **Migration Plan:** Three-phase approach: Phase 1 (Groovy-to-Python conversion), Phase 2 (container testing with Docker Compose), Phase 3 (Airflow scheduling on Kubernetes)
- **GDAL Docker Image:** Multi-stage build (`gdal-full`) with Oracle OCI, ECW raster support, GSB grid files for PROJ, and Python
- **Cross-Platform Abstraction:** `OGR2OGR_CMD` environment variable for Windows/Linux portability
- **Grid-Based Reprojection:** Precise coordinate transformations from Italian datum GB to ETRK2K (EPSG:7791) using GSB grid files
- **Script Inventory:** 18+ scripts covering domains: bilancio-idrico, cem, centri-impiego, geoportale, geoserver, libioss, psa, rqa, scuoladigitale, sentieri, varie
- **Test Commands:** Working examples of Oracle-to-PostgreSQL and Oracle-to-Shapefile transformations with real connection strings and coordinate systems

## Relevance

This document is the modernization plan for the [[oracle-to-postgresql-gdal-etl]] pattern and directly extends the [[legacy-geospatial-etl-pipeline]] documentation. It provides a concrete case study for [[kubernetes-etl-deployment-strategies]] and [[container-image-strategy-for-data-pipelines]].