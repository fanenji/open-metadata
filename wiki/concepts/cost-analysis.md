---
type: concept
title: Cost Analysis
created: 2026-05-14
updated: 2026-05-15
tags: [saas, cost-management, data-insights, collate-cloud, cost-analysis, roi, openmetadata]
related: [collate-inc, data-insights-application-troubleshooting, openmetadata-insights, data-insights-report, tiers]
sources: ["OpenMetadata Community Meeting Oct 2023 Release 1 2 0 datamesh openmetadata.md", "data-insights-report-openmetadata-reporting-guide--20260514.md"]
---

# Cost Analysis

Cost Analysis is a SaaS-only feature available in [[collate-inc|Collate Cloud]] (the SaaS offering of [[OpenMetadata]]) introduced in the 1.2.0 release. It extends the [[openmetadata-insights|Data Insights]] capabilities with active data estate management focused on cost optimization by helping administrators measure the return on investment (ROI) of their data initiatives. It analyzes used vs. unused data assets to identify cost-saving opportunities and eliminate unnecessary infrastructure expenses.

## Features

- **Used vs. Unused Asset Count**: Time-series representation of how many assets are actively used versus unused, with filtering by time range. Also available as a percentage ratio (Used vs. Unused Assets Count Percentage).
- **Size Analysis**: Breakdown of used vs. unused assets by data size (Used vs. Unused Assets Size), revealing situations where a small count of unused assets represents a large storage footprint. A percentage ratio (Used vs. Unused Assets Size Percentage) is also provided.
- **Storage Cost Estimation**: Representation of storage costs associated with used and unused assets (planned for a subsequent release).
- **Unused Assets Drill-down**: Detailed lists of unused assets with last access time, size, and storage information, filterable by time range (e.g., "not accessed in last 30 days").
- **Frequently Used Assets**: View of the most actively accessed assets at configurable frequency thresholds.

## Use Case

Data platform administrators can identify unused datasets that are consuming storage and incurring costs, then take action — archiving, deleting, or tagging for review. This transforms the data catalog from a passive inventory into an active cost management tool.

## Availability

Cost Analysis is **exclusively available in Collate Cloud** (the SaaS offering of OpenMetadata). It is not part of the open-source OpenMetadata distribution. The initial release supports Snowflake, with plans to expand to other data sources.

## Relationship to Data Insights

Cost Analysis appears as a new tab within the existing Data Insights section of the UI, alongside the open-source data insights reports. It can also be accessed through the [[data-insights-report]]. See [[data-insights-application-troubleshooting]] for troubleshooting the open-source Data Insights features.

## Open Questions

- The criteria for defining "used" vs. "unused" assets are not specified in the source documentation.
- The data source and refresh cadence for Cost Analysis metrics are not documented.