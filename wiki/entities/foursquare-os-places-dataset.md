---
type: entity
title: Foursquare OS Places Dataset
created: 2026-04-04
updated: 2026-04-04
tags: [dataset, geospatial, foursquare, locations]
related: [duckdb, motherduck, duckdb-spatial-extension]
sources: ["Mastering Geospatial Analysis with DuckDB Spatial and MotherDuck.md"]
---
# Foursquare OS Places Dataset

A large-scale, open geospatial dataset published by Foursquare containing over 104 million location records worldwide. The dataset is available on Hugging Face and includes rich metadata including place names, categories, addresses, geographic coordinates, and geometry data.

## Key Characteristics

- **Size:** 104,588,312 records (11.05 GB in Parquet format)
- **Access:** Available via Hugging Face Datasets (`hf://datasets/foursquare/fsq-os-places`)
- **Schema:** Includes `fsq_place_id`, `name`, `latitude`, `longitude`, `address`, `locality`, `region`, `country`, `geom` (GEOMETRY type), `bbox` (bounding box struct), `fsq_category_ids`, and more
- **Categories:** Hierarchical category system stored in a companion `fsq_os_categories` table

## Usage with DuckDB

The dataset can be queried directly from Hugging Face using DuckDB's `hf://` interface:

```sql
SELECT count(*) FROM read_parquet('hf://datasets/foursquare/fsq-os-places/release/dt=2025-01-10/places/parquet/*.parquet');
```

Or loaded into MotherDuck for persistent, shared access:

```sql
CREATE TABLE fsq_os_places AS
SELECT * FROM read_parquet('hf://datasets/foursquare/fsq-os-places/release/dt=2025-01-10/places/parquet/*.parquet');
```

## Shared MotherDuck Database

A shared database is available on MotherDuck for easy access:
```sql
ATTACH 'md:_share/foursquare/0cbf467d-03b0-449e-863a-ce17975d2c0b';
```

## Connections

- [[duckdb]] — Primary query engine for the dataset
- [[motherduck]] — Shared database hosting
- [[duckdb-spatial-extension]] — Used for spatial analysis on this dataset