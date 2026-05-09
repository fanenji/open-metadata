---
type: source
title: "ETL VETTORIALI SINTESI: Vector ETL Pipeline Design Analysis"
created: 2026-01-15
updated: 2026-01-15
tags: [etl, geospatial, vector, gis, crs-transformation, postgis, spark, duckdb, gdal, geoparquet, iceberg, nessie]
related: [legacy-geospatial-etl-pipeline, oracle-to-postgresql-gdal-etl, geospatial-etl-pipeline-iceberg, duckdb, nessie-catalog-versioning, iceberg-table-versioning, geoparquet-vs-iceberg-metadata, kubernetes, postgis-as-staging-layer-for-geospatial-etl, crs-transformation-strategies-for-geospatial-etl, spark-for-geospatial-etl, geospatial-etl-hypothesis-comparison, proj-grid-configuration-for-python-duckdb]
sources: ["ETL VETTORIALI SINTESI.md"]
---
# ETL VETTORIALI SINTESI: Vector ETL Pipeline Design Analysis

This document is a design analysis for modernizing the vector geospatial ETL pipeline for the Data Platform. It evaluates multiple architectural hypotheses for ingesting vector data from Oracle/PostGIS sources into S3 as GeoParquet files, with optional Iceberg/Nessie integration.

## Core Architectural Decision

The primary decision is whether to use **PostGIS as a validated staging layer** (two-phase ETL) or bypass it (one-phase ETL). This determines pipeline complexity, latency, and SDI compatibility.

## Hypotheses Overview

### Two-Phase ETL (Hypothesis 1): Oracle → PostGIS → S3
- **1a (GDAL/OGR)**: Uses Geoscript/ogr2ogr for both phases. CRS transformation in GDAL. Robust but limited scalability.
- **1b (Python/GeoPandas)**: Phase 2 uses Python/GeoPandas with PyProj for CRS transformation. Familiar stack but single-node limited.
- **1c (Python/DuckDB)**: Phase 2 uses DuckDB spatial extension for CRS transformation. Potentially fast but single-node limited.
- **1d (Spark)**: Phase 2 uses Spark reading from PostGIS via JDBC. **CRS transformation delegated to PostGIS `ST_Transform`** — the optimal environment for grid-based transforms. Only hypothesis that natively supports Iceberg/Nessie.

### One-Phase ETL (Hypothesis 2): Oracle/PostGIS → S3 directly
- **2a (GDAL/OGR)**: Direct GDAL/OGR pipeline. Simpler but loses PostGIS validation benefits.
- **2b (Python/GeoPandas)**: Direct Python pipeline with PyProj CRS transformation.
- **2c (Python/DuckDB)**: Direct DuckDB pipeline with spatial extension.

## Key Findings

1. **Hypothesis 1d (Spark) is strategically superior**: Delegating `ST_Transform` to PostGIS (optimal for grid-based CRS) while using Spark only for scalable I/O is the most robust approach. The critical bottleneck is potential PostGIS overload during JDBC reads.

2. **Hypothesis 1d is the only viable path to Iceberg/Nessie**: Spark's mature Iceberg connector makes it the only hypothesis that can natively integrate Iceberg tables with ACID, time travel, and schema evolution.

3. **Non-Spark hypotheses share a fundamental scalability limitation**: Python/GeoPandas, DuckDB, and GDAL are all single-node, limiting throughput on large datasets.

4. **Iceberg/Nessie integration is optional**: The document suggests starting with GeoParquet and migrating to Iceberg later with minimal code changes (changing `.write.format("parquet")` to `.write.format("iceberg")`).

## PoCs Required
- PostGIS `ST_Transform` read performance under concurrent JDBC reads from Spark
- Python/GeoPandas and DuckDB memory usage on representative datasets (10M+ features)
- PROJ grid configuration correctness in Python/DuckDB environments
- Necessity of Iceberg/Nessie for cartographic data vs. GeoParquet sufficiency

## Infrastructure
Kubernetes is recommended as the execution environment for all hypotheses, given Docker image availability.