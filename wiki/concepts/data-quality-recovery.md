---
type: concept
title: Data Quality Recovery
created: 2026-05-08
updated: 2026-05-08
tags: [data-quality, recovery, rollback, iceberg, dbt]
related: [data-quality-score, data-quality-dimensions, iceberg-table-versioning, nessie-catalog-versioning, dbt-slim-ci, dbt-data-contract-implementation, write-audit-publish-pattern, data-incident-management, data-root-cause-analysis, error-recovery-mechanisms]
sources: ["research-error-recovery-mechanisms-2026-05-08.md"]
---
# Data Quality Recovery

Recovery from data quality incidents (bad backfill, corrupted dimension tables, incorrect transformations) is an underserved area in existing tooling. Unlike application deployment rollbacks, data "rollback" often relies on storage-level mechanisms rather than code re-deployment.

## Recovery Mechanisms

- **Iceberg Time Travel:** Query or restore a table to a specific point-in-time snapshot, providing native data-level recovery independent of code deployment.
- **Nessie Branching/Tagging:** Catalog-level branching and tagging for data-level rollback, complementing Iceberg's table-level versioning.
- **dbt State-Based Deployments:** Using `dbt` state-aware selectors to limit blast radius. If a model fails, revert the code and re-run only affected models.
- **Write-Audit-Publish Pattern:** Data is written and audited before being published to the production schema. If validation fails, data is discarded, preventing the need for downstream rollback.

## Prevention as Recovery

The strongest recovery mechanism is prevention. Enforcing [[dbt-data-contract-implementation]] and [[delta-lake-schema-enforcement]] stops schema-breaking or quality-violating changes from entering production.

## Open Questions

- How should recovery mechanisms differ between batch and streaming pipelines?
- Should a contract violation trigger an automatic rollback of the data artifact, or just an alert?
- Is there a pattern for "data canary" — gradually exposing a new data model to consumers and monitoring for quality degradation before full promotion?
