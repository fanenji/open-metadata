---
type: entity
title: Usage Metrics
created: 2026-05-14
updated: 2026-05-14
tags: [usage, metrics, data-discovery, openmetadata]
related: [data-discovery, data-profiling, tiers, advanced-search]
sources: ["how-to-discover-assets-of-interest---openmetadata--20260514.md"]
---

# Usage Metrics

Usage Metrics in OpenMetadata capture how data consumers are using data assets. These metrics are computed during metadata and profiler ingestion, and are used to power sorting and filtering options in the data discovery interface.

## Key Metrics

- **Last Updated**: Filter data by recent updates and changes.
- **Weekly Usage**: Based on data asset usage metrics captured during ingestion.
- **Relevance**: A sorting criterion that prioritizes assets based on usage patterns.

## Role in Data Discovery

Usage Metrics enable users to filter and sort search results by importance and activity. They are accessible via the quick filter dropdown on the Explore page, where users can sort by ascending or descending order.

## Relationship to Other Features

- **[[data-profiling]]**: The data profiler captures usage profiles for tables during ingestion, which feed into usage metrics.
- **[[tiers]]**: Tiers provide a manual importance classification; usage metrics provide an automated, activity-based importance signal.
- **[[advanced-search]]**: Usage metrics may be combined with advanced search for more precise discovery.

## Open Questions

- How is "Weekly Usage" computed? Is it from profiler runs, query history, or both?
- What is the "Relevance" sorting algorithm based on?
- Are usage metrics available for non-table assets (dashboards, pipelines, etc.)?