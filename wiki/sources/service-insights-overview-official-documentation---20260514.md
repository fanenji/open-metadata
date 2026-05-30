---
type: source
title: Service Insights Overview | Official Documentation
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, data-insights, service-insights, documentation]
related: [service-insights, data-insights-pipeline, metadata-ingestion-workflow, auto-classification, auto-tiering-pipeline, data-quality, usage-pipeline, openmetadata-ai-application]
sources: ["service-insights-overview-official-documentation---20260514.md"]
authors: [OpenMetadata]
year: 2026
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/data-insights/service-insights"
venue: "OpenMetadata Documentation"
---
# Service Insights Overview | Official Documentation

This source is the official OpenMetadata v1.12.x documentation page for the Service Insights feature. It provides a comprehensive guide to the Service Insights tab, which displays per-service analytics across 11 charts and tables. The documentation covers the purpose of each chart, the prerequisite pipelines required for data to appear, and basic troubleshooting steps when charts show no data.

The source details the following charts and tables: Total Data Assets, Description Coverage, PII Coverage, Tier Coverage, Ownership Coverage, Generated Data with OpenMetadata AI, PII Distribution, Tier Distribution, Most Used Data Assets, Most Expensive Queries, and Data Quality. For each, it specifies the exact pipelines that must be successfully executed for data to be displayed.

Key insights from this source include the service-level granularity of insights (distinct from the global Data Insights report), the dependency on multiple specialized pipelines (Auto Classification, Auto Tiering, Usage, Data Quality), and the connector-dependent nature of the "Most Expensive Queries" chart. The source also introduces the concept of tracking AI-generated metadata separately from manually created metadata.