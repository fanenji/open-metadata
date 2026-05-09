---
type: entity
title: GitLab CI/CD Data Platform
created: 2026-05-07
updated: 2026-05-07
tags: [ci-cd, source-control, infrastructure, devops]
related: [kestra, dbt, minio, dremio, openmetadata, apache-superset]
sources: ["Sintesi Architettura (Claude).md"]
---
# GitLab CI/CD Data Platform

GitLab serves as the central source control, CI/CD, and Docker Registry platform for the Regione Liguria Data Platform. A single GitLab instance governs all environments (dev, test, prod).

## Scope

- **Infrastructure Code**: Helm charts for all platform components (MinIO, Dremio, Nessie, Kestra, OpenMetadata, Superset, etc.)
- **Application Code**: dbt projects, pipeline scripts, transformation logic
- **Container Registry**: Docker images for custom components and services

## Key Features

- **Git Repository Hosting**: Centralized version control for all platform code
- **Branching & Versioning**: Git-based workflow for code promotion across environments
- **CI/CD Pipelines**: Automated testing, building, and deployment
- **Docker Registry**: Built-in container image storage
- **Multi-Environment**: Single instance managing dev, test, and prod deployments

## Architecture Decision

The choice of a single GitLab instance (rather than separate instances per environment) simplifies management and ensures consistency, but requires careful access control and CI/CD pipeline design to prevent accidental cross-environment issues.