---
type: concept
title: dbt Preflight Validation
created: 2026-05-07
updated: 2026-05-07
tags: [dbt, data-contracts, validation, CI-CD]
related: [dbt-data-contract-implementation, data-contract-platform, CI-CD-for-data-pipelines]
sources: ["dbt and Data Contracts Enabling Reliable, API-Driven Analytics.md"]
---
# dbt Preflight Validation

Preflight validation is a proactive check performed by dbt before materializing a model when a data contract is enforced. dbt compares the contract definition (columns, data types, constraints) against the model's SQL output. If there is a mismatch, the build halts with a clear error message showing side-by-side differences.

## Benefits

- **Early Feedback:** Developers catch schema drift immediately in their dev loop.
- **No Pipeline Pollution:** Prevents incorrect or misaligned data from being written to the warehouse.
- **Clear Error Messages:** Side-by-side diff makes it easy to identify and fix the issue.

## Integration with CI/CD

Preflight validation is naturally integrated into CI/CD pipelines. Running `dbt build` in CI ensures that contract-breaking changes are caught before deployment. This pattern is a core part of [[CI-CD-for-data-pipelines]] for data contracts.