---
type: concept
title: dbt Slim CI
created: 2026-04-04
updated: 2026-04-04
tags: [dbt, ci-cd, testing, data-engineering]
related: [dbt-state-aware-selectors, dbt-artifact-publishing, dbt-ci-testing-strategy, ci-cd-for-data-pipelines, dbt-data-contract-implementation, dbt-preflight-validation, dbt-artifacts, neurobyte]
sources: ["dbt Slim CI Tactics for Large Repos.md"]
---
# dbt Slim CI

A CI/CD strategy for dbt projects that runs only changed models and their dependencies, rather than performing full builds on every pull request. Slim CI is essential for scaling large dbt repositories where full builds become slow, flaky, and wasteful.

## Core Philosophy

Slim CI is a discipline built on five interdependent tactics:

1. **State-Aware Selection** — Use `state:modified+` selectors to capture the blast radius: changed models, their parents (data inputs), and children (consumers).
2. **Smart Deferral to Prod** — Reuse already-built relations from a reference environment so CI does not re-materialize the world. Requires guardrails like stale state checks.
3. **Tests That Matter in PRs** — Run only generic schema tests and contract checks in PRs; defer data-heavy custom tests, source freshness, and snapshot validations to nightly runs.
4. **Partial Parse + Artifact-First Workflows** — Keep planning near-instant by reusing metadata from prior runs. Treat artifacts (manifest.json, run_results.json, catalog.json) as first-class CI citizens.
5. **Hygiene: Contracts, Ownership, and Stale State Guards** — Enforce model contracts where stability matters, add ownership metadata, verify artifact freshness before deferral, and keep CI schemas ephemeral.

## Key Patterns

- **PR Scope Selector:** Combines `state:modified+` with ephemeral model inclusion to capture the smallest complete subgraph.
- **PR Tests Selector:** Intersects `test_type: generic` with `state:modified+` to run only schema tests on the impacted surface.
- **Stale State Guard:** A Python script that checks the age of reference artifacts (e.g., >6 hours) and fails the build if too old.
- **Ephemeral CI Schemas:** CI schemas are destroyed on job completion or by a nightly janitor job to avoid collisions and quota waste.

## Pitfalls

- **Dangling refs:** Deleted models can break selection logic; include parents so failure appears early.
- **Ephemeral surprises:** Ephemeral models folding into different materializations can change performance; include them in `pr_scope`.
- **Snapshot drift:** Snapshots rarely need PR-time runs; validate them nightly unless the PR touches snapshot logic.
- **Seed noise:** Large seeds should gate PR refresh behind labels or a separate job.

## Limitations

- The approach assumes a single-project repo and does not address [[dbt-mesh]] cross-project dependencies.
- No quantitative performance benchmarks are provided in the source.
- The interaction between contract enforcement (Tactic 5a) and generic schema tests (Tactic 3) is not fully clarified.

## Connections

- Strengthens [[CI-CD-for-data-pipelines]] with concrete dbt-specific implementation patterns.
- Extends [[dbt-data-contract-implementation]] by showing contracts as a Slim CI guardrail.
- Related to [[dbt-preflight-validation]] (similar preflight check concept for state freshness).
- Related to [[dbt-artifacts]] (artifact-first workflow directly uses manifest.json, run_results.json).
- Related to [[dbt-testing-patterns]] (PR vs nightly testing split aligns with existing categorization).