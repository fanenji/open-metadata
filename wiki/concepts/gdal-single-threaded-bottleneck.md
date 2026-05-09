---
type: concept
title: GDAL Single-Threaded Bottleneck
created: 2026-04-29
updated: 2026-04-29
tags: [gdal, performance, geospatial, etl]
related: [gdal-ogr, legacy-geospatial-etl-pipeline, geospatial-etl-pipeline-iceberg, apache-spark, apache-sedona]
sources: ["Ingestione dati cartografici_ analisi alternative.md"]
---
# GDAL Single-Threaded Bottleneck

The GDAL Single-Threaded Bottleneck refers to the fundamental performance limitation of GDAL/OGR tools (ogr2ogr, gdal_translate) where core geometric processing and raster transformation operations execute in a predominantly single-threaded manner.

## Nature of the Bottleneck

While certain operations like output compression (for COG or GeoParquet) can benefit from multithreading when configured (via GDAL_NUM_THREADS), the core processing pipeline remains bound by the capacity of a single CPU core. This creates a scalability ceiling for processing individual large files or complex vector layers.

## Current Mitigation Strategy

The current architecture achieves parallelism by running multiple independent GDAL processes via KubernetesPodOperator (e.g., one pod per source file or geographic region). This is **process-level parallelism** — it does not solve the single-core limitation within a single large file.

## Comparison with Distributed Frameworks

| Aspect | GDAL/KPO Approach | Spark/Sedona |
|--------|-------------------|--------------|
| Parallelism Model | Process-level (multiple independent processes) | Intra-data (distributes work across nodes/cores) |
| Single Large File | Single-core limited | Parallelized across cluster |
| Scalability Ceiling | Number of independent tasks | Cluster resources |

## Performance Data Points

- OSM planet conversion can take days with basic ogr2ogr
- Arrow interface optimization can provide 3x improvement for GPKG→Parquet, 10x for Parquet→Parquet
- PG_USE_COPY option significantly improves PostGIS reads

## Related

- [[gdal-ogr]] — The library exhibiting this bottleneck
- [[legacy-geospatial-etl-pipeline]] — Current pipeline affected by this limitation
- [[geospatial-etl-pipeline-iceberg]] — Proposed alternative using distributed processing
- [[apache-spark]] — Distributed framework that avoids this bottleneck
- [[apache-sedona]] — Geospatial extension for Spark
