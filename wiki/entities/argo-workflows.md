---
type: entity
title: Argo Workflows
created: 2026-05-07
updated: 2026-05-07
tags: [orchestration, workflow, kubernetes, security, cncf]
related: [flyte, kubernetes, reverse-proxy-authentication-pattern, apache-airflow]
sources: ["Orchestrazione Data Platform - Analisi Comparativa.md"]
---
# Argo Workflows

Argo Workflows is an open-source, container-native workflow engine specifically designed for Kubernetes. It is a CNCF project and part of the broader Argo ecosystem.

## Architecture

- **Workflow Controller**: Main component that observes Workflow CRDs and orchestrates execution as Kubernetes pods
- **Argo Server**: Optional server providing REST API and web UI for workflow management
- **Workflow CRD**: Custom Resource Definition describing workflow structure, tasks, dependencies, and templates
- **Executor**: Component inside each worker pod that executes task logic

## Security

Argo Workflows' security model is intrinsically tied to Kubernetes RBAC.

- **Native Auth Modes**:
  - `server`: Uses the Argo Server's own ServiceAccount
  - `client` (default v3.0+): Uses the client's Kubernetes bearer token
  - `sso`: Enables Single Sign-On via OIDC
- **OIDC/OAuth2 (SSO)**: Native support for integration with Identity Providers (Dex, Okta, Keycloak)
- **LDAP/SAML**: Achieved through an OIDC bridge like Dex
- **RBAC**: Relies heavily on Kubernetes RBAC. SSO RBAC (v2.12+) maps OIDC users/groups to K8s ServiceAccounts. Namespace-level delegation (v3.3+) enables self-service permission management.

## Deployment on Kubernetes

Installed directly on a K8s cluster by applying YAML manifests or using community Helm charts. Being K8s-native, it leverages Kubernetes directly for scheduling, scaling, and resource management.

## Pros and Cons

**Pros**: Truly K8s-native, highly scalable, ideal for CI/CD and parallel processing, flexible YAML configuration, part of the Argo ecosystem (CNCF)

**Cons**: Requires strong Kubernetes expertise, UI simpler than Airflow, smaller community than Airflow, initial production setup can be complex, multi-cluster management challenges

## Related Pages

- [[flyte]] — ML-focused K8s-native alternative
- [[kubernetes]] — Target deployment environment
- [[reverse-proxy-authentication-pattern]] — Alternative auth approach
- [[apache-airflow]] — Traditional task-centric alternative