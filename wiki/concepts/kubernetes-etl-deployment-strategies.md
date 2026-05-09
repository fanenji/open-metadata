---
type: concept
title: Kubernetes ETL Deployment Strategies
created: 2026-02-13
updated: 2026-05-07
tags: [kubernetes, etl, deployment, container-strategy, devops, docker, fastapi]
related: [container-image-strategy-for-data-pipelines, elt-pattern, data-ingestion-architectural-patterns, kubernetes, fastapi, single-image-strategy, two-image-strategy]
sources: ["Deploy ETL in Kubernetes_ Strategie_ .md", "GEOSCRIPTS - DEPLOY KUBERNETS.md"]
---

# Kubernetes ETL Deployment Strategies

Decision framework for deploying ETL systems on Kubernetes, comparing single-image vs. multi-image approaches for workloads that include both batch scripts and API services. This extends the general [[container-image-strategy-for-data-pipelines]] principles to a concrete use case.

## The Problem

An ETL system running on Kubernetes may need to execute Python scripts (via Job/CronJob) and expose a FastAPI service (via Deployment/Service) from the same codebase. The question is whether to use one Docker image for both workloads or separate images.

## The Two Strategies

### Single Image Strategy

One Docker image containing both ETL scripts and the FastAPI application, differentiated only by the container command.

**When to use:**
- Small/simple projects
- Prototyping and initial development phases

**Trade-offs / Advantages & Disadvantages:**
- **Advantages:** Simpler image management (build, version, scan one image); consistent environment across workloads.
- **Disadvantages:** Larger image size for Job pods (includes unnecessary web server code); less precise resource allocation; slightly larger attack surface.

### Two-Image Strategy (Recommended)

Two Docker images: one optimized for script execution (lighter, no web dependencies) and one for the FastAPI service.

**When to use:**
- Production systems
- Growing complexity and team size
- When batch and API workloads have different resource profiles

**Trade-offs / Advantages & Disadvantages:**
- **Advantages:** Better resource efficiency and granular tuning; improved security (reduced attack surface for Job pods); independent scalability for batch and API workloads; better alignment with Kubernetes Single Responsibility Principle; components can evolve independently.
- **Disadvantages:** More complex image management (two builds, two version streams); requires shared code management strategy.

## Shared Code Management

When splitting into two images, shared logic (internal libraries, data models, utility functions) must be managed carefully. Common strategies include:

1. **Internal Python package** — Create an installable package from a private repository, installed via `pip` in both images.
2. **Shared directory structure** — Organize the repository so Dockerfiles can copy common code during build.
3. **Multi-stage builds** — Use Docker multi-stage builds to extract shared artifacts.

## Resource Allocation Considerations

- **Batch Jobs:** Typically bursty, requiring high CPU/memory for short periods. Separate images allow aggressive resource requests/limits without over-provisioning the API.
- **API Services:** Typically steady, requiring moderate resources per pod with horizontal scaling. Separate images allow fine-tuning of requests/limits and HPA thresholds.

## Decision Framework

| Factor | Single Image | Two Images |
|--------|-------------|------------|
| Project size | Small | Medium/Large |
| Complexity | Low | High |
| Team maturity | Early stage | Established |
| Scaling needs | Uniform | Differentiated |
| Security requirements | Low | High |

## Related Concepts

This deployment strategy is part of the infrastructure layer for [[data-ingestion-architectural-patterns]] and [[elt-pattern]]. The choice of image strategy affects pipeline reliability, cost, and operational complexity.

- [[container-image-strategy-for-data-pipelines]] — General design principles
- [[kubernetes]] — Container orchestration platform
- [[fastapi]] — Python web framework for APIs