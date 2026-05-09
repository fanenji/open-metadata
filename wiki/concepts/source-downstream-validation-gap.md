---
type: concept
title: Source-to-Downstream Validation Gap
created: 2026-01-30
updated: 2026-01-30
tags: [data-quality, validation, ci-cd, failure-pattern]
related: [shift-left-data-quality, ci-cd-for-data-pipelines, data-contract-observability, dbt-preflight-validation, data-quality-resolution-workflow, dual-pipeline-strategy, rollback-on-error-strategy, branch-based-ingestion-pattern]
sources: ["Problema PDS - VDS (Anastasia).md"]
---
# Source-to-Downstream Validation Gap

A failure pattern in data pipelines where modifications to a Primary Data Source (PDS) pass all source-level tests but cause downstream View/Data Sources (VDS) to break. This gap demonstrates that source-level testing is necessary but not sufficient for ensuring downstream data quality.

## Description

The validation gap occurs when:
1. A change is made to the upstream data source (PDS).
2. All tests defined on the source pass successfully.
3. The change propagates downstream and breaks consumers (VDS).

This is a classic [[shift-left-data-quality]] failure: moving validation earlier in the pipeline is valuable, but if source tests do not cover downstream impact, the gap remains.

## Proposed Mitigations

Three operational patterns have been proposed to address this gap:

- [[dual-pipeline-strategy]] — Run stage and prod pipelines; promote only after stage validation.
- [[rollback-on-error-strategy]] — Revert downstream to last valid tag on error.
- [[branch-based-ingestion-pattern]] — Isolate PDS changes on an ingestion branch.

## Open Questions

- **Severity:** Is this a frequent, real-world problem or a theoretical edge case?
- **Root Cause:** Do source tests fail to cover downstream semantics, schema evolution, or data content?
- **Solution Selection:** Which mitigation is most appropriate under which conditions?