---
type: entity
title: GeoScript Migration Plan
created: 2026-04-29
updated: 2026-04-29
tags: [migration, etl, geospatial, python, groovy]
related: [gdal-docker-image, groovy-to-python-etl-migration, italian-datum-transformations, oracle-to-postgresql-gdal-etl, legacy-geospatial-etl-pipeline, kubernetes-etl-deployment-strategies]
sources: ["ETL CARTO 2.md"]
---
# GeoScript Migration Plan

The plan to migrate the legacy Groovy-based geospatial ETL system (GeoScript) to a modern Python-based, containerized architecture. The system is hosted in the [geoscript-docker](https://git.liguriadigitale.it/GEO/geoscript-docker) repository.

## Three-Phase Approach

### Phase 1: Script Conversion
- Create ETL directory structure under `geoscript/etl`
- Copy Groovy files from existing exercise
- Create `.env` configuration file
- Use `uv` + `pyproject.toml` for Python environment management
- Convert Groovy scripts to Python with:
  - `OGR2OGR_CMD` environment variable abstraction
  - `config.properties` → `.env` migration
  - `argparse` for parameter handling
  - UUID-based logging

### Phase 2: Container Testing
- Build on [[gdal-docker-image]] base
- Mount scripts at `/srv/geoscript/`
- Test with Docker Compose environment
- Execute `ogr2ogr` via Kubernetes jobs

### Phase 3: Airflow Scheduling
- Convert Python scripts to Airflow DAGs
- Schedule and monitor via Airflow

## Script Inventory

18+ scripts organized by domain:
- **bilancio-idrico:** scrivi-shape
- **cem:** elabora-richiesta
- **centri-impiego:** aggiorna
- **geoportale:** load_postgis_catalog
- **geoserver:** cache_controlla_timeout, cache_elabora_richiesta, cache_sched, cache_create, cluster_postgis_table, postgis_cache_mngr, update_cache
- **libioss:** load_postgis
- **psa:** scarico_iren (uses certificates)
- **rqa:** download, load_postgis_cor_mv, load_postgis_corsto_aa, load_postgis_corsto_gg, load_postgis
- **scuoladigitale:** aggiorna
- **sentieri:** create_kml_gpx
- **varie:** architetture_post_1945_download

## Repository

- Git: [https://git.liguriadigitale.it/GEO/geoscript-docker](https://git.liguriadigitale.it/GEO/geoscript-docker)