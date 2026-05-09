---
type: concept
title: Kubernetes Airflow Deployment (Local)
created: 2026-02-13
updated: 2026-02-13
tags: [kubernetes, airflow, helm, local-development, orchestration]
related: [kubernetes-development-best-practices, kubernetes-secrets-management, helm, airflow, kubernetes-prefect-deployment-local]
sources: ["Kubernetes Dev Environment on MacBook_ .md"]
---
# Kubernetes Airflow Deployment (Local)

Patterns for deploying Apache Airflow on a local Kubernetes cluster using Helm, with a focus on the KubernetesExecutor, external database configuration, and DAG persistence.

## Helm Deployment

Use the official Apache Airflow Helm chart (`apache-airflow/airflow`). Add the repo and install with custom `values.yaml`:

```bash
helm repo add apache-airflow https://airflow.apache.org
helm repo update
helm install airflow apache-airflow/airflow -f values.yaml --namespace airflow
```

## KubernetesExecutor Configuration

Set `executor: KubernetesExecutor` in `values.yaml`. This executor dynamically launches a separate Pod for each Airflow task, providing dynamic scaling and isolation.

## External Database Configuration

For production-like local setups connecting to remote Oracle/PostGIS databases:

- Disable the chart's built-in PostgreSQL: `postgresql.enabled: false`
- Create a Kubernetes Secret containing the database connection URI
- Reference this secret in `values.yaml` using `data.metadataSecretName` or the `externalDatabase` section
- Ensure necessary database drivers (e.g., `apache-airflow[oracle]`, `apache-airflow[postgres]`) are installed via `airflow.extraPipPackages`

## Secrets Management

Configure `webserverSecretKey` and `fernetKey` using Kubernetes Secrets. Generate strong keys and store them in Secrets, then reference them via `webserverSecretKeySecretName` and `fernetKeySecretName` in `values.yaml`. Avoid using default insecure keys.

## DAG Persistence

Configure how DAGs are made available to Airflow components:

- **PVC (PersistentVolumeClaim):** Mounts a PVC where DAG files can be placed. Requires a StorageClass that supports ReadWriteMany (RWX) if multiple pods need access.
- **Git Sync:** Uses a sidecar container to clone/pull DAGs from a Git repository. Often the most practical approach for keeping DAGs updated. Configure `repo`, `branch`, `sshKeySecret` (if private repo), etc.