---
type: entity
title: Iceberg V3 Geo Types
created: 2026-04-29
updated: 2026-04-29
tags: [iceberg, geospatial, v3, geometry]
related: [geoparquet-origins, spatial-predicate-pushdown, iceberg-rest-catalog, foursquare-geospatial-architecture, geoparquet-vs-iceberg-metadata, iceberg-geospatial-support]
sources: ["Geospatial Tables in the Open Lakehouse A New Era for Iceberg & Parquet - Summary.md"]
---
# Iceberg V3 Geo Types

Apache Iceberg V3 introduces native geospatial types (geometry and geography) with two configurable parameters: **CRS** (Coordinate Reference System) and **edge interpolation** (spherical/geodesic vs. planar/Cartesian). This is the first time a table format has native geospatial support, enabling row-group-level bounding box statistics and two-level spatial pruning.

## Key Features

- **CRS + edge interpolation as compact identifiers**: Solves the core problem that the same WKB bytes can represent different places on Earth depending on the CRS and edge convention used by the writer.
- **Row-group-level bounding box statistics**: Unlike GeoParquet (file-level only), native Parquet geo types store bounding box statistics at the row-group level, enabling finer-grained predicate pushdown.
- **Two-level spatial pruning**: Iceberg file-level statistics + Parquet row-group-level statistics combine to skip irrelevant data before any geometry is decoded.
- **Versioned into Iceberg V3**: The spec was near-final vote at the time of the panel (May 2025).

## Design Debates

The hardest design challenge was balancing **completeness** (geospatial has many obscure edge cases like anti-meridian, spherical vs. planar edges, different CRS authority codes) against **compactness** (Iceberg types are serialized; verbose JSON-based CRS definitions are not feasible). The resolution was two compact parameters that correctly interpret any real-world dataset without specifying every possible obscure case.

## Implementation Timeline

- Parquet geo type specification: Merged February 2025
- Iceberg V3 geo type specification: Near-final vote (May 2025)
- Wherobots (Havasu) early implementation: Available on Wherobots Cloud
- Java/Rust/Python Iceberg reference implementations: In progress
- Snowflake/BigQuery/Spark native support: Pending V3 spec finalization

## Relationship to Other Formats

The geo types were defined at the Parquet level (not Iceberg-specific) so that Delta Lake and any other Parquet-based format can adopt the same definition. GeoParquet remains the file-level metadata convention; Iceberg V3 adds native types with row-group statistics on top.
