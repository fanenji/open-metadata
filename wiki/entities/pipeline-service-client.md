---
type: entity
title: Pipeline Service Client
created: 2026-05-14
updated: 2026-05-14
tags: [configuration, ingestion, orchestration, kubernetes, airflow]
related: [kubernetes-native-orchestrator, omjob-operator, ingestion-framework, openmetadata]
sources: ["OMD - Kubernetes Native Orchestrator.md"]
---
# Pipeline Service Client

The Pipeline Service Client is the OpenMetadata component responsible for interfacing with the orchestration backend that executes ingestion pipelines. It is configured through the `pipelineServiceClientConfig` block in the OpenMetadata Helm values.

## Configuration

The client supports multiple backend types, configured via the `type` field:

| Type | Backend | Status |
|------|---------|--------|
| `k8s` | Kubernetes-native orchestration (v1.12+) | Recommended for K8s deployments |
| `airflow` | Apache Airflow | Legacy default |

## Kubernetes Backend

When `type: k8s` is set, the client manages ingestion pipelines as Kubernetes resources. The `k8s` sub-configuration controls:

- **`useOMJobOperator`** — Whether to use the OMJob Operator CRDs (`true`) or native Jobs/CronJobs (`false`)
- **`ingestionImage`** — Container image for ingestion jobs (e.g., `ingestion-base:1.12.0`)
- **`serviceAccountName`** — Service account used by ingestion pods
- **`ttlSecondsAfterFinished`** — How long completed job resources are retained
- **`activeDeadlineSeconds`** — Maximum runtime before a job is terminated
- **`backoffLimit`** — Number of retries on failure
- **`securityContext`** — Pod security settings (runAsUser, fsGroup, etc.)
- **`resources`** — CPU and memory requests/limits for ingestion pods
- **`enableFailureDiagnostics`** — Enables automatic log and event collection on failure (OMJob Operator only)
- **`rbac.enabled`** — Whether the chart should create RBAC resources for the ingestion service account

## Metadata API Endpoint

The `metadataApiEndpoint` field specifies the URL that ingestion pods use to report status back to the OpenMetadata server (e.g., `http://openmetadata:8585/api`).