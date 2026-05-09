---
type: concept
title: dbt Blue/Green Deployment
created: 2026-04-04
updated: 2026-04-04
tags: [dbt, deployment, blue-green, promotion]
related: [dbt-promotion-strategies, dbt-canary-deployment, dbt-cloud-environments, dbt-state-aware-selectors]
sources: ["Mastering dbt Deployment Multi-Environment, CICD, and Promotion Strategies.md"]
---
# dbt Blue/Green Deployment

A deployment pattern for dbt that minimizes downtime and risk by maintaining two parallel production schemas: the current "blue" schema and the new "green" schema.

## Procedure

1. Deploy new model versions to the green schema (e.g., `analytics_prod_v2`).
2. Run smoke tests to validate results against the green schema.
3. Change BI tool connections and downstream consumers to point to the green schema.
4. Monitor for issues; if problems arise, redirect connections back to the blue schema.
5. After a confidence period, decommission the blue schema.

## Benefits

- **Zero-downtime switchover:** No interruption to existing queries during deployment.
- **Instant rollback:** Reverting connections to the previous schema is immediate.
- **Parallel validation:** Compare results between blue and green schemas before cutover.

## Configuration

Use dbt's dynamic schema configuration in `dbt_project.yml` to manage parallel schemas:

```yaml
models:
  prod:
    +schema: analytics_prod_v2  # green
```

## Related Concepts

- [[dbt-promotion-strategies]] — Overview of promotion patterns.
- [[dbt-canary-deployment]] — Gradual rollout alternative.
- [[dbt-state-aware-selectors]] — Stateful builds for promotion.