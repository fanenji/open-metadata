---
type: concept
title: Great Expectations for Data Contracts
created: 2026-04-04
updated: 2026-04-04
tags: [data-quality, data-contracts, validation, great-expectations]
related: [data-contract-platform, delta-lake-schema-enforcement, data-contract-versioning-strategy, dbt-testing-patterns]
sources: ["Data Contract Enforcement Ensuring Reliability in Distributed Pipelines.md"]
---
# Great Expectations for Data Contracts

The use of [[great-expectations]] as an enforcement engine for data contracts. In this pattern, a YAML contract defines the expected schema, allowed values, and constraints for a dataset, and Great Expectations validates incoming data batches against those expectations.

## Implementation Pattern

1. Load the contract YAML file containing schema definitions.
2. Read incoming data (e.g., from CSV, Kafka, or API).
3. Build Great Expectations expectations manually from the contract fields (e.g., `expect_column_to_exist`, `expect_column_values_to_not_be_null`, `expect_column_values_to_be_in_set`).
4. Run validation; if it fails, quarantine the batch and trigger an alert.

## Known Limitation

The source code example does **not** demonstrate automated generation of Great Expectations expectations from the contract YAML. A human must read the YAML and code the checks by hand. This is a significant gap noted by reader S Parodi in the article's comments. True contract-driven validation would require a parser that translates contract definitions into expectations programmatically.

## Relationship to dbt Testing

Contrasts with [[dbt-testing-patterns]]: Great Expectations for data contracts focuses on **pre-ingestion** validation (before data enters the warehouse), while dbt tests validate data **after** it has been loaded and transformed.
