type: concept
title: Continuous Deployment
created: 2026-04-29
updated: 2026-04-29
tags: [ci-cd, deployment, dbt]
related: [continuous-delivery, direct-promotion, dbt-git-branching-strategies]
sources: ["getting-started-with-git-branching-strategies-and-dbt.md"]
---
# Continuous Deployment

**Continuous Deployment** is a software development practice where every change that passes automated testing is automatically deployed to production. In the context of [[dbt-git-branching-strategies]], it is the deployment model enabled by [[direct-promotion]].

## Characteristics

- Changes are "streamed" to production as soon as they are merged to `main`.
- No manual release gates or batching of changes.
- Fastest path from development to production.
- Requires robust automated testing and CI/CD pipelines.

## Relationship to dbt

Direct Promotion enables continuous deployment: once a feature branch PR is merged to `main` and `main` is deployed, the changes are immediately in production. This contrasts with [[continuous-delivery]], which is enabled by [[indirect-promotion]] and involves batched releases.