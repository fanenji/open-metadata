---
type: concept
title: Kubernetes Geospatial ETL Deployment
created: 2026-02-13
updated: 2026-02-13
tags: [kubernetes, geospatial, etl, gdal, geopandas, python, jobs, cronjobs]
related: [kubernetes-development-best-practices, kubernetes-secrets-management, container-image-strategy-for-data-pipelines, gdal, duckdb, geospatial-etl-pipeline-iceberg, legacy-geospatial-etl-pipeline]
sources: ["Kubernetes Dev Environment on MacBook_ .md"]
---
# Kubernetes Geospatial ETL Deployment

Specific patterns for deploying Python-based geospatial ETL scripts (using GDAL, GeoPandas, DuckDB) as Kubernetes Jobs or CronJobs. This covers containerization strategies for large geospatial dependencies, resource sizing, and secure connections to external databases.

## Containerizing Geospatial ETL Scripts

- **Base Image:** Start with a base image containing GDAL and its dependencies, as installing GDAL manually can be complex. The `osgeo/gdal:ubuntu-small-latest` or `osgeo/gdal:ubuntu-full-latest` images are good starting points.
- **Dependencies:** Install Python, pip, and essential build tools (`libspatialindex-dev` is often needed for GeoPandas performance). Use a `requirements.txt` file to list Python dependencies (e.g., `geopandas`, `duckdb`, `psycopg2-binary` or `oracledb`, `fiona`, `rasterio`, `shapely`).
- **Multi-Stage Builds:** Use a "builder" stage to install dependencies, then copy only the installed packages and application code to a minimal final stage (e.g., based on `python:3.x-slim`). Ensure necessary system libraries used by GDAL/Python libs are present in the final stage. Use a non-root user for the final stage.

## Executing Scripts with Kubernetes Jobs and CronJobs

- **Jobs:** Use `kind: Job` for running ETL tasks once or on demand. The Job creates one or more Pods and ensures they complete successfully. Set `spec.template.spec.restartPolicy` to `Never` or `OnFailure`.
- **CronJobs:** Use `kind: CronJob` for scheduled tasks (e.g., nightly data processing). Configure `spec.schedule` with standard cron syntax, `spec.concurrencyPolicy` (often `Forbid` for ETL to prevent overlapping runs), and `spec.successfulJobsHistoryLimit` / `spec.failedJobsHistoryLimit` to avoid cluttering the cluster.

## Resource Considerations for Geospatial Processing

Geospatial processing (especially with GDAL and large geometries) can be memory-intensive. Recommended resource settings:

- **Requests:** Memory: "1Gi", CPU: "500m"
- **Limits:** Memory: "4Gi", CPU: "1500m"

These values should be adjusted based on actual workload profiling. The "Goldilocks" principle of monitoring actual usage to right-size requests and limits applies strongly here.

## Secure External Connections

Use Kubernetes Secrets to manage credentials for remote databases (Oracle, PostGIS) and external APIs. Mount secrets as volumes (e.g., `/etc/secrets/oracle`, `/etc/secrets/postgis`) or inject as environment variables. Never hardcode credentials in application code, Dockerfiles, or ConfigMaps.