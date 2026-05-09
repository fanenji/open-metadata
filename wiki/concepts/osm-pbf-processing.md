---
type: concept
title: OSM PBF Processing
created: 2026-04-08
updated: 2026-04-08
tags: [openstreetmap, geospatial, data-ingestion, file-format]
related: [quackosm, openstreetmap-data-model, legacy-geospatial-etl-pipeline, cloud-native-geospatial-workflow, duckdb-spatial-extension]
sources: ["QuackOSM.md"]
---

# OSM PBF Processing

OSM PBF (Protocol Buffer Format) is the primary binary format for distributing [[openstreetmap-data-model|OpenStreetMap]] data. Processing PBF files involves reading nodes, ways, and relations, filtering by tags and geometry, and converting to usable geospatial formats.

## Processing Approaches

### Traditional: GDAL/OGR
- Single-threaded execution
- Requires pre-clipping with `ogr2ogr` for spatial filtering
- Outputs to various formats (Shapefile, GeoJSON, etc.)
- Documented in [[legacy-geospatial-etl-pipeline]]

### Modern: QuackOSM
- Multithreaded execution using [[duckdb|DuckDB]] and its [[duckdb-spatial-extension]]
- Geometry-based filtering without pre-clipping
- Direct output to [[geoparquet-vs-iceberg-metadata|GeoParquet]] for cloud-native workflows
- Caching for repeatable computations
- See [[quackosm]]

## Pipeline Integration

OSM PBF processing fits into the [[cloud-native-geospatial-workflow]] as an upstream ingestion step. The GeoParquet output can be queried directly by DuckDB or ingested into [[geospatial-etl-pipeline-iceberg|Iceberg tables]] for further transformation.