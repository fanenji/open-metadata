---
type: entity
title: Data Insights Email Report
created: 2026-05-14
updated: 2026-05-14
tags: [data-insights, email-report, application-framework, reporting]
related: [openmetadata-insights, application-framework, data-insights-application-troubleshooting, data-insights-ingestion]
sources: ["configure-the-data-insights-report---openmetadata--20260514.md"]
---
# Data Insights Email Report

The Data Insights Email Report is an installable application within the [[application-framework]] that distributes scheduled email summaries of data insights to Administrators and Teams. It provides a periodic delivery mechanism for the data collected by [[data-insights-ingestion]].

## Prerequisites

- **Data Insights Ingestion** must be set up and running before configuring the email report. Without this prerequisite, the report will have no data to distribute.

## Configuration

The report is configured via the UI at **Settings >> Applications >> Add Apps**. The setup process involves four steps:

1. **Install** the Data Insights Report application.
2. **Authorize** the application.
3. **Select Recipients**: Choose to send the report to Admins, Teams, or both.
4. **Schedule**: Set the desired frequency for email delivery (e.g., daily, weekly).

After submission, the report is active. The configuration can be modified later to change the schedule or recipient list.

## History

A history view is available after configuration, showing when the report was last sent.

## Relationship to Other Components

- [[openmetadata-insights]] — The email report is a delivery mechanism for the data insights platform.
- [[application-framework]] — The report is installed as a pluggable application via this framework.
- [[data-insights-application-troubleshooting]] — Covers display issues for Data Insights; email report failures may require separate investigation.
- [[backfill-configuration]] — Backfill populates historical insights data; the email report distributes it.

## Open Questions

- What email infrastructure (SMTP, from address) is required?
- Can the report be sent to specific Teams or only all Teams?
- What is the exact content of the email report?
- What happens if the report fails to send (retry logic, error notifications)?
- Is there a way to test the report configuration before scheduling?