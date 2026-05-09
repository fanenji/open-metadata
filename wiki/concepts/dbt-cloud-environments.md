---
type: concept
title: dbt Cloud Environments
created: 2026-05-07
updated: 2026-05-07
tags: [dbt, cloud, environments, deployment]
related: [dbt-cloud, dbt-git-branching-strategies, CI-CD-for-data-pipelines]
sources: ["dbt Certified Architect Path beta - dbt Learn.md"]
---
# dbt Cloud Environments

dbt Cloud Environments are configurations that define how dbt projects connect to data platforms and execute jobs. They are a core concept in the [[dbt-cloud-architect-certification]] learning path (Milestone #2: Configuring and Managing Projects).

## Types of Environments

- **Development**: Used by individual developers for building and testing models. Typically connected to a personal schema or database.
- **Staging/QA**: Used for integration testing before production deployment. Often associated with a QA branch in Git.
- **Production**: Used for running scheduled jobs that serve downstream consumers. Connected to production data warehouse schemas.

## Key Configuration

Each environment specifies:
- **Connection**: Data platform credentials and connection details.
- **Deployment**: Which Git branch to use and how to promote code between environments.
- **Credentials**: Separate service accounts or user credentials per environment.

## Relationship to Git Branching

Environments are closely tied to [[dbt-git-branching-strategies]]. In Direct Promotion, a single main branch maps to production. In Indirect Promotion, a QA or staging branch maps to a non-production environment for testing before merging to main.