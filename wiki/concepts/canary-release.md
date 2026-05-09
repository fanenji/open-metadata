---
type: concept
title: Canary Release
created: 2026-05-08
updated: 2026-05-08
tags: [deployment, ci-cd, recovery, kubernetes]
related: [blue-green-deployment, feature-toggles, error-recovery-mechanisms, ci-cd-rollback-strategies, kubernetes]
sources: ["research-error-recovery-mechanisms-2026-05-08.md"]
---
# Canary Release

A new version is gradually rolled out to a small subset of users or pods. Error rates are monitored, and if thresholds are exceeded, the release is automatically halted and rolled back.

## Advantages

- Limits blast radius to a small subset of traffic.
- Automated safety via error rate thresholds.
- Provides real-world validation before full rollout.

## Best Practices

- Define clear failure criteria (e.g., error rate > 5%, response time > 500ms).
- Monitor error rates and automatically halt on threshold breach.
- Combine with feature flags for additional safety.
