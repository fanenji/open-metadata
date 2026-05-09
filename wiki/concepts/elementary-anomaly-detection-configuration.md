---
type: concept
title: Elementary Anomaly Detection Configuration
created: 2026-04-29
updated: 2026-04-29
tags: [dbt, testing, anomaly-detection, configuration]
related: [elementary-dbt-package, dbt-anomaly-detection-tests, elementary-slack-alerts]
sources: ["Elementary on dbt — An Overview.md"]
---
# Elementary Anomaly Detection Configuration

Elementary Anomaly Detection Configuration refers to the YAML-based test definition parameters for the [[elementary-dbt-package]]'s volume anomaly detection tests. These tests automatically flag row count deviations based on configurable statistical thresholds.

## Configuration Parameters

- **Sensitivity**: Controls the number of standard deviations used as the threshold. A setting of 1 standard deviation is described as "hyper-sensitive."
- **Bucketing**: Allows grouping data by time periods (e.g., weekly) for calculating standard deviations.
- **Direction**: Specifies whether to flag only positive deviations, only negative deviations, or both.
- **Training Window**: Controls how much historical data is used to calculate the baseline standard deviation (e.g., one week's worth of data).

## Example YAML

```yaml
version: 2

models:
  - name: my_model
    tests:
      - elementary.volume_anomalies:
          sensitivity: 2
          bucketing: day
          direction: both
          training_period: 7
```

## Relationship to Existing Wiki

This concept provides concrete configuration details for [[dbt-anomaly-detection-tests]], which previously only described the general concept of time-series anomaly detection using moving standard deviations. Elementary's implementation offers a specific, production-tested approach with well-documented parameters.