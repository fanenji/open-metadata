---
type: concept
title: Spatial Partitioning in Iceberg
created: 2026-04-29
updated: 2026-04-29
tags: [iceberg, geospatial, partitioning, performance, data-lakehouse]
related: [iceberg-geo-v3, iceberg-geospatial-support, geoparquet-vs-iceberg-metadata, geospatial-etl-pipeline-iceberg, h3-geospatial-indexing]
sources: ["Ingestione dati cartografici_ analisi alternative.md"]
---
# Spatial Partitioning in Iceberg

Spatial Partitioning in Iceberg refers to the techniques and mechanisms for organizing geospatial data within Iceberg tables to optimize spatial query performance through data skipping and pruning.

## Iceberg's Hidden Partitioning

Iceberg uses "hidden partitioning" where partition values do not need to be physical columns in the table. This mechanism can be extended for geospatial data through various transformation strategies.

## Proposed Spatial Partitioning Techniques

### XZ2 Curve
A spatial partitioning transformation proposed for Iceberg, explored in implementations like Havasu and GeoLake. It converts 2D spatial coordinates into a single partition value using a space-filling curve approach.

### Hilbert Curve Ordering
A space-filling curve proposed for ordering data within files to improve row-group level spatial filtering. Data points close in space are likely to be close in the Hilbert curve order, improving compression and filtering efficiency.

### Z-ordering
A technique for colocating spatially close data within files. It can be applied by computing discrete spatial indices (geohash, H3, S2) on a geometry column and using these computed indices for ordering or partitioning. Dremio supports Z-ordering for Iceberg tables in general.

## Metadata-Based Pruning

Iceberg's key performance feature for spatial queries is the use of min/max column statistics (including spatial bounds for geometry columns) stored in manifest files. During query planning, Iceberg uses these statistics to:

1. **Manifest Pruning**: Skip entire manifest files based on statistics
2. **File Pruning**: Skip individual data files that don't satisfy spatial filters

## Maturity Considerations

- Native spatial indexing within Iceberg itself (like R-trees in traditional spatial databases) is still an area under development
- Performance depends heavily on the query engine's ability to leverage Iceberg metadata
- External spatial indexing approaches (e.g., Apache Lucene) are being explored
- Achieving high spatial query performance may depend more on the query engine's capabilities (e.g., Sedona's spatial indexing) or careful physical data organization (Z-ordering) than on mature spatial indexing within Iceberg itself

## Related

- [[iceberg-geo-v3]] — Native GEO types in Iceberg V3
- [[iceberg-geospatial-support]] — Broader overview of Iceberg's geospatial capabilities
- [[geoparquet-vs-iceberg-metadata]] — Metadata coordination between GeoParquet and Iceberg
- [[h3-geospatial-indexing]] — Alternative spatial indexing approach using H3 hexagons
- [[geospatial-etl-pipeline-iceberg]] — ETL pattern for spatial data into Iceberg
