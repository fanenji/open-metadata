---
type: concept
title: Scheduled Distribution
created: 2026-05-14
updated: 2026-05-14
tags: [scheduling, distribution, email, reporting]
related: [data-insights-email-report, email-report-configuration, openmetadata-insights]
sources: ["configure-the-data-insights-report---openmetadata--20260514.md"]
---
# Scheduled Distribution

Scheduled Distribution is the mechanism by which the [[data-insights-email-report]] delivers periodic email summaries to configured recipients. It is a core feature of the [[email-report-configuration]] process.

## Characteristics

- **Frequency**: Configurable to a desired schedule (e.g., daily, weekly).
- **Recipients**: Can be Administrators, Teams, or both.
- **Trigger**: The report is sent automatically based on the configured schedule.

## Relationship to OpenMetadata

- The Data Insights Report uses scheduled distribution to deliver insights data to stakeholders without requiring manual access to the platform.
- It is part of the broader [[openmetadata-insights]] ecosystem.

## Open Questions

- What are the exact frequency options available?
- Is there a minimum interval between distributions?
- How is the distribution time determined (e.g., time of day)?