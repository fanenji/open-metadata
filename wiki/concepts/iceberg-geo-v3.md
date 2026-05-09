---
type: concept
title: Iceberg GEO V3
created: 2026-04-29
updated: 2026-04-29
tags: [iceberg, geospatial, data-lakehouse, standard]
related: [iceberg-geospatial-support, geoparquet-vs-iceberg-metadata, geospatial-etl-pipeline-iceberg, apache-sedona, dremio-geospatial-limitations, geoarrow]
sources: ["Ingestione dati cartografici_ analisi alternative.md"]
---
# Iceberg GEO V3

Iceberg GEO V3 refers to the native geospatial type support introduced in Apache Iceberg specification version 3. It represents a significant evolution in treating geospatial data as first-class citizens within the data lakehouse architecture.

## Native Types

- **geometry**: Assumes calculations on a Cartesian plane, suitable for local or projected analyses.
- **geography**: Designed for calculations on an ellipsoidal surface, appropriate for global-scale applications.

Both types are based on OGC Simple Features and ISO 19107 standards, supporting Point, LineString, Polygon, Multi* variants, and GeometryCollection.

## Encoding

The primary encoding for geometry/geography types within underlying file formats (Parquet) is Well-Known Binary (WKB). WKB is an established OGC standard that supports geometries with additional dimensions (Z for elevation, M for measures) but does not inherently include SRID information. Alternative encodings like [[geoarrow]] are discussed as potential higher-performance options.

## Spatial Partitioning and Indexing

- **Hidden Partitioning**: Iceberg's mechanism where partition values do not need to be physical columns in the table.
- **XZ2 Curve**: A proposed partition transformation for spatial data, explored in implementations like Havasu and GeoLake.
- **Hilbert Curve**: Space-filling curve proposed for ordering data within files to improve row-group level spatial filtering.
- **Z-ordering**: Technique for colocating spatially close data, applicable by computing discrete spatial indices (geohash, H3, S2) on a geometry column.

Native spatial indexing within Iceberg itself (like R-trees in traditional spatial databases) is still an area under development. Performance depends heavily on the query engine's ability to leverage Iceberg metadata for pruning.

## CRS Management

Supports SRID (e.g., srid:4326), PROJJSON (self-contained, detailed CRS definitions), and EPSG formats. WKT2 compatibility is also discussed.

## Maturity and Adoption

- Relatively recent feature (Iceberg V3), still evolving
- Query engine support is not universal
- Documentation and best practices are still being consolidated
- Contrasts with the maturity of dedicated spatial databases like PostGIS

## Related

- [[iceberg-geospatial-support]] — Broader overview of Iceberg's geospatial capabilities
- [[geoparquet-vs-iceberg-metadata]] — Metadata overlap between GeoParquet and Iceberg
- [[geospatial-etl-pipeline-iceberg]] — ETL pattern for ingesting spatial data into Iceberg
- [[apache-sedona]] — One of the first engines to support Iceberg GEO types
- [[dremio-geospatial-limitations]] — Dremio's limited native support for Iceberg GEO types
