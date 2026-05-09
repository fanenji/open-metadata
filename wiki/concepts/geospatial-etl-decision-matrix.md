---
type: concept
title: Geospatial ETL Decision Matrix
created: 2026-04-29
updated: 2026-04-29
tags: [geospatial, etl, decision-matrix, architecture, postgis, spark, sedona, duckdb, python]
related: [crs-transformation-strategies, postgis-performance-tuning-for-etl, geospatial-etl-pipeline-iceberg, legacy-geospatial-etl-pipeline, apache-sedona, duckdb, pyiceberg-usage-patterns]
sources: ["ETL VETTORIALI.md"]
---
# Geospatial ETL Decision Matrix

This concept page provides a structured comparison of all architectural alternatives for ingesting geospatial vector data from Oracle into the Data Platform (MinIO/Iceberg/Nessie), as analyzed in [[ETL VETTORIALI]].

## Alternatives Summary

| # | Approach | Phases | CRS Transform | Iceberg Integration | Scalability | Complexity | Risk |
|---|----------|--------|---------------|---------------------|-------------|------------|------|
| H1 | Oracle → PostGIS → DP | 2 | PostGIS (ST_Transform) | Spark | Medium | Medium | Low |
| H2 | Oracle → DP (Direct) | 1 | Python/GDAL | PyIceberg or Spark | Low | High | High |
| A | Spark/Sedona (Native) | 1 | Sedona (limited grid) | Spark (native) | High | High | Medium |
| A-Var | Python ETL + Spark Register | 2 | Python/GeoPandas or DuckDB | Spark (register) | Medium | High | Medium |
| B-Rev | PostGIS → Spark (JDBC ST_Transform) | 2 | PostGIS (ST_Transform) | Spark (native) | Medium | Medium | Low-Medium |
| B-Py | PostGIS → Python/GeoPandas | 2 | Python/GeoPandas | PyIceberg | Low | High | High |
| B-Duck | PostGIS → DuckDB | 2 | DuckDB (spatial ext.) | PyIceberg | Low | Medium | Medium |

## Decision Criteria

### 1. Data Volume
- **Small (< 1M rows)**: Any approach works. Python/GeoPandas or DuckDB variants are acceptable.
- **Medium (1M-10M rows)**: Spark-based approaches (H1, B-Rev) recommended. Python variants may struggle.
- **Large (> 10M rows)**: Spark/Sedona (A) or Spark with PostGIS delegation (B-Rev) required.

### 2. Latency Requirements
- **Near real-time (< 1 hour)**: Single-phase approaches (H2, A) preferred.
- **Batch (daily)**: Two-phase approaches (H1, B-Rev) acceptable.

### 3. CRS Transformation Accuracy
- **Grid-based transformation required**: PostGIS delegation (H1, B-Rev) mandatory. Sedona (A) has limited grid support.
- **Simple transformation (no grids)**: Any approach works.

### 4. Team Skills
- **Strong SDI team, weaker DP team**: H1 (clear separation of concerns).
- **Strong DP team, weaker SDI team**: A or B-Rev.
- **Python-focused team**: B-Py or B-Duck (with acknowledged limitations).

### 5. Existing Infrastructure
- **PostGIS already in use for SDI**: H1 or B-Rev (leverage existing investment).
- **Spark cluster already available**: A or B-Rev.
- **No Spark cluster**: B-Duck or B-Py (with scalability caveats).

## Recommendation Flowchart

1. Is `viscarto` (PostGIS) needed for SDI purposes?
   - **Yes** → Go to step 2.
   - **No** → Consider H2 or A (single-phase).
2. Is grid-based CRS transformation required?
   - **Yes** → Use PostGIS delegation (H1 or B-Rev).
   - **No** → Consider A (Spark/Sedona) for better scalability.
3. Is latency critical?
   - **Yes** → B-Rev (single Spark phase after PostGIS load).
   - **No** → H1 (two-phase, more robust).
4. Validate with PoC:
   - Test `ST_Transform` performance in JDBC reads (B-Rev).
   - Test Sedona grid file handling (A).
   - Test Python/GeoPandas scalability with representative data volumes.

## Recommended Initial Implementation

**Hypothesis 1 (Oracle → PostGIS → DP)** is the recommended starting point:
- Leverages existing PostGIS capabilities.
- Clear separation of SDI and DP responsibilities.
- Lowest risk for grid-based CRS transformations.
- Acceptable latency for batch processing.

## Related
- [[crs-transformation-strategies]] — Detailed analysis of CRS transformation options.
- [[postgis-performance-tuning-for-etl]] — Mitigation strategies for PostGIS bottlenecks.
- [[geospatial-etl-pipeline-iceberg]] — The overall ETL pipeline pattern.
- [[apache-sedona]] — Spark geospatial library for alternative approaches.