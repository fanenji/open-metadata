type: concept
title: Continuous Delivery
created: 2026-04-29
updated: 2026-04-29
tags: [ci-cd, deployment, dbt, release-management]
related: [continuous-deployment, indirect-promotion, dbt-git-branching-strategies, dbt-release-management]
sources: ["getting-started-with-git-branching-strategies-and-dbt.md"]
---
# Continuous Delivery

**Continuous Delivery** is a software development practice where changes are automatically tested and prepared for release to production, but the actual deployment is a manual, business decision. In the context of [[dbt-git-branching-strategies]], it is the deployment model enabled by [[indirect-promotion]].

## Characteristics

- Changes are "batched" together and released as a group.
- A release manager manually triggers the deployment to production.
- Enables scheduled releases and holds features back from production.
- Provides a dedicated environment (e.g., `qa`) for end-to-end testing before release.

## Relationship to dbt

Indirect Promotion enables continuous delivery: changes from feature branches accumulate on a middle branch (e.g., `qa`), and a release manager opens a PR from the middle branch to `main` when the batch is ready. This contrasts with [[continuous-deployment]], which is enabled by [[direct-promotion]] and involves streaming changes to production immediately.