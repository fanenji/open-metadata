---
type: entity
title: dbt-expectations
tags: [dbt, testing, package, data-quality, open-source]
related: [dbt, dbt-labs, great-expectations, dbt-best-practices, dbt-testing-patterns, great-expectations-for-data-contracts, dbt-anomaly-detection-tests, dbt-data-contract-implementation, environmental-data-quality-hierarchy]
sources: ["7 dbt testing best practices.md", "Boost your dbt tests using Great Expectations in dbt.md", "dbt-expectations - Port of Great Expectations to dbt test macros.md"]
created: 2026-04-07
updated: 2026-05-07
---
# dbt-expectations

## Overview

`dbt-expectations` is an open-source dbt package by calogica that provides 60+ data quality test macros inspired by [[great-expectations]]. All tests run natively in the data warehouse as SQL, eliminating the need for a separate Python integration. It enables advanced testing capabilities for dbt models beyond the standard built-in generic tests, allowing for more complex data assertions.

## Key Features

- **60+ test macros** covering table shape, missing values, uniqueness, types, sets/ranges, string matching, aggregate functions, multi-column relationships, and distributional analysis.
- **Native SQL execution** — tests run inside the warehouse via dbt's generic test mechanism.
- **Anomaly detection** — time-series anomaly detection using moving standard deviations.
- **Distributional tests** — statistical profile validation (standard deviation, quantiles, proportion of unique values).
- **Cross-table comparisons** — compare aggregates and row counts across models.
- **Regex Validation**: `expect_column_values_to_match_regex` for pattern matching.
- **Outlier Detection**: `expect_column_values_to_be_within_n_stdevs` for identifying anomalous data.
- **Structural Integrity**: `expect_table_column_count_to_equal_other_table` to ensure transformations do not inadvertently change the schema shape.
- **Supported adapters**: Postgres, Snowflake, BigQuery, DuckDB, Spark (experimental), Trino.

## Requirements

- dbt 1.7.x or higher.
- Dependency on `dbt-date` (included automatically).
- Timezone variable must be set in `dbt_project.yml`.

## Installation

Installation is performed by adding the package to the `packages.yml` file and running `dbt deps`.

```yaml
# packages.yml
packages:
  - package: calogica/dbt_expectations
    version: [">=0.10.0", "<0.11.0"]
```

Also set the required timezone variable in `dbt_project.yml`:

```yaml
# dbt_project.yml
vars:
  'dbt_date:time_zone': 'America/Los_Angeles'
```

## Relationship to Great Expectations

`dbt-expectations` is described as a "port(ish)" — it implements a subset of Great Expectations functionality as native dbt test macros. Missing features compared to full GE include: expectation suites, batch-level expectations, data docs generation, and the GE validation layer. However, it provides the core value of warehouse-native testing without external Python dependencies.

## Usage in Data Contracts

These tests can be used to enforce constraints defined in [[dbt-data-contract-implementation]], providing runtime validation of schema and data quality expectations. The distributional and anomaly detection tests are particularly valuable for [[environmental-data-quality-hierarchy]] patterns where statistical profile validation is needed.

## See Also

- [[dbt-testing-patterns]] – Broader categorization of dbt testing strategies
- [[great-expectations-for-data-contracts]] – Using Great Expectations as an enforcement engine
- [[dbt-anomaly-detection-tests]] – Dedicated page for the moving standard deviation anomaly test
- [[dbt-data-contract-implementation]] – How these tests can enforce contract constraints
- [[environmental-data-quality-hierarchy]] – Multi-tier validation pattern that can use these tests