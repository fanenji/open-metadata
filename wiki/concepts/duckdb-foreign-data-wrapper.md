---
type: concept
title: DuckDB Foreign Data Wrapper
created: 2026-05-07
updated: 2026-05-07
tags: [duckdb, postgis, foreign-data-wrapper, postgresql, integration]
related: [duckdb, postgis, duckdb-postgis-integration, postgis-as-central-hub]
sources: ["spatial-sql-the-modern-data-stack-and-postgis.md"]
---
# DuckDB Foreign Data Wrapper

A PostgreSQL extension that allows DuckDB queries to be exposed as foreign tables in PostgreSQL (and by extension, PostGIS). This enables hybrid processing where DuckDB handles bulk/long data and PostGIS handles complex spatial analysis — all queryable from a single interface.

## How It Works

1. Install the DuckDB FDW extension (requires `pg_config` to be available)
2. Create a foreign server in PostgreSQL pointing to a DuckDB database file
3. Create foreign tables that map to DuckDB queries or tables
4. Query the foreign tables as if they were native PostgreSQL tables

## Key Benefits

- **No data movement**: DuckDB reads remote files directly; PostgreSQL queries them via FDW
- **Best tool for each job**: DuckDB excels at columnar OLAP on long data; PostGIS excels at spatial analysis
- **Single interface**: Run DuckDB queries from pgAdmin or any PostgreSQL client

## Use Case Example

From [[Matt Forrest]]'s flash flood analysis:
- DuckDB reads multiple gzipped CSV files from NOAA's FTP server
- DuckDB processes the data (casting, FTS classification)
- The processed data is exposed as a foreign table in PostGIS
- PostGIS performs spatial joins against FEMA flood zones and Copernicus DEM raster data

## Related

- [[duckdb-postgis-integration]] — The broader integration pattern
- [[postgis-as-central-hub]] — How this fits into the central hub thesis