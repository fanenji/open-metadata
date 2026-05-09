---
type: entity
title: dbt_expectations
created: 2024-05-22
updated: 2024-05-22
tags: [dbt, testing, data-quality]
related: [dbt, regex-pattern-matching]
sources: ["A comprehensive and guide to automating data testing in dbt.md"]
---
# dbt_expectations

`dbt_expectations` is a dbt package that provides advanced testing capabilities inspired by the "Great Expectations" framework. It allows for much more granular and complex data assertions than the standard dbt generic tests.

## Key Capabilities

- **Regex Pattern Matching**: Validating that string columns (like emails or phone numbers) follow a specific format using regular expressions.
- **Data Type Validation**: Ensuring that columns contain the expected data types.
- **Complex Assertions**: Testing for specific patterns, ranges, or distributions within the data.

## Example: Email Validation

Using `dbt_expectations` to ensure an email column follows a valid pattern:

```yaml
columns:
  - name: email
    tests:
      - dbt_expectations.expect_column_values_to_match_regex:
          regex: "%__@_%.__%"
```