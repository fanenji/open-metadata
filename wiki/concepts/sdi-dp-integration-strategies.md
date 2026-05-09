---
type: concept
title: SDI-DP Integration Strategies
created: 2026-04-29
updated: 2026-04-29
tags: [integration, sdi, data-platform, geospatial, etl]
related: [sdi-regione-liguria, geoscript-etl-system, postgis-viscarto, raster-ingestion-cog-pipeline, geospatial-streaming-kafka-geomesa, legacy-geospatial-etl-pipeline, geospatial-etl-pipeline-iceberg, cloud-native-geospatial-workflow]
sources: ["Integrazione SDI DP Analisi.md"]
---
# SDI-DP Integration Strategies

This concept page documents the strategies for integrating the Spatial Data Infrastructure (SDI) of Regione Liguria with the new Data Platform (DP). The integration involves ingesting vector and raster geospatial data from legacy systems into the modern Lakehouse architecture.

## Vector Data Integration

### Hypothesis 1: Two-Phase Ingestion (Oracle → PostGIS → DP)

**Flow**: Oracle → PostGIS/viscarto (via Geoscript/ogr2ogr) → DP Object Storage (via Spark/Dremio)

**Advantages**:
- Reuses existing, proven copy procedures
- PostGIS/viscarto already contains most Oracle data
- Easy to extend for new data layers
- PostGIS provides geometry validation and native grid-based coordinate transformations
- PostGIS acts as a buffer, isolating DP from Oracle load spikes

**Disadvantages**:
- Dual orchestration (SDI and DP) requires coordination
- Update latency from two sequential loading phases
- Dependency on PostGIS availability
- Ongoing operational costs for PostgreSQL/PostGIS management

**Phase 1 (Oracle → PostGIS)**:
- Reads layer configuration from Catalogo SIT
- Executes ogr2ogr with appropriate configuration
- Scheduling: daily, monthly, or on-demand via SITAR
- Orchestration: cron on Geoscript or Airflow in DP

**Phase 2 (PostGIS → DP)**:
- Reads from PostGIS, writes to S3 object storage
- Target formats: GeoParquet (file) and Iceberg/GeoIceberg (tabular)
- Coordinate transformation to EPSG:7791 (RDN2008 / UTM zone 32N)
- Orchestration: Airflow in DP

### Hypothesis 2: Single-Phase Ingestion (Oracle → DP via Geoscript)

**Flow**: Oracle → DP Object Storage (parallel to existing PostGIS feed, within Geoscript)

**Advantages**:
- Single process eliminates cascading synchronization
- Reduced latency compared to two-phase approach
- Simpler orchestration (one job)
- Pipeline can be parameterized for multiple targets

**Disadvantages**:
- Requires full migration of Geoscript from Groovy to Python
- Dependency on legacy Geoscript system during transition
- Limited scalability (single VM)
- Poor monitoring and no automatic retries in current setup
- Less elastic than containerized/Kubernetes deployment

## Raster Data Integration

Raster ingestion occurs within the Geoscript system using Python scripts:
- **Coordinate transformation**: gdalwarp
- **Format conversion**: gdal_translate
- **Target format**: Cloud-Optimized GeoTIFF (COG) on S3

**Advantages**: Compact standard format, explicit control over reprojection/tiling/compression, reuses Geoscript codebase.

**Disadvantages**: Single-node batch processing can saturate resources, fragmented monitoring, hybrid orchestration complexity.

## Alternative Proposals

### Direct Oracle → Iceberg/GeoIceberg
Use Spark or Dremio to read directly from Oracle via JDBC+OCI and write GeoIceberg datasets to S3. Eliminates intermediate PostGIS and Geoscript, leverages ACID transactions and time-travel. Requires geospatial connector development (GeoSpark/Sedona).

### Streaming Geospatial with Kafka + GeoMesa
Oracle changes published to Kafka topics, consumed by GeoMesa to populate a distributed catalog and produce GeoParquet in S3. Enables near-real-time updates and horizontal scalability. High setup complexity and learning curve.

### Serverless GDAL Processing
Cloud functions triggered by S3 events or schedulers execute containerized GDAL for conversions. Auto-scaling and immutable containers, but limited by function timeout/memory constraints.

## Decision Factors

The optimal strategy depends on requirements for:
- **Latency**: How fresh must the data be in the DP?
- **Resilience**: What is the acceptable downtime?
- **Monitoring**: What level of observability is needed?
- **Scalability**: What data volumes and update frequencies are expected?
- **Skills**: What team capabilities are available for new technologies?

## Related Pages

- [[sdi-regione-liguria]] — The existing SDI system
- [[geoscript-etl-system]] — The legacy ETL system
- [[postgis-viscarto]] — The PostGIS analytical database
- [[raster-ingestion-cog-pipeline]] — Raster ingestion pattern
- [[geospatial-streaming-kafka-geomesa]] — Streaming alternative
- [[legacy-geospatial-etl-pipeline]] — Related legacy pipeline
- [[geospatial-etl-pipeline-iceberg]] — Related Iceberg ingestion
- [[cloud-native-geospatial-workflow]] — Related cloud-native workflow