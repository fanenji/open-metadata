---
type: concept
title: dbt + Hex Integration
created: 2026-05-08
updated: 2026-05-08
tags: [dbt, hex, analytics, integration, metadata]
related: [count-co, dbt-cloud, dbt-observability-implementation, hex-egg-table, geospatial-analytics-with-dbt]
sources: ["research-hexegg-table-2026-05-08.md"]
---
# dbt + Hex Integration

The integration between [[dbt]] and [[count-co]]'s Hex analytics platform, enabling the surfacing of dbt metadata, documentation, and test results directly within analytical notebooks. This integration is a key component of the [[hex-egg-table]] pattern, where dbt model descriptions and freshness information are pushed to the warehouse and displayed in Hex's schema browser.

## Key Capabilities

- **Metadata Surfacing**: dbt model descriptions (via `persist_docs`) appear in Hex's schema browser alongside the data.
- **Observability**: dbt Cloud's Metadata API provides freshness and test statuses directly in analytical notebooks.
- **Semantic Layer**: The dbt Semantic Layer integration enables consistent metric definitions across dbt and Hex.

## Relevance to HEX_EGG

In the [[hex-egg-table]] pattern, this integration allows analysts working with H3-aggregated data to see column descriptions, test results, and freshness information without leaving the analytics interface, reducing context switching and improving data trust.