---
type: concept
title: Usage Pipeline
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, usage, analytics, pipeline]
related: [service-insights, data-insights-pipeline, metadata-ingestion-workflow]
sources: ["service-insights-overview-official-documentation---20260514.md"]
---
# Usage Pipeline

The Usage Pipeline is a pipeline in OpenMetadata that tracks data asset usage and query execution costs. It is a prerequisite for the [[service-insights|Service Insights]] "Most Used Data Assets" and "Most Expensive Queries" charts.

## Purpose

The Usage Pipeline collects data on how frequently data assets are accessed and the cost of query execution. This information is used to populate usage analytics in Service Insights, enabling users to identify the most popular and most expensive data assets within a service.

## Connector Dependency

The "Most Expensive Queries" chart is connector-dependent — not all connectors support extracting query cost. Users must verify that their connector supports this feature for the chart to display data.

## Relationship to Other Pipelines

The Usage Pipeline is distinct from the [[metadata-ingestion-workflow|Metadata Ingestion Pipeline]] and the [[data-insights-pipeline|Data Insights Pipeline]]. It is a specialized pipeline focused solely on usage tracking.