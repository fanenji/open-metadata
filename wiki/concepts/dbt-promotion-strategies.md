---
type: concept
title: dbt Promotion Strategies
created: 2026-04-04
updated: 2026-04-04
tags: [dbt, deployment, promotion, ci-cd]
related: [dbt-blue-green-deployment, dbt-canary-deployment, dbt-cloud-environments, dbt-state-aware-selectors, dbt-git-branching-strategies, CI-CD-for-data-pipelines]
sources: ["Mastering dbt Deployment Multi-Environment, CICD, and Promotion Strategies.md"]
---
# dbt Promotion Strategies

Strategies for safely promoting dbt model changes from development through staging to production. These patterns borrow from software deployment practices and adapt them to the data warehouse context.

## Core Patterns

- **Blue/Green Deployment:** Deploy parallel schemas (green = new production, blue = current). Switch read/write endpoints after smoke tests. Allows swift rollback by rerouting.
- **Canary Deployments:** Gradually direct a small portion of workload or users to new models before full rollout.
- **Safe Switchover:** Deploy to a new schema, run smoke tests, change BI tool connections, then decommission the old schema after confidence is established.

## Key Techniques

- Use dbt's `state:modified` and `--defer` flags for promotion-aware builds that only process changed models.
- Maintain versioned snapshots of critical datasets for redundancy.
- Use orchestrator features (Airflow, Prefect) for automatic retries and alerts on failure.

## Related Concepts

- [[dbt-blue-green-deployment]] — Detailed guide on parallel schema deployment.
- [[dbt-canary-deployment]] — Gradual rollout pattern.
- [[dbt-state-aware-selectors]] — Using state comparison for incremental builds.
- [[dbt-cloud-environments]] — Environment configuration in dbt Cloud.