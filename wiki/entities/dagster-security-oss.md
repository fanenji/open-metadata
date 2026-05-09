---
type: entity
title: Dagster Security (OSS)
created: 2026-05-07
updated: 2026-05-07
tags: [dagster, security, authentication, authorization, open-source, kubernetes]
related: [reverse-proxy-auth-pattern, oss-vs-cloud-security-gap, orchestration-tool-comparison, kubernetes]
sources: ["Orchestratori Data Platform_ Analisi Comparativa 2.md"]
---
# Dagster Security (OSS)

Dagster is an asset-centric orchestration platform with a modern developer experience. However, its open-source version has the weakest native authentication and authorization among major orchestrators.

## Architecture on K8s

- **Dagster Webserver (Dagit)**: UI and GraphQL API for development, monitoring, and operations
- **Dagster Daemon**: Background service for scheduling, sensors, and run queue management
- **User Code Deployments (Code Locations)**: Isolated gRPC server processes for user-defined code
- **Storages**: RunStorage, EventLogStorage, ScheduleStorage, SensorStorage (PostgreSQL recommended for production)
- **K8sRunLauncher**: Launches job executions as K8s pods or jobs

## Security (OSS)

- **No built-in authentication or RBAC** for Dagit UI/API in the open-source version
- These are primarily features of **Dagster+** (commercial/cloud version)
- The only native access control is a **read-only mode** for Dagit, which prevents UI modifications but does not authenticate users

## Workaround: Reverse Proxy

The standard approach for securing Dagster OSS is to place Dagit behind a reverse proxy (e.g., Nginx, Caddy, Traefik) that handles authentication:
- **LDAP/OIDC/SAML**: Integrated through the reverse proxy (e.g., using Authelia for LDAP)
- **RBAC**: Must be implemented at the proxy level, typically resulting in coarse-grained access (all-or-nothing)
- **Multiple Dagit instances**: A complex workaround for different access levels

## Deployment Considerations

- Deploy and configure a reverse proxy with appropriate authentication modules
- Use NetworkPolicies to force traffic through the proxy
- Execution authorization is managed via K8s ServiceAccounts (separate from UI/API auth)

## Pros

- Modern asset-centric paradigm
- Excellent local development and testing experience
- Strong observability and lineage in Dagit UI
- Best-in-class dbt integration

## Cons

- No native auth/RBAC in OSS version
- Requires reverse-proxy workaround for enterprise security
- Smaller community than Airflow
- API/documentation can be verbose or subject to change