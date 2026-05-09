---
type: concept
title: Data Quality Resolution Workflow
created: 2026-04-08
updated: 2026-04-08
tags: [data-quality, observability, workflow]
related: [openmetadata-data-quality, data-observability-definition, data-contract-observability]
sources: ["Data Quality  OpenMetadata Quality Management Guide.md"]
---
# Data Quality Resolution Workflow

A data quality resolution workflow is a process that closes the feedback loop on data quality issues by informing data consumers when a test failure has been investigated and resolved. This concept extends beyond any single tool and represents a best practice for operational data quality management.

## Key Elements

1. **Detection** — A data quality test fails, triggering an alert.
2. **Notification** — Relevant stakeholders (data producers, owners, governance teams) are informed.
3. **Investigation** — Root cause analysis is performed to understand why the test failed.
4. **Remediation** — The underlying data issue is fixed (e.g., pipeline bug, source system error, schema change).
5. **Resolution Communication** — Data consumers are explicitly notified that the issue is resolved and the data can be trusted again.

## Importance

Without a resolution workflow, data consumers may continue to distrust data long after a quality issue has been fixed. The workflow ensures that trust is actively restored, not passively assumed. This is particularly important in [[data-mesh]] architectures where data is treated as a product and consumers rely on clear quality signals.

## Implementation Patterns

- **Manual workflow** — A human investigates the failure, fixes the issue, and manually marks the test as resolved in a dashboard or catalog.
- **Automated workflow** — A CI/CD pipeline or orchestration system automatically re-runs the test after a fix is deployed and notifies consumers upon success.
- **Integrated workflow** — The resolution workflow is embedded in a [[data-contract-platform]] or [[openmetadata-data-quality]] system, providing a single interface for detection, investigation, and resolution communication.

## Relationship to Data Observability

The resolution workflow can be considered an eighth dimension of [[data-observability-definition]], extending the traditional seven dimensions (freshness, security, redundancy, discrepancy, documentation, quality, lineage) by adding the feedback loop that restores trust after a quality incident.