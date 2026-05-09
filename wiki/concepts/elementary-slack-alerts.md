---
type: concept
title: Elementary Slack Alerts
created: 2026-04-29
updated: 2026-04-29
tags: [dbt, observability, alerting, slack]
related: [elementary-dbt-package, dbt-observability-implementation, elementary-anomaly-detection-configuration, elementary-reporting-dashboard]
sources: ["Elementary on dbt — An Overview.md"]
---
# Elementary Slack Alerts

Elementary Slack Alerts is a feature of the [[elementary-dbt-package]] that provides real-time notification of dbt test failures and anomalies directly to Slack channels. According to Noah Kennedy's article "[[Elementary on dbt: An Overview]]", the integration can be set up in under an hour by following Elementary's official guide.

## Key Features

- **User Tagging**: Tests can @mention specific users or groups (owners/subscribers) when they fail.
- **Persistent Alerts**: Alerts continue until the issue is resolved or the test is turned off.
- **Rich Context**: Each alert includes test description, relevant tags, and owner information.
- **Anomaly Detection Alerts**: Volume anomaly detection failures are also reported through Slack.

## Comparison with Custom Solutions

Before Elementary, the Tempus team used a custom solution involving regex parsing of dbt logs via an entrypoint script and a custom Slack app. Elementary provides a more advanced, easier-to-set-up alternative that requires no custom scripting.

## Relationship to Existing Wiki

This concept extends [[dbt-observability-implementation]], which describes the on-run-end hook pattern for monitoring. Elementary Slack Alerts provide a concrete, production-ready implementation of that pattern with richer features (user tagging, persistent alerts, anomaly integration).