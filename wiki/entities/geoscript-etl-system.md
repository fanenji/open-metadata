---
type: entity
title: Geoscript ETL System
created: 2026-04-29
updated: 2026-05-07
tags: [geospatial, etl, migration, gdal, legacy, groovy]
related: [regione-liguria-sdi, postgis-staging-environment, legacy-geospatial-etl-pipeline, oracle-to-postgresql-gdal-etl, ingestion-dati-geo-strategy, sdi-regione-liguria, postgis-viscarto, sdi-dp-integration-strategies]
sources: ["Ingestion Dati Geo.md", "Integrazione SDI DP Analisi.md"]
---

# Geoscript ETL System

The Geoscript system is the legacy ETL engine within the Regione Liguria SDI, responsible for processing and moving geospatial data between environments. It uses Groovy scripts with the GDAL/OGR library to perform format conversions and coordinate reference system transformations. The system is currently running on Windows Server 2019 (host: srvcarto.regione.liguria.it) and is scheduled via Windows Task Scheduler.

## Current Architecture

- **Operating System**: Windows Server 2019 (srvcarto.regione.liguria.it)
- **Language**: Groovy (targeting migration to Python)
- **Library**: GDAL/OGR for format and CRS transformations
- **Scheduling**: Windows Task Scheduler (targeting migration to cron or Airflow)

## Known Issues

- Windows environment (prefer Ubuntu)
- Groovy language (prefer Python)
- Obsolete GDAL/OGR version
- Complex GDAL/OGR configuration on Windows
- Difficult pipeline monitoring capabilities

## Migration Plan

The system is planned to be migrated to an Ubuntu/Python environment with:
- Ubuntu operating system, deployed either as a VM or containerized
- GDAL/OGR with Oracle (OCI) and ECW support
- Python scripting instead of Groovy
- Scheduling via cron or external orchestration (e.g., Airflow with SSH operator)

A Docker image is available that satisfies all requirements.

## Related Pages

- [[regione-liguria-sdi]] — The Spatial Data Infrastructure
- [[postgis-staging-environment]] — The proposed PostGIS staging environment
- [[legacy-geospatial-etl-pipeline]] — The legacy ETL pipeline
- [[oracle-to-postgresql-gdal-etl]] — The Oracle to PostgreSQL ETL workflow
- [[ingestion-dati-geo-strategy]] — The ingestion strategy decision
- [[sdi-regione-liguria]] — The parent SDI system
- [[postgis-viscarto]] — The PostGIS database fed by Geoscript
- [[sdi-dp-integration-strategies]] — How Geoscript fits into integration plans