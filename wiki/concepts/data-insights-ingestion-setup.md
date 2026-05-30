---
type: concept
title: Data Insights Ingestion Setup
created: 2026-05-14
updated: 2026-05-14
tags: [data-insights, ingestion, application-framework, admin, scheduling]
related: [data-insights-application-troubleshooting, application-framework, openmetadata-insights, backfill-configuration, openmetadata-administration]
sources: ["set-up-data-insights-ingestion-official-documentat-20260514.md"]
---
# Data Insights Ingestion Setup

Data Insights Ingestion is the process of installing, configuring, and scheduling the Data Insights application within OpenMetadata to generate platform analytics and reports. It is a scheduled daily workflow accessible only to Admin users via the Application Framework.

## Prerequisites

- **Admin role:** Only users with Admin privileges can perform this setup.
- **Application Framework:** The Data Insights application is installed through Settings → Applications.

## Setup Procedure

1. Navigate to **Settings >> Applications**.
2. If the Data Insights application does not appear, click **Add Apps**.
3. Click **Read more** for the Data Insights application.
4. Click **Install** to install the Data Insights application.
5. Click **Configure** to adjust the batch size and other settings according to specific requirements.
6. Click **Schedule** to authorize the Data Insights app.
7. Choose a schedule execution time (displayed in UTC). The workflow runs daily. It is recommended to run overnight or when platform activity is at its lowest to ensure accurate data.
8. Click **Submit** to complete installation.

## Post-Installation

- Click **Configure** to view the installed application details.
- Click **Run now** to trigger the ingestion pipeline on demand.
- The ingestion schedule can be edited after installation.
- The **Recent Runs** tab provides visibility into execution history and status.

## Important Caveats

- **24-hour data delay:** On fresh deployments, App Analytics data may not be present immediately. Data is fetched from the previous day (UTC), meaning there is a natural delay before reports populate.
- **Admin-only restriction:** Non-Admin users cannot self-service this setup.
- **Overnight scheduling:** Running during low-activity periods is recommended for accuracy, suggesting the ingestion may be resource-intensive or depend on a complete day's data.

## Troubleshooting

If Data Insights reports are not displaying after setup, refer to [[data-insights-application-troubleshooting]] for diagnostic steps. The first step should always be to verify that the setup procedure was completed correctly.

## Related Concepts

- [[application-framework]] — The pluggable system through which Data Insights is installed.
- [[openmetadata-insights]] — Broader analytics and reporting capabilities.
- [[backfill-configuration]] — Configuration for processing historical data to populate insights views.
- [[openmetadata-administration]] — Overview of administrative capabilities, including Data Insights.