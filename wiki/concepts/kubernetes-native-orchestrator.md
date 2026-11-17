---
sources: [OMD - Kubernetes Native Orchestrator.md, Announcing OpenMetadata 1.12 1.md]
tags: [kubernetes, orchestration, ingestion, operator, crd, openmetadata, deployment]
related: [omjob-operator, pipeline-service-client, ingestion-framework, openmetadata, kubernetes, airflow-to-kubernetes-migration, helm-charts]
type: concept
title: Kubernetes Native Orchestrator
created: 2026-05-14
updated: 2026-07-07
---
# Kubernetes Native Orchestrator

The **Kubernetes Native Orchestrator** is OpenMetadata's native scheduler for ingestion workflows, using Kubernetes directly instead of Apache Airflow. Introduced as a GA feature in OpenMetadata 1.12, it eliminates the Airflow dependency for cloud-native deployments. Starting with v1.12, ingestion pipelines can run directly on Kubernetes without requiring Apache Airflow — a significant architectural shift for organizations already operating Kubernetes workloads.

## Architecture

With the Kubernetes Orchestrator, OpenMetadata deployment is simplified from four components to three:

| Before (with Airflow) | After (Kubernetes Orchestrator) |
|-----------------------|-------------------------------|
| Application Server | Application Server |
| Database (MySQL/Postgres) | Database (MySQL/Postgres) |
| Search Index (OpenSearch/ES) | Search Index (OpenSearch/ES) |
| Airflow | *(removed)* |

## Key Benefits

- **Simplified Operations**: Fewer components mean simpler monitoring, updates, and troubleshooting
- **Cloud-Native**: Leverages existing Kubernetes clusters without managing a separate Airflow installation
- **Community-Driven**: Built in response to feedback that Airflow complexity was creating deployment friction
- **Native K8s Primitives**: Uses Kubernetes Jobs and CronJobs via the [[omjob-operator]] for scheduling

## Orchestration Modes

Two deployment options are available, representing a trade-off between production reliability and operational simplicity.

### Option 1: OMJob Operator (Recommended)

Uses custom CRDs (`OMJob` and `CronOMJob`) managed by the [[omjob-operator]]. This is the recommended path for production environments because it provides:

- **Exit Handler Guarantee** — Pipeline status is always reported to OpenMetadata, even if the ingestion pod crashes unexpectedly
- **Failure Diagnostics** — Automatic collection of pod logs and Kubernetes events on failure
- **Real-time Status Updates** — The operator monitors pod lifecycle events and updates pipeline status continuously

**Requirements:** Elevated permissions to install CRDs in the cluster.

### Option 2: Native Kubernetes Jobs

Uses standard `Job` and `CronJob` resources without any custom CRDs. Suitable for development, evaluation, or environments with restricted permissions.

**Limitations:**
- No guaranteed exit handler — if a pod is killed unexpectedly (OOMKilled, node failure), status updates may not reach OpenMetadata
- No automatic failure diagnostics — troubleshooting requires manual log inspection

## Configuration Entry Point

All Kubernetes orchestration settings are configured through the [[pipeline-service-client]] (`pipelineServiceClientConfig`) in the OpenMetadata Helm values. The `type` field must be set to `k8s`.

## Choosing a Mode

| Criterion | Option 1 (Operator) | Option 2 (Native) |
|-----------|---------------------|-------------------|
| Production readiness | Yes | Not recommended |
| Exit handler guarantee | Yes | No |
| Failure diagnostics | Automatic | Manual |
| CRD installation required | Yes | No |
| Setup complexity | Moderate | Low |

For production deployments, Option 1 is strongly recommended due to the exit handler guarantee and automatic diagnostics. Option 2 is appropriate for development, testing, or restricted environments where CRD installation is not possible.

## Migration from Airflow

See [[airflow-to-kubernetes-migration]] for migration guidance from Airflow-based ingestion to the Kubernetes Orchestrator.

## Requirements

- Kubernetes cluster (1.25+)
- [[omjob-operator]] deployed in the cluster
- [[helm-charts]] for OpenMetadata deployment

## See Also

- [[omjob-operator]] — Kubernetes operator for ingestion jobs
- [[airflow-to-kubernetes-migration]] — Migration guide from Airflow
- [[kubernetes]] — Kubernetes platform details
- [[ingestion-framework]] — Ingestion framework overview
