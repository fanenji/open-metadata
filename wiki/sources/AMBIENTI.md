type: source
title: Environment and Infrastructure Strategy
created: 2026-01-15
updated: 2026-01-15
tags: [infrastructure, ci-cd, kubernetes, dbt]
authors: []
year: 2026
url: ""
venue: ""
---
# Environment and Infrastructure Strategy

This document outlines the architectural strategy for the Kubernetes (K8s) deployment, environment isolation, and the data storage/virtualization stack (Dremio, Nessie, Minio).

## Kubernetes Organization
A single Kubernetes cluster is utilized, partitioned into three distinct namespaces to ensure isolation:
- **sviluppo** (Development)
- **produzione** (Production)
- **test** (Software updates/testing)

The entire infrastructure is controlled via a single **GitLab** repository, serving as the single source of truth for CI/CD pipelines.

## Environment Lifecycle
The deployment lifecycle follows these stages:
1. **Development**
2. **Test**
3. **Pre-production (Staging)**
4. **Production**

The first two stages occur within the development environment, while the latter two occur within the production environment.

## Data Stack Components

### Dremio, Nessie, and Minio
The architecture employs a multi-layered isolation strategy for the data and semantic layers.

#### Development Environment
- A single **Dremio** instance.
- Points to a **Nessie** catalog based on a specific **Minio** bucket.

#### Production Environment
To prevent resource contention and ensure stability, the production environment is split into two distinct instances:
- **Staging Instance**: For pre-production testing.
- **Production Instance**: For live workloads.

Each instance uses its own Nessie catalog and Minio bucket. This separation ensures that heavy workloads in Staging do not impact the Production environment.

#### Semantic Layer Organization (Dremio Spaces)
Dremio "Spaces" are used to structure project-specific queries and business logic across environments:
- **DEV**: Development of pipelines.
- **SANDBOX**: For ephemeral experiments and testing.
- **STAGING**: Pre-production testing.
- **PROD**: Live production environment.

The structure follows a hierarchical pattern (e.g., `dev/Project_1/Application/query1`).

### Nessie Versioning Strategies
There are two proposed strategies for managing data state in Nessie:

#### 1. Folder-based Isolation (Recommended for Stability)
- Data tables (PDS) are contained within separate root-level folders.
- Each project has its own folder structure.
- **dbt Integration**: The `profiles.yml` must specify the environment-specific `object_storage_path` (e.g., `dev.test_local_4`, `stg.test_local_4`, `prd.test_local_4`).

#### 2. Branch-based Isolation (High Risk)
- Uses a `main` branch for production and `project-xxx` branches for individual projects.
- Branches are ephemeral and managed via custom dbt macros.
- **Risks**: Requires complex custom macro implementation and carries a high risk of data inconsistency if merges to `main` are not strictly regulated.

## Orchestration and CI/CD
- **Kestra**: Deployed in two distinct instances (**Kestra DEV** and **Kestra PROD**) to separate workflow execution.
- **dbt**: Each dbt project maintains its own Git repository with a branching strategy (e.g., `main`, `feature-xxx`).
- **GitLab**: Acts as the central orchestrator for all platforms.
