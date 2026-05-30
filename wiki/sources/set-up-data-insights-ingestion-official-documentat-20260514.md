---
type: source
title: Set Up Data Insights Ingestion | Official Documentation - OpenMetadata Documentation
created: 2026-05-14
updated: 2026-05-14
tags: [data-insights, ingestion, application-framework, admin]
related: [data-insights-ingestion-setup, data-insights-application-troubleshooting, application-framework, openmetadata-insights, backfill-configuration]
sources: ["set-up-data-insights-ingestion-official-documentat-20260514.md"]
---
# Set Up Data Insights Ingestion

This source is the official OpenMetadata v1.12.x documentation for setting up the Data Insights ingestion pipeline. It provides a step-by-step UI-driven procedure for Admin users to install, configure, and schedule the Data Insights application via the Application Framework (Settings → Applications).

## Key Content

- **Admin-only operation:** Only users with Admin privileges can install and configure the Data Insights application.
- **UI navigation path:** Settings >> Applications → Add Apps → Data Insights → Install → Configure → Schedule → Submit.
- **Batch size configuration:** Adjustable parameter within the application settings to control processing granularity.
- **Schedule execution (UTC):** Daily schedule; recommended to run overnight or during low-activity periods for accuracy.
- **On-demand execution:** The ingestion pipeline can be triggered manually via "Run now."
- **Recent Runs tab:** Provides visibility into ingestion execution history and status.
- **24-hour data delay:** On fresh deployments, App Analytics data may not be present immediately because it is fetched from the previous day (UTC).

## Connections

- Directly provides the correct setup procedure for [[data-insights-application-troubleshooting]].
- Data Insights is an application installed via the [[application-framework]].
- Contributes to the broader [[openmetadata-insights]] concept.
- The 24-hour data delay connects to [[backfill-configuration]] needs for historical data.