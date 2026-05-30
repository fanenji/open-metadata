---
type: source
title: "OMD - Kubernetes On Premises"
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, kubernetes, deployment, on-premises, helm]
related: [openmetadata, kubernetes, on-premises-kubernetes-deployment, external-dependencies-configuration, airflow-storage-requirements, kubernetes-native-orchestrator]
sources: ["OMD - Kubernetes On Premises.md"]
---

# OMD - Kubernetes On Premises

Official OpenMetadata documentation (v1.12.x) covering the deployment of OpenMetadata on a self-managed, on-premises Kubernetes cluster using Helm charts. This guide addresses the additional prerequisites and configurations required beyond a standard cloud Kubernetes deployment.

## Key Topics

- **External Dependencies**: Configuring external MySQL/PostgreSQL databases and ElasticSearch/OpenSearch search engines instead of the bundled Helm chart dependencies.
- **Persistent Volumes**: Addressing the ReadWriteMany (RWX) access mode requirement imposed by the Airflow dependency, using an NFS share and the `nfs-subdir-external-provisioner`.
- **Dynamic Provisioning**: Setting up a StorageClass for automatic PersistentVolume provisioning via the NFS provisioner.

## Relationship to Other Deployment Models

This source describes a deployment model that still depends on Apache Airflow as part of the Helm chart. This contrasts with the [[kubernetes-native-orchestrator]] model, which eliminates Airflow entirely by running ingestion pipelines as native Kubernetes Jobs and CronJobs. Users evaluating on-premises Kubernetes deployments should consider both approaches.