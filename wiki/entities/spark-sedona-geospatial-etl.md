---
type: entity
title: Spark+Sedona Geospatial ETL
created: 2026-04-29
updated: 2026-04-29
tags: [geospatial, spark, sedona, etl, iceberg]
related: [two-phase-ingestion-problem, gsb-grid-files, gdal-ogr-container-pipeline, geospatial-etl-pipeline-iceberg, iceberg-geospatial-support]
sources: ["Ingestione Dati Geospaziali_ Analisi e Opzioni_ .md"]
---
# Spark+Sedona Geospatial ETL

Apache Spark with Apache Sedona is the most promising alternative to the current GDAL/OGR container pipeline for geospatial ETL. It provides distributed, scalable processing with native Iceberg integration.

## Key Advantages

- **Distributed Processing:** Spark parallelizes computation across multiple nodes and cores, overcoming GDAL's single-threaded limitation for large datasets.
- **Native Iceberg Integration:** Spark can write directly to Iceberg tables, avoiding the [[two-phase-ingestion-problem]].
- **Geospatial Functions:** Sedona provides a comprehensive set of geospatial operations (spatial joins, indexing, transformations) as Spark SQL functions and DataFrame operations.
- **Scalability:** Can handle arbitrarily large datasets by adding more nodes to the Spark cluster.

## Architecture

1. **Read:** Spark reads from Oracle/PostGIS sources using JDBC connectors, or from filesystem for raster data.
2. **Transform:** Sedona performs coordinate transformations (including GSB support — **unverified**), spatial operations, and data cleaning.
3. **Write:** Spark writes directly to Iceberg tables in MinIO, using Iceberg's native write path.

## GSB Support Status

**Critical Blocker:** Support for GSB grid files in Sedona is unverified. This must be confirmed before adopting Spark+Sedona as the primary alternative. GDAL's GSB support is mature and reliable; Sedona's support depends on its underlying PROJ integration.

## Comparison with GDAL Approach

| Aspect | GDAL/KPO | Spark+Sedona |
|--------|----------|--------------|
| Processing model | Single-threaded per pod | Distributed across cluster |
| Iceberg integration | Two-phase (manual registration) | Native write support |
| GSB support | Mature and reliable | Unverified |
| Complexity | Moderate (Docker + Airflow) | Higher (Spark cluster management) |
| Scalability | Process-level parallelization | Intra-dataset parallelization |
| Learning curve | Lower (familiar GIS tools) | Higher (Spark ecosystem) |

## Recommendations

1. **Verify GSB support** in Sedona through a proof-of-concept test.
2. **Benchmark** Spark+Sedona against the current GDAL pipeline for representative datasets.
3. **Consider hybrid approach:** Use GDAL for simple transformations and Spark+Sedona for large-scale processing.