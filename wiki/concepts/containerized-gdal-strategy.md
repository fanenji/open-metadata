---
type: concept
title: Containerized GDAL Strategy
created: 2026-04-29
updated: 2026-04-29
tags: [gdal, docker, containerization, geospatial, etl]
related: [gdal-docker-image, geoscript-migration-plan, container-image-strategy-for-data-pipelines, kubernetes-etl-deployment-strategies]
sources: ["ETL CARTO 2.md"]
---
# Containerized GDAL Strategy

The architectural approach of packaging GDAL with all required dependencies (Oracle OCI, ECW, GSB grids, Python) into a Docker image for portable, reproducible geospatial ETL execution.

## Design Principles

1. **Multi-Stage Build:** Separate build and runtime stages to minimize image size
2. **All Dependencies Included:** Oracle OCI client, ECW SDK, PROJ grid files, Python
3. **Configuration via Mounts:** Grid files, TNSNAMES.ORA, and data directories mounted at runtime
4. **Environment-Driven:** All configuration via `.env` files and environment variables

## Deployment Options

- **Development:** Docker Compose with mounted source code and data
- **Production:** Kubernetes jobs for `ogr2ogr` execution, Airflow for scheduling

## Advantages

- Eliminates "works on my machine" problems for GDAL builds
- Enables consistent Oracle OCI configuration across environments
- Simplifies deployment of GSB grid files for datum transformations
- Supports both interactive testing and scheduled batch processing