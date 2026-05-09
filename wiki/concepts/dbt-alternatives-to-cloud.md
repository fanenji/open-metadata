---
type: concept
title: dbt Alternatives to Cloud
created: 2026-04-29
updated: 2026-04-29
tags: [dbt, scheduling, deployment, self-hosted, orchestration]
related: [dbt-cloud, dbt-core, kubernetes, kestra, airflow]
sources: ["How to manage and schedule dbt.md"]
---
# dbt Alternatives to Cloud

The range of options for scheduling and running dbt outside of dbt Cloud, motivated by dbt Labs' 2022 pricing changes (100% increase to $100/month/dev, 8-dev team limit, opaque Enterprise pricing). dbt scheduling is described as "tricky but not complicated" because dbt only sends SQL queries to warehouses (low compute needs).

## Key Considerations

- dbt does not run queries — it sends SQL to the underlying warehouse, so compute requirements are minimal.
- Scheduling involves deciding where dbt runs (server) and what triggers execution.
- Options range from self-hosted solutions to managed alternatives.

## Scheduling Approaches

- **Self-hosted dbt Core**: Run dbt on your own infrastructure (server, container, Kubernetes).
- **Orchestration tools**: Use workflow orchestrators like Airflow, Kestra, or Dagster to trigger dbt runs.
- **CI/CD triggers**: Run dbt as part of CI/CD pipelines for development and staging environments.
- **Cron-based scheduling**: Simple cron jobs for production runs.

## Management Considerations

- Git repository structure (monorepo vs. multirepo).
- Development experience (DevEx) for analytics teams.
- CI/CD pipelines for validation and deployment.
- Alerting and monitoring for production runs.
- Environment management (dev, staging, production).

## Motivation

The 2022 dbt Cloud pricing changes made alternative solutions worth evaluating for many teams. The 100% price increase, 8-dev team limit, and opaque Enterprise pricing pushed organizations to consider self-hosted and third-party scheduling options.