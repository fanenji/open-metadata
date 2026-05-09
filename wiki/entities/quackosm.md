---
type: entity
title: QuackOSM
created: 2026-04-08
updated: 2026-04-08
tags: ["geospatial", "openstreetmap", "duckdb", "tool", "library"]
related: ["duckdb", "duckdb-spatial-architecture", "openstreetmap-data-model", "duckdb-spatial-extension", "geoparquet", "geoarrow", "osm-pbf-processing", "cloud-native-geospatial-workflow", "kraina-ai"]
sources: ["DuckDB Spatial Supercharged Geospatial SQL.md", "QuackOSM.md"]
---

# QuackOSM

QuackOSM is an open-source Python library and CLI tool for reading [[openstreetmap-data-model|OpenStreetMap]] PBF files using [[duckdb|DuckDB]]. It is maintained by [[kraina-ai|Kraina AI]].

## Capabilities

- **Scalable OSM PBF reading**: Processes Protocol Buffer files with multithreading, unlike GDAL's single-threaded approach.
- **GeoParquet output**: Converts OSM data directly to [[geoparquet-vs-iceberg-metadata|GeoParquet]] format for cloud-native geospatial workflows.
- **Spatial filtering**: Filters OSM features by geometry without requiring pre-clipping via `ogr2ogr`.
- **Tag filtering**: Filters features by OSM key-value tags (e.g., `highway`, `building`).
- **Caching**: Reduces repeatable computations for improved performance on repeated queries.

## Dependencies

- [[duckdb]] (>=0.9.2) with [[duckdb-spatial-extension]]
- [[geoarrow]] (via geoarrow-pyarrow >=0.1.1)
- geopandas, shapely, pyarrow

## Usage

```python
import quackosm as qosm

# Load as GeoDataFrame
gdf = qosm.get_features_gdf("monaco.osm.pbf")

# Convert to GeoParquet
gpq_path = qosm.convert_pbf_to_gpq("monaco.osm.pbf")
```

## Role in the Geospatial Pipeline

QuackOSM serves as a modern alternative to the [[legacy-geospatial-etl-pipeline]]'s GDAL/OGR approach for OSM data ingestion. It fits naturally into the [[cloud-native-geospatial-workflow]] as an upstream step, producing GeoParquet files that can be queried directly by DuckDB or ingested into [[geospatial-etl-pipeline-iceberg|Iceberg tables]].