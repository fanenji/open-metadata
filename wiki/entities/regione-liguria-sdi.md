---
type: entity
title: Regione Liguria SDI (Spatial Data Infrastructure)
created: 2026-04-29
updated: 2026-04-29
tags: [geospatial, sdi, regione-liguria, infrastructure]
related: [geoscript-etl-system, postgis-staging-environment, catalogo-sit-metadata, legacy-geospatial-etl-pipeline, oracle-to-postgresql-gdal-etl, ingestion-dati-geo-strategy]
sources: ["Ingestion Dati Geo.md"]
---
# Regione Liguria SDI

The Spatial Data Infrastructure (SDI) of Regione Liguria is the existing geospatial system that manages, processes, and serves cartographic data. It has functional overlap with the new Data Platform (DP), particularly in ETL processing and analytical database environments.

## Key Components

- **Postgres/PostGIS (viscarto database)**: Analytical database environment used for query acceleration, CRS conversion, and advanced spatial functions.
- **Geoscript ETL System**: Groovy-based ETL scripts using GDAL/OGR, running on Windows Server 2019, scheduled via Task Scheduler.
- **Oracle Database**: Source database for geospatial data management.
- **Catalogo SIT**: Metadata catalog that guides ETL configuration, listing layers and their transformation parameters.

## Relationship to Data Platform

The SDI and DP have overlapping functions (ETL, analytical databases), requiring clear boundary definition and integration strategy. The SDI's PostGIS environment can serve as a staging area for DP ingestion, leveraging existing procedures and spatial capabilities.

## Related Pages

- [[geoscript-etl-system]] — The current ETL system and migration plan
- [[postgis-staging-environment]] — The proposed PostGIS staging environment
- [[catalogo-sit-metadata]] — The metadata system guiding ETL configuration
- [[legacy-geospatial-etl-pipeline]] — The legacy ETL pipeline
- [[oracle-to-postgresql-gdal-etl]] — The Oracle to PostgreSQL ETL workflow
- [[ingestion-dati-geo-strategy]] — The ingestion strategy decision