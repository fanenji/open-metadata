type: source
title: Getting Started with git Branching Strategies and dbt
created: 2026-04-29
updated: 2026-04-29
tags: [dbt, git, branching-strategies, ci-cd, dbt-cloud]
related: [dbt-git-branching-strategies, dbt-cloud-environments, dbt-cloud, direct-promotion, indirect-promotion, hierarchical-promotion, dbt-branch-protection, dbt-release-management, dbt-cloud-environment-configuration]
sources: ["getting-started-with-git-branching-strategies-and-dbt.md"]
---
# Getting Started with git Branching Strategies and dbt

**Authors:** Christine Berger, Carol Ohms, Taylor Dunlap, Steve Dowling (Resident Architects at dbt Labs)
**Published:** 2025-03-10
**URL:** https://docs.getdbt.com/blog/git-branching-strategies-with-dbt?version=1.12

## Summary

This article provides authoritative, prescriptive guidance from dbt Labs Resident Architects on choosing and implementing git branching strategies for dbt projects. It introduces two fundamental strategies — [[direct-promotion]] and [[indirect-promotion]] — and strongly recommends starting with Direct Promotion as the default. The article covers the full development workflow (development, quality assurance, promotion, deployment) and provides concrete configuration tables for [[dbt-cloud]] environments, data platform organization (databases and schemas), and branch protection rules.

## Key Contributions

- **Direct Promotion** is defined as the foundational strategy with only one long-lived branch (`main`). Features branch from `main`, are reviewed via PR, and merge back to `main` for continuous deployment.
- **Indirect Promotion** adds a middle long-lived branch (e.g., `qa`, `staging`) for dedicated QA environments, end-to-end testing, and release management (continuous delivery).
- **"Just get started" philosophy:** Direct Promotion is recommended as the default because it requires minimal provisioning, works with basic git knowledge, and can easily evolve into Indirect Promotion later.
- **Detailed configuration tables** mapping dbt Cloud environments (Development, CI, QA, Production) to base branches, database names, and schema settings for both strategies.
- **Flags for Indirect Promotion:** Dedicated QA environment, end-to-end testing needs, non-developer reviewers, batched releases, and high-stakes data consumption.

## Connections

- Strengthens the existing [[dbt-git-branching-strategies]] concept page with authoritative dbt Labs guidance.
- Extends [[dbt-cloud-environments]] by showing how environments map to specific branching strategies.
- Introduces the concept of [[dbt-release-management]] for the release process in Indirect Promotion.
- Introduces [[dbt-branch-protection]] as a recommended practice.
- Relates to [[CI-CD-for-data-pipelines]], [[dbt-slim-ci]], and [[dbt-cloud-webhooks]].