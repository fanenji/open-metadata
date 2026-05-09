---
type: query
title: "<think>Thinking. 1.  **Analyze the Request:**"
created: 2026-05-09
tags: []
---
Based on the wiki content, dbt unit tests are a method of validating model logic by using **predefined inputs and expected outputs, completely isolated from upstream data sources** [3].

They were introduced as a **first-class feature in dbt v1.8** [3]. Unlike standard data tests (which run against actual warehouse data), unit tests allow you to mock your upstream `ref` or `source` calls directly in the YAML configuration to test the transformation logic in isolation [3].

#### Key Characteristics
- **High Effort, High Specificity**: Defining precise test cases requires work, but they provide extremely clear pass/fail results for exactly the logic you are testing [3], [10].
- **Logic-Focused**: They are best suited for complex SQL logic (e.g., window functions, multiple joins, conditional expressions) rather than general data quality checks [3], [10].

#### Syntax & Example
Unit tests are defined in the `unit_tests:` block of a YAML configuration file [3], [29]:
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

#### Strategic Use & Best Practices
- **Enables TDD**: They power [[test-driven-development-with-dbt]], where you write the unit test *before* writing the model SQL [3], [13].
- **UDF Testing**: Unit tests can validate User-Defined Functions (UDFs) when called within a model, though there is no first-class `dbt test` command for UDFs alone [3], [14].
- **CI/CD Integration**: In a [[dbt-slim-ci]] or [[dbt-ci-testing-strategy]], you use them sparingly for logic-heavy models that have changed (e.g., `dbt test --select state:modified,type:unit`) [5], [12].
- **Testing Hierarchy**: They sit between generic schema tests and data diffing in terms of precision, used for "complex business logic validation" [10].
- **Distinction**: This native model testing feature is different from [[macro-unit-testing-in-dbt]], which is a community workaround pattern for testing *Jinja macros* [1].

<!-- cited: 1, 2, 3, 5, 10, 12, 13, 14, 29 -->