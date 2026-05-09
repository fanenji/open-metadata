---
type: concept
title: dbt State-Aware Selectors
created: 2026-04-04
updated: 2026-04-04
tags: [dbt, ci-cd, selectors, testing]
related: [dbt-slim-ci, dbt-artifact-publishing, dbt-ci-testing-strategy, ci-cd-for-data-pipelines]
sources: ["dbt Slim CI Tactics for Large Repos.md"]
---
# dbt State-Aware Selectors

Selectors that use dbt's state comparison mechanism to identify and run only models and tests affected by changes in a pull request. They are the foundation of [[dbt-slim-ci]].

## Core Selectors

### PR Scope Selector
Captures the blast radius of a PR: changed models, their parents (data inputs), and children (consumers), plus ephemeral models.

```yaml
# selectors.yml
selectors:
  - name: pr_scope
    definition:
      union:
        - method: state
          value: modified+       # changed + parents + children
        - method: config.materialized
          value: ephemeral       # allow ephemeral deps to materialize in graphs
    description: "Models impacted by this PR"
```

### PR Tests Selector
Runs only generic schema tests on the impacted surface, keeping PR CI fast and focused.

```yaml
  - name: pr_tests
    definition:
      intersection:
        - method: test_type
          value: generic         # schema tests only (fast, focused)
        - method: state
          value: modified+       # test the impacted surface
```

## Usage

```bash
dbt --warn-error --partial-parse --state target/artifacts \
  build --select pr_scope pr_tests
```

## Key Principles

- **Smallest complete subgraph:** Exercise only the subgraph that could be broken by the PR.
- **Trust the state:** State-aware selection relies on accurate reference artifacts from a known-good environment.
- **Combine with deferral:** Use `--defer` to reuse prod relations for unchanged models, so only the changed slice is recomputed.

## Pitfalls

- **Dangling refs:** If a PR deletes a model, ensure selectors include parents so failure appears early.
- **Ephemeral surprises:** Ephemeral models folding into different materializations can change performance; include them in `pr_scope`.
- **Stale state:** Reference artifacts must be fresh; use a stale state guard (see [[dbt-slim-ci]]) to verify before running.