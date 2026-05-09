---
type: concept
title: Cloud-Native Geospatial Workflow
created: 2026-04-04
updated: 2026-05-07
tags: [geospatial, cloud-native, duckdb, geoparquet, workflow, s3]
related: [duckdb, geoparquet-vs-iceberg-metadata, geospatial-etl-pipeline-iceberg, duckdb-geoparquet-limitations, duckdb-geoparquet-workflow, duckdb-spatial-extension-usage]
sources: ["duckdb geoparquet tutorials.md", "duckdb-geoparquet-tutorials.md"]
---
# Cloud-Native Geospatial Workflow

A pattern for querying and transforming large geospatial datasets directly from cloud object storage (e.g., S3) without downloading entire files to local storage. Using [[DuckDB]] with the `httpfs` and `spatial` extensions, users can query remote [[geoparquet|GeoParquet]] files via S3 URLs, filter and aggregate data using SQL, and output results to local formats.

## Core Pattern

1. **Install and load DuckDB extensions** – The `httpfs` extension enables direct S3 access, and the `spatial` extension provides geometry functions. Load both in a DuckDB session:
   ```sql
   INSTALL httpfs;
   LOAD httpfs;
   INSTALL spatial;
   LOAD spatial;
   ```
2. **Query remote Parquet files with glob patterns** – Use a standard `SELECT` statement and reference remote files with S3 URLs. Glob patterns (`*`) allow multiple partitioned files to be treated as a single table:
   ```sql
   SELECT * FROM 's3://bucket/country=LAO/*.parquet';
   ```
3. **Convert WKB geometry to DuckDB geometry type** – The `spatial` extension's `ST_GEOMFROMWKB()` function converts binary geometry columns to spatial types:
   ```sql
   SELECT ST_GEOMFROMWKB(geometry) AS geom, * FROM 's3://.../*.parquet';
   ```
4. **Filter and transform** – Apply SQL filters, aggregations, and spatial operations on the streamed data while it remains in the cloud.
5. **Export results** – Write output to local GIS formats (e.g., FlatGeobuf) using DuckDB's GDAL FORMAT output:
   ```sql
   COPY (SELECT ...) TO 'output.fgb' WITH (FORMAT GDAL, DRIVER 'FlatGeobuf');
   ```

## Advantages

- **No local storage required** for source data – query directly on cloud object storage.
- **Simple SQL interface** for complex geospatial queries, enabling rapid ad‑hoc analysis.
- **Fast performance** for small‑to‑medium datasets, leveraging Parquet’s columnar storage for efficient filtering.
- **Lightweight alternative** to heavier Spark‑based pipelines (see [[geospatial-etl-pipeline-iceberg]]).

## Limitations

- **No native GeoParquet output** – DuckDB does not natively produce valid GeoParquet files. WKB output must be converted using the external `gpq` CLI tool.
- **Spatial reference system (SRS)** – The SRS is not consistently set in output files.
- **Progress reporting** – The progress indicator is inaccurate for remote files.
- **Large datasets** – Very large datasets may require local persistence for repeated access due to streaming overhead.

## Related Patterns

- [[duckdb-geoparquet-workflow]] – Structured step‑by‑step implementation of this pattern.
- [[duckdb-spatial-extension-usage]] – Detailed function reference for spatial operations.
- [[duckdb-geoparquet-limitations]] – Known limitations and workarounds.
- [[geoparquet-vs-iceberg-metadata]] – Comparison of GeoParquet and Iceberg metadata.
- [[geospatial-etl-pipeline-iceberg]] – Alternative Spark‑based ETL pipeline.