---
type: entity
title: Kubernetes
created: 2026-05-14
updated: 2026-05-14
tags: [kubernetes, orchestration, container, platform]
related: [openmetadata, on-premises-kubernetes-deployment, kubernetes-native-orchestrator, helm-charts]
sources: ["OMD - Kubernetes On Premises.md"]
---

# Kubernetes

Kubernetes (K8s) is an open-source container orchestration platform for automating deployment, scaling, and management of containerized applications. In the context of OpenMetadata, Kubernetes serves as the underlying infrastructure for both the [[on-premises-kubernetes-deployment]] model (using Helm charts with Airflow) and the [[kubernetes-native-orchestrator]] model (running ingestion pipelines directly as Jobs and CronJobs).

## Role in OpenMetadata Deployments

- **Application Hosting**: OpenMetadata server components run as Kubernetes Deployments and Services.
- **Ingestion Orchestration**: Depending on the chosen architecture, ingestion pipelines are either managed by Airflow (deployed within the cluster) or executed as native Kubernetes resources via the [[omjob-operator]].
- **Storage**: Requires PersistentVolumes, with specific access modes (e.g., ReadWriteMany) depending on the components deployed.