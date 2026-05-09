---
type: concept
title: dbt Anomaly Detection Tests
created: 2026-04-07
updated: 2026-04-07
tags: [dbt, data-quality, anomaly-detection, testing, time-series]
related: [dbt-expectations, dbt-testing-patterns, great-expectations-for-data-contracts]
sources: ["dbt-expectations - Port of Great Expectations to dbt test macros.md"]
---
# dbt Anomaly Detection Tests

## Overview

The `dbt-expectations` package provides two anomaly detection test macros that enable statistical outlier detection natively in dbt without external Python dependencies. These tests are unique capabilities not available in dbt's built-in test suite.

## Moving Standard Deviation Test

### `expect_column_values_to_be_within_n_moving_stdevs`

This test performs time-series anomaly detection based on the assumption that differences between periods in a given time series follow a log-normal distribution. It compares logged differences (vs N periods ago) in metric values against a moving average with configurable sigma thresholds.

**Parameters:**
- `date_column_name` — the date column for time ordering
- `period` — granularity (default: `day`)
- `lookback_periods` — periods to look back for comparison (default: 1)
- `trend_periods` — periods for moving average calculation (default: 7)
- `test_periods` — periods to test (default: 14)
- `sigma_threshold` — number of standard deviations for anomaly detection (default: 3)
- `take_logs` — whether to log-transform values (default: true)
- `take_diffs` — whether to difference values (default: true)
- `group_by` — optional grouping columns for per-group anomaly detection

**Example:**
```yaml
tests:
  - dbt_expectations.expect_column_values_to_be_within_n_moving_stdevs:
      date_column_name: date
      period: day
      lookback_periods: 1
      trend_periods: 7
      test_periods: 14
      sigma_threshold: 3
      group_by: [group_id]
```

## Static Standard Deviation Test

### `expect_column_values_to_be_within_n_stdevs`

This test checks whether (optionally grouped and summed) metric values fall within Z sigma of the column average. It is a simpler, non-time-series anomaly test suitable for detecting outliers in cross-sectional data.

**Parameters:**
- `group_by` — optional grouping column
- `sigma_threshold` — number of standard deviations (default: 3)

**Example:**
```yaml
tests:
  - dbt_expectations.expect_column_values_to_be_within_n_stdevs:
      group_by: group_id
      sigma_threshold: 3
```

## Use Cases

- **Monitoring data freshness** — detect when data volumes drop unexpectedly
- **Revenue/transaction monitoring** — flag unusual changes in daily metrics
- **Sensor data validation** — identify anomalous readings in IoT or environmental monitoring
- **Quality control** — detect drift in distributional properties over time

## Limitations

- Moving standard deviation test assumes log-normal distribution of period-over-period differences
- Does not handle seasonality or complex trend patterns beyond simple moving averages
- Requires sufficient historical data for meaningful moving average calculation
- Performance may degrade on very large datasets without proper partitioning

## Related Pages

- [[dbt-expectations]] — The package providing these tests
- [[dbt-testing-patterns]] — Broader categorization of dbt testing strategies
- [[great-expectations-for-data-contracts]] — Using Great Expectations as an enforcement engine