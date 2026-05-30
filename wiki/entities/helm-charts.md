---
type: entity
title: Helm Charts
created: 2026-05-14
updated: 2026-05-14
tags: [helm, kubernetes, deployment, packaging]
related: [openmetadata, kubernetes, on-premises-kubernetes-deployment, nfs-subdir-external-provisioner]
sources: ["OMD - Kubernetes On Premises.md"]
---

# Helm Charts

Helm is the package manager for Kubernetes. Helm Charts are collections of pre-configured Kubernetes resources that can be deployed as a unit. OpenMetadata provides official Helm Charts for deploying the platform and its dependencies on Kubernetes clusters.

## OpenMetadata Helm Chart

The official OpenMetadata Helm Chart bundles the core application along with dependencies, including Apache Airflow for ingestion orchestration. For on-premises deployments, the chart supports extensive configuration to connect to external databases and search engines, and to disable bundled dependencies that are not needed.

## Related Charts

- **nfs-subdir-external-provisioner**: A community Helm Chart used in on-premises deployments to provide dynamic ReadWriteMany PersistentVolume provisioning via NFS. See [[airflow-storage-requirements]].