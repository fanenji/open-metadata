---
type: entity
title: GDAL/OGR
created: 2026-04-29
updated: 2026-04-29
tags: [geospatial, gis, etl, library]
related: [legacy-geospatial-etl-pipeline, oracle-to-postgresql-gdal-etl, geospatial-etl-pipeline-iceberg, apache-sedona, dremio-geospatial-limitations]
sources: ["Ingestione dati cartografici_ analisi alternative.md"]
---
# GDAL/OGR

GDAL (Geospatial Data Abstraction Library) and OGR (its vector component) are foundational open-source libraries for reading, writing, and transforming geospatial data formats. They form the core of the current geospatial ingestion pipeline.

## Role in Current Architecture

The current pipeline uses GDAL/OGR commands (ogr2ogr for vector, gdal_translate for raster) executed inside Docker containers, orchestrated by Apache Airflow via KubernetesPodOperator. Output is written as GeoParquet (vector) and Cloud Optimized GeoTIFF (COG, raster) to MinIO object storage.

## Key Capabilities

- **Format Support**: Reads/writes hundreds of geospatial formats including Oracle Spatial, PostGIS, Shapefile, GeoJSON, GeoPackage, GeoParquet, and COG.
- **CRS Transformation**: Intrinsic support for coordinate reference system transformations via integration with the PROJ library, including GSB grid shift files for precise datum transformations.
- **Cloud-Optimized I/O**: Supports virtual filesystems (/vsis3/) for S3-compatible storage, with range requests for COG/GeoParquet and multi-part uploads for writes.
- **Arrow Interface**: Optimized Arrow output in ogr2ogr can provide 3x improvement for GPKG→Parquet and 10x for Parquet→Parquet conversions.

## Critical Limitations

1. **Single-Threaded Core Processing**: Core geometric processing and raster transformations are predominantly single-threaded. While compression can benefit from multithreading, the bottleneck remains single-core capacity for large files.
2. **Complex Dependency Management**: GDAL has a complex dependency tree (PROJ, GEOS, format-specific libraries, Oracle OCI, database drivers). Building and maintaining custom Docker images with correct versions and GSB files requires significant effort.
3. **Iceberg Disconnection**: GDAL operates at the file level and is completely unaware of Iceberg table structure. A separate post-processing step is required for Iceberg registration, introducing complexity and potential consistency issues.

## Performance Tuning Parameters

- GDAL_CACHEMAX: Memory cache size
- GDAL_NUM_THREADS: Threading for compression
- VSI_CACHE / CPL_VSIL_CURL_CACHE_SIZE: Virtual filesystem cache
- VSIS3_CHUNK_SIZE: S3 chunk size for writes
- PG_USE_COPY: PostGIS driver optimization for faster reads

## Related

- [[legacy-geospatial-etl-pipeline]] — The current pipeline built on GDAL/OGR
- [[oracle-to-postgresql-gdal-etl]] — Specific ETL workflow using GDAL/OGR
- [[geospatial-etl-pipeline-iceberg]] — Proposed Iceberg-based pipeline that could replace GDAL
- [[apache-sedona]] — Distributed alternative to GDAL for geospatial processing
