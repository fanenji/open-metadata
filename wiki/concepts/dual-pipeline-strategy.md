---
type: concept
title: Dual Pipeline Strategy (Stage/Prod)
created: 2026-01-30
updated: 2026-01-30
tags: [ci-cd, data-pipeline, validation, deployment-pattern]
related: [source-downstream-validation-gap, rollback-on-error-strategy, branch-based-ingestion-pattern, ci-cd-for-data-pipelines]
sources: ["Problema PDS - VDS (Anastasia).md"]
---
# Dual Pipeline Strategy (Stage/Prod)

An operational pattern for mitigating the [[source-downstream-validation-gap]] by running two parallel pipelines: a stage pipeline and a production pipeline. Changes are promoted to production only after the stage pipeline passes all validation checks.

## How It Works

1. A change to the Primary Data Source (PDS) triggers the **stage pipeline**.
2. The stage pipeline processes the change and runs comprehensive validation.
3. Only if the stage pipeline succeeds is the change promoted to the **production pipeline**.
4. The production pipeline processes the validated change for downstream consumers (VDS).

## Advantages

- Provides a safety net between source changes and downstream consumption.
- Allows validation of downstream impact before production deployment.
- Compatible with existing [[CI-CD-for-data-pipelines]] workflows.

## Considerations

- Requires double the infrastructure for pipeline execution.
- Adds latency between source change and production availability.
- The stage pipeline must accurately reflect production conditions to be effective.