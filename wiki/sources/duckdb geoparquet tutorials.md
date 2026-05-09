---
type: source
title: DuckDB and GeoParquet Tutorial
created: 2026-04-04
updated: 2026-04-04
tags: [duckdb, geoparquet, tutorial, geospatial]
related: [duckdb, cloud-native-geospatial-workflow, duckdb-geoparquet-limitations, geoparquet-vs-iceberg-metadata, geospatial-etl-pipeline-iceberg]
sources: ["duckdb geoparquet tutorials.md"]
authors: [cholmes]
year: 2024
url: "https://github.com/cholmes/duckdb-geoparquet-tutorials"
venue: GitHub
---
# DuckDB and GeoParquet Tutorial

A practical tutorial demonstrating how to use [[DuckDB]] to access and transform cloud-native geospatial data from the Google Open Buildings dataset hosted on source.coop. The tutorial covers setting up DuckDB with the `httpfs` and `spatial` extensions, querying remote GeoParquet files directly from S3, converting WKB geometry to valid GeoParquet using `gpq`, and outputting to formats like FlatGeobuf via GDAL. It highlights DuckDB's simplicity for cloud-native geospatial workflows compared to heavier Spark-based pipelines, while also documenting current limitations such as the lack of native GeoParquet output and inconsistent spatial reference system handling.