---
type: concept
title: Two-Image Strategy
created: 2026-04-29
updated: 2026-04-29
tags: [kubernetes, deployment, docker, etl]
related: [kubernetes-etl-deployment-strategies, single-image-strategy, container-image-strategy-for-data-pipelines]
sources: ["GEOSCRIPTS - DEPLOY KUBERNETS.md"]
---
# Two-Image Strategy

A deployment strategy for Kubernetes where separate Docker images are built for different workload types (e.g., batch scripts and a web API), each containing only the dependencies needed for its specific purpose.

## How It Works

- **Image A (Script Runner):** Contains Python environment and only the ETL scripts and common libraries. No web server code.
- **Image B (API Service):** Contains Python environment, FastAPI application, and its specific dependencies (e.g., uvicorn).

## Trade-offs

**Pros:** Resource optimization, improved security (script pods lack web server code), independent scaling, maintainability.

**Cons:** More complex image management (two Dockerfiles, two builds), requires a code sharing strategy for common logic.

## Code Sharing

Common logic must be managed without duplication:
- Internal Python package (installable via pip)
- Shared directory copied into both builds
- Multi-stage builds with a common base

## When to Use

- Production systems
- Medium to large projects
- Teams needing independent scaling and resource tuning
- When security requirements are significant

## Related

- [[single-image-strategy]] — The simpler alternative
- [[kubernetes-etl-deployment-strategies]] — Decision framework
- [[container-image-strategy-for-data-pipelines]] — General principles