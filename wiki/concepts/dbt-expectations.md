---
type: concept
title: dbt-expectations
created: 2026-07-15
updated: 2026-07-15
tags: [dbt, data-quality, testing, great-expectations]
related: [dbt, dbt-integration, data-quality, data-quality-as-code, great-expectations]
sources: ["https://aistudio.google.com/u/1/prompts/12pyOVNHefRrcRS5vjPsrwEwHKb3hi-Tr"]
---

# dbt-expectations

A dbt package (`calogica/dbt_expectations`) that brings **Great Expectations-style tests** into dbt YAML configurations. It allows writing advanced data quality assertions (e.g., `expect_column_values_to_be_unique`, `expect_column_values_to_be_between`) directly in dbt `schema.yml` files.

## Relationship to OpenMetadata

- OpenMetadata's [[dbt-integration]] already ingests dbt test results into the unified metadata graph
- dbt-expectations provides more expressive test types than dbt's built-in generic tests
- When combined with OpenMetadata, dbt-expectations results can be visualized in the Data Quality dashboard
- OpenMetadata's [[data-quality-as-code]] SDK provides a more pipeline-integrated alternative to dbt-expectations for non-dbt workflows

## Comparison

- **dbt-expectations**: Embedded in dbt workflow, YAML-driven, limited to dbt projects
- **OpenMetadata Data Quality as Code**: SDK-driven, pipeline-embedded, works with any Python ETL, integrates with [[unified-metadata-graph]]
- **OpenMetadata UI Quality**: No-code, business-user accessible, built into the platform