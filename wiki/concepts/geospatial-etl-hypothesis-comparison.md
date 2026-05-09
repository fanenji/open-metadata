---
type: concept
title: Geospatial ETL Hypothesis Comparison
created: 2026-04-29
updated: 2026-04-29
tags: [geospatial, etl, architecture, comparison, decision-framework]
related: [postgis-as-staging-layer-for-geospatial-etl, crs-transformation-strategies-for-geospatial-etl, spark-for-geospatial-etl, proj-grid-configuration-for-python-duckdb, legacy-geospatial-etl-pipeline, geospatial-etl-pipeline-iceberg]
sources: ["ETL VETTORIALI SINTESI.md"]
---
# Geospatial ETL Hypothesis Comparison

A living document tracking the architectural hypotheses for the vector geospatial ETL pipeline, their trade-offs, and the decision process.

## Hypothesis Overview

### Two-Phase ETL (Hypothesis 1): Oracle → PostGIS → S3
| Variant | Phase 2 Engine | CRS Transformation | Scalability | Iceberg/Nessie |
|---------|---------------|-------------------|-------------|----------------|
| 1a (GDAL/OGR) | GDAL/OGR | GDAL | Single-node | No |
| 1b (Python/GeoPandas) | Python/GeoPandas | PyProj | Single-node | No |
| 1c (Python/DuckDB) | Python/DuckDB | DuckDB Spatial | Single-node | No |
| 1d (Spark) | Spark | PostGIS ST_Transform | Distributed | Yes |

### One-Phase ETL (Hypothesis 2): Oracle/PostGIS → S3 directly
| Variant | Engine | CRS Transformation | Scalability | Iceberg/Nessie |
|---------|--------|-------------------|-------------|----------------|
| 2a (GDAL/OGR) | GDAL/OGR | GDAL | Single-node | No |
| 2b (Python/GeoPandas) | Python/GeoPandas | PyProj | Single-node | No |
| 2c (Python/DuckDB) | Python/DuckDB | DuckDB Spatial | Single-node | No |

## Key Decision Criteria

1. **PostGIS staging**: Is the validation and SDI compatibility worth the latency?
2. **CRS transformation location**: PostGIS (optimal) vs. Python/DuckDB/GDAL (requires PROJ config)
3. **Scalability requirements**: Is single-node sufficient or is distributed processing needed?
4. **Iceberg/Nessie integration**: Is it needed now or can it be added later?
5. **Infrastructure complexity**: Is a Spark cluster justified?

## Current Recommendation

Hypothesis 1d (Spark) is strategically superior because:
- Delegates CRS transformation to PostGIS (optimal environment)
- Provides distributed scalability
- Is the only path to Iceberg/Nessie
- Can start with GeoParquet and migrate to Iceberg later

## PoCs Required
- PostGIS ST_Transform read performance under concurrent JDBC reads
- Python/GeoPandas and DuckDB memory usage on representative datasets
- PROJ grid configuration correctness in Python/DuckDB environments
- Necessity of Iceberg/Nessie for cartographic data