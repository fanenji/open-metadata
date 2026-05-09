---
type: entity
title: Flyte
created: 2026-05-07
updated: 2026-05-07
tags: [orchestration, workflow, kubernetes, security, ml]
related: [argo-workflows, kubernetes, apache-airflow, temporal]
sources: ["Orchestrazione Data Platform - Analisi Comparativa.md"]
---
# Flyte

Flyte is a Kubernetes-native orchestration platform originally developed by Lyft, strongly typed and oriented toward reproducibility, particularly suited for machine learning and complex data processing workflows.

## Architecture

Flyte is a K8s-native platform with components deployed via Helm charts. Workflows are defined in Python and versioned. It provides strong typing, reproducibility, and native OIDC/OAuth2 support for authentication.

## Security

- **Native Auth**: OIDC/OAuth2 support is built-in for API and UI access
- **RBAC**: Leverages Kubernetes RBAC for execution security, similar to Argo Workflows
- **K8s Integration**: ServiceAccounts and K8s-native security primitives are used for workload isolation

## Deployment on Kubernetes

The official Helm chart is the primary deployment method. Being K8s-native, it integrates deeply with Kubernetes for scheduling, scaling, and resource management.

## Pros and Cons

**Pros**: K8s-native with strong typing and reproducibility, excellent for ML workflows, native OIDC support, good versioning

**Cons**: Requires strong Kubernetes expertise, smaller community than Airflow, primarily focused on ML/data science use cases

## Related Pages

- [[argo-workflows]] — General-purpose K8s-native alternative
- [[kubernetes]] — Target deployment environment
- [[apache-airflow]] — Traditional task-centric alternative
- [[temporal]] — Durable workflow alternative