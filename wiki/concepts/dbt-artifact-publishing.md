---
type: concept
title: dbt Artifact Publishing
created: 2026-04-04
updated: 2026-04-04
tags: [dbt, ci-cd, artifacts, data-engineering]
related: [dbt-slim-ci, dbt-state-aware-selectors, dbt-ci-testing-strategy, dbt-artifacts, ci-cd-for-data-pipelines]
sources: ["dbt Slim CI Tactics for Large Repos.md"]
---
# dbt Artifact Publishing

The practice of treating dbt artifacts (manifest.json, run_results.json, catalog.json) as first-class citizens in CI/CD pipelines. Artifacts are published from the main branch after green builds and consumed in PR CI for state-aware selection, deferral, and PR summaries.

## Workflow

1. **Publish:** After a successful build on the main branch, upload artifacts to a durable location (S3, GCS, or Git LFS).
2. **Consume:** In PR CI, fetch the latest artifacts via `--state` for slim selection and deferral.
3. **Summarize:** Use `run_results.json` to render PR summaries (e.g., "3 models changed, 7 tests executed, 0 failures").

## Example (GitHub Actions)

```yaml
# .github/workflows/dbt-ci.yml
jobs:
  slim-ci:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: "3.11" }
      - run: pip install dbt-core dbt-bigquery
      - name: Fetch state artifacts
        run: aws s3 cp s3://artifacts/dbt/main/last_success ./state/ --recursive
      - name: dbt Slim CI
        run: |
          dbt deps
          dbt --warn-error --partial-parse --state ./state \
            build --select pr_scope pr_tests --target ci
      - name: Upload PR summary
        if: always()
        run: python ./.ci/render_summary.py  # reads run_results.json
```

## Key Benefits

- **Sub-minute planning:** Partial parse combined with state artifacts makes DAG planning near-instant for large repos.
- **Accurate deferral:** CI can reuse prod relations for unchanged models, avoiding unnecessary recomputation.
- **PR context:** Reviewers get a clear summary of what changed and what was tested.

## Guardrails

- **Stale state check:** Verify artifact freshness before deferral (e.g., fail if artifacts are older than 6 hours).
- **Ephemeral CI schemas:** Destroy CI schemas on job completion or via a nightly janitor job.
- **Consistent naming:** Use a schema naming convention (e.g., `ci_${GITHUB_RUN_NUMBER}`) to avoid collisions.