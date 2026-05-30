---
type: concept
title: Data Insights Application Troubleshooting
created: 2026-05-14
updated: 2026-05-14
tags: [data-insights, troubleshooting, administration, openmetadata]
related: [openmetadata-insights, reindexing-search, openmetadata-administration, backfill-configuration, recreate-data-insights-index]
sources: ["resolving-data-insights-and-kpi-display-issues-in--20260514.md"]
---
# Data Insights Application Troubleshooting

A diagnostic workflow for resolving four specific symptom patterns in the OpenMetadata Data Insights Application: empty insights menu results, missing KPI charts, reports showing no data, and time-filter failures (e.g., filtering by "Yesterday" or "Last 3 Days" yields no results).

## The Three-Step Resolution Path

### 1. Verify Data Insights Application Installation
Data Insights is an installable application within OpenMetadata, not a pre-enabled core feature. Navigate to **Settings > Applications** and confirm that the Data Insights Application is listed. If absent, click **Add Apps** and install it. This is the most commonly missed prerequisite.

### 2. Run the Data Insights Application
Once installed, click **Configure** to set parameters, **Schedule** to define execution timing, and **Run Now** to execute the workflow immediately. Without an initial execution, no data will populate the insights views.

### 3. Enable Backfill and Recreate Index Options
During configuration, two critical toggles must be enabled:
- **Backfill Configuration** — Processes historical data to populate insights that would otherwise only show forward-looking data from the point of installation onward.
- **Recreate DataInsights DataAssets Index** — Rebuilds the application-specific search index used for rendering charts and reports. This is distinct from the general [[reindexing-search]] operation and targets only the Data Insights data assets.

## Relationship to Other Concepts

This troubleshooting workflow extends the [[openmetadata-insights]] feature documentation with operational resolution steps. The **Recreate DataInsights DataAssets Index** toggle is an application-specific index rebuild, lighter in scope than the full [[reindexing-search]] operation documented elsewhere, though its performance impact in production environments warrants consideration. The entire workflow falls under the administrative capabilities covered in [[openmetadata-administration]].

## Common Root Causes

- **Missing installation** — The Data Insights Application was never added via Settings > Applications.
- **No initial execution** — The application is installed but has never been run.
- **Missing backfill** — Historical data is unavailable because Backfill Configuration was not enabled.
- **Stale index** — The DataInsights DataAssets Index is corrupted or out of date, requiring recreation.
