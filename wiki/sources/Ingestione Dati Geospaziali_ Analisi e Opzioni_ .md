---
type: source
title: "Ingestione Dati Geospaziali: Analisi e Opzioni"
created: 2026-02-13
updated: 2026-02-13
tags: [geospatial, ingestion, gdal, iceberg, spark, sedona, gsb]
related: [gdal-ogr-container-pipeline, two-phase-ingestion-problem, spark-sedona-geospatial-etl, cloud-optimized-geotiff-cog, gsb-grid-files, iceberg-geospatial-support, dremio-geospatial-limitations, geospatial-etl-pipeline-iceberg, legacy-geospatial-etl-pipeline]
sources: ["Ingestione Dati Geospaziali_ Analisi e Opzioni_ .md"]
---
# Ingestione Dati Geospaziali: Analisi e Opzioni

This source is a technical evaluation of a geospatial data ingestion pipeline for a data lakehouse architecture. It analyzes the current approach (GDAL/OGR in Docker containers orchestrated by Airflow/KubernetesPodOperator, outputting GeoParquet and COG to MinIO) and explores alternatives, focusing on integration with Apache Iceberg.

## Key Topics

- **Current Pipeline Analysis:** GDAL/OGR container pipeline with Airflow/KubernetesPodOperator, including performance bottlenecks (single-threaded GDAL operations), dependency management complexity, and distributed debugging challenges.
- **Apache Iceberg for Geospatial:** Iceberg V3 GEO types (geometry, geography), WKB encoding, hidden partitioning (XZ2 curve), spatial indexing (Hilbert, Z-ordering), and CRS management via SRID/PROJJSON.
- **Two-Phase Ingestion Problem:** The fundamental disconnect between GDAL writing files to object storage and the separate process required to register them in Iceberg, introducing consistency risks and latency.
- **Alternative Approaches:** Apache Spark with Apache Sedona as the most promising alternative for distributed, scalable geospatial ETL with native Iceberg integration. Python+Dask as a lighter-weight alternative.
- **GSB Grid File Support:** Critical requirement for high-accuracy coordinate transformations. GDAL supports GSB natively via PROJ; Sedona support requires verification.

## Critical Findings

1. GDAL operations are predominantly single-threaded; parallelization is at the process level (multiple pods), not within a single large dataset.
2. The two-phase ingestion (GDAL writes → separate Iceberg registration) introduces complexity, latency, and consistency risks.
3. Spark+Sedona can write directly to Iceberg tables, avoiding the two-phase problem, but GSB support is unverified.
4. Iceberg V3 GEO types are promising but still maturing; query engine support (Dremio, Trino, DuckDB) is variable.

## Recommendations

- Prioritize investigation of Apache Spark with Apache Sedona as the primary alternative, contingent on GSB support verification.
- Optimize the current GDAL pipeline in parallel (performance tuning, robust Iceberg post-hoc integration).
- Adopt Apache Iceberg as the table format for geospatial data in the data lakehouse.
- Use Project Nessie for transactional, versioned catalog management.