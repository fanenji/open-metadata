type: concept
title: dbt Branch Protection
created: 2026-04-29
updated: 2026-04-29
tags: [dbt, git, security, governance]
related: [dbt-git-branching-strategies, direct-promotion, indirect-promotion, dbt-cloud-security, dbt-cloud-environments]
sources: ["getting-started-with-git-branching-strategies-and-dbt.md"]
---
# dbt Branch Protection

**Branch Protection** refers to repository rules that enforce code review and quality gates before changes can be merged to protected branches. In the context of [[dbt-git-branching-strategies]], branch protection is a critical practice for maintaining code quality and governance.

## Recommended Rules

### For Direct Promotion
- **Protected branch:** `main`
- **Requirements:**
  - Pull request required (no direct commits)
  - At least 1 reviewer approval

### For Indirect Promotion
- **Protected branches:** `main` and the middle branch (e.g., `qa`)
- **Requirements:**
  - Pull request required for both branches
  - At least 1 reviewer approval for both

## Implementation

Branch protection is configured at the repository level (e.g., GitHub branch protection settings). It is a foundational practice that works alongside [[dbt-cloud-security]] and [[dbt-cloud-environments]] to create a secure and governed development workflow.