---
type: source
title: QuackOSM
created: 2026-04-08
updated: 2026-04-08
tags: [duckdb, mapping, openstreetmap, geospatial]
related: [quackosm, duckdb, duckdb-spatial-extension, geoparquet, openstreetmap-data-model, geoarrow, osm-pbf-processing, cloud-native-geospatial-workflow]
sources: ["QuackOSM.md"]
authors: [Kraina AI]
year: 2024
url: "https://kraina-ai.github.io/quackosm/0.2.0/"
venue: ""
---

# QuackOSM

An open-source tool for reading OpenStreetMap PBF files using DuckDB. QuackOSM provides a scalable, multithreaded alternative to GDAL for processing OSM data, outputting results in the GeoParquet format for integration with modern cloud-native geospatial stacks.

## Key Features

- **Multithreaded OSM PBF reading**: Unlike GDAL's single-threaded execution, QuackOSM utilizes multithreading for faster processing.
- **GeoParquet output**: Saves results in the GeoParquet format for cloud-native workflows.
- **Geometry-based filtering**: Filter OSM data by spatial geometry without requiring pre-clipping with `ogr2ogr`.
- **OSM tag filtering**: Filter features by OSM key-value tags.
- **Caching**: Reduces repeatable computations for performance optimization.
- **Dual interface**: Usable as a Python module or via a CLI built on Typer.

## Dependencies

- duckdb (>=0.9.2)
- pyarrow (>=13.0.0)
- geoarrow-pyarrow (>=0.1.1)
- geopandas
- shapely
- typeguard

## Usage

```python
import quackosm as qosm

# Load as GeoDataFrame
gdf = qosm.get_features_gdf(monaco_pbf_path)

# Convert PBF to GeoParquet
gpq_path = qosm.convert_pbf_to_gpq(monaco_pbf_path)
```

## Connections

QuackOSM strengthens the [[duckdb-spatial-extension]] by demonstrating a real-world use case for DuckDB's spatial capabilities. It extends the [[cloud-native-geospatial-workflow]] by adding an OSM PBF → GeoParquet pipeline. It serves as a modern alternative to the [[legacy-geospatial-etl-pipeline]]'s GDAL/OGR approach for OSM data ingestion.