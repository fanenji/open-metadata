---
type: source
title: Testing Dbt Macros
created: 2026-04-07
updated: 2026-04-07
tags: [dbt, testing, macros, unit-testing]
related: [dbt-macro-unit-testing, leo-godin, dbt-testing-patterns, dbt-macros]
sources: ["Testing Dbt Macros.md"]
authors: [Leo Godin]
year: 2024
url: "https://blog.dataengineerthings.org/testing-dbt-macros-a80e76243ae4"
venue: "Data Engineer Things (Medium)"
---
# Testing Dbt Macros

This article by [[Leo Godin]], Senior Data Engineer at Shopify, presents a practical pattern for unit testing dbt Jinja macros. It argues that dbt's built-in data quality tests are insufficient for ensuring pipeline reliability — code validation is also necessary.

## Core Pattern

The article introduces a **validation model pattern**: create a dedicated dbt model that calls the macro with test inputs and unions expected outputs, then apply dbt tests (custom `expression_is_true` or `dbt_utils.expression_is_true`) to compare actual vs. expected values.

## Testing Methodology

- **Core functionality**: Verify the macro returns correct results for its primary use case.
- **Path coverage**: Test all code paths (e.g., `run_at_day`, `run_at_week`, `run_at_month`).
- **Boundary testing**: Test beginning, middle, and end of valid ranges (e.g., start, middle, end of week/month).

## Key Example

The article demonstrates the pattern on a `get_model_start_date` macro for a fictional company "Moon Walks." The test suite caught a real bug: the `run_at_week` logic used Python's ISO week start (Monday) instead of the company's Sunday start. This bug would not have been caught by manual testing.

## Practical Considerations

- Uses a custom `expression_is_true` test over `dbt_utils.expression_is_true` because the latter doesn't provide useful troubleshooting information in compiled code.
- Validation models are disabled in production using dbt variables (`--vars '{run_validation: true}'`).
- A catch-all test at the top of the YAML file provides full coverage, while individual tests identify specific failures.

## Connections

This source strengthens [[dbt-testing-patterns]] by adding a concrete macro unit testing category, and extends [[dbt-macros]] with a testing dimension. The pattern is complementary to [[dbt-slim-ci]] and [[dbt-ci-testing-strategy]] for CI/CD integration.