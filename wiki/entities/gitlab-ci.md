---
type: entity
title: GitLab CI
created: 2026-05-08
updated: 2026-05-08
tags: [ci-cd, gitlab, deployment, rollback]
related: [argo-cd, kubernetes, ci-cd-rollback-strategies, error-recovery-mechanisms, blue-green-deployment, canary-release]
sources: ["research-error-recovery-mechanisms-2026-05-08.md"]
---
# GitLab CI

GitLab CI/CD provides incremental rollout capabilities and rollback features for Kubernetes deployments. A critical documented limitation is that standard CI "rollback" only redeploys the previous code version and does **not** automatically revert database migrations.

## Key Features

- Incremental rollouts to Kubernetes pods in tranches (manual or timed with a 5-minute default pause).
- Blast radius limitation via gradual rollout.
- Runbook automation for structured, audited recovery processes.

## Database Migration Gap

Pipelines must be explicitly designed with down-migration jobs or adopt a forward-migration-only strategy, as GitLab's standard rollback does not handle database schema state.
