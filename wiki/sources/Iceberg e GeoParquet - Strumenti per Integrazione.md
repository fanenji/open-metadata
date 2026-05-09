---
type: source
title: "Iceberg e GeoParquet: Strumenti per Integrazione"
created: 2026-03-18
updated: 2026-03-18
tags: [geospatial, iceberg, geoparquet, data-lakehouse, gis]
related: [iceberg-geospatial-support, geoparquet-vs-iceberg-metadata, geospatial-etl-pipeline-iceberg, nessie-catalog-versioning, duckdb-iceberg-extension, spatial-partitioning-strategies-for-iceberg, iceberg-geoparquet-integration-patterns]
sources: ["Iceberg e GeoParquet - Strumenti per Integrazione.md"]
authors: []
year: 2025
url: ""
venue: ""
---
# Iceberg e GeoParquet: Strumenti per Integrazione

This source document provides a comprehensive overview of integrating Apache Iceberg with GeoParquet for managing cartographic data in a data lakehouse architecture. It covers the native geospatial support in Iceberg v3 (geometry and geography types), the metadata structure of GeoParquet, and the tooling ecosystem (Apache Spark + Apache Sedona, DuckDB, Project Nessie, GDAL, Geopandas) for reading, writing, and analyzing GeoParquet data managed by Iceberg. The document also discusses architectural patterns, best practices for spatial partitioning and indexing, and use cases such as large-scale geospatial processing, location intelligence, historical versioning, and collaborative workflows.