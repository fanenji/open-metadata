---
type: concept
title: Metric Lineage
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, metrics, data-lineage, data-governance]
related: [metrics, data-lineage, data-quality, openmetadata-features]
sources: ["metrics-for-openmetadata---openmetadata-documentat-20260514.md"]
---

# Metric Lineage

**Metric Lineage** extends the general [[data-lineage]] concept in [[OpenMetadata]] to include metrics as first-class lineage nodes. It provides end-to-end traceability from raw data sources to business metric reporting.

## Typical Lineage Path

A typical metric lineage follows the pattern:

**Database Table → Metric → Pipeline → Dashboard**

This means:
- A **Database Table** provides the raw data.
- A **Metric** is calculated from that data using a formula or SQL query.
- A **Pipeline** processes or transforms the data for the metric.
- A **Dashboard** visualizes the metric for reporting.

## Capabilities

- **Traceability**: Users can view associated tables, pipelines, and dashboards to understand how metrics are generated and utilized.
- **Dependency Mapping**: Metrics can be linked to other metrics, creating a dependency graph.
- **Impact Analysis**: When a source table changes, the lineage shows which metrics and dashboards are affected.

## Relationship to General Lineage

Metric lineage is a specialized form of [[data-lineage]]. While general lineage tracks data movement and transformation across the entire data estate, metric lineage focuses specifically on the path from raw data to business metrics. This distinction is important for governance teams that need to certify and audit metric definitions.

## Best Practices

- Always associate metrics with source tables and pipelines for complete traceability.
- Document the formula or SQL query used for each metric in the metric definition.
- Review metric lineage when source schemas change to identify impacted reports.