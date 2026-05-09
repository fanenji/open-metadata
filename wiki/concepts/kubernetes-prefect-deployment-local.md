---
type: concept
title: Kubernetes Prefect Deployment (Local)
created: 2026-02-13
updated: 2026-02-13
tags: [kubernetes, prefect, helm, local-development, orchestration]
related: [kubernetes-development-best-practices, kubernetes-secrets-management, helm, prefect, kubernetes-airflow-deployment-local]
sources: ["Kubernetes Dev Environment on MacBook_ .md"]
---
# Kubernetes Prefect Deployment (Local)

Patterns for deploying Prefect on a local Kubernetes cluster using Helm, with a focus on Kubernetes Work Pools and Worker configuration.

## Architecture

The recommended pattern involves defining the execution environment defaults in a Prefect Cloud/Server "Kubernetes Work Pool" and then deploying a lightweight "Prefect Worker" to the cluster using Helm. The worker polls the work pool for flow runs and creates Kubernetes Jobs to execute them based on the pool's configuration.

## Work Pool Configuration (UI/API)

Define default settings for jobs launched by this pool:
- Kubernetes namespace
- Base Docker image (can be overridden per-deployment)
- Image pull policy
- Environment variables (e.g., `EXTRA_PIP_PACKAGES` for runtime installs)
- Base job template JSON to customize resources, volume mounts, etc.

## Worker Helm Deployment

1. Add the repo: `helm repo add prefect https://prefecthq.github.io/prefect-helm` and `helm repo update`
2. Create a Kubernetes Secret for the Prefect API key
3. Configure `values.yaml` for the `prefect/prefect-worker` chart with `worker.cloudApiConfig` (accountId, workspaceId, apiKeySecretName) and `worker.config.workPool` (the name of the Kubernetes Work Pool)

## Key Configuration

```yaml
# values.yaml (Prefect Worker example)
worker:
  cloudApiConfig:
    apiKeySecretName: prefect-api-key
    accountId: "<your-prefect-cloud-account-id>"
    workspaceId: "<your-prefect-cloud-workspace-id>"
  config:
    workPool: "<your-kubernetes-work-pool-name>"
```