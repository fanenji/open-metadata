---
type: concept
title: OSS vs. Cloud Security Feature Gap
created: 2026-05-07
updated: 2026-05-07
tags: [security, orchestration, licensing, architecture]
related: [dagster, prefect, reverse-proxy-authentication-pattern, apache-airflow]
sources: ["Orchestrazione Data Platform - Analisi Comparativa.md"]
---
# OSS vs. Cloud Security Feature Gap

A critical architectural consideration: many modern orchestration tools (Dagster, Prefect) reserve enterprise security features — SSO, granular RBAC, audit logging — for their commercial/cloud versions. The open-source versions provide only basic or no authentication, requiring external components for production-grade security.

## Tools Affected

- **Dagster**: OSS has no native auth; Dagster+ has SSO and RBAC
- **Prefect**: OSS has basic auth only; Prefect Cloud has SSO, RBAC, audit logs
- **Airflow**: Less affected — Flask AppBuilder provides mature native auth in OSS
- **Argo Workflows**: Less affected — leverages K8s RBAC natively
- **Flyte**: Less affected — native OIDC support

## Implications

- **Operational burden**: Organizations must deploy and maintain reverse proxies, identity providers, and custom auth solutions
- **Cost pressure**: If enterprise features are needed, organizations may be forced into paid versions
- **Vendor lock-in risk**: Cloud versions may have different APIs or deployment models
- **Security expertise required**: Teams need deep knowledge of K8s security, OIDC, and proxy configuration

## Decision Framework

When evaluating orchestrators, consider:
1. Are SSO and granular RBAC required?
2. Is the team willing to invest in external auth infrastructure?
3. Is there budget for commercial versions?
4. What is the team's Kubernetes security expertise level?

## Related Pages

- [[dagster]] — Exhibits this gap significantly
- [[prefect]] — Exhibits this gap significantly
- [[reverse-proxy-authentication-pattern]] — Mitigation strategy
- [[apache-airflow]] — Less affected by this gap