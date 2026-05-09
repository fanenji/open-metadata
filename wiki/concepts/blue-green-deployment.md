---
type: concept
title: Blue-Green Deployment
created: 2026-05-08
updated: 2026-05-08
tags: [deployment, ci-cd, recovery, kubernetes]
related: [canary-release, feature-toggles, error-recovery-mechanisms, ci-cd-rollback-strategies, kubernetes]
sources: ["research-error-recovery-mechanisms-2026-05-08.md"]
---
# Blue-Green Deployment

Two identical environments ("blue" and "green") are maintained. Only one is live at a time except during a switch-over. If the new version fails, traffic is instantly routed back to the old environment.

## Advantages

- Zero-downtime recovery for the application layer.
- Instant traffic switching between environments.
- Simple mental model for rollback.

## Trade-offs

- Requires double the infrastructure resources.
- Database schema changes must be backward-compatible during the switch.
