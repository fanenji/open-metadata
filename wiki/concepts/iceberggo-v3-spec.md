type: concept
title: Iceberg GEO v3 Specification
created: 2026-04-29
updated: 2026-04-29
tags: [iceberg, geospatial, specification, v3]
related: [iceberg-geospatial-support, geoparquet-vs-iceberg-metadata, geospatial-vendor-lock-in-avoidance, iceberggo-vs-delta-lake-geospatial, wherobots, havasi]
sources: ["Geospatial Tables in the Open Lakehouse A New Era for Iceberg & Parquet.md"]
---
# Iceberg GEO v3 Specification

The native geospatial data type support introduced in Apache Iceberg v3, enabling spatial data (geometry and geography types) as first-class citizens in the open lakehouse architecture. This specification was developed collaboratively by the Iceberg community, with key contributions from [[Jia Yu]] and [[Szehon Ho]].

## Key Features

- **Geometry and Geography Types**: Two distinct types for planar and spherical coordinate systems.
- **CRS and Edge Interpolation Parameters**: Two metadata parameters that allow writers to specify how data was generated and readers to interpret it correctly. The spec deliberately kept metadata compact to balance simplicity with correctness.
- **Bounding Box Statistics**: Native bounding box statistics at the Parquet row group level (not just file level), enabling finer-grained spatial predicate pushdown for performance optimization.
- **ACID Transactions**: Full support for atomic, consistent, isolated, and durable operations on spatial tables, enabling GDPR compliance and concurrent operations.
- **Schema Evolution and Time Travel**: Standard Iceberg features now available for geospatial data.

## Technical Debates

The specification process involved significant debate around:
- **Anti-meridian bounding boxes**: How to handle bounding boxes that cross the 180° meridian.
- **CRS specification**: Whether to include projjson or keep it simple.
- **Spherical vs. geometry types**: The distinction between geography (spherical) and geometry (planar) types.

## Implementation Status

- The spec has been merged into Iceberg v3 (final vote pending minor additions).
- Parquet logical type release is a dependency for full implementation.
- [[Wherobots]]' Havasu engine already provides an early implementation.
- Other engines (Spark, Flink, Trino) are expected to follow after the Parquet release.

## Significance

Iceberg GEO v3 represents a paradigm shift from file-level (GeoParquet) to table-level geospatial data management, eliminating the need for separate geospatial systems and enabling multi-engine query access.