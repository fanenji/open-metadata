type: entity
title: SWORD Dataset
created: 2026-04-08
updated: 2026-04-08
tags: [geospatial, dataset, hydrology]
related: [geoparquet, duckdb]
sources: ["A Modern Geospatial Workflow PyEnv, Poetry, DuckDB, and JuPySQL.md"]
---
# SWORD Dataset

The **SWORD (SWOT River Database) v16** is a large-scale geospatial dataset designed to support the **SWOT (Surface Water and Ocean Topography)** satellite mission.

### Characteristics
- **Scale:** Contains approximately 4GB of uncompressed data, comprising millions of river nodes and reaches.
- **Content:** Provides high-resolution attributes such as water surface elevation, width, flow accumulation, and river geometry.

- **Formats:** Available in Shapefile, GeoPackage, and netCDF.

In modern workflows, it is recommended to convert these datasets from GeoPackage to [[geoparquet]] to leverage the high-performance analytical capabilities of engines like [[duckdb]].