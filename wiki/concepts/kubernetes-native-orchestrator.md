---
type: concept
title: Kubernetes Native Orchestrator
created: 2026-05-14
updated: 2026-05-14
tags: [kubernetes, orchestration, ingestion, operator, crd]
related: [omjob-operator, pipeline-service-client, ingestion-framework, openmetadata]
sources: ["OMD - Kubernetes Native Orchestrator.md"]
---
# Kubernetes Native Orchestrator

Starting with OpenMetadata v1.12, ingestion pipelines can run directly on Kubernetes without requiring Apache Airflow. This represents a significant architectural shift, allowing organizations that already operate Kubernetes workloads to use native scheduling and execution primitives.

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