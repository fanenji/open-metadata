---
type: entity
title: Prefect
created: 2026-05-07
updated: 2026-05-07
tags: ["orchestration", "workflow", "python", "kubernetes", "security", "pythonic", "modern-data-stack"]
related: ["airflow", "kestra", "orchestration-system-comparison", "orchestration-code-portability", "orchestration-authn-authz", "kubernetes", "dbt", "dremio", "datahub", "apache-airflow", "dagster", "reverse-proxy-authentication-pattern", "oss-vs-cloud-security-feature-gap", "kubernetes-etl-deployment-strategies"]
sources: ["Orchestratori Data Platform_ Analisi Comparativa 1.md", "Orchestrazione Data Platform - Analisi Comparativa.md", "The Modern Data Stack in 2025 What Actually Won.md"]
---
# Prefect

Prefect is a modern Pythonic workflow orchestration system that emphasizes developer experience, dynamic pipeline creation, and resilience.

## Market Position

Prefect holds 14% adoption in the orchestration market and is growing, particularly among teams moving away from [[Airflow]]. Job posting mentions are increasing +40% year-over-year.

**Strengths:**
- Modern Python approach
- Higher developer satisfaction than [[Airflow]]
- Simpler operational model

**Weaknesses:**
- Smaller ecosystem than [[Airflow]]
- Less enterprise adoption

## Architecture

- **Prefect Server/API**: Backend that orchestrates flow executions, stores metadata, and serves the UI and GraphQL API
- **Database**: PostgreSQL recommended for production
- **Agent**: Lightweight process that polls for new flow runs and executes them
- **Work Pools**: Define how and where agents execute flows (Kubernetes, Docker, local)
- **Flows**: Fundamental orchestration unit, defined by Python functions decorated with @flow
- **Tasks**: Individual units of work within a flow
- **Deployments**: Definitions of how a flow should be executed

## Security

**Critical limitation**: The open-source version of Prefect has basic authentication only. Enterprise features like SSO and granular RBAC are primarily in Prefect Cloud.

- **Native (OSS)**: Basic authentication via configurable auth string (username:password format). CSRF protection available. **No native RBAC**.
- **External**: Standard approach for robust auth (OIDC, SAML, LDAP) is to use a reverse proxy (Nginx, Traefik, OAuth2‑Proxy)
- **RBAC**: Any granular RBAC must be implemented at the proxy level or through external systems

## Deployment on Kubernetes

The official Helm chart deploys the Prefect Server (API and UI) and configures agents. Flow runs are typically executed as Kubernetes Jobs or pods managed by an agent with a Kubernetes work pool.

## Strengths and Weaknesses

**Strengths:**
- Easy to use with low learning curve
- Excellent support for dynamic workflows
- Good error handling and observability
- Scalable with agents/work pools
- Higher developer satisfaction than [[Airflow]]
- Simpler operational model

**Weaknesses:**
- Smaller community and ecosystem than [[Airflow]]
- Advanced features are Cloud‑centric
- Less enterprise adoption
- Documentation can be lacking for complex OSS setups
- Frequent breaking changes

## Competitive Landscape

Prefect competes in a fragmented orchestration market alongside [[Dagster]] (9%, growing), [[Airflow]] (42%, declining), and native warehouse scheduling (28%, growing). The orchestration market has no clear winner and remains fragmented by use case and company size.

## Related Pages

- [[airflow]]
- [[kestra]]
- [[orchestration-system-comparison]]
- [[orchestration-code-portability]]
- [[orchestration-authn-authz]]
- [[kubernetes]]
- [[dbt]]
- [[dremio]]
- [[datahub]]
- [[apache-airflow]]
- [[dagster]]
- [[reverse-proxy-authentication-pattern]]
- [[oss-vs-cloud-security-feature-gap]]
- [[kubernetes-etl-deployment-strategies]]