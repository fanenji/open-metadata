---
type: concept
title: On-Premises Kubernetes Deployment
created: 2026-05-14
updated: 2026-05-14
tags: [kubernetes, deployment, on-premises, openmetadata, helm]
related: [openmetadata, kubernetes, helm-charts, external-dependencies-configuration, airflow-storage-requirements, kubernetes-native-orchestrator]
sources: ["OMD - Kubernetes On Premises.md"]
---

# On-Premises Kubernetes Deployment

The process of installing and running OpenMetadata on a self-managed Kubernetes cluster using official Helm Charts. This deployment model is designed for organizations that require full control over their infrastructure, security, and compliance posture, and cannot or choose not to use managed Kubernetes services.

## Overview

Unlike cloud-based deployments where managed services handle databases, search engines, and storage, an on-premises deployment requires the operator to provision and configure these components externally. The OpenMetadata Helm Chart is then configured to connect to these external services rather than using its bundled dependencies.

## Key Prerequisites

1. **External Database**: A separately managed MySQL (8+) or PostgreSQL (12+) instance.
2. **External Search Engine**: A separately managed ElasticSearch (9.x) or OpenSearch (3.x) instance.
3. **ReadWriteMany Storage**: An NFS share and the `nfs-subdir-external-provisioner` to satisfy Airflow's RWX PersistentVolume requirement.
4. **Kubernetes Secrets**: Credentials for the external database and search engine must be stored as Kubernetes Secrets.

## Contrast with Kubernetes Native Orchestrator

This deployment model relies on Apache Airflow (bundled as a Helm chart dependency) for ingestion pipeline orchestration. The newer [[kubernetes-native-orchestrator]] model eliminates Airflow entirely, running ingestion pipelines as native Kubernetes Jobs and CronJobs. Users should evaluate both approaches:

- **Airflow-dependent (this model)**: Familiar for teams already using Airflow; requires RWX storage and additional resource overhead.
- **K8s-native orchestrator**: Lighter weight, no Airflow dependency, uses the [[omjob-operator]] for guaranteed exit handling and diagnostics.

## Namespace Consideration

The official guide assumes deployment in the `default` namespace, which is generally discouraged for production environments. Operators should consider deploying OpenMetadata in a dedicated namespace with appropriate resource quotas and network policies.