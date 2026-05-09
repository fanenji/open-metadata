---
type: entity
title: Prefect Security (OSS)
created: 2026-05-07
updated: 2026-05-07
tags: [prefect, security, authentication, authorization, open-source, kubernetes]
related: [reverse-proxy-auth-pattern, oss-vs-cloud-security-gap, orchestration-tool-comparison, kubernetes]
sources: ["Orchestratori Data Platform_ Analisi Comparativa 2.md"]
---
# Prefect Security (OSS)

Prefect is a modern Pythonic workflow orchestration system emphasizing dynamic workflows and developer experience. Its open-source version provides basic authentication but lacks enterprise-grade security features.

## Architecture on K8s

- **Prefect Server/API**: Backend orchestrating flow runs, storing metadata, serving UI and GraphQL API
- **Database**: PostgreSQL recommended for production
- **Agent**: Lightweight process polling for new flow runs and executing them in specified infrastructure
- **Work Pools**: Define how and where agents execute flows (e.g., Kubernetes, Docker)
- **Flows**: Python functions decorated with `@flow`
- **Tasks**: Python functions decorated with `@task`
- **Deployments**: Definitions of how a flow should be executed (schedule, parameters, infrastructure, triggers)

## Security (OSS)

- **Basic Authentication**: Configurable via `server.api.auth_string` (username:password format)
- **CSRF Protection**: Can be enabled for the server API
- **No granular RBAC**: RBAC is a Prefect Cloud feature
- Basic auth provides a single "administrative" access level

## Workaround: Reverse Proxy

Similar to Dagster, the standard approach for enterprise-grade authentication is a reverse proxy:
- **OIDC/SAML/LDAP**: Integrated through the proxy (e.g., OAuth2-Proxy, Nginx with auth modules)
- **RBAC**: Must be implemented at the proxy level, typically coarse-grained

## Deployment Considerations

- Helm chart supports basic auth configuration via Kubernetes Secrets
- NetworkPolicies should force traffic through the reverse proxy
- CORS configuration is important when accessing the API from different domains

## Pros

- Low learning curve, very Pythonic
- Excellent support for dynamically defined pipelines at runtime
- Good error handling and observability basics
- Scalable with agents/work pools

## Cons

- Basic auth only in OSS version
- SSO and granular RBAC are Prefect Cloud features
- Smaller community than Airflow
- Documentation can be lacking for complex OSS configurations
- Frequent breaking changes between versions