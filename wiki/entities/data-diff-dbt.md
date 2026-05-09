---
type: entity
title: data-diff for dbt
created: 2026-04-29
updated: 2026-04-29
tags: [data-diff, dbt, testing, datafold]
related: [dbt-core-slim-ci-implementation, dbt-ci-testing-strategy]
sources: ["How to Create CI-CD Pipelines for dbt Core.md"]
---
# data-diff for dbt

A tool by Datafold for comparing row counts and data differences between two table versions. In dbt CI/CD pipelines, it can be used to compare the original table version against a version containing proposed changes.

## Key Features

- Compares row counts between development and production table versions.
- Helps detect unintended data changes introduced by model modifications.
- Integrates with dbt development workflows in Snowflake and other warehouses.

## Usage in CI/CD

Used as an enhancement to the Slim CI pattern, data-diff runs after model changes are compiled, comparing the output of the modified model against the production version to ensure data integrity.

## Related

- [[dbt-core-slim-ci-implementation]] — The CI/CD pattern where data-diff is a recommended enhancement.
- [[dbt-ci-testing-strategy]] — Broader testing strategy for dbt CI/CD.