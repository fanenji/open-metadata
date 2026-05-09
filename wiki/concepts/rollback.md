---
type: concept
title: Rollback
created: 2026-05-08
updated: 2026-05-08
tags: [rollback, deployment, recovery, ci-cd]
related: [roll-forward, feature-toggles, error-recovery-mechanisms, ci-cd-rollback-strategies, data-quality-recovery, iceberg-table-versioning, nessie-catalog-versioning]
sources: ["research-error-recovery-mechanisms-2026-05-08.md"]
---
# Rollback

Rolling back is the process of reverting a deployment, data transformation, or configuration to a previous stable version.

## Types

- **System-Wide Rollback:** Reverting an entire application or deployment stack to a previous state.
- **Component-Level Rollback:** Reverting specific services, microservices, or individual [[dbt]] models.
- **Database Rollback:** The most complex variant, requiring explicit handling of schema changes and down-migrations.
- **ArgoCD Native Rollback:** Using tooling like ArgoCD to revert to a previous sync revision.
- **Git Revert:** Creating a new commit that undoes the problematic changes, keeping history intact.
- **Image Tag Revert:** Pointing the deployment manifest back to the previous container image tag.

## Best Practices

- Test rollback procedures before needing them in production.
- Set reasonable timeouts for rollout and failure detection.
- Notify the team on every rollback so root cause is investigated.
- Prevent rollback loops: detect if the rollback target is itself a problematic version.
