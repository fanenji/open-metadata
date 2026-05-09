---
type: concept
title: dbt Canary Deployment
created: 2026-04-04
updated: 2026-04-04
tags: [dbt, deployment, canary, promotion]
related: [dbt-promotion-strategies, dbt-blue-green-deployment, dbt-cloud-environments, dbt-state-aware-selectors]
sources: ["Mastering dbt Deployment Multi-Environment, CICD, and Promotion Strategies.md"]
---
# dbt Canary Deployment

A gradual rollout pattern for dbt where new model versions are initially exposed to a small subset of users or workloads before full production deployment.

## Procedure

1. Deploy new models to a canary schema alongside the production schema.
2. Route a small percentage of queries or users to the canary schema.
3. Monitor for errors, performance degradation, or data quality issues.
4. Gradually increase the canary's traffic share as confidence grows.
5. Once fully validated, promote the canary schema to full production and decommission the old schema.

## Benefits

- **Reduced blast radius:** Issues affect only a small subset of users initially.
- **Real-world validation:** Test under actual production query patterns.
- **Controlled rollout:** Ability to pause or roll back at any stage.

## Considerations

- Requires infrastructure to route queries dynamically between schemas.
- More complex to implement than Blue/Green for most dbt deployments.
- Best suited for high-traffic environments where gradual exposure is feasible.

## Related Concepts

- [[dbt-promotion-strategies]] — Overview of promotion patterns.
- [[dbt-blue-green-deployment]] — All-at-once switchover alternative.
- [[dbt-state-aware-selectors]] — Stateful builds for promotion.