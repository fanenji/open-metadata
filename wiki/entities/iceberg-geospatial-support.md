---
type: entity
title: Iceberg Geospatial Support (GEO V3)
created: 2026-05-07
updated: 2026-05-07
tags: [iceberg, geospatial, gis, data-format]
related: [dremio-geospatial-limitations, geospatial-etl-pipeline-iceberg, geoparquet-vs-iceberg-metadata, iceberg-table-versioning, data-lakehouse]
sources: ["Dati Geo con Dremio e Nessie.md"]
---
# Iceberg Geospatial Support (GEO V3)

Apache Iceberg introduced native geospatial types (geometry, geography) in specification V3. This is a relatively recent addition, and its adoption by query engines is not yet universal or fully mature.

## Key Features

- **Native Types:** `geometry` and `geography` column types for storing spatial data directly in Iceberg tables.
- **Spatial Partitioning:** Techniques like XZ2 curves and Hilbert curves are emerging for organizing spatial data within Iceberg to enable query pruning.
- **Spatial Ordering:** Z-ordering can be applied to spatial columns to improve file layout and query performance.
- **Metadata Statistics:** Iceberg manifests can store bounding box statistics for geometry columns, enabling partition pruning at the query planning stage.

## Maturity Status

- Best practices for encoding (WKB vs GeoArrow), partitioning, and indexing are still being consolidated.
- Query engine support varies: [[dremio-geospatial-limitations|Dremio]] has limited native support, while Spark + Sedona is implementing native support.
- The format is a moving target; capabilities and optimizations are expected to improve over time.

## Related Pages

- [[dremio-geospatial-limitations]] — Dremio's specific challenges with Iceberg GEO types.
- [[geospatial-etl-pipeline-iceberg]] — ETL patterns for ingesting spatial data into Iceberg.
- [[geoparquet-vs-iceberg-metadata]] — Overlap and coordination between GeoParquet and Iceberg metadata.
- [[iceberg-table-versioning]] — Iceberg's table-level versioning capabilities.
