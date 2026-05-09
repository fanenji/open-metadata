---
type: concept
title: Data Contract Observability
created: 2026-04-04
updated: 2026-04-04
tags: [data-contracts, observability, data-quality, governance]
related: [data-contract-platform, great-expectations-for-data-contracts, data-contract-versioning-strategy]
sources: ["Data Contract Enforcement Ensuring Reliability in Distributed Pipelines.md"]
---
# Data Contract Observability

The practice of tracking data contract violations and compliance metrics through a dedicated dashboard. This enables teams to identify problematic datasets and focus data quality improvement efforts at the source.

## Implementation Pattern

Violations detected during contract validation are logged to a persistent store (e.g., DynamoDB) with metadata including timestamp, dataset name, violation count, and status. A visualization tool (e.g., AWS QuickSight) renders this data into a dashboard.

## Key Metrics

- **Violation count per dataset**: Identifies which datasets frequently violate contracts.
- **Violation trend over time**: Shows whether data quality is improving or degrading.
- **Compliance rate**: Percentage of batches that pass contract validation.
- **Status distribution**: Breakdown of datasets by status (healthy, warning, critical).

## Role in Data Contract Platform

Observability closes the feedback loop in [[data-contract-platform]]. Without visibility into violations, teams cannot prioritize improvements or hold producers accountable for data quality.
