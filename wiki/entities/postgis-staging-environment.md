---
type: entity
title: PostGIS Staging Environment (viscarto)
created: 2026-04-29
updated: 2026-04-29
tags: [geospatial, postgis, staging, etl]
related: [regione-liguria-sdi, geoscript-etl-system, ingestion-dati-geo-strategy, legacy-geospatial-etl-pipeline, geospatial-etl-pipeline-iceberg]
sources: ["Ingestion Dati Geo.md"]
---
# PostGIS Staging Environment (viscarto)

The Postgres/PostGIS database (named "viscarto") within the Regione Liguria SDI is proposed as a staging environment for ingesting geospatial data into the Data Platform (DP). It is currently used by the SDI as an analytical environment for query acceleration, CRS conversion, and advanced spatial functions.

## Advantages as Staging Environment

- **Performance**: Fast query execution and data processing
- **Robust Spatial Functions**: Powerful geometry validation and correction capabilities
- **Native CRS Transformations**: Built-in coordinate reference system conversion
- **Geometry Validation**: Ensures data loaded into PostGIS is geometrically and topologically correct
- **Grid-Shift File Support**: Native use of grid-shift files installed on the database server for high-precision transformations

## Role in Two-Phase Ingestion

In the recommended two-phase ingestion approach (Hypothesis 1), PostGIS serves as the intermediate staging environment:
1. **Phase 1**: Oracle → PostGIS (via Geoscript/GDAL)
2. **Phase 2**: PostGIS → Data Platform (GeoParquet/Iceberg on S3)

## Related Pages

- [[regione-liguria-sdi]] — The Spatial Data Infrastructure
- [[geoscript-etl-system]] — The current ETL system
- [[ingestion-dati-geo-strategy]] — The ingestion strategy decision
- [[legacy-geospatial-etl-pipeline]] — The legacy ETL pipeline
- [[geospatial-etl-pipeline-iceberg]] — Geospatial ETL patterns for Iceberg