---
type: entity
title: dbt Cloud
created: 2026-05-07
updated: 2026-05-07
tags: [dbt, cloud, platform, enterprise]
related: [dbt-cloud-architect-certification, dbt-mesh, dbt-catalog, dbt-cloud-environments, dbt-cloud-security, dbt-cloud-webhooks, dbt-git-branching-strategies]
sources: ["dbt Certified Architect Path beta - dbt Learn.md"]
---
# dbt Cloud

dbt Cloud is the managed platform by dbt Labs for deploying, orchestrating, and governing dbt projects at scale. It provides a web-based IDE, job scheduling, CI/CD integration, environment management, and enterprise features such as SSO, RBAC, and the dbt Mesh and dbt Catalog capabilities.

## Key Features

- **Environments**: Dev, staging, and production configurations with connection and credential management.
- **Git Integration**: Native integration with GitHub, GitLab, and other providers; supports Direct and Indirect Promotion branching strategies.
- **Advanced Deployment**: Continuous integration, job orchestration, and environment-specific behavior customization.
- **Security**: SSO (Okta, Microsoft Entra ID, Google Workspace), RBAC, SCIM, and multifactor authentication.
- **Automation**: Webhooks for triggering workflows on job completion, run failures, and other events.
- **Governance**: dbt Mesh for cross-project dependency management and dbt Catalog for data discovery and documentation.

## Relevance

dbt Cloud is the central platform for the [[dbt-cloud-architect-certification]] learning path. It represents the enterprise-grade evolution of dbt, adding administration, security, and governance layers on top of the open-source transformation framework.