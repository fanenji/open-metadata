---
type: concept
title: Orchestration Authentication and Authorization
created: 2026-05-06
updated: 2026-05-06
tags: [orchestration, authentication, authorization, rbac, security]
related: [airflow, prefect, kestra, orchestration-system-comparison, dbt-cloud-security]
sources: ["Orchestratori Data Platform_ Analisi Comparativa 1.md"]
---
# Orchestration Authentication and Authorization

This page compares authentication and authorization capabilities across the three orchestration candidates: [[airflow|Apache Airflow]], [[prefect|Prefect]], and [[kestra|Kestra]].

## Apache Airflow (2.x)

- **Native System**: Yes. Includes a built-in Role-Based Access Control (RBAC) system for the UI.
- **Integrations**: Supports OAuth, LDAP, and OpenID Connect providers.
- **Customization**: The authentication and authorization mechanisms are extensible and customizable.

## Prefect (2.x)

- **Native System**: Yes, in Prefect Server (on-premise) and Prefect Cloud.
- **Features**: Offers user management, API keys, and RBAC (Workspaces, roles).
- **Integrations**: Prefect Cloud supports SSO with common providers. The on-premise server may have more limited options or require custom configuration. The open-source server may have more basic AuthN/AuthZ features compared to the Cloud or Enterprise versions.

## Kestra

- **Native System**: Yes, but with tiered capabilities.
- **Open-Source (OSS)**: Basic authentication (e.g., basic auth, or via Google/GitHub/Microsoft accounts if configured) and namespace-level permissions.
- **Enterprise**: Offers OpenID Connect (OIDC), LDAP, and more granular RBAC.
- **Customization**: For the OSS version, advanced authentication may require a reverse proxy with authentication capabilities (e.g., Keycloak) managed externally.

## Key Considerations

- If advanced AuthN/AuthZ (OIDC, LDAP, RBAC) is a strict requirement without additional licensing costs, Airflow or Prefect may be preferable.
- If the organization already has an Identity Provider (IdP) integrated with OpenShift/Rancher, OIDC support becomes important, favoring Airflow or Kestra Enterprise.
- Kestra OSS can be augmented with external authentication proxies, but this adds operational complexity.
