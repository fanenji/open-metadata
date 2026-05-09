---
type: entity
title: GDAL/OGR Container Pipeline
created: 2026-04-29
updated: 2026-04-29
tags: [geospatial, gdal, ingestion, docker, airflow]
related: [two-phase-ingestion-problem, cloud-optimized-geotiff-cog, gsb-grid-files, spark-sedona-geospatial-etl, legacy-geospatial-etl-pipeline]
sources: ["Ingestione Dati Geospaziali_ Analisi e Opzioni_ .md"]
---
# GDAL/OGR Container Pipeline

The GDAL/OGR Container Pipeline is the current approach for geospatial data ingestion. It uses GDAL/OGR commands (`ogr2ogr` for vector, `gdal_translate` for raster) running in Docker containers, orchestrated by Apache Airflow using the `KubernetesPodOperator`.

## Architecture

1. **Source Data:** Oracle Spatial, PostgreSQL/PostGIS, filesystem (`/dtuff/raster`).
2. **Processing:** GDAL/OGR commands in Docker containers, one pod per task.
3. **Output:** GeoParquet (vector) and Cloud Optimized GeoTIFF (raster) written to MinIO.
4. **Orchestration:** Airflow DAGs with `KubernetesPodOperator` for each GDAL task.

## Critical Limitations

- **Single-Threaded Processing:** GDAL operations are predominantly single-threaded. Parallelization is at the process level (multiple pods), not within a single large dataset.
- **Two-Phase Ingestion:** GDAL writes files to object storage; a separate process must register them in Iceberg. This introduces [[two-phase-ingestion-problem|consistency risks and latency]].
- **Dependency Management:** Complex GDAL dependency chain (PROJ, GEOS, Oracle OCI, etc.) requires careful Docker image maintenance.
- **Distributed Debugging:** Error diagnosis requires correlating logs from Airflow, Kubernetes, and the container.

## Performance Considerations

- **GDAL Cache:** `GDAL_CACHEMAX` setting significantly impacts performance.
- **Multi-threading:** `GDAL_NUM_THREADS` can parallelize compression but not core geometric processing.
- **S3 Interaction:** `VSI_CACHE`, `CPL_VSIL_CURL_CACHE_SIZE`, and `VSIS3_CHUNK_SIZE` tuning critical for MinIO performance.
- **PostGIS Optimization:** `PG_USE_COPY` can improve read performance from PostGIS.

## Alternatives

- [[spark-sedona-geospatial-etl]] — Distributed processing with native Iceberg integration.
- Python+Dask — Lighter-weight alternative for moderate-scale processing.

## Status

This approach is viable for moderate volumes but has fundamental scalability limits. It is the legacy approach being evaluated for replacement or optimization.