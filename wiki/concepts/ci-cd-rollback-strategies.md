---
type: concept
title: CI/CD Rollback Strategies
created: 2026-05-08
updated: 2026-05-08
tags: [ci-cd, rollback, gitops, kubernetes, database-migrations]
related: [ci-cd-for-data-pipelines, argo-cd, gitlab-ci, kubernetes, error-recovery-mechanisms, feature-toggles, blue-green-deployment, canary-release, dbt-cloud-environments, dbt-git-branching-strategies]
sources: ["research-error-recovery-mechanisms-2026-05-08.md"]
---
# CI/CD Rollback Strategies

Rollback strategies in CI/CD pipelines span multiple tools and patterns, with a critical gap between application deployment rollback and database schema state handling.

## Tool-Specific Patterns

- **ArgoCD & GitOps:** Rollbacks are treated as Git operations. An automated CI pipeline can detect deployment failures and automatically execute an ArgoCD rollback or `git revert`.
- **GitLab CI Incremental Rollouts:** Releases can be distributed to Kubernetes pods in tranches (manually or timed with a 5-minute default pause), limiting blast radius.
- **Image Tag Revert:** Pointing the deployment manifest back to the previous container image tag.

## The Database Migration Gap

Standard CI "rollback" (e.g., GitLab's feature) only redeploys the previous code version. It does **not** automatically revert database migrations from the reverted version. Pipelines must be explicitly designed with down-migration jobs or adopt a forward-migration-only strategy.

## Best Practices

- Test rollback procedures before needing them in production.
- Set reasonable timeouts for rollout and failure detection.
- Notify the team on every rollback so root cause is investigated.
- Prevent rollback loops: detect if the rollback target is itself a problematic version.
- Combine with feature flags when a toggle is sufficient to disable the fault.
- Treat runbooks as code: document and automate recovery steps.
