---
type: entity
title: Data Insights Report
created: 2026-05-14
updated: 2026-05-14
tags: [data-insights, reporting, analytics, governance, openmetadata]
related: [openmetadata-insights, data-insights-application-troubleshooting, cost-analysis, tiers, data-asset-ownership, classification-tags, backfill-configuration, recreate-data-insights-index]
sources: ["data-insights-report-openmetadata-reporting-guide--20260514.md"]
---
# Data Insights Report

The Data Insights Report is a suite of analytical reports within [[openmetadata-insights]] that provides administrators with a quick glance at platform health, data governance coverage, user engagement, and cost efficiency. It is the primary tool for monitoring data ownership, description coverage, data tiering, and platform adoption.

## Report Categories

The Data Insights Report is organized into four sections:

### Data Assets Report
Displays metrics around data assets and organizational health:
- **Total Data Assets** — Count of all data assets broken down by asset type (DatabaseSchema, Database, Dashboard, Chart, Topic, ML Model, etc.).
- **Percentage of Data Assets with Description** — Description coverage by asset type. For Table assets, both table and column descriptions must be filled.
- **Percentage of Data Assets with Owners** — Ownership coverage; excludes assets that do not support ownership assignment.
- **Percentage of Service with Description** — Description coverage broken down by service; supports search filtering.
- **Percentage of Service with Owners** — Ownership coverage broken down by service; supports search filtering.
- **Total Data Assets by Tier** — Breakdown of data assets by [[tiers]]; excludes assets with no tier assigned.

### App Analytics
Tracks user engagement and platform usage:
- **Most Viewed Data Assets** — Top 10 most viewed data assets.
- **Page Views by Data Assets** — Total page views grouped by asset type.
- **Daily Active Users on the Platform** — Users with at least one session per day.
- **Most Active Users** — Users with the highest page views (power users).

### Key Performance Indicators (KPI)
Displays percentage coverage of description and ownership of data assets, driving platform adoption.

### Cost Analysis (OpenMetadata SaaS only)
Available exclusively to OpenMetadata SaaS users. Analyzes used vs. unused assets to measure ROI and eliminate unnecessary costs:
- **Used vs Unused Assets Count** — Identifies which assets are used and which are not.
- **Used vs Unused Assets Size** — Storage size of used vs. unused assets.
- **Used vs Unused Assets Size Percentage** — Size ratio over time.
- **Used vs Unused Assets Count Percentage** — Count ratio over time.
- **Unused Assets** — List of unused assets.
- **Frequently Used Assets** — List of frequently used assets.

## Filtering

All reports can be filtered by **Teams**, **Data Tiers**, and a **Time Filter**.

## Relationship to Other Pages

- [[data-insights-application-troubleshooting]] — Diagnoses display failures; this page describes what the reports should show when working.
- [[backfill-configuration]] — Configuration parameter that processes historical data to populate insights views.
- [[recreate-data-insights-index]] — Application-specific index rebuild toggle for Data Insights data assets.
- [[openmetadata-insights]] — Parent concept page for all analytics and reporting capabilities.