type: concept
title: Direct Promotion
created: 2026-04-29
updated: 2026-04-29
tags: [dbt, git, branching-strategy, ci-cd]
related: [indirect-promotion, hierarchical-promotion, dbt-git-branching-strategies, dbt-cloud-environments, dbt-branch-protection, continuous-deployment]
sources: ["getting-started-with-git-branching-strategies-and-dbt.md"]
---
# Direct Promotion

**Direct Promotion** is a git branching strategy where only one long-lived branch (`main`) exists in the repository. It is the foundational strategy recommended by [[dbt Labs]] as the default for teams getting started with [[dbt-git-branching-strategies]].

## Workflow

- **Development:** A developer creates a `feature` branch from `main` to make, test, and personally review changes.
- **Quality Assurance:** A pull request is opened comparing the `feature` branch against `main`, reviewed by peers (required), stakeholders, or subject matter experts.
- **Promotion:** After all required approvals and checks, the feature branch is merged to `main`.
- **Deployment:** Changes are immediately available in production after merge and deployment of `main`.

## dbt Cloud Configuration

| Environment | Type | Base Branch | Database | Schema |
|---|---|---|---|---|
| Development | development | `main` | `development` | User-specified |
| Continuous Integration | deployment (General) | `main` | `development` | `dev_ci` (overridden by job) |
| Production | deployment (Production) | `main` | `production` | `analytics` |

## Repository Rules

- Branch protection on `main` requiring pull requests with at least 1 reviewer approval.
- A PR template for feature branch PRs against `main`.

## Strengths and Weaknesses

**Strengths:**
- Fastest path to production — changes are live once the PR is merged and deployed.
- Management is distributed — every developer owns their branch.
- No releases or extra processes to manage.

**Weaknesses:**
- Challenges for end-to-end or time-based testing in a non-production environment.
- Difficult for stakeholders with differing schedules or technical abilities to review before production.
- Harder to test configurations or job changes before they hit production.

## Relationship to Other Strategies

Direct Promotion enables **continuous deployment** (streaming changes to production). It is the foundation of all branching strategies and can easily evolve into [[indirect-promotion]] when the team's needs grow.