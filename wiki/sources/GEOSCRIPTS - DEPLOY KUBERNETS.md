---
type: source
title: "GEOSCRIPTS - Deploy Kubernetes"
created: 2026-04-29
updated: 2026-04-29
tags: [kubernetes, etl, deployment, docker, fastapi]
related: [kubernetes-etl-deployment-strategies, container-image-strategy-for-data-pipelines, kubernetes, fastapi]
sources: ["GEOSCRIPTS - DEPLOY KUBERNETS.md"]
---
# GEOSCRIPTS - Deploy Kubernetes

## Summary

This source analyzes two deployment strategies for an ETL system on Kubernetes where the codebase includes both Python batch scripts and a FastAPI application. It compares a single-image strategy (one Docker image for both workloads) against a two-image strategy (separate images for scripts and API), recommending the two-image approach as best practice for Kubernetes environments.

## Key Points

- **Single Image Strategy:** One Docker image containing both scripts and FastAPI, differentiated by container command (Job/CronJob vs. Deployment/Service). Simpler but less efficient.
- **Two-Image Strategy:** Separate images for script execution and API service, each containing only necessary dependencies. Recommended as best practice.
- **Resource Optimization:** Two images reduce image size and pod resource waste.
- **Separation of Concerns:** Components can evolve independently.
- **Code Sharing Challenge:** Common logic must be managed via shared libraries or internal packages.

## Context

The source is an internal analysis document for a geospatial ETL system (GEOSCRIPTS) being migrated to Kubernetes. It extends the existing [[kubernetes-etl-deployment-strategies]] concept with a concrete use case and detailed trade-off analysis.

## Connections

- Extends [[kubernetes-etl-deployment-strategies]] with specific ETL + FastAPI use case
- Relates to [[container-image-strategy-for-data-pipelines]] design principles
- References [[kubernetes]] and [[fastapi]] as core technologies