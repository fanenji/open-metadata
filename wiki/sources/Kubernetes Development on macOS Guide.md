---
type: source
title: "Kubernetes Development on macOS Guide"
created: 2026-03-15
updated: 2026-03-15
tags: [kubernetes, macos, geospatial, development, orbstack, docker, helm]
related: [orbstack, local-kubernetes-tooling-comparison, helm-for-data-platforms, kubernetes-secrets-management, kubernetes-probes, kubernetes-jobs-cronjobs, geospatial-docker-base-images, kubernetes-local-data-access, container-image-strategy-for-data-pipelines, kubernetes-etl-deployment-strategies, kubernetes, fastapi, duckdb]
sources: ["Kubernetes Development on macOS Guide.md"]
---
# Kubernetes Development on macOS Guide

A comprehensive guide to setting up and using local Kubernetes development environments on macOS, specifically for Python-based geospatial ETL workloads using libraries like GDAL, GeoPandas, DuckDB, FastAPI, and orchestrators like Airflow and Prefect.

## Key Topics

- **Local Kubernetes Tooling**: Evaluation of OrbStack, Docker Desktop, Minikube, Kind, k3d, and Rancher Desktop for macOS development.
- **OrbStack**: Primary recommendation due to performance (VirtioFS, Rosetta), low resource consumption, and integrated networking.
- **Kubernetes Best Practices**: Multi-stage builds, ConfigMaps/Secrets, health probes, resource management, and development loop tools (Skaffold, Tilt, DevSpace, Telepresence).
- **Deployment Patterns**: Containerizing Python ETL scripts with GDAL/GeoPandas, deploying Airflow/Prefect with Helm, and deploying FastAPI services.
- **Geospatial Workload Challenges**: Managing large dependencies, accessing local data within containers, and resource optimization.
- **Secure Credential Management**: Using Kubernetes Secrets mounted as volumes for database credentials and API keys.

## Main Recommendations

1. **OrbStack** is the optimal local K8s solution for macOS geospatial workloads due to performance and ease of use.
2. **Rancher Desktop** is the strongest free/open-source alternative.
3. **k3d** is best for CLI-focused, fast, ephemeral clusters.
4. **Multi-stage builds** are essential for geospatial containers to reduce image size.
5. **Helm** is the recommended deployment method for stateful orchestrators like Airflow and Prefect.
6. **Kubernetes Secrets** (mounted as volumes) are the recommended credential management pattern.

## Connections to Existing Wiki

- Extends [[kubernetes]] with local development specifics.
- Provides concrete Deployment + Service YAML examples for [[fastapi]].
- Aligns with and extends [[container-image-strategy-for-data-pipelines]] with multi-stage build guidance.
- Aligns with [[kubernetes-etl-deployment-strategies]] with Jobs/CronJobs patterns.
- Mentions [[duckdb]] in the target stack.