---
type: source
title: "Ingestione dati cartografici: analisi alternative"
created: 2026-03-18
updated: 2026-03-18
tags: [gis, geospatial, etl, iceberg, geoparquet, spark, sedona, gdal]
related: [legacy-geospatial-etl-pipeline, geospatial-etl-pipeline-iceberg, iceberg-geospatial-support, geoparquet-vs-iceberg-metadata, apache-sedona, gdal-ogr, apache-spark, nessie-catalog-versioning, dremio-geospatial-limitations, geoarrow, write-audit-publish-pattern, data-lakehouse, cloud-native-geospatial-workflow, duckdb-geoparquet-limitations]
sources: ["Ingestione dati cartografici_ analisi alternative.md"]
---
# Ingestione dati cartografici: analisi alternative

## Summary

This document provides a comprehensive technical evaluation of the proposed geospatial data ingestion pipeline based on GDAL/OGR in Docker containers orchestrated by Airflow/Kubernetes, with output in GeoParquet/COG format on MinIO object storage. It analyzes the critical issues of the current approach, explores Apache Iceberg's capabilities and limitations for geospatial data management, evaluates open-source on-premise alternatives, and formulates strategic recommendations.

## Key Findings

### Current Pipeline Criticisms (GDAL/OGR + Airflow/Kubernetes)

1. **Performance and Scalability Bottlenecks**: GDAL operations (ogr2ogr, gdal_translate) are predominantly single-threaded for core geometric processing. While parallelization is achieved by running multiple independent GDAL processes via KubernetesPodOperator, each individual process remains limited by single-core performance for large files or complex vector layers. This contrasts with distributed frameworks like Apache Spark that parallelize within a single dataset.

2. **Dependency Management Complexity**: GDAL has a complex dependency tree (PROJ, GEOS, format-specific libraries, Oracle OCI, database drivers). Building and maintaining custom Docker images with correct versions and GSB grid shift files requires significant effort. Version mismatches between GDAL, PROJ, and grid files can introduce subtle, hard-to-diagnose errors.

3. **Distributed Debugging and Monitoring Challenges**: Failures can originate from multiple levels (GDAL errors, Kubernetes pod eviction, network issues, Airflow orchestration). Root cause analysis requires correlating information from Airflow logs, Kubernetes pod logs, cluster events, and application metrics. KubernetesPodOperator reports only pod success/failure status, not detailed application errors.

4. **Fundamental Disconnection from Iceberg Metadata Management**: GDAL operates at the file level, writing GeoParquet/COG output to object storage but is completely unaware of Iceberg table structure and metadata. A separate post-processing step is required to register files in Iceberg, calculate column statistics, update manifests, and create snapshots. This two-phase process introduces complexity, latency, and potential consistency issues.

### Apache Iceberg for Geospatial Data

- **Native GEO Types (V3)**: Iceberg V3 introduces native geometry and geography types based on OGC Simple Features and ISO 19107 standards, supporting Point, LineString, Polygon, Multi* variants, and GeometryCollection.
- **WKB Encoding**: Well-Known Binary is the primary encoding for geometry/geography types within underlying file formats (Parquet). GeoArrow is discussed as a potential higher-performance alternative.
- **Spatial Partitioning and Indexing**: Hidden partitioning can be extended with XZ2 curves (explored in Havasu/GeoLake). Hilbert curve ordering and Z-ordering improve spatial data locality. However, native spatial indexing within Iceberg itself is still an area under development, with performance heavily dependent on the query engine.
- **CRS Management**: Supports SRID (e.g., srid:4326), PROJJSON, and EPSG formats for coordinate reference system definitions.
- **Query Engine Support**: Apache Sedona is among the first to support native Iceberg GEO types. Support in Trino is planned. DuckDB, Flink, Presto, Hive, BigQuery, and Snowflake are potential adopters as support matures.
- **Nessie Integration**: Provides Git-like catalog-level versioning (branches, tags, commits) enabling isolated development, zero-copy cloning, and atomic multi-table transactions.

### Alternative Architectures

1. **Apache Spark + Apache Sedona**: The most promising alternative due to intrinsic scalability, distributed geospatial functions, and potential to unify the entire ETL pipeline (extraction from Oracle/PostGIS, transformations, writing GeoParquet to MinIO, and registering in Iceberg tables) within a single framework. **Critical open question**: whether Sedona's ST_Transform directly supports GSB grid shift files. If not, workarounds (external GDAL invocation, custom UDFs) would be needed.

2. **Python + GeoPandas + Dask**: Offers a familiar development environment for Python teams. GeoPandas' to_crs() method uses pyproj (PROJ wrapper), which should support GSB files if the execution environment is properly configured. However, achieving optimal performance at scale requires careful Dask tuning (partitioning, memory management, scheduler overhead) and may not match Spark/Sedona efficiency for extremely complex or voluminous distributed operations.

3. **Other Tools**: Talend Open Studio (with spatial extension), GeoKettle, HALE, and generic ELT tools (Airbyte, Meltano, Singer) were evaluated but found less suitable for this specific geospatial use case due to scalability limitations or lack of native geospatial capabilities.

### Recommendations

1. **Prioritize investigation of Apache Spark + Apache Sedona**, contingent on confirmation of GSB grid shift file support.
2. **In parallel, optimize the current GDAL pipeline** by improving performance configuration and implementing a robust post-hoc Iceberg integration process.
3. **Adopt Apache Iceberg as the table format** for geospatial data in the data lakehouse, regardless of the ETL approach chosen.
4. **Use Nessie for transactional, versioned catalog management**.
5. **Consider STAC (SpatioTemporal Asset Catalog)** for cataloging COG raster outputs, improving interoperability with external geospatial tools.

## Tags

- gis
- geospatial
- etl
- iceberg
- geoparquet
- spark
- sedona
- gdal
- data-lakehouse
- cloud-native
