type: concept
title: Infrastructure Architecture
created: 2026-05-22
updated: 2026-05-22
tags: [infrastructure, architecture, deployment]
related: [kubernetes, kestra, gitlab]
sources: ["AMBIENTI.md"]
---
# Infrastructure Architecture

The infrastructure architecture of the Data Platform is designed around the principles of **isolation**, **reproducibility**, and **centralized control**.

## Core Components
- **Orchestration**: **Kubernetes** provides the container runtime, organized via namespaces (`sviluppo`, `produzione`, `test`).
- **Workflow Management**: **Kestra** is deployed in dual instances (**DEV** and **PROD**) to separate workflow execution environments.
- **CI/CD & Control**: **GitLab** serves as the single source of truth for both infrastructure-as-code and data pipeline deployment.

## Environment Isolation Strategy
The architecture employs a multi-layered isolation strategy:
- **Compute Isolation**: Achieved through Kubernetes namespaces and separate K8s nodes/clusters for Dev vs. Prod.
- **Data Isolation**: Achieved through separate **Dremio** instances and distinct **Minio** buckets for Production and Staging.
- **Workflow Isolation**: Achieved through separate **Kestra** instances.

This strategy ensures that development, testing, and staging activities cannot impact the stability or performance of the production environment.
