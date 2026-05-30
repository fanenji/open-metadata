---
type: source
title: "Resolving Data Insights and KPI Display Issues in OpenMetadata"
created: 2026-05-14
updated: 2026-05-14
tags: [data-insights, troubleshooting, administration, openmetadata]
related: [openmetadata-insights, reindexing-search, openmetadata-administration, data-insights-application-troubleshooting]
sources: ["resolving-data-insights-and-kpi-display-issues-in--20260514.md"]
authors: ["OpenMetadata Documentation Team"]
year: 2026
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/admin-guide/data-insights"
venue: "OpenMetadata Official Documentation v1.12.x"
---
# Resolving Data Insights and KPI Display Issues in OpenMetadata

Official troubleshooting guide from the OpenMetadata v1.12.x Administration documentation. This source provides a three-step diagnostic workflow for resolving four common Data Insights display failures: empty insights menu results, missing KPI charts, reports showing no data, and time-filter failures (e.g., "Yesterday" or "Last 3 Days" returning no results).

The resolution path consists of: (1) verifying that the Data Insights Application is installed under Settings > Applications, (2) running the application with appropriate configuration and scheduling, and (3) enabling two critical toggles — **Backfill Configuration** (to process historical data) and **Recreate DataInsights DataAssets Index** (to rebuild the rendering index). This source establishes that Data Insights is an installable application module, not a pre-enabled core feature, and introduces the concept of application-specific index recreation distinct from general search reindexing.
