---
type: entity
title: FastAPI
created: 2026-02-13
updated: 2026-05-07
tags:
  - python
  - web-framework
  - api
  - etl
  - rest-api
  - async
  - migration
related:
  - kubernetes-etl-deployment-strategies
  - container-image-strategy-for-data-pipelines
  - kubernetes
  - fastapi-background-tasks-pattern
  - celery-integration-pattern
  - geoscript-rest-api-architecture
  - legacy-geospatial-etl-pipeline
  - migration-strategy-two-phase
  - api-regression-test-suite
  - container-separation-principle
  - java-groovy-tomcat-stack
sources:
  - "Deploy ETL in Kubernetes_ Strategie_ .md"
  - "GEOSCRIPTS - REST API.md"
  - "Migrazione API REST Java:Groovy a Python:FastAPI.md"
---
# FastAPI

FastAPI is a modern, fast (high-performance) Python web framework for building APIs with automatic interactive documentation, based on Python 3.7+ standard type hints. In the context of this wiki, FastAPI serves both as the service layer that exposes ETL logic or data via HTTP endpoints (especially for geospatial ETL scripts deployed on Kubernetes) and as the target technology for the migration from the legacy Java/Groovy/Tomcat stack.

## Role

### In ETL Architecture

- Provides an API endpoint for triggering ETL processes or querying processed data.
- Runs as a long-lived service managed by Kubernetes Deployment and Service resources.
- Shares codebase with batch ETL scripts, creating the need for careful container image strategy.
- In geospatial ETL, FastAPI exposes existing [[GEOSCRIPTS - REST API.md|legacy geospatial scripts]] as REST endpoints.

### In Migration

FastAPI is the target framework in the two-phase migration strategy, replacing the Java/Groovy/Tomcat stack with a Python-native, ASGI-based architecture.

## Execution Patterns

The source [[GEOSCRIPTS - REST API.md]] documents two patterns for executing long-running geospatial scripts via FastAPI:

1. **BackgroundTasks**: FastAPI's built-in mechanism for executing operations after returning an HTTP response. Suitable for simple background execution but blocks the worker thread.
2. **Celery Integration**: A distributed task queue system for robust, scalable background execution. Requires a message broker (e.g., Redis) and separate worker processes.

## Implementation Details

- Endpoints receive script names mapped to secure paths via a hardcoded dictionary.
- Scripts are executed via `subprocess.Popen` using the `/srv/geoscript/run` shell script.
- Email notifications are sent on completion or failure using SMTP configuration from `.env`.
- Task status can be polled via a dedicated endpoint when using Celery.

## Key Libraries

Used in the migration context and generally for FastAPI development:

- **Pydantic**: Data validation and serialization/deserialization (used natively by FastAPI)
- **pydantic-settings**: Configuration management via environment variables
- **pytest**: Testing framework for API regression tests
- **httpx**: Async HTTP client for testing
- **DeepDiff**: JSON structural comparison for API response validation

## Deployment

### Server and Port

- **Server**: Uvicorn (ASGI server) or Gunicorn with Uvicorn workers
- **Port**: Typically 8000
- **Container**: Separate Docker container based on Ubuntu 22.04 or official Python images. The [[container-separation-principle]] mandates that FastAPI reside in a separate container from the legacy Java stack.

### Dockerfile Pattern

A multi-stage Docker build is recommended:

1. **Builder stage**: Install Python, pip, build dependencies, and all Python packages.
2. **Final stage**: Minimal Ubuntu with only Python runtime, copied libraries, and application code.

### Co-deployment with Batch ETL Scripts

When co-deployed with batch ETL scripts, FastAPI introduces additional dependencies (e.g., uvicorn) that increase image size and attack surface for Job pods. This drives the recommendation for separate images in production environments.

## Security Considerations

The source explicitly warns about path traversal vulnerabilities in script name mapping. Input validation is critical — the current implementation uses a hardcoded dictionary rather than dynamic path resolution.

## Related Pages

- [[fastapi-background-tasks-pattern]] — Detailed pattern documentation
- [[celery-integration-pattern]] — Celery setup for data pipeline task queues
- [[geoscript-rest-api-architecture]] — Overall architecture of the REST API layer
- [[legacy-geospatial-etl-pipeline]] — The legacy pipeline being modernized
- [[kubernetes-etl-deployment-strategies]] — Broader ETL deployment strategies
- [[container-image-strategy-for-data-pipelines]] — Container image strategy
- [[migration-strategy-two-phase]] — The migration strategy that uses FastAPI as the target
- [[api-regression-test-suite]] — Testing methodology for verifying FastAPI implementation correctness
- [[container-separation-principle]] — Why FastAPI must be in a separate container from Java
- [[java-groovy-tomcat-stack]] — The legacy stack being migrated