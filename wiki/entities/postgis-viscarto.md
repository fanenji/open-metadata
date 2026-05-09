---
type: entity
title: PostGIS viscarto
created: 2026-04-29
updated: 2026-05-07
tags: [postgis, geospatial, database, sdi]
related: ["sdi-regione-liguria", "geoscript-etl-system", "sdi-dp-integration-strategies", "legacy-geospatial-etl-pipeline", "oracle-to-postgresql-gdal-etl", "geoscript-system", "oracle-database-sdi", "postgis-to-dp-ingestion", "sdi-dp-integration-strategy"]
sources: ["Integrazione SDI DP Analisi.md", "Integrazione SDI_DP_ Analisi e Proposte_ .md"]
---
# PostGIS viscarto

The Postgres/PostGIS database (named "Viscarto") is the analytical environment within the SDI of Regione Liguria. It serves as an intermediate staging and transformation layer between the source Oracle database and the Data Platform, accelerating queries for visualization and analysis systems and extending functionality with native gridded conversion and advanced geospatial functions not available on Oracle.

## Functions

- **Query Acceleration**: Speeds up queries for visualization and analysis systems.
- **Advanced Spatial Functions**: Provides capabilities not available in Oracle, including native grid-based coordinate transformations and CRS transformation.
- **Geometry Validation**: Offers ST_IsValid, ST_MakeValid, and other geometry check functions.
- **Data Staging**: Acts as a buffer between Oracle and downstream systems.
- **Extensibility**: Can be easily extended to include new layers required by the Data Platform.

## Role in Integration

In Hypothesis 1 (two-phase ingestion), PostGIS Viscarto serves as the intermediate hop:

1. **Phase 1 — Oracle to PostGIS**: Data is copied from Oracle to PostGIS using existing Geoscript procedures (via ogr2ogr).
2. **Phase 2 — PostGIS to Data Platform**: Data is read from PostGIS and written to the Data Platform's object storage (MinIO) in GeoParquet/Iceberg format, transformed to EPSG:7791.

The database is considered ideal for feeding the Data Platform due to its performance, spatial functionality, existing data coverage (it already contains a large portion of the data needed), and the fact that it leverages proven, existing data copy procedures.

## Related Pages

- [[sdi-regione-liguria]] — The parent SDI system
- [[geoscript-etl-system]] — The ETL system that feeds this database
- [[sdi-dp-integration-strategies]] — How PostGIS fits into integration plans
- [[legacy-geospatial-etl-pipeline]] — Related legacy pipeline
- [[oracle-to-postgresql-gdal-etl]] — The ETL workflow feeding this database