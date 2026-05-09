---
type: entity
title: Geoscript Modernization
created: 2026-02-13
updated: 2026-02-13
tags: [sdi, etl, geospatial, modernization]
related: [legacy-geospatial-etl-pipeline, oracle-to-postgresql-gdal-etl, sdi-data-platform-integration]
sources: ["SDI Data Integration to Data Platform.md"]
---
# Geoscript Modernization

The planned evolution of the Geoscript ETL system from its current state (Windows Server 2019, Groovy language, GDAL/OGR) to a modernized environment (Ubuntu, Python, updated GDAL/OGR). This modernization is a prerequisite for any SDI-to-DP integration strategy.

## Current State (As-Is)

- **Platform**: Windows Server 2019 (srvcarto.regione.liguria.it)
- **Language**: Groovy scripts
- **Library**: GDAL/OGR (obsolete version)
- **Scheduling**: Windows Task Scheduler
- **Key Criticisms**: Complex GDAL configuration on Windows, difficult pipeline monitoring, outdated environment

## Target State (To-Be)

- **Platform**: Ubuntu (VM or containerized)
- **Language**: Python
- **Library**: GDAL/OGR with Oracle (OCI) and ECW support
- **Scheduling**: Cron or external orchestration (e.g., Airflow via SSHOperator)

## Key Capabilities

- Read vector data from Oracle database
- Execute `ogr2ogr` for format and CRS transformations
- Read/write raster data using `gdalwarp` and `gdal_translate`
- Support for Cloud Optimized GeoTIFF (COG) conversion
- Integration with DP orchestration for monitoring and dependency management