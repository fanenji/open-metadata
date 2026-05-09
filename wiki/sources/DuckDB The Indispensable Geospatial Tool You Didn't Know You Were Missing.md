---
type: source
title: "DuckDB: The Indispensable Geospatial Tool You Didn't Know You Were Missing"
created: 2026-04-29
updated: 2026-04-29
tags: [duckdb, geospatial, cloud-native-geospatial, geoparquet, spatial-extension]
related: [duckdb, duckdb-spatial-extension, cloud-native-geospatial-with-duckdb, cloud-native-geospatial-workflow, duckdb-geoparquet-limitations, geoparquet-vs-iceberg-metadata, postgis]
sources: ["DuckDB The Indispensable Geospatial Tool You Didn't Know You Were Missing.md"]
authors: [Chris Holmes]
year: 2023
url: "https://cloudnativegeo.org/blog/2023/09/duckdb-the-indispensable-geospatial-tool-you-didnt-know-you-were-missing"
venue: "Cloud Native Geospatial Blog"
---
# DuckDB: The Indispensable Geospatial Tool You Didn't Know You Were Missing

A blog post by Chris Holmes (Radiant Earth Technical Fellow) arguing that DuckDB is a transformative tool for geospatial analytics. The author shares his experience using DuckDB to process the 100GB Google Open Buildings dataset, highlighting its ease of use, performance advantages over Pandas and PostGIS, and cloud-native capabilities. The post covers DuckDB's spatial extension (leveraging GEOS and GDAL/OGR), its ability to query remote Parquet files on S3/HTTPS without configuration, and its potential to democratize geospatial analysis by meeting non-spatial users where they are (SQL, not GDAL). Key limitations noted include lack of persistent CRS, no native GeoParquet output, and absence of spatial indexing, though the author argues brute-force performance is often sufficient. The post positions DuckDB as complementary to PostGIS, not a replacement.
