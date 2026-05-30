---
type: entity
title: OMJob Operator
created: 2026-05-14
updated: 2026-05-14
tags: [kubernetes, operator, crd, ingestion, orchestration]
related: [kubernetes-native-orchestrator, pipeline-service-client, ingestion-framework, openmetadata]
sources: ["OMD - Kubernetes Native Orchestrator.md"]
---
# OMJob Operator

The OMJob Operator is a Kubernetes operator that manages ingestion pipelines for OpenMetadata using Custom Resource Definitions (CRDs). It is the recommended production path for running ingestion workloads on Kubernetes, introduced in OpenMetadata v1.12.

## Custom Resources

The operator introduces two CRDs:

| Resource | Purpose |
|----------|---------|
| **CronOMJob** | Scheduled pipelines that run on a cron schedule |
| **OMJob** | On-demand pipelines triggered for one-off execution |

## Key Guarantees

### Exit Handler Guarantee
Even if the ingestion pod crashes (OOMKilled, node failure, etc.), the operator ensures that pipeline status is always reported back to OpenMetadata. This is the primary differentiator from native Kubernetes Jobs.

### Failure Diagnostics
When pipelines fail, the operator automatically collects detailed error context from pod logs and Kubernetes events, attaching them to the pipeline status for easier troubleshooting.

### Pod Lifecycle Monitoring
The operator watches pod events in real-time and updates pipeline status accordingly, providing accurate, up-to-date information in the OpenMetadata UI.

## Deployment

The operator is deployed as part of the OpenMetadata Helm chart by enabling `omjobOperator.enabled: true`. It runs as a separate deployment using the `docker.getcollate.io/openmetadata/omjob-operator` image.

## RBAC Requirements

The operator requires elevated permissions to manage CRDs, pods, configmaps, secrets, and events. The CRDs are installed under the `pipelines.openmetadata.org` API group.