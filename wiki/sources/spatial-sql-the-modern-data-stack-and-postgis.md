type: source
title: "Spatial SQL, the Modern Data Stack, and PostGIS"
created: 2026-05-07
updated: 2026-05-07
tags: [spatial-sql, postgis, modern-data-stack, geospatial, duckdb, dbt, h3]
related: [postgis, duckdb, dbt, h3-geospatial-indexing, duckdb-spatial-extension, modern-geospatial-data-stack, postgis-as-central-hub, duckdb-postgis-integration, spatial-sql-book-mbforr, noaa-storms-database, cloud-native-geospatial-workflow, modern-gis-workshop]
sources: ["spatial-sql-the-modern-data-stack-and-postgis.md"]
authors: [Matt Forrest]
year: 2023
url: "https://www.youtube.com/watch?v=IPSNyGL1YN0"
venue: "Crunchy Data"
---
# Spatial SQL, the Modern Data Stack, and PostGIS

A talk by [[Matt Forrest]] (Carto) presented at Crunchy Data, arguing that PostGIS remains the central hub of any modern geospatial data infrastructure. The talk demonstrates a practical flash flood analysis use case combining NOAA storm data, FEMA flood zones, Copernicus DEM, and H3 aggregation — all orchestrated through PostGIS, DuckDB, and dbt.

## Key Arguments

- **PostGIS as central hub**: PostGIS connects to DuckDB (via Foreign Data Wrapper), dbt, H3, remote rasters (COG/STAC), QGIS, GeoPandas, and Leafmap — making it the interconnectivity layer of the modern geospatial data stack.
- **SQL as lingua franca**: All tools in the modern data stack (dbt, DuckDB, BI) converge on SQL, making spatial SQL the natural language for geospatial analytics.
- **Simplified geospatial workflows**: Specialized tools for specific tasks (DuckDB for bulk CSV, PostGIS for complex spatial joins, dbt for orchestration) work together seamlessly.

## Demonstrated Use Case

Flash flood analysis combining:
1. **NOAA Historical Storms Database** — FTP-hosted, gzipped CSV files (1950–present) with event narratives
2. **FEMA National Flood Hazard Layer** — Esri JSON served via GDAL into PostGIS
3. **Copernicus 30m DEM** — Cloud-Optimized GeoTIFF accessed via STAC/AWS Open Data
4. **H3 polyfill** — Converting polygons to H3 hex cells for massive-scale string joins

## Technical Demonstrations

- **DuckDB Foreign Data Wrapper**: Running DuckDB queries as foreign tables inside PostGIS (demonstrated in pgAdmin)
- **Full-Text Search (FTS) for flash flood classification**: Using PostgreSQL FTS on event narratives to score/classify flash flood events
- **dbt + DuckDB pipeline**: dbt orchestrates DuckDB to process remote CSV data, append to PostGIS
- **Remote raster querying**: Reading Cloud-Optimized GeoTIFFs directly from S3 via PostGIS raster functions
- **H3 polyfill performance**: Claimed as "most efficient" implementation for polygon-to-hex conversion

## Related Resources

- Book: "Spatial SQL" by Matt Forrest (Manning Publications, released concurrently with this talk)
- Slides: https://docs.google.com/presentation/d/1H62w-XdtkInHNsN2wHyUBfJBEV0Ods3s31c6trG0T8Y