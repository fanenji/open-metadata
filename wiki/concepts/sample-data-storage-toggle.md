---
type: concept
title: Sample Data Storage Toggle
created: 2026-05-14
updated: 2026-05-14
tags: [auto-classification, configuration, sample-data, privacy, performance]
related: [auto-classification, pii-sample-data-masking, metadata-agent]
sources: ["adding-auto-classification-workflow-through-ui---o-20260514.md"]
---
# Sample Data Storage Toggle

The Sample Data Storage Toggle is a configuration option within the [[auto-classification|Auto Classification Agent]] that controls whether sample data is ingested during scheduled classification runs. It is enabled by default.

## Purpose

When enabled, the agent retrieves sample data from the target database to analyze content for sensitive patterns (e.g., PII detection). This analysis informs which [[classification-tags|classification tags]] the agent applies.

## When to Disable

- **Privacy concerns**: Sample data may contain sensitive values that should not be stored or processed by the agent.
- **Performance optimization**: Skipping sample data ingestion reduces the load on the source database and the agent's processing time.
- **Known schema**: If classification rules are based solely on column names or types rather than content analysis, sample data may be unnecessary.

## Relationship to PII Masking

Once auto-classification applies tags like `PII.Sensitive`, the [[pii-sample-data-masking|PII sample data masking]] behavior is triggered in the UI, replacing displayed sample values with `******`. The sample data storage toggle controls whether the agent *ingests* sample data for analysis; PII masking controls whether ingested sample data is *displayed* in the UI.