---
type: concept
title: dbt CI Testing Strategy
created: 2026-04-04
updated: 2026-04-04
tags: [dbt, ci-cd, testing, data-quality]
related: [dbt-slim-ci, dbt-state-aware-selectors, dbt-testing-patterns, dbt-data-contract-implementation, ci-cd-for-data-pipelines]
sources: ["dbt Slim CI Tactics for Large Repos.md"]
---
# dbt CI Testing Strategy

A split testing approach for dbt projects that separates fast, focused tests for pull requests from deep, broad tests for nightly runs. This strategy keeps PR CI fast while maintaining comprehensive coverage.

## PR CI (Fast & Focused)

- **Generic schema tests** on the impacted surface (`unique`, `not_null`, `accepted_values`).
- A small set of **unit tests** (dbt v1.6+) for logic-heavy models that changed.
- **Contract checks** if model contracts are adopted (great for downstream stability).

```bash
# Schema tests for the impacted graph
dbt test --select pr_tests

# Unit tests (namespaced near the model)
dbt test --select state:modified,type:unit
```

## Nightly (Deep & Broad)

- Data-heavier custom tests.
- Source freshness checks.
- Snapshot validations.
- End-to-end mart tests.

## Governance

- Broken **schema tests** should be a merge blocker.
- Nightly failures should ping the owning team (using `meta: {owner: "team-analytics"}`).

## Rationale

Running every test on every PR feels "safe" but isn't scalable: it burns time, raises flake risk, and numbs reviewers. The split strategy ensures that PRs get fast, actionable feedback while comprehensive coverage is maintained asynchronously.

## Connections

- Extends [[dbt-testing-patterns]] by adding a strategic dimension (when to run which tests).
- Related to [[dbt-data-contract-implementation]] (contracts as a PR-time guardrail).
- Related to [[dbt-slim-ci]] (testing strategy is Tactic 3 of the five-tactic system).