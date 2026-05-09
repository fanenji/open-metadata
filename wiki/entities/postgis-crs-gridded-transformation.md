---
type: entity
title: PostGIS CRS Gridded Transformation
created: 2026-02-13
updated: 2026-02-13
tags: [postgis, crs, transformation, geospatial]
related: [postgis, crs-transformation-strategy, sdi-data-platform-integration]
sources: ["SDI Data Integration to Data Platform.md"]
---
# PostGIS CRS Gridded Transformation

The capability of PostGIS to perform coordinate reference system (CRS) transformations using gridded data files installed on the database server. This is a critical capability for the SDI-to-DP integration, as the transformation from source CRS to EPSG:7791 requires grid-based correction.

## Key Function

- `ST_Transform(geometry, target_srid)` — transforms geometry from its current CRS to the target CRS
- Uses grid shift files (e.g., NTv2) installed on the PostgreSQL server for high-accuracy transformations
- Grid files are configured in the `proj` library that PostGIS depends on

## Advantages Over Alternatives

- **Native Support**: Grid files are managed at the database level, not in application code
- **Accuracy**: PostGIS uses the PROJ library with proper grid file handling
- **Performance**: Can be optimized with spatial indexes and server tuning
- **Reliability**: Mature, well-tested implementation

## Performance Considerations

- `ST_Transform` is computationally expensive, especially for complex geometries
- Under concurrent read/write load, the database server must be adequately sized
- Materialized Views can pre-compute transformed data to reduce runtime load
- Regular `VACUUM ANALYZE` on source tables helps maintain performance

## Usage in SDI-DP Integration

In the recommended Alternative B approach:
1. PostGIS performs `ST_Transform(geometry, 7791)` during Phase 1 (Oracle→PostGIS)
2. Spark reads already-transformed data via JDBC with `ST_AsBinary(ST_Transform(...))`
3. The transformation burden is on PostGIS, not the DP ingestion layer