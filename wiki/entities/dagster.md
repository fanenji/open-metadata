---
type: entity
title: Dagster
created: 2024-03-13
updated: 2026-05-07
tags:
  - orchestration
  - workflow
  - kubernetes
  - security
  - asset-centric
  - orchestrator
  - python
  - asset-based
  - modern-data-stack
related: ["apache-airflow", "prefect", "reverse-proxy-authentication-pattern", "oss-vs-cloud-security-feature-gap", "kubernetes", "airflow", "kubernetes-etl-deployment-strategies", "software-defined-assets", "auto-materialization", "dbt"]sources:
  - Orchestrazione Data Platform - Analisi Comparativa.md
  - Airflow vs Dagster vs Kestra.md
  - The Modern Data Stack in 2025 What Actually Won.md
---

# Dagster

**Dagster** is a Python-based orchestrator that shifts the focus from executing tasks to managing data objects. It is an asset-centric orchestration platform designed for modern data engineering, with a focus on testability, observability, and integration with the modern data stack. In the current landscape, Dagster holds 9% adoption and is experiencing strong growth, particularly among teams seeking alternatives to [[Airflow]].

## Paradigm

Dagster is built around the concept of **Software-Defined Assets (SDA)**. Instead of defining tasks and dependencies, you define the data assets themselves, making the platform naturally suited for complex data engineering pipelines.

## Key Characteristics

- **Implementation**: Python-based, using decorators and definitions to define assets, jobs, and schedules.
- **Strengths**:
  - Excellent for complex data engineering pipelines.
  - Native support for [[dbt]] integration.
  - Advanced automation via **auto-materialization** rules.
  - Flexible Python decorators for creating custom [[sensors]].
- **Features**: Provides first-class support for asset observation, lineage, and testing.

## Architecture

- **Dagster Webserver (Dagit)**: UI and GraphQL API for development, monitoring, and operations.
- **Dagster Daemon**: Background service responsible for scheduling, sensors, and execution queue management.
- **User Code Deployments (Code Locations)**: User code is hosted in separate gRPC server processes, allowing separation of concerns.
- **Storages**: RunStorage, EventLogStorage, ScheduleStorage, SensorStorage (PostgreSQL recommended for production deployments).

## Security

**Critical limitation**: The open-source version of Dagster **does not include any built-in authentication or authorization** for the Dagit UI/API. These are features of Dagster+ (the commercial/cloud version).

- **Native (OSS)**: No auth mechanism. A read-only mode is available but does not authenticate users.
- **External**: Standard approach is to place Dagit behind a reverse proxy (Nginx, Caddy, Traefik) that handles authentication.
- **LDAP/OIDC/SAML**: Integrated through the reverse proxy, not directly by Dagster.
- **RBAC**: No native RBAC in OSS. Any role-based access must be implemented at the proxy level.

## Deployment on Kubernetes

The official Helm chart is the primary deployment method. Dagster can launch job executions as Kubernetes pods or jobs through `K8sRunLauncher` and `k8s_job_executor`.

## Market Position

Dagster holds 9% adoption in the orchestration market and is growing rapidly.

- **Adoption**: 9% (growing)
- **Trend**: Growing, +40% YoY in job posting mentions
- **Strengths**: Modern Python approach, asset-oriented design, higher developer satisfaction than [[Airflow]]
- **Weaknesses**: Smaller ecosystem than [[Airflow]], less enterprise adoption

### Competitive Landscape

Dagster competes in a fragmented orchestration market alongside [[Prefect]] (14%, growing), [[Airflow]] (42%, declining), and native warehouse scheduling (28%, growing). The orchestration market has no clear winner and remains fragmented by use case and company size.

## Pros and Cons

**Pros**:
- Modern asset-centric paradigm.
- Excellent local development and testing experience.
- Strong observability and data lineage tracing.
- Good [[dbt]] integration.
- Advanced automation via auto-materialization rules.
- Flexible sensor creation.
- Higher developer satisfaction compared to [[Airflow]].
- Modern Python approach.

**Cons**:
- OSS authentication/authorization severely limited; external proxy required.
- Smaller community and ecosystem compared to [[Airflow]].
- Less enterprise adoption.
- API and documentation can be verbose or subject to change.
- Potential costs if Dagster+ features become necessary.

## Related Pages

- [[apache-airflow]] — Task-centric alternative
- [[prefect]] — Pythonic dynamic workflow alternative
- [[reverse-proxy-authentication-pattern]] — Required external auth approach
- [[oss-vs-cloud-security-feature-gap]] — Security feature gap between OSS and commercial versions
- [[kubernetes]] — Target deployment environment
- [[software-defined-assets]] — Core paradigm concept
- [[auto-materialization]] — Automation rule concept
- [[dbt]] — Integrated transformation tool
- [[kubernetes-etl-deployment-strategies]] — ETL deployment strategies on Kubernetes