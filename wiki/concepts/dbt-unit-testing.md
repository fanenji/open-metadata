---
type: concept
title: dbt Unit Testing
created: 2026-04-07
updated: 2026-05-08
tags: 
  - testing
  - dbt
  - software-engineering
  - unit-tests
  - v1.8
related:
  - dbt
  - dbt-testing-hierarchy
  - dbt-testing-patterns
  - test-driven-development-with-dbt
  - dbt-utils
  - dbt-expectations
  - user-defined-function-testing
sources:
  - "7 dbt testing best practices.md"
  - "research-dbt-testing-patterns-update-2026-05-08.md"
---
# dbt Unit Testing

dbt unit tests are a method of validating model logic by using predefined inputs and expected outputs, isolated from upstream data sources. Introduced as a first-class feature in dbt v1.8, they are defined in the `unit_tests:` section of a YAML file and can directly test both SQL models and user-defined functions (UDFs). Unlike data tests that run against actual database data, unit tests isolate the validation of the SQL code itself from the variability of the underlying source data.

## Key Characteristics

- **High Effort**: Requires defining specific test cases and curated input/output datasets.
- **High Specificity**: Provides clear results regarding whether the logic is correct.

## Syntax

Unit tests are defined in the `unit_tests:` block of a YAML configuration file. The following example tests a model `my_model` that determines whether values in a column are positive integers:

```yaml
unit_tests:
  - name: test_is_positive_int
    model: my_model
    given:
      - input: ref('a_model_i_like')
        rows:
          - { maybe_positive_int_column: 10 }
          - { maybe_positive_int_column: -4 }
          - { maybe_positive_int_column: +8 }
          - { maybe_positive_int_column: 1.0 }
    expect:
      rows:
        - { maybe_positive_int_column: 10, is_positive: true }
        - { maybe_positive_int_column: -4, is_positive: false }
        - { maybe_positive_int_column: +8, is_positive: true }
        - { maybe_positive_int_column: 1.0, is_positive: true }
```

## Use Cases

- Validating complex SQL logic (window functions, multiple joins, conditional expressions).
- Testing UDFs when used within a model.
- Enabling [[test-driven-development-with-dbt|TDD workflows]].
- Isolating model correctness from source data issues.
- Testing complex, high-risk business logic with intricate transformation rules.

## Adoption Considerations

- **Requires dbt v1.8+**: Older projects may still rely on custom equality macros (e.g., `dbt_utils.equality`).
- **No formal comparison**: There is no comprehensive benchmark comparing native unit tests vs. `dbt_utils.equality` on large datasets.
- **UDF testing**: Unit tests can validate UDFs when called within a model, but there is no first-class `dbt test` command for UDFs alone.

## Related Concepts

- [[dbt-testing-patterns]] — Overall categorization of dbt testing strategies.
- [[dbt-testing-hierarchy]] — Broader context of testing types in dbt.
- [[test-driven-development-with-dbt]] — TDD workflow enabled by unit tests.
- [[dbt-utils]] — Provides `equality` macro as an older alternative.
- [[dbt-expectations]] — Advanced test macros for expressive validation.
- [[user-defined-function-testing]] — UDF testing patterns.