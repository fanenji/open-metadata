---
type: concept
title: DremioFrame Data Quality Framework
created: 2026-04-29
updated: 2026-04-29
tags: [dremio, data-quality, testing, python]
related: [dremioframe, data-quality-dimensions, dbt-expectations, openmetadata-data-quality, great-expectations-for-data-contracts]
sources: ["DremioFrame - Dremio Dataframe Library.md"]
---
# DremioFrame Data Quality Framework

The DremioFrame Data Quality Framework provides built-in expectation testing for data quality validation within the [[dremioframe|DremioFrame]] library. It allows users to define and run data quality checks programmatically using a `.quality` accessor on dataframe objects.

## Key Features

- **Expectation Testing**: Methods like `.quality.expect_not_null("column_name")` and `.quality.expect_row_count("condition", count, operator)`
- **YAML Syntax**: Supports defining data quality tests in YAML format
- **Integration with Orchestration**: Data quality tasks can be scheduled and executed as part of [[dremioframe-orchestration]] pipelines

## Comparison

The DremioFrame DQ framework provides a lightweight, programmatic approach to data quality testing, similar to [[dbt-expectations]] but integrated directly into the Dremio Python client. It is less comprehensive than dedicated platforms like [[openmetadata-data-quality]] or [[great-expectations-for-data-contracts]], but offers the advantage of tight integration with the Dremio ecosystem.

## Related

- [[dremioframe]] — The parent library
- [[data-quality-dimensions]] — The seven dimensions of data quality
- [[dremioframe-orchestration]] — Orchestration integration for DQ tasks