---
type: source
title: "dbt-expectations: Port of Great Expectations to dbt test macros"
created: 2026-04-07
updated: 2026-04-07
tags: [dbt, data-quality, testing, great-expectations]
related: [dbt-expectations, dbt-testing-patterns, great-expectations-for-data-contracts, dbt-anomaly-detection-tests, dbt-data-contract-implementation, environmental-data-quality-hierarchy]
sources: ["dbt-expectations - Port of Great Expectations to dbt test macros.md"]
---
# dbt-expectations: Port of Great Expectations to dbt test macros

## Overview

`dbt-expectations` is an open-source dbt package by calogica that ports a subset of Great Expectations' data quality tests into native dbt SQL test macros. It allows dbt users to deploy Great Expectations-like tests directly in their data warehouse without adding a separate Python integration.

## Key Details

- **Author/Maintainer**: calogica (Claus Herther)
- **Repository**: [github.com/calogica/dbt-expectations](https://github.com/calogica/dbt-expectations)
- **Latest Version**: v0.10.x
- **dbt Version Requirement**: 1.7.x or higher
- **Dependency**: `dbt-date` (included automatically)
- **Supported Adapters**: Postgres, Snowflake, BigQuery, DuckDB, Spark (experimental), Trino

## Test Categories

The package provides 60+ test macros organized into the following categories:

1. **Table shape** — column existence, row counts, column counts, column sets
2. **Missing values, unique values, and types** — null checks, uniqueness, data type validation, casing consistency
3. **Sets and ranges** — value membership, between checks, monotonicity (increasing/decreasing)
4. **String matching** — regex patterns, SQL LIKE patterns, string length validation
5. **Aggregate functions** — distinct counts, mean, median, quantiles, standard deviation, sum, min, max, proportion of unique values
6. **Multi-column** — column pair comparisons, compound uniqueness, multi-column sum
7. **Distributional functions** — moving standard deviation anomaly detection, static standard deviation, date completeness

## Key Differentiators

- **Native SQL execution** — all tests run inside the warehouse, no external Python process needed
- **Anomaly detection** — `expect_column_values_to_be_within_n_moving_stdevs` enables time-series anomaly detection using moving averages and sigma thresholds
- **Distributional tests** — statistical profile validation (standard deviation, quantiles, proportion of unique values) not available in dbt's built-in tests
- **Cross-table comparisons** — tests can compare aggregates and row counts across models

## Limitations

- Not a full Great Expectations port — missing features include: expectation suites, batch-level expectations, data docs generation, and the GE validation layer
- Requires dbt 1.7.x or higher
- Anomaly detection assumes log-normal distribution of period-over-period differences; may not handle seasonality or complex trends

## Installation

```yaml
# packages.yml
packages:
  - package: calogica/dbt_expectations
    version: [">=0.10.0", "<0.11.0"]
```

```yaml
# dbt_project.yml
vars:
  'dbt_date:time_zone': 'America/Los_Angeles'
```

## Related Wiki Pages

- [[dbt-expectations]] — Entity page for this package
- [[dbt-testing-patterns]] — Broader categorization of dbt testing strategies
- [[great-expectations-for-data-contracts]] — Using Great Expectations as an enforcement engine
- [[dbt-anomaly-detection-tests]] — Dedicated page for the moving standard deviation anomaly test
- [[dbt-data-contract-implementation]] — How these tests can enforce contract constraints
- [[environmental-data-quality-hierarchy]] — Multi-tier validation pattern that can use these tests