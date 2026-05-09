---
type: entity
title: Kubernetes
created: 2026-02-13
updated: 2026-05-07
tags: ["kubernetes", "container-orchestration", "infrastructure", "orchestration", "containerization"]
related: ["kubernetes-etl-deployment-strategies", "container-image-strategy-for-data-pipelines", "elt-pattern", "data-ingestion-architectural-patterns", "infrastructure-architecture", "containerized-development-environment"]
sources: ["Deploy ETL in Kubernetes_ Strategie_ .md", "AMBIENTI.md"]
---
# Kubernetes

**Kubernetes** (K8s) is a container orchestration platform for automating deployment, scaling, and management of containerized applications. It serves as the underlying infrastructure layer for running ETL/ELT pipelines, data APIs, and supporting services within the Data Platform.

## Key Kubernetes Resources for Data Pipelines

- **Job/CronJob** — For batch execution of ETL scripts (one-time or scheduled).
- **Deployment/Service** — For long-running services like FastAPI endpoints that expose data or trigger pipelines.
- **Pod** — The smallest deployable unit, running one or more containers.

## Namespace-Based Segmentation

The platform utilizes a single Kubernetes cluster partitioned into three distinct **namespaces** to ensure workload isolation:
- **sviluppo** (Development)
- **produzione** (Production)
- **test** (Software updates and testing)

This namespace-based segmentation allows for efficient resource management within a single cluster while preventing development or testing workloads from impacting production services.

## Deployment Strategies for ETL Workloads

The choice between single-image and multi-image strategies for ETL workloads depends on project complexity, team maturity, and operational requirements. See [[kubernetes-etl-deployment-strategies]] for the full decision framework.