---
type: concept
title: GeoParquet vs Iceberg Metadata
created: 2026-04-04
updated: 2026-04-04
tags: [geoparquet, iceberg, metadata, geospatial, comparison]
related: [duckdb, cloud-native-geospatial-workflow, geospatial-etl-pipeline-iceberg, duckdb-iceberg-extension]
sources: ["duckdb geoparquet tutorials.md"]
---
# GeoParquet vs Iceberg Metadata

Analysis of metadata overlap and coordination strategies between GeoParquet and Apache Iceberg for geospatial data management.

## DuckDB as a Lightweight Query Engine

[[DuckDB]] serves as a lightweight query engine for both GeoParquet and Iceberg tables. For GeoParquet, DuckDB can query remote files directly from S3 using the `httpfs` extension, providing a simple alternative to heavier Spark-based pipelines. This pattern parallels the [[duckdb-iceberg-extension]] pattern for Iceberg tables.

### Key Differences
- **GeoParquet**: DuckDB queries Parquet files directly via S3 URLs, with geometry stored as WKB. No catalog or table management required.
- **Iceberg**: DuckDB uses the `iceberg` extension with `iceberg_scan()` to query Iceberg tables, requiring catalog metadata.

### Practical Considerations
- GeoParquet workflows are simpler for ad-hoc geospatial queries on static datasets.
- Iceberg provides ACID transactions, time travel, and schema evolution for production pipelines.
- DuckDB's lack of native GeoParquet output is a limitation for both formats when writing geospatial results.

For a detailed comparison of versioning strategies, see [[data-lakehouse-versioning-strategies]].