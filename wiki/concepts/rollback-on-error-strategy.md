---
type: concept
title: Rollback on Error Strategy
created: 2026-01-30
updated: 2026-01-30
tags: [ci-cd, data-pipeline, error-handling, rollback]
related: [source-downstream-validation-gap, dual-pipeline-strategy, branch-based-ingestion-pattern, data-contract-versioning-strategy]
sources: ["Problema PDS - VDS (Anastasia).md"]
---
# Rollback on Error Strategy

An operational pattern for mitigating the [[source-downstream-validation-gap]] by reverting downstream View/Data Sources (VDS) to the last known valid tag when errors are detected.

## How It Works

1. A change to the Primary Data Source (PDS) propagates downstream.
2. If an error is detected in a VDS, the system automatically rolls back that VDS to its last valid tagged version.
3. The rollback restores downstream consumers to a known-good state while the source issue is investigated.

## Advantages

- Provides rapid recovery for downstream consumers.
- Minimizes the blast radius of problematic source changes.
- Leverages existing versioning mechanisms (e.g., [[data-contract-versioning-strategy]]).

## Considerations

- Requires a robust versioning and tagging system for downstream data products.
- Rollback may cause data loss if the VDS has been updated with additional data since the last valid tag.
- Does not prevent the problem — it only mitigates the impact after detection.