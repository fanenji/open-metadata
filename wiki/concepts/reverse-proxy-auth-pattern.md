---
type: concept
title: Reverse Proxy Auth Pattern
created: 2026-05-07
updated: 2026-05-07
tags: [security, authentication, authorization, reverse-proxy, nginx, traefik, kubernetes]
related: [dagster-security-oss, prefect-security-oss, oss-vs-cloud-security-gap, kubernetes]
sources: ["Orchestratori Data Platform_ Analisi Comparativa 2.md"]
---
# Reverse Proxy Auth Pattern

A common architectural pattern for adding authentication and authorization to open-source orchestration tools that lack native enterprise security features. This pattern is the standard workaround for [[dagster-security-oss|Dagster OSS]] and [[prefect-security-oss|Prefect OSS]] in on-premise Kubernetes deployments.

## How It Works

1. A reverse proxy (e.g., Nginx, Traefik, Caddy, OAuth2-Proxy) is deployed in front of the orchestration tool's UI/API.
2. The proxy handles authentication (e.g., OIDC, LDAP, SAML) before forwarding requests to the backend.
3. The orchestration tool itself remains unaware of authentication; it receives only authenticated requests.

## Supported Authentication Protocols

- **OIDC/OAuth2**: Via proxy plugins (e.g., OAuth2-Proxy, Authelia)
- **LDAP**: Via proxy with LDAP support (e.g., Authelia)
- **SAML**: Via proxy or bridge (e.g., Dex as OIDC bridge to SAML IdP)

## Limitations

- **Coarse-grained access control**: Typically all-or-nothing access to the UI/API. Granular RBAC at the DAG/asset level is difficult to implement via proxy.
- **Operational complexity**: Adds another component to deploy, configure, and maintain.
- **Performance overhead**: Additional network hop and authentication processing.
- **Workaround complexity**: For Dagster, multiple Dagit instances with different access configurations have been suggested as a complex workaround.

## When to Use

- When SSO/RBAC is a hard requirement but the chosen orchestrator lacks native support
- In multi-tenant environments where access control is necessary
- When the team has operational capacity to manage an additional infrastructure component

## When to Avoid

- When the orchestrator has sufficient native auth (e.g., Airflow with FAB)
- When the team lacks operational capacity for proxy management
- When granular per-resource access control is required