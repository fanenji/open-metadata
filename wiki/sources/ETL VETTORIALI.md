---
type: source
title: "ETL VETTORIALI: Geospatial Vector Ingestion Strategies for the Data Platform"
created: 2026-01-15
updated: 2026-01-15
tags: [gis, etl, geospatial, vector-data, ingestion, postgis, spark, sedona, duckdb, geopandas, crs-transformation]
related: [legacy-geospatial-etl-pipeline, oracle-to-postgresql-gdal-etl, geospatial-etl-pipeline-iceberg, dremio-geospatial-limitations, apache-sedona, crs-transformation-strategies, postgis-performance-tuning-for-etl, pyiceberg-usage-patterns, geospatial-etl-decision-matrix, duckdb, geoparquet-vs-iceberg-metadata, data-lakehouse, iceberg-table-versioning, nessie-catalog-versioning]
sources: ["ETL VETTORIALI.md"]
---
# ETL VETTORIALI: Geospatial Vector Ingestion Strategies for the Data Platform

This document is a comprehensive technical analysis of strategies for ingesting geospatial vector data from legacy systems (Oracle) into the modern Data Platform (MinIO/Iceberg/Nessie). It systematically evaluates multiple architectural hypotheses and alternatives, providing a decision framework for the vector ETL pipeline.

## Core Hypotheses

### Hypothesis 1: Oracle → PostGIS (`viscarto`) → DP
A two-phase pipeline where an evolved Geoscript first loads data from Oracle into PostGIS (`viscarto`), and then the DP ingestion layer reads from PostGIS, applies final CRS transformation to EPSG:7791, and writes GeoParquet to MinIO/Iceberg. This is recommended as the most prudent and robust initial choice, leveraging existing PostGIS capabilities for quality control and CRS transformation.

### Hypothesis 2: Oracle → DP (Direct via Evolved Geoscript)
A single-phase pipeline where Geoscript performs all transformations and writes directly to MinIO/Iceberg. This is considered riskier due to the complexity transferred to Geoscript and the loss of PostGIS optimizations.

## Alternatives

### Alternative A: Native DP Ingestion (Spark/Sedona)
Uses Spark with Apache Sedona for the entire ETL process from Oracle to Iceberg. Architecturally coherent but faces challenges with grid file management for CRS transformations in Spark.

### Alternative A Variant: Python ETL + Spark/Iceberg Registration
Separates the ETL logic (Python/GeoPandas or DuckDB) from the Iceberg registration (Spark). A compromise that isolates CRS transformation complexity in Python while leveraging Spark for robust Iceberg integration.

### Alternative B (Revised): Oracle → PostGIS → DP (Spark with JDBC ST_Transform)
Spark reads from PostGIS using a JDBC query that includes `ST_Transform(geometry, 7791)`, delegating the CRS transformation to PostGIS. Technically feasible but introduces a potential performance bottleneck on PostGIS during reads.

### Alternative B Variant: Python/GeoPandas
Replaces Spark with Python/GeoPandas for the PostGIS → DP phase. Faces significant scalability limitations and complex Iceberg integration via `pyiceberg`.

### Alternative B Variant: DuckDB
Uses DuckDB with its `spatial` and `postgres` extensions as the processing engine. Offers potential efficiency but remains single-node.

## Key Technical Insights

- **CRS Transformation with Grid Files**: Accurate transformation to EPSG:7791 requires proper PROJ configuration and grid file access. PostGIS handles this natively; Spark/Sedona and Python environments require careful setup.
- **WKB/WKT Conversion**: Geometry data from PostGIS JDBC reads must be converted from binary/text representations to internal geometry types. Apache Sedona provides robust parsing and GeoParquet writing.
- **Materialized Views**: A mitigation strategy for PostGIS performance bottlenecks during JDBC reads with `ST_Transform`.
- **GeoParquet vs. Iceberg**: Standard Iceberg with WKB/WKT geometry columns and GeoParquet is a more consolidated option than GeoIceberg.

## Recommendations

1. **Prioritize Hypothesis 1** (via PostGIS) as the initial implementation.
2. **Validate performance** of `ST_Transform` in JDBC reads from PostGIS via PoCs.
3. **Consider Materialized Views** in PostGIS if direct `ST_Transform` reads are too slow.
4. **Use Apache Sedona** for WKB/WKT conversion and GeoParquet writing in Spark.
5. **Avoid Python/GeoPandas variant** for production due to scalability and Iceberg integration complexity.
6. **Evaluate DuckDB variant** only for smaller datasets where single-node processing is sufficient.

## Open Questions
- Actual data volumes (impact scalability requirements)
- Whether `viscarto` is needed for SDI purposes regardless
- Acceptable latency window for the two-phase pipeline
- Sedona's ability to handle grid files in the Spark environment
- Feasibility of CDC from Oracle