---
type: concept
title: OSS vs Cloud Security Gap
created: 2026-05-07
updated: 2026-05-07
tags: [security, authentication, authorization, open-source, cloud, decision-framework]
related: [reverse-proxy-auth-pattern, airflow-on-premise-k8s, dagster-security-oss, prefect-security-oss, argo-workflows-security, flyte-security, temporal-security]
sources: ["Orchestratori Data Platform_ Analisi Comparativa 2.md"]
---
# OSS vs Cloud Security Gap

A critical observation from the orchestration tool comparison: **the "open-source and on-premise" label does not imply complete security features.** There is a significant gap between what open-source self-hosted versions offer and what commercial/cloud versions provide, particularly in authentication and authorization.

## Key Findings

- **Airflow** is the exception: its Flask AppBuilder (FAB) framework provides RBAC, LDAP, and OIDC support in the OSS version, making it the most security-complete OSS orchestrator.
- **Dagster OSS** has no built-in authentication or RBAC for its UI/API. These are primarily features of Dagster+ (commercial/cloud).
- **Prefect OSS** offers only basic authentication (username:password string). SSO and granular RBAC are Prefect Cloud features.
- **Argo Workflows** and **Flyte** leverage K8s RBAC for execution security but require OIDC integration for UI/API authentication.
- **Temporal** uses a custom plugin model requiring development effort for security customization.

## Implications for On-Premise Deployments

- Organizations requiring enterprise-grade security (SSO, granular RBAC) must either:
  - Choose Airflow (most mature OSS auth)
  - Implement reverse-proxy workarounds (for Dagster, Prefect)
  - Invest in custom security plugins (for Temporal)
  - Accept the operational complexity of K8s RBAC + OIDC (for Argo, Flyte)
- The security gap adds operational complexity and maintenance burden to on-premise deployments.
- This is a critical planning factor: the choice of orchestrator may be influenced by how easily it integrates with existing enterprise identity infrastructure.

## Decision Framework

| Requirement | Recommended Approach |
|-------------|---------------------|
| SSO + RBAC out-of-the-box | Airflow |
| SSO + K8s-native | Argo Workflows + OIDC |
| ML-focused + SSO | Flyte + OIDC |
| Developer experience priority | Dagster/Prefect + reverse proxy |
| Durable workflows | Temporal + custom auth plugin |