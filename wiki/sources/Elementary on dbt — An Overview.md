---
type: source
title: "Elementary on dbt: An Overview"
created: 2026-04-29
updated: 2026-04-29
tags: [dbt, observability, elementary, anomaly-detection]
related: [elementary-dbt-package, elementary-slack-alerts, elementary-anomaly-detection-configuration, elementary-reporting-dashboard, dbt-observability-implementation, dbt-anomaly-detection-tests, data-observability-definition]
sources: ["Elementary on dbt — An Overview.md"]
authors: [Noah Kennedy]
year: 2023
url: "https://noahlk.medium.com/elementary-on-dbt-an-overview-5dd038d0d3b8"
venue: Medium
---
# Elementary on dbt: An Overview

This article by Noah Kennedy, a Data Engineer at Meta (formerly Tempus), provides a practical introduction to the [[elementary-dbt-package]], an open-source dbt package for enhancing dbt's observability and alerting capabilities. The author argues that while dbt tests are powerful for catching errors in theory, they lack built-in alerting and observability infrastructure. Elementary addresses these gaps through three main features: Slack alerts, a reporting dashboard, and anomaly detection tests.

The article describes the author's team's experience adopting Elementary at Tempus, a healthcare AI company. Key benefits highlighted include: Slack integration that can be set up in under an hour (replacing a previous custom regex/entrypoint solution), a code-free reporting dashboard generated via the `edr report` command, and YAML-configurable anomaly detection tests that automatically flag row count deviations based on standard deviation thresholds.

The source is anecdotal (single team experience) and from 2023-11. It does not provide benchmarks, comparisons with alternatives like [[dbt-expectations]], or address limitations such as performance overhead, false positive rates, or scalability for large projects. The article notes that serving the dashboard securely is "tricky" and that Elementary offers a paid version for hosted dashboards.