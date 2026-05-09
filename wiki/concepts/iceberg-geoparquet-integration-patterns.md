---
type: concept
title: Iceberg-GeoParquet Integration Patterns
created: 2026-04-29
updated: 2026-04-29
tags: [iceberg, geoparquet, geospatial, architecture, data-lakehouse]
related: [iceberg-geospatial-support, geoparquet-vs-iceberg-metadata, geospatial-etl-pipeline-iceberg, spatial-partitioning-strategies-for-iceberg, nessie-catalog-versioning, duckdb-iceberg-extension]
sources: ["Iceberg e GeoParquet - Strumenti per Integrazione.md"]
---
# Iceberg-GeoParquet Integration Patterns

This concept synthesizes architectural patterns, tooling choices, and best practices for combining Apache Iceberg and GeoParquet for geospatial workloads. The integration leverages Iceberg's table management (ACID transactions, schema evolution, time travel, hidden partitioning) with GeoParquet's columnar storage, spatial metadata, and cloud-native access. Key patterns include:

- **Centralized Data Lakehouse**: Iceberg manages tables of GeoParquet files, with Apache Spark + Apache Sedona used for processing and analysis.
- **Distributed Architecture with Nessie**: Project Nessie provides version control and governance of metadata across multiple Iceberg catalogs containing GeoParquet data.
- **Lightweight Query with DuckDB**: DuckDB's spatial extension enables direct querying of Iceberg tables and standalone GeoParquet files.
- **Interoperability with GDAL and Geopandas**: Established geospatial libraries can read/write GeoParquet files managed by Iceberg.

Best practices include strategic spatial partitioning, leveraging spatial indexing (e.g., from Sedona), optimizing GeoParquet file sizes, and careful schema evolution management. The integration is particularly suited for large-scale geospatial processing, location intelligence, historical versioning, and collaborative data science workflows.