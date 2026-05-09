type: concept
title: Indirect Promotion
created: 2026-04-29
updated: 2026-04-29
tags: [dbt, git, branching-strategy, ci-cd, release-management]
related: [direct-promotion, hierarchical-promotion, dbt-git-branching-strategies, dbt-cloud-environments, dbt-branch-protection, dbt-release-management, continuous-delivery]
sources: ["getting-started-with-git-branching-strategies-and-dbt.md"]
---
# Indirect Promotion

**Indirect Promotion** is a git branching strategy that adds one or more long-lived branches (e.g., `qa`, `staging`, `uat`) between feature branches and `main`. The most common form is **hierarchical promotion**, where branches derive from and merge back in the same order.

## Workflow

- **Development:** A developer creates a `feature` branch from the middle branch (e.g., `qa`) to make, test, and review changes.
- **Quality Assurance (Feature):** A pull request is opened comparing the `feature` branch to the middle branch, reviewed by peers and optionally SMEs.
- **Promotion (Feature):** After approvals, the feature branch is merged to the middle branch.
- **Quality Assurance (Release):** SMEs or stakeholders review the middle branch's data outputs.
- **Promotion (Release):** A release manager opens a PR from the middle branch to `main` (a "release").
- **Deployment:** Changes are deployed to production after the middle branch is merged to `main`.

## dbt Cloud Configuration (1:1 Pattern)

| Environment | Type | Base Branch | Database | Schema |
|---|---|---|---|---|
| Development | development | `qa` | `development` | User-specified |
| Feature CI | deployment (General) | `qa` | `development` | `dev_ci` (overridden) |
| Quality Assurance | deployment (Staging) | `qa` | `qa` | `analytics` |
| Release CI | deployment (General) | `main` | `development` | Safe default |
| Production | deployment (Production) | `main` | `production` | `analytics` |

## Repository Rules

- Branch protection on `main` and the middle branch requiring pull requests with at least 1 reviewer approval.
- A PR template for feature PRs against the middle branch.
- A release PR template for middle branch PRs against `main`.

## Strengths and Weaknesses

**Strengths:**
- Dedicated environment for end-to-end testing over time.
- Easier review from BI tools via a stable staging location.
- Configurations and job changes can be tested with production-like parameters.
- Changes merged to the middle branch are not reflected in production.

**Weaknesses:**
- Slower path to production due to extra processes.
- Valid changes can get stuck behind other changes that aren't ready.
- Requires dedicated branch management and release ownership.
- Additional compute for QA environment and release CI jobs.

## When to Consider Indirect Promotion

- A dedicated QA/UAT/staging environment is needed.
- End-to-end testing over time is required before production.
- Non-developer stakeholders review data outputs.
- Environments use different (scrubbed/limited) data.
- Changes are batched for scheduled releases.
- Data consumption is high-stakes.

Indirect Promotion enables **continuous delivery** (batched changes to production via releases).