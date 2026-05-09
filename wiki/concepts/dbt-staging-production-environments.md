---
type: concept
title: dbt Staging and Production Environments
created: 2026-04-29
updated: 2026-04-29
tags: [dbt, environments, ci-cd, deployment]
related: [dbt-cloud-environments, dbt-ci-cd-github-actions, ci-cd-for-data-pipelines, implementing-cicd-for-dbt-first-steps]
sources: ["Implementing CICD for dbt First Steps.md"]
---
# dbt Staging and Production Environments

A pattern for setting up separate staging and production environments in [[dbt]] CI/CD workflows. The staging environment acts as an integration layer to validate changes before pushing to production, while production contains vetted changes ready for consumption.

## Staging Environment

- Mirrors production but keeps risk away from end users.
- Allows running full dbt builds to catch breaking changes.
- Enables integration testing with downstream dependencies.
- Validates metrics and reporting are as expected.
- Reviews performance impacts under load before releasing.

## Production Environment

- Contains vetted changes ready for consumption.
- Provides stability for applications relying on dbt models.
- Triggered after successful staging validation.

## Workflow Trigger

In [[GitHub Actions]], the staging environment is typically triggered on pull requests to the staging branch:

```yaml
on:
  pull_request:
    branches:
    - staging
```

## Evolution

The article recommends starting with staging and production, then later adding development environments for engineers and UAT (User Acceptance Testing) environments for business users.