---
type: concept
title: Reverse Proxy Authentication Pattern
created: 2026-05-07
updated: 2026-05-07
tags: [authentication, security, kubernetes, architecture]
related: [dagster, prefect, luigi, apache-airflow, oss-vs-cloud-security-feature-gap]
sources: ["Orchestrazione Data Platform - Analisi Comparativa.md"]
---
# Reverse Proxy Authentication Pattern

The reverse proxy authentication pattern is a standard approach for adding authentication and authorization to tools that lack native support. It involves placing a reverse proxy (Nginx, Traefik, OAuth2-Proxy) in front of the tool's UI/API to handle authentication before forwarding requests.

## When to Use

This pattern is required for:
- **Dagster OSS**: No native auth for Dagit UI/API
- **Prefect OSS**: Only basic auth; SSO and RBAC require external proxy
- **Luigi**: Minimal security; requires external proxy for any auth

## How It Works

1. All traffic to the tool's UI/API is routed through the reverse proxy
2. The proxy handles authentication (OIDC, SAML, LDAP) before forwarding requests
3. The tool itself remains unaware of the authentication layer
4. Network policies in Kubernetes force traffic through the proxy

## Limitations

- **Coarse-grained access control**: Typically provides all-or-nothing access to the UI/API
- **No granular RBAC**: Cannot easily enforce permissions on individual pipelines, assets, or DAGs
- **Operational complexity**: Adds another component to deploy, configure, and maintain
- **GraphQL inspection**: Complex to implement fine-grained access based on GraphQL query content

## Related Pages

- [[dagster]] — Requires this pattern for OSS deployments
- [[prefect]] — Requires this pattern for SSO/RBAC
- [[luigi]] — Requires this pattern for any auth
- [[apache-airflow]] — Has native auth via Flask AppBuilder, avoiding this pattern
- [[oss-vs-cloud-security-feature-gap]] — Why this pattern is needed