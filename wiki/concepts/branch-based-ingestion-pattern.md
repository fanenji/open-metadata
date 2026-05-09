---
type: concept
title: Branch-Based Ingestion Pattern
created: 2026-01-30
updated: 2026-01-30
tags: [ci-cd, data-pipeline, git-pattern, isolation]
related: [source-downstream-validation-gap, dual-pipeline-strategy, rollback-on-error-strategy, ci-cd-for-data-pipelines, dbt-git-branching-strategies]
sources: ["Problema PDS - VDS (Anastasia).md"]
---
# Branch-Based Ingestion Pattern

An operational pattern for mitigating the [[source-downstream-validation-gap]] by isolating changes to the Primary Data Source (PDS) on a dedicated "ingestion" branch. The changes are merged to the main branch only after validation is complete.

## How It Works

1. Changes to the PDS are applied on a branch named `ingestion` (or similar).
2. The ingestion branch is processed and validated independently.
3. Only after successful validation is the ingestion branch merged into the main branch.
4. Downstream consumers (VDS) read from the main branch, which always contains validated data.

## Advantages

- Provides full isolation between unvalidated and validated data.
- Prevents problematic changes from ever reaching downstream consumers.
- Aligns with Git-based branching strategies used in [[dbt-git-branching-strategies]] and [[CI-CD-for-data-pipelines]].

## Considerations

- Requires infrastructure to support branching at the data level (e.g., [[nessie-catalog-versioning]], [[iceberg-table-versioning]], or [[lakefs-file-versioning]]).
- Adds complexity to the ingestion workflow.
- May introduce latency between source change and availability to consumers.