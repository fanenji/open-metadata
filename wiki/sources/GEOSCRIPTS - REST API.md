---
type: source
title: GEOSCRIPTS - REST API
created: 2026-05-07
updated: 2026-05-07
tags: [fastapi, celery, rest-api, geospatial, etl, background-tasks]
related: [fastapi, celery, legacy-geospatial-etl-pipeline, oracle-to-postgresql-gdal-etl, kubernetes-etl-deployment-strategies, data-download-service, fastapi-background-tasks-pattern, celery-integration-pattern, geoscript-rest-api-architecture]
sources: ["GEOSCRIPTS - REST API.md"]
---
# GEOSCRIPTS - REST API

This source documents the architecture and implementation of exposing existing Python geospatial ETL scripts (`ora_to_pg.py`, `load_postgis.py`) as REST services using FastAPI. It covers two execution modes: lightweight BackgroundTasks for simple background execution and Celery for robust, scalable distributed task processing. The source includes complete code examples for FastAPI endpoints, Celery worker configuration, subprocess execution via the `/srv/geoscript/run` script, and email notification on task completion or failure.

## Key Topics

- FastAPI BackgroundTasks pattern for non-blocking script execution
- Celery distributed task queue integration with Redis broker
- Subprocess execution of legacy Python scripts
- Task status polling via REST endpoint
- Email notification on completion/error using SMTP configuration
- Docker deployment considerations
- Security concerns around script name mapping and path traversal

## Connections

- Directly related to the [[legacy-geospatial-etl-pipeline]] as a modernization path
- Extends [[fastapi]] with concrete implementation examples
- Connects to [[kubernetes-etl-deployment-strategies]] for container deployment
- Related to [[data-download-service]] pattern of exposing data processing via REST APIs
- The scripts being exposed are part of the [[oracle-to-postgresql-gdal-etl]] workflow