---
type: entity
title: SDI Data Platform Integration
created: 2026-02-13
updated: 2026-02-13
tags: [sdi, data-platform, integration, architecture]
related: [legacy-geospatial-etl-pipeline, oracle-to-postgresql-gdal-etl, geospatial-etl-pipeline-iceberg, postgis, geoscript-modernization, crs-transformation-strategy, raster-ingestion-pattern]
sources: ["SDI Data Integration to Data Platform.md"]
---
# SDI Data Platform Integration

The integration architecture between the existing Spatial Data Infrastructure (SDI) of Regione Liguria and the new Data Platform (DP). This integration involves ingesting vector and raster geospatial data from the SDI into the DP's modern lakehouse architecture.

## Integration Hypotheses

### Hypothesis 1: Two-Phase Ingestion (Oracle→PostGIS→DP)
- Phase 1: Oracle→PostGIS via evolved Geoscript (existing, working process)
- Phase 2: PostGIS→DP via Spark/Python with CRS transformation to EPSG:7791
- **Advantages**: Leverages existing PostGIS capabilities, clear separation of responsibilities
- **Disadvantages**: Two-phase latency, triple data storage, orchestration complexity

### Hypothesis 2: Direct Ingestion via Geoscript (Oracle→DP)
- Single flow: Oracle→DP via evolved Geoscript (Python/GDAL)
- **Advantages**: Single process, no cascading synchronization
- **Disadvantages**: Loses PostGIS optimizations, complexity transferred to Geoscript, tight coupling

### Alternative A: Native DP Ingestion (Oracle→DP via DP Tools)
- DP tools (Spark) read directly from Oracle, bypassing Geoscript entirely
- **Advantages**: Architectural purity, DP scalability, single control point
- **Disadvantages**: Complex CRS transformation in Spark, direct Oracle access, requires advanced geospatial Spark skills

### Alternative B: Optimized Hybrid (Oracle→PostGIS→DP via DP Tools) — RECOMMENDED
- Phase 1 (SDI): Oracle→PostGIS with CRS transformation to EPSG:7791 using native PostGIS gridded data
- Phase 2 (DP): Spark/Python reads transformed data from PostGIS, converts to GeoParquet, writes to MinIO/Iceberg
- **Advantages**: Best compromise — leverages PostGIS for complex spatial operations, simplifies DP ingestion, clear separation of responsibilities
- **Disadvantages**: Two-phase latency, triple data storage, operational dependency on SDI Phase 1

## Key Technical Details

- CRS transformation uses PostGIS `ST_Transform` with gridded data files installed on the database server
- Spark reads from PostGIS via JDBC with a query that includes `ST_Transform(geometry, 7791)` and exports as WKB
- Materialized Views in PostGIS can mitigate performance concerns by pre-computing transformed data
- Orchestration coordination via Airflow/Mage is essential for monitoring and dependency management

## Open Questions

1. Performance characteristics of PostGIS ST_Transform with gridded data under concurrent read/write load
2. Can the DP orchestration tool effectively trigger and monitor the SDI-managed Phase 1?
3. How will COG raster files be cataloged in DataHub/OpenMetadata?
4. What is the refresh frequency requirement — does two-phase latency meet business needs?
5. Is viscarto (PostGIS) still needed for SDI purposes if Alternative B is adopted?