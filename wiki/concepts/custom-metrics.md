---
type: concept
title: Custom Metrics
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, data-profiling, data-quality, custom-metrics]
related: [custom-metrics, data-profiling, data-quality, profiler-agent, metadata-agent, data-observability-alerts]
sources: ["custom-metrics---openmetadata-documentation-20260514.md"]
---
# Custom Metrics

**Custom Metrics** is a concept in [[OpenMetadata]] that extends the [[data-profiling]] framework by allowing users to define and compute business-specific metrics using custom SQL queries. This capability bridges the gap between system-provided profiling metrics and domain-specific analytical needs.

## Why It Matters

Built-in profiler metrics cover common data quality dimensions (null counts, distinct values, min/max, etc.), but organizations often require metrics aligned with their specific business logic. Custom metrics fill this gap by enabling:

- **Domain-specific KPIs:** Track metrics like "percentage of orders with delayed shipping" or "number of records with invalid country codes."
- **Tailored data quality checks:** Define quality thresholds that match business rules rather than generic statistical measures.
- **Enhanced visibility:** Display computed values alongside system metrics in table and column profiles for a unified view.

## Relationship to Other Concepts

- **[[data-profiling]]:** Custom metrics are an extension point within the profiling workflow, executed by the [[profiler-agent]].
- **[[data-quality]]:** Custom metrics can serve as domain-specific quality checks, complementing the built-in data quality test framework.
- **[[metadata-agent]]:** The Profiler Agent is a specialized type of metadata agent that runs profiling workflows, including custom metrics.
- **[[data-observability-alerts]]:** Custom metrics values can inform alerting thresholds, though this integration is not explicitly documented.

## Best Practices

- Use meaningful names that describe the business purpose of the metric.
- Test SQL queries for performance and correctness before adding them to production profiling workflows.
- Consider the impact of schema changes on custom metric queries; they may need to be updated when table structures change.
- For column-level metrics, ensure the selected column exists and the query is scoped appropriately.

## Open Questions

- What SQL syntax is supported? (Standard SQL? Dialect-specific?)
- Are there performance or security guardrails for custom SQL queries?
- Can custom metrics be reused across multiple tables/columns or shared between users?
- How are custom metrics handled during re-profiling or schema changes?