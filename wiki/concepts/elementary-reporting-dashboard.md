---
type: concept
title: Elementary Reporting Dashboard
created: 2026-04-29
updated: 2026-04-29
tags: [dbt, observability, dashboard, visualization]
related: [elementary-dbt-package, elementary-slack-alerts, elementary-anomaly-detection-configuration]
sources: ["Elementary on dbt — An Overview.md"]
---
# Elementary Reporting Dashboard

The Elementary Reporting Dashboard is a feature of the [[elementary-dbt-package]] that provides an auto-generated, code-free visualization of dbt test failures and anomalies. It is generated as a single `index.html` file by running the command `edr report`.

## Key Features

- **No-Code Generation**: The dashboard is created entirely without manual coding — a single CLI command produces the full report.
- **Test Failure Visualization**: Shows failing tests with details, including anomaly detection test results.
- **Anomaly Detection Charts**: Visualizes row count trends over time, highlighting deviations that triggered anomaly detection tests.
- **Historical View**: Provides a timeline of test results for trend analysis.

## Limitations

- **Hosting Friction**: Serving the `index.html` file to a secure website is described as "tricky" by the author.
- **Paid Version**: Elementary offers a paid version that handles hosting for the dashboard.
- **No Authentication**: The free version's dashboard has no built-in authentication or access control.

## Relationship to Existing Wiki

This concept adds a concrete dashboard implementation to the wiki's coverage of [[dbt-observability-implementation]]. It provides a practical alternative to building custom dashboards in tools like Data Studio (which the Tempus team previously used).