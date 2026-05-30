---
type: concept
title: Backfill Configuration
created: 2026-05-14
updated: 2026-05-14
tags: [data-insights, configuration, openmetadata]
related: [data-insights-application-troubleshooting, openmetadata-insights, recreate-data-insights-index]
sources: ["resolving-data-insights-and-kpi-display-issues-in--20260514.md"]
---
# Backfill Configuration

A configuration parameter within the Data Insights Application that, when enabled, processes historical data to populate insights views. Without backfill, the Data Insights Application only captures data from the point of its first successful execution forward, leaving historical periods empty in charts, KPIs, and reports.

## Role in Troubleshooting

Enabling Backfill Configuration is the third step in the [[data-insights-application-troubleshooting]] workflow. It is one of two critical toggles (alongside [[recreate-data-insights-index|Recreate DataInsights DataAssets Index]]) that differentiate a partially functional installation from full resolution. When users report that reports show no data or time-based filters like "Yesterday" or "Last 3 Days" return no results, missing backfill is a likely cause.

## Considerations

- Backfill processes all available historical metadata, which may increase the initial execution time of the Data Insights Application.
- The feature requires that metadata ingestion has already populated the platform with historical data; backfill cannot create data that was never ingested.
- In production environments, the resource impact of backfill should be assessed before enabling it during peak usage periods.
