---
type: concept
title: DuckDB Spatial Functions Reference
created: 2026-04-04
updated: 2026-04-04
tags: [duckdb, spatial, functions, reference]
related: [duckdb-spatial-extension, spatial-indexing-concepts, geospatial-performance-patterns]
sources: ["Mastering Geospatial Analysis with DuckDB Spatial and MotherDuck.md"]
---
# DuckDB Spatial Functions Reference

Key spatial functions provided by the DuckDB Spatial extension, as demonstrated in the "Mastering Geospatial Analysis" article.

## Core Functions

### `ST_Point(x, y)`
Creates a point geometry from longitude (x) and latitude (y) coordinates.
```sql
ST_Point(8.5417, 47.3769)  -- Creates a point for Zurich
```

### `ST_Distance_Spheroid(geom1, geom2)`
Calculates the distance in meters between two geometries on a spheroidal Earth model. More accurate than planar distance for large areas.
```sql
ST_Distance_Spheroid(ST_Point(p.longitude, p.latitude), c.center)
```

### `ST_DWithin(geom1, geom2, distance)`
Returns true if geometries are within a specified distance of each other. More efficient than calculating exact distances for proximity filtering.
```sql
ST_DWithin(a.location, b.location, 2)  -- Stores within 2 meters
```

### `ST_Read(path)`
Reads geospatial vector file formats via GDAL.
```sql
ST_Read('some/file/path/filename.geojson')
```

### `ST_Intersects(geom1, geom2)`
Returns true if geometries share any space.

## GDAL-based COPY

Export DuckDB tables to geospatial vector formats:
```sql
COPY table_name TO 'output.geojson'
WITH (FORMAT GDAL, DRIVER 'GeoJSON', LAYER_CREATION_OPTIONS 'WRITE_BBOX=YES');
```

## Installation and Loading

```sql
INSTALL spatial;
LOAD spatial;
```

## Connections

- [[duckdb-spatial-extension]] — The extension providing these functions
- [[spatial-indexing-concepts]] — Performance concepts behind spatial operations
- [[geospatial-performance-patterns]] — How to use these functions efficiently