---
type: concept
title: Helm for Data Platforms
created: 2026-03-15
updated: 2026-03-15
tags: [kubernetes, helm, deployment, orchestration, airflow, prefect]
related: [kubernetes, airflow, prefect, kubernetes-secrets-management, kubernetes-jobs-cronjobs, kubernetes-etl-deployment-strategies]
sources: ["Kubernetes Development on macOS Guide.md"]
---
# Helm for Data Platforms

Helm is the package manager for Kubernetes, bundling complex applications into reusable "charts." For data platforms, Helm is the recommended deployment method for stateful orchestrators like Airflow and Prefect.

## Key Concepts

- **Chart**: A package of pre-configured Kubernetes resources (Deployments, Services, ConfigMaps, Secrets, etc.).
- **values.yaml**: A configuration file for customizing chart behavior without modifying templates.
- **Release**: A deployed instance of a chart with specific configuration.

## Airflow Deployment with Helm

- **Chart**: Official Apache Airflow Helm chart (`apache-airflow/airflow`).
- **Executor**: Set `executor: KubernetesExecutor` to launch per-task Pods.
- **Database**: Disable built-in PostgreSQL (`postgresql.enabled: false`) and use external database via Kubernetes Secret.
- **DAGs**: Configure via `dags.gitSync` (Git repository) or `dags.persistence` (PVC).
- **Secrets**: Use `webserverSecretKeySecretName` and `fernetKeySecretName` for secure key management.

## Prefect Deployment with Helm

- **Pattern**: Define execution environment in a Prefect "Kubernetes Work Pool" (UI/API), then deploy a lightweight "Prefect Worker" to the cluster using Helm.
- **Chart**: Official Prefect Helm chart (`prefect/prefect-worker`).
- **Configuration**: Worker connects to Prefect Cloud/Server via `cloudApiConfig` (accountId, workspaceId, apiKeySecretName).
- **Work Pool**: Defines default settings for Kubernetes Jobs (namespace, base image, environment variables, resources).

## Best Practices

- Store custom values.yaml in version control.
- Use Kubernetes Secrets for sensitive configuration (database URIs, API keys).
- Reference secrets via `metadataSecretName` or `externalDatabase` sections.
- Adjust resource requests/limits for local machine capacity.
- Use `extraPipPackages` for additional Python dependencies (e.g., `apache-airflow-providers-oracle`).