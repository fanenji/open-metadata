---
type: entity
title: GeoParquet vs Iceberg Metadata Overlap
created: 2026-05-07
updated: 2026-05-07
tags: [geoparquet, iceberg, metadata, geospatial, gis]
related: [iceberg-geospatial-support, geospatial-etl-pipeline-iceberg, dremio-geospatial-limitations]
sources: ["Dati Geo con Dremio e Nessie.md"]
---
# GeoParquet vs Iceberg Metadata Overlap

GeoParquet and Iceberg both manage metadata about spatial data, creating potential overlap and coordination challenges.

## GeoParquet Metadata

- Embedded within the Parquet file format.
- Includes Coordinate Reference System (CRS), bounding box per row group, and geometry encoding type.
- Provides row-group-level spatial statistics for query engines that read GeoParquet directly.

## Iceberg Metadata

- Managed in Iceberg manifest files at the table level.
- Includes column-level statistics, including spatial bounds (min/max for geometry columns).
- Enables partition pruning and query optimization at the Iceberg catalog level.

## Overlap and Coordination

- Both systems can store bounding box information, potentially leading to inconsistency if not synchronized.
- Query engines (like Dremio) may use one or both sources of metadata, affecting query optimization.
- Best practices for ensuring consistency are still evolving.

## Implications

For optimal performance, the ETL pipeline should ensure that Iceberg manifest statistics are computed correctly from the GeoParquet data. See [[geospatial-etl-pipeline-iceberg]] for the recommended pipeline pattern.
