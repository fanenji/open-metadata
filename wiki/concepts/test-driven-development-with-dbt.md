---
type: concept
title: Test-Driven Development with dbt
created: 2026-05-08
updated: 2026-05-09
tags:
  - dbt
  - tdd
  - testing
  - unit-tests
  - development-workflow
related: ["dbt-testing-patterns", "dbt-unit-testing", "dbt-utils", "dbt-expectations", "dbt-macros", "dbt-unit-tests", "dbt-ci-testing-strategy", "dbt-artifacts"]sources:
  - research-dbt-testing-patterns-update-2026-05-08.md
  - thinkthinking-1-analyze-the-request-2026-05-09-175447.md
---
# Test-Driven Development with dbt

Test-Driven Development (TDD) with dbt is a workflow pattern where unit tests are written **before** the model SQL code. This leverages [[dbt-unit-testing]] (introduced in dbt v1.8) to define expected behavior upfront using mock input rows and expected output rows, then develop the model logic to satisfy those expectations. This workflow reduces debug cycles and enforces early validation of business logic.

## Workflow

1. **Write the unit test**: Define mock input rows and expected output rows in the `unit_tests:` section of a YAML configuration file.
2. **Write the model SQL**: Implement the transformation logic to match the expected output.
3. **Run the test**: Execute `dbt test --select type:unit` (or `dbt test --select test_name` for a specific test) to validate.
4. **Iterate**: Refine the model until the test passes.

## Example

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

## Benefits

- Forces clear specification of business logic before implementation.
- Provides immediate feedback on logic correctness.
- Reduces debugging time by isolating logic from data dependencies.
- Enables confident refactoring of complex SQL transformations.

## Supporting Packages

- **dbt_utils**: Provides expressive test macros like `expression_is_true`, `unique_combination_of_columns`.
- **dbt-expectations**: Provides advanced tests like `expect_sum_between`, anomaly detection, and distribution checks.

## Best Practices

- Use TDD for critical transformations with complex SQL logic (window functions, multiple joins, conditionals).
- Combine with [[dbt-slim-ci]] to run only affected tests in pull requests.
- Keep test cases focused and minimal — one logical assertion per test.
- Log test results via [[dbt-artifacts]] for observability.

## Related Concepts

- [[dbt-testing-patterns]] — Overall categorization of dbt testing strategies.
- [[dbt-unit-testing]] — Native unit test feature enabling TDD.
- [[dbt-utils]] — Utility package with generic test macros.
- [[dbt-expectations]] — Advanced test macros for expressive validation.
- [[dbt-macros]] — Custom test macros for project-specific logic.
- [[dbt-ci-testing-strategy]] — Integrating unit tests into CI pipeline.