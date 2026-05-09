---
type: concept
title: dbt Core Slim CI Implementation
created: 2026-04-29
updated: 2026-04-29
tags: [dbt, ci-cd, slim-ci, dbt-core, state-processing]
related: [dbt-slim-ci, dbt-state-aware-selectors, dbt-artifacts, dbt-ci-testing-strategy, paul-fry, dbt-checkpoint, sqlfluff-dbt-integration, data-diff-dbt]
sources: ["How to Create CI-CD Pipelines for dbt Core.md"]
---
# dbt Core Slim CI Implementation

A 4-step process for replicating dbt Cloud's "Slim CI" job pattern in dbt Core using state processing. This pattern enables CI/CD pipelines to run only modified dbt models when a pull request is created, reducing runtime and cost.

## The 4-Step Process

### Step 1: Generate Main Branch Manifest
Run `dbt compile --target-path=prod-run-artifacts` on the main/master branch to produce a `manifest.json` file.

### Step 2: Push Manifest to Git
Push the `manifest.json` file from `prod-run-artifacts` to the main branch of the Git repository. This makes it available for comparison in CI/CD jobs.

### Step 3: Generate Feature Branch Manifest
In the CI/CD job, run `dbt compile` on the feature branch to generate a second `manifest.json`.

### Step 4: Apply State Processing
Use the `defer` and `state` flags to identify and run only modified models:
```bash
dbt run --select state:modified+ --defer --state=prod-run-artifacts
```

## Known Limitations

- The `--defer` flag is not available for `dbt ls`, contradicting some code examples.
- Pushing manifest.json to the main branch requires rebasing feature branches, creating operational overhead.
- The manifest storage strategy in Git is not fully addressed by the original guide.

## Enhancement Candidates

1. **SQLFluff** — Incremental linting with `diff-quality`.
2. **Git Standards Enforcement** — Branch naming convention validation.
3. **dbt-checkpoint** (High-Value) — Verifies data quality tests are set.
4. **data-diff** — Row count comparison between table versions.

## Related

- [[dbt-slim-ci]] — The broader Slim CI concept this implementation operationalizes.
- [[dbt-state-aware-selectors]] — The `state:modified` selector used in this pattern.
- [[dbt-artifacts]] — The manifest files that enable state comparison.
- [[dbt-ci-testing-strategy]] — Broader testing strategy for dbt CI/CD.
- [[paul-fry]] — The author who documented this implementation.