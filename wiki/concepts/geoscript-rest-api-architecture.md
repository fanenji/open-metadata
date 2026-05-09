---
type: concept
title: Geoscript REST API Architecture
created: 2026-05-07
updated: 2026-05-07
tags: [rest-api, fastapi, celery, geospatial, etl, architecture]
related: [fastapi, celery-integration-pattern, fastapi-background-tasks-pattern, legacy-geospatial-etl-pipeline, oracle-to-postgresql-gdal-etl, kubernetes-etl-deployment-strategies, subprocess-execution-pattern, task-status-polling-pattern, email-notification-pattern]
sources: ["GEOSCRIPTS - REST API.md"]
---
# Geoscript REST API Architecture

This concept describes the overall architecture of exposing existing Python geospatial ETL scripts as REST services. The architecture provides a modernization path for the [[legacy-geospatial-etl-pipeline]] by wrapping scripts (`ora_to_pg.py`, `load_postgis.py`) behind HTTP endpoints.

## Architecture Overview

The system consists of the following layers:

1. **REST API Layer (FastAPI)**: Exposes HTTP endpoints for triggering script execution and checking task status
2. **Execution Layer**: Two modes — BackgroundTasks (simple) or Celery (robust)
3. **Script Execution Layer**: Uses `/srv/geoscript/run` shell script to execute Python scripts in the correct Docker virtual environment
4. **Notification Layer**: Sends email notifications on script completion or failure
5. **Deployment Layer**: Docker container with FastAPI, Celery worker, and Redis

## Execution Modes

### Mode 1: BackgroundTasks (Simple)
- FastAPI's built-in mechanism
- No additional infrastructure required
- Suitable for development or short-lived tasks
- Blocks the worker thread during execution

### Mode 2: Celery (Production)
- Distributed task queue with Redis broker
- Scalable across multiple workers
- Automatic retry and monitoring
- Requires separate worker processes and Redis

## Security Considerations

- **Path traversal**: Script names must be validated against a hardcoded dictionary
- **Input validation**: All parameters should be sanitized before passing to subprocess
- **Environment isolation**: Scripts run inside the Docker container's virtual environment

## Email Notification Pattern

After script execution (success or failure), an email is sent:
- If an `email` parameter is provided, it is used as the recipient
- Otherwise, `ERROR_TO_ADDRESS` and `OK_TO_ADDRESS` from the `.env` file are used
- SMTP configuration (`SMTP_MAIL_SERVER`, `FROM_ADDRESS`) is read from `.env`

## Deployment

The FastAPI application and Celery worker are deployed as Docker containers. The architecture supports:
- Single-container deployment with BackgroundTasks
- Multi-container deployment with Celery, Redis, and workers
- Kubernetes orchestration for scaling workers

## Related Pages

- [[fastapi-background-tasks-pattern]] — BackgroundTasks implementation details
- [[celery-integration-pattern]] — Celery implementation details
- [[legacy-geospatial-etl-pipeline]] — The legacy pipeline being modernized
- [[kubernetes-etl-deployment-strategies]] — Container deployment strategies
- [[subprocess-execution-pattern]] — Subprocess execution mechanism
- [[task-status-polling-pattern]] — Task status polling endpoint
- [[email-notification-pattern]] — Email notification on completion