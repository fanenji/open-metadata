---
type: entity
title: GDAL Docker Image (gdal-full)
created: 2026-04-29
updated: 2026-04-29
tags: [gdal, docker, geospatial, etl]
related: [geoscript-migration-plan, italian-datum-transformations, oracle-to-postgresql-gdal-etl, container-image-strategy-for-data-pipelines, kubernetes-etl-deployment-strategies]
sources: ["ETL CARTO 2.md"]
---
# GDAL Docker Image (gdal-full)

A multi-stage Docker image built from the [gdal-docker](https://git.liguriadigitale.it/GEO/gdal-docker) repository. This image provides a full GDAL installation with specialized support for the Regione Liguria geospatial ETL pipeline.

## Key Features

- **Oracle OCI Support:** Enables direct Oracle database connectivity via `OCI:` connection strings
- **ECW Raster Support:** Compressed raster format support requiring special GDAL build configuration
- **GSB Grid Files:** PROJ grid files mounted at `/usr/share/proj` for precise Italian datum transformations
- **Python:** Python runtime for executing migrated ETL scripts

## Configuration

- **Grid Files:** Mount directory with GSB grids to `/usr/share/proj`
- **TNSNAMES.ORA:** Oracle Net configuration for database aliases
- **Data Directory:** Mount data directory to `/data`
- **Environment Variables:** Managed via `.env` file

## Usage

The image serves as the base for the [[geoscript-migration-plan]] containerized ETL system. Scripts are mounted at `/srv/geoscript/` and executed via a `run_script` shell wrapper.

## Repository

- Git: [https://git.liguriadigitale.it/GEO/gdal-docker](https://git.liguriadigitale.it/GEO/gdal-docker)