---
type: concept
title: dbt Unit Tests
created: 2026-05-09
updated: 2026-05-09
tags: [dbt, testing, unit-tests, data-quality, ci-cd]
related: [dbt-testing-patterns, dbt-ci-testing-strategy, test-driven-development-with-dbt, macro-unit-testing-in-dbt, dbt-slim-ci]
sources: ["thinkthinking-1-analyze-the-request-2026-05-09-175447.md"]
---
# dbt Unit Tests

dbt unit tests are a first-class feature introduced in **dbt v1.8** for validating model logic using predefined inputs and expected outputs, completely isolated from upstream data sources. Unlike standard data tests that run against actual warehouse data, unit tests allow mocking upstream `ref` or `source` calls directly in YAML configuration to test transformation logic in isolation.

## Key Characteristics

- **High Effort, High Specificity**: Defining precise test cases requires significant work, but provides extremely clear pass/fail results for exactly the logic being tested.
- **Logic-Focused**: Best suited for complex SQL logic (e.g., window functions, multiple joins, conditional expressions) rather than general data quality checks.

## Syntax & Configuration

Unit tests are defined in the `unit_tests:` block of a YAML configuration file:

```yaml
unit_tests:
  - name: test_is_positive_int
    model: my_model
    given:
      - input: ref('a_model_i_like')
        rows:
          - { maybe_positive_int_column: 10 }
          - { maybe_positive_int_column: -4 }
    expect:
      rows:
        - { maybe_positive_int_column: 10, is_positive: true }
        - { maybe_positive_int_column: -4, is_positive: false }
```

## Use Cases

- **Complex SQL Logic Validation**: Testing window functions, multiple joins, and conditional expressions.
- **UDF Testing**: Validating User-Defined Functions when called within a model (no first-class `dbt test` command for UDFs alone).
- **Test-Driven Development (TDD)**: Writing unit tests before model SQL to drive development (see [[test-driven-development-with-dbt]]).

## CI/CD Integration

In [[dbt-slim-ci]] or [[dbt-ci-testing-strategy]], unit tests are used sparingly for logic-heavy models that have changed:
```
dbt test --select state:modified,type:unit
```

## Testing Hierarchy

Unit tests sit between generic schema tests and data diffing in terms of precision, used for "complex business logic validation." They are distinct from [[macro-unit-testing-in-dbt]], which is a community workaround pattern for testing Jinja macros.

## Limitations & Considerations

- Not suitable for general data quality checks.
- Performance impact in large dbt projects is not well-documented.
- Interaction with dbt Mesh cross-project dependencies is unclear.
- Potential limitations with complex data types (nested JSON, geospatial geometries) in `given`/`expect` rows.
