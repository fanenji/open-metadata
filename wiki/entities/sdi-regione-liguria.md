---
type: entity
title: SDI Regione Liguria
created: 2026-04-29
updated: 2026-05-07
tags:
  - sdi
  - geospatial
  - data-platform
  - integration
  - regione-liguria
  - infrastructure
related:
  - geoscript-etl-system
  - postgis-viscarto
  - sdi-dp-integration-strategies
  - legacy-geospatial-etl-pipeline
  - oracle-to-postgresql-gdal-etl
  - geoscript-system
  - oracle-database-sdi
  - sdi-dp-integration-strategy
sources:
  - "Integrazione SDI DP Analisi.md"
  - "Integrazione SDI_DP_ Analisi e Proposte_ .md"
---
# SDI Regione Liguria

The Spatial Data Infrastructure (SDI) of Regione Liguria is the existing geospatial data management system that must be integrated with the new Data Platform (DP). It contains ETL functions and analytical database environments that overlap with the DP's capabilities, creating integration complexity.

## Components

- **Geoscript ETL System**: Groovy/GDAL/OGR scripts running on Windows Server 2019 for data movement and transformation.
- **PostGIS/viscarto Database**: Analytical PostgreSQL/PostGIS environment for query acceleration and advanced spatial functions.
- **Oracle Database**: Source management database for geospatial data.
- **Catalogo SIT**: Configuration source for layer definitions in ETL processes.
- **SITAR**: System that triggers manual (on‑command) data updates.

## Integration Context

The SDI's functions overlap with the DP in several areas:
- **ETL Capabilities**: The Geoscript system (Groovy/GDAL/OGR) mirrors the DP's ingestion and transformation layer for data movement and transformation.
- **Analytical Database**: The PostGIS/viscarto environment serves similar purposes to the DP's analysis layer, providing query acceleration and advanced spatial functions.

Additionally, the SDI's PostGIS environment performs coordinate transformations using native grid files, a capability the DP would need to replicate or leverage. The integration aims to leverage existing SDI investments while extending analytical capabilities through the DP.

## Related Pages

- [[geoscript-etl-system]] — The legacy ETL system within SDI
- [[geoscript-system]] — The Geoscript system (alternative page)
- [[postgis-viscarto]] — The PostGIS analytical database
- [[sdi-dp-integration-strategies]] — Integration hypotheses and trade-offs
- [[sdi-dp-integration-strategy]] — Integration strategy options
- [[legacy-geospatial-etl-pipeline]] — Related legacy pipeline
- [[oracle-to-postgresql-gdal-etl]] — Related ETL workflow pattern
- [[oracle-database-sdi]] — Oracle database within SDI