---
type: concept
title: Data Release Pipeline
created: 2026-04-04
updated: 2026-04-04
tags: [ci-cd, deployment, data-pipeline, orchestration]
related: [data-ci-cd-principles, deployment-critical-vs-monitoring-tests, CI-CD-for-data-pipelines, dbt-slim-ci]
sources: ["How CI-CD should look for Data teams.md"]
---
# Data Release Pipeline

An automated pipeline for deploying data changes to production, combining data transformation, orchestration, and observability. The concept is introduced by [[Hugo Lu]] as the mechanism for automating the deployment process in data teams' CI/CD workflows.

## Components
- **Data transformation**: code that materializes data assets (e.g., dbt models).
- **Data orchestration**: tooling that schedules and manages pipeline execution.
- **Observability**: monitoring of data quality, job status, and system health.

## Key Characteristics
- Automates the deployment of data changes to production without manual intervention.
- Integrates with [[deployment-critical-vs-monitoring-tests]] to determine which tests block deployment.
- Supports the "flat cloning" pattern where staging data that passes quality checks is cloned directly into production.
- Enables [[data-ci-cd-principles]] such as trunk-based development and efficient test automation.

## Relationship to Existing Wiki
The data release pipeline concept provides a unifying framework for the wiki's existing coverage of dbt (transformation), Kestra (orchestration), and data observability tools. It extends [[CI-CD-for-data-pipelines]] by defining the specific pipeline structure for data deployment.