---
type: concept
title: Email Report Configuration
created: 2026-05-14
updated: 2026-05-14
tags: [data-insights, email-report, configuration, scheduling]
related: [data-insights-email-report, openmetadata-insights, application-framework, data-insights-ingestion]
sources: ["configure-the-data-insights-report---openmetadata--20260514.md"]
---
# Email Report Configuration

Email Report Configuration is the process of installing, authorizing, and scheduling the [[data-insights-email-report]] application to send periodic email summaries of data insights to Administrators and Teams. It is a feature of the [[application-framework]] and depends on [[data-insights-ingestion]] being operational.

## Steps

1. Navigate to **Settings >> Applications >> Add Apps**.
2. Install the Data Insights Report application.
3. Authorize the application.
4. Select recipients: Admins, Teams, or both.
5. Set the desired frequency for email delivery.
6. Submit to activate the report.

## Post-Configuration

- The schedule and recipient list can be modified at any time.
- A history view shows when the report was last sent.

## Prerequisites

- [[data-insights-ingestion]] must be set up and running. Without it, the report will have no data to distribute.

## Related Concepts

- [[scheduled-distribution]] — The general pattern of distributing reports on a recurring schedule.
- [[application-framework]] — The pluggable system that hosts the Data Insights Report application.