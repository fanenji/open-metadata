---
type: concept
title: DuckDB-PostGIS Integration
created: 2026-05-07
updated: 2026-05-07
tags: [duckdb, postgis, foreign-data-wrapper, geospatial, integration]
related: [duckdb, postgis, postgis-as-central-hub, modern-geospatial-data-stack, duckdb-spatial-extension]
sources: ["spatial-sql-the-modern-data-stack-and-postgis.md"]
---
# DuckDB-PostGIS Integration

The integration pattern between DuckDB and PostGIS using the DuckDB Foreign Data Wrapper (FDW) for PostgreSQL. This enables hybrid processing where each tool handles the workloads it is best suited for.

## Architecture

The DuckDB FDW allows DuckDB queries to be exposed as foreign tables inside PostGIS. This means:
- DuckDB handles bulk CSV processing, remote file reading, and large-scale joins on non-spatial data
- PostGIS handles complex spatial analysis, raster processing, and H3 aggregation
- Both tools can be queried from a single interface (e.g., pgAdmin)

## Use Case Example

From [[Matt Forrest]]'s flash flood analysis:
1. DuckDB reads multiple gzipped CSV files from NOAA's FTP server (remote files, auto-detected schema)
2. DuckDB processes the data (casting, FTS classification)
3. The processed data is exposed as a foreign table in PostGIS
4. PostGIS performs spatial joins against FEMA flood zones and Copernicus DEM raster data
5. Results are aggregated using H3 polyfill

## Benefits

- **No data movement**: DuckDB reads remote files directly; PostGIS queries them via FDW
- **Best tool for each job**: DuckDB excels at columnar OLAP on long data; PostGIS excels at spatial analysis
- **SQL everywhere**: Both tools use SQL, making the integration seamless

## Setup

1. Install the DuckDB FDW extension (requires `pg_config`)
2. Create a foreign server in PostGIS pointing to the DuckDB database file
3. Create foreign tables that map to DuckDB queries
4. Query the foreign tables as if they were native PostGIS tables

## Related

- [[postgis-as-central-hub]] — The broader thesis of PostGIS as interconnectivity layer
- [[duckdb-spatial-extension]] — DuckDB's own spatial capabilities
- [[cloud-native-geospatial-workflow]] — Complementary DuckDB + GeoParquet pattern