---
type: concept
title: dbt Git Branching Strategies
created: 2026-05-07
updated: 2026-05-07
tags: [dbt, git, branching, deployment, ci-cd]
related: [dbt-cloud-environments, CI-CD-for-data-pipelines, dbt-cloud]
sources: ["dbt Certified Architect Path beta - dbt Learn.md"]
---
# dbt Git Branching Strategies

dbt Git Branching Strategies define how code changes flow through environments in dbt Cloud. This is a key topic in the [[dbt-cloud-architect-certification]] learning path (Milestone #2: Configuring and Managing Projects).

## Direct Promotion

In Direct Promotion, a single main branch is used for all environments. Developers work in feature branches, merge to main, and the main branch is deployed to production. This is simpler but offers less isolation between environments.

## Indirect Promotion

In Indirect Promotion, additional branches (e.g., QA, staging) are introduced between feature branches and main. Code is promoted through environments by merging to the corresponding branch. This provides better isolation and testing before production deployment.

## Considerations

- **Hotfixes**: Both strategies need a process for urgent production fixes that bypass normal promotion flow.
- **Multiple Middle Branches**: Organizations may use multiple intermediate branches (e.g., dev, qa, staging) for complex workflows.
- **dbt Cloud Configuration**: Environments in dbt Cloud are mapped to specific branches, and the deployment mechanism (e.g., CI/CD jobs) handles promotion between them.

## Relationship to CI/CD

These branching strategies are the Git-level foundation for the [[CI-CD-for-data-pipelines]] concept already in the wiki. dbt Cloud's advanced deployment features (continuous integration, job orchestration) build on top of the chosen branching strategy.