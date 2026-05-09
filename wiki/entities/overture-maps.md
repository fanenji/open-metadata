---
type: entity
title: Overture Maps
created: 2026-04-08
updated: 2026-04-08
tags: [geospatial, dataset, open-data, mapping]
related: [geoparquet, duckdb-wasm, browser-based-geospatial-analytics, cloud-native-geospatial-workflow]
sources: ["Querying Overture Maps GeoParquet Directly in the Browser with DuckDB WASM.md"]
---
# Overture Maps

An open, collaborative geospatial dataset from companies including Meta, Microsoft, Amazon, and TomTom. Overture Maps provides rich geospatial features (places, buildings, transportation, divisions) designed to power routing, visualization, and analytics.

## Data Format

Overture Maps datasets are distributed in [[GeoParquet]] format — a cloud-native, efficient, columnar storage format with spatial metadata. The data is organized with hive partitioning and is hosted on S3.

## Dataset Structure

The Overture Maps schema includes several thematic layers:
- **places**: Points of interest (hotels, restaurants, shops, etc.)
- **divisions**: Administrative areas (countries, states, localities)
- **buildings**: Building footprints
- **transportation**: Road networks and transit infrastructure

## Access

Official releases are available on S3 with root-level filesystem entry. However, direct querying from browser environments is limited because DuckDB-WASM does not support the HTTPFS extension. Users typically extract subsets using the [Overture Maps Python CLI](https://docs.overturemaps.org/getting-data/overturemaps-py/) and host them in their web application.

## Related

- [[geoparquet]] — The storage format used
- [[duckdb-wasm]] — Browser-based query engine
- [[browser-based-geospatial-analytics]] — Pattern for client-side spatial analysis