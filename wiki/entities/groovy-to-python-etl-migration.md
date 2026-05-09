---
type: entity
title: Groovy-to-Python ETL Migration
created: 2026-04-29
updated: 2026-04-29
tags: [migration, groovy, python, etl, geospatial]
related: [geoscript-migration-plan, gdal-docker-image, oracle-to-postgresql-gdal-etl, legacy-geospatial-etl-pipeline]
sources: ["ETL CARTO 2.md"]
---
# Groovy-to-Python ETL Migration

The pattern and methodology for converting legacy Groovy ETL scripts to Python, as part of the [[geoscript-migration-plan]].

## Conversion Patterns

### Environment Variable Abstraction
- **Windows:** `OGR2OGR_CMD=OGR2OGR.bat`
- **Linux/Docker:** `OGR2OGR_CMD=ogr2ogr`
- **Code:** `os.environ.get("OGR2OGR_CMD", "ogr2ogr")`

### Configuration Migration
- Legacy: `config.properties` (Java properties format)
- Target: `.env` file (key-value pairs)

### Parameter Handling
- Legacy: Groovy script arguments
- Target: Python `argparse` module

### Logging
- Legacy: Groovy logging
- Target: Python logging with UUID correlation IDs

## Development Environment

- **Python Version:** 3.12
- **Package Manager:** `uv` with `pyproject.toml`
- **Virtual Environment:** `uv venv` in project directory
- **Environment Variable:** `GEOETL_HOME` set to project root

## Cross-Platform Considerations

The `OGR2OGR_CMD` abstraction is critical for portability between Windows development environments and Linux production containers. The `.env` file or Docker environment variables configure the command name at runtime.