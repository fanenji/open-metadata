---
type: concept
title: PostGIS as Central Hub
created: 2026-05-07
updated: 2026-05-07
tags: [postgis, modern-data-stack, geospatial, architecture]
related: [postgis, duckdb, dbt, h3-geospatial-indexing, modern-geospatial-data-stack, duckdb-postgis-integration, cloud-native-geospatial-workflow]
sources: ["spatial-sql-the-modern-data-stack-and-postgis.md"]
---
# PostGIS as Central Hub

The thesis that PostGIS serves as the central interconnectivity layer in the modern geospatial data stack. Rather than being replaced by cloud data warehouses or lakehouse architectures, PostGIS connects to and enhances all emerging geospatial tools.

## Core Argument

As articulated by [[Matt Forrest]] in his talk "Spatial SQL, the Modern Data Stack, and PostGIS," PostGIS remains essential because:

1. **Interconnectivity**: PostGIS connects to DuckDB (FDW), dbt, H3, remote rasters (COG/STAC), QGIS, GeoPandas, and Leafmap
2. **Spatial functionality**: Cloud data warehouses have a core set of spatial functions but "nowhere near the volume and the breadth" of PostGIS
3. **Raster support**: PostGIS "set the standards for rasters in databases" — most comprehensive raster tooling
4. **Performance**: `ST_Intersects` is "very performant" at scale; H3 polyfill is "incredibly fast"

## Architecture

The central hub pattern works as follows:
- **DuckDB** handles bulk CSV processing, remote file reading, and large-scale non-spatial joins
- **PostGIS** handles complex spatial analysis, raster processing, and H3 aggregation
- **dbt** orchestrates the pipeline end-to-end
- All data flows through PostGIS as the central storage and analysis layer

## Tensions

- The actual workflow has DuckDB doing significant preprocessing — PostGIS's "centrality" is more about interconnectivity than processing dominance
- The full workflow requires PostgreSQL, PostGIS, DuckDB FDW, dbt, and Docker — significant infrastructure
- Performance claims ("very performant," "incredibly fast") are asserted without quantitative benchmarks
- This architecture contrasts with lakehouse approaches (Iceberg + Dremio/Spark) that use object storage as the primary storage layer

## Related

- [[modern-geospatial-data-stack]] — The broader architecture diagram
- [[duckdb-postgis-integration]] — Technical details of the DuckDB FDW pattern
- [[cloud-native-geospatial-workflow]] — Complementary pattern using DuckDB + GeoParquet