---
type: concept
title: Macro Unit Testing in dbt
created: 2026-04-07
updated: 2026-04-07
tags: [dbt, testing, macros, unit-testing, validation]
related: [dbt-testing-patterns, dbt-macros, leo-godin, dbt-slim-ci, dbt-ci-testing-strategy]
sources: ["Testing Dbt Macros.md"]
---
# Macro Unit Testing in dbt

Macro unit testing in dbt is the practice of validating Jinja macros by creating a dedicated **validation model** that calls the macro with test inputs and unions expected outputs, then applying dbt tests to compare actual vs. expected values.

## Core Pattern

1. Create a dbt model (e.g., `models/validation/validate_<macro_name>.sql`) that unions multiple `SELECT` statements, each calling the macro with specific arguments and providing an `expected_date` column.
2. Define dbt tests in a corresponding YAML file (e.g., `validate_<macro_name>.yml`) using `expression_is_true` to assert `expected_date = actual_date`.
3. Disable the validation folder in production via `dbt_project.yml` and enable it only with `--vars '{run_validation: true}'`.

## Testing Methodology

- **Core functionality**: Verify the macro returns correct results for its primary use case.
- **Path coverage**: Test all code paths through the macro (e.g., `run_at_day`, `run_at_week`, `run_at_month`).
- **Boundary testing**: Test beginning, middle, and end of valid ranges (e.g., start, middle, end of week/month).

## Implementation Details

- Use `modules.datetime` within dbt Jinja to access Python date functions.
- Prefer a custom `expression_is_true` test over `dbt_utils.expression_is_true` because the latter doesn't provide useful troubleshooting information in compiled code.
- Include a catch-all test at the top of the YAML file for full coverage, with individual tests for specific failure identification.
- Use unique `name` properties for each test to improve readability and avoid duplicate unique IDs.

## Benefits

- Catches logic errors that manual testing would miss (e.g., ISO week start vs. company-specific week start).
- Provides automated, reproducible validation that can be integrated into CI/CD pipelines.
- Increases confidence in macro correctness for downstream consumers.

## Connections

This concept extends [[dbt-testing-patterns]] by adding a "Macro Unit Testing" category alongside singular, generic, and advanced testing strategies. It also complements [[dbt-slim-ci]] and [[dbt-ci-testing-strategy]] for CI/CD integration.