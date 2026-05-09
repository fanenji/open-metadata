---
type: concept
title: dbt Testing Patterns
created: 2026-04-04
updated: 2026-05-08
tags:
  - dbt
  - data-quality
  - testing
  - patterns
  - unit-tests
  - udf
  - tdd
  - best-practices
related:
  - dbt-best-practices
  - data-quality-dimensions
  - dbt-expectations
  - dbt-anomaly-detection-tests
  - great-expectations-for-data-contracts
  - dbt-data-contract-implementation
  - environmental-data-quality-hierarchy
  - dbt-unit-testing
  - user-defined-function-testing
  - test-driven-development-with-dbt
  - dbt-utils
  - dbt-macros
  - dbt-slim-ci
  - dbt-ci-testing-strategy
  - dbt-observability-implementation
  - dbt-artifacts
  - singular-tests
sources:
  - "Boost your dbt tests using Great Expectations in dbt.md"
  - "dbt-expectations - Port of Great Expectations to dbt test macros.md"
  - "research-dbt-testing-patterns-update-2026-05-08.md"
---

# dbt Testing Patterns

dbt provides a flexible testing framework for validating data as it moves through the transformation pipeline. The framework can be extended through packages like [[dbt-expectations]], offering patterns from simple built-in tests to advanced statistical and anomaly detection capabilities. This page categorizes dbt testing patterns and covers strategies such as unit testing, custom tests, singular tests, user-defined function testing, and test-driven development (TDD).

## Test Categories

### 1. Built-in Generic Tests

dbt ships with four generic tests: `unique`, `not_null`, `accepted_values`, and `relationships`. These are schema-level tests applied via YAML configuration and cover basic data quality constraints.

### 2. Singular Tests

Singular tests are one-off SQL queries stored in the `tests/` directory. They return failing rows when data integrity checks fail; if the query returns zero rows, the test passes. This pattern is ideal for business-rule validations that do not need reuse.

**Example** (no negative order quantities):
```sql
SELECT transaction_id
FROM {{ ref('fact_transactions') }}
WHERE quantity < 0
```

### 3. Custom Generic Tests

Using dbt macros (Jinja), developers can create reusable SQL templates that can be applied across multiple models and columns via YAML configuration. These templates allow parametrization and can reference external packages such as `dbt_utils` and `dbt_expectations`. This is the foundation for extending the built-in test suite.

### 4. Package-Based Tests

The `dbt_utils` package extends built-in tests with additional patterns such as `equal_rowcount`, `expression_is_true`, and `recency`.

The [[dbt-expectations]] package provides over 60 test macros organized into seven categories, bridging the gap between simple SQL checks and the advanced capabilities of frameworks like [[great-expectations]]. These tests implement complex validation logic such as regular expressions, statistical outlier detection, and table shape comparisons.

**Example YAML application** using `dbt_utils.expression_is_true`:
```yaml
models:
  - name: my_model
    tests:
      - dbt_utils.expression_is_true:
          expression: "sales_empire + sales_rebellion = total_sales_galaxy"
```

| Category | Example Tests | Use Case |
|----------|--------------|----------|
| Table shape | `expect_table_row_count_to_be_between`, `expect_table_columns_to_match_set` | Schema validation, data volume checks |
| Missing values & types | `expect_column_values_to_not_be_null`, `expect_column_values_to_be_of_type` | Completeness and type safety |
| Sets and ranges | `expect_column_values_to_be_between`, `expect_column_values_to_be_increasing` | Value range and monotonicity |
| String matching | `expect_column_values_to_match_regex`, `expect_column_values_to_match_like_pattern` | Format validation |
| Aggregate functions | `expect_column_mean_to_be_between`, `expect_column_quantile_values_to_be_between` | Statistical profile validation |
| Multi-column | `expect_compound_columns_to_be_unique`, `expect_column_pair_values_to_be_equal` | Cross-column relationships |
| Distributional | `expect_column_values_to_be_within_n_moving_stdevs` | Anomaly detection |

### 5. Unit Tests (v1.8+)

First-class feature in dbt v1.8+ that validates model logic with mock inputs and expected outputs, isolated from upstream data sources. Enables TDD workflows.

**Example unit test**:
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

## Advanced Patterns

### Statistical and Distributional Tests

Beyond simple constraints, these tests enable statistical profile validation:

- **Standard deviation bounds** — `expect_column_stdev_to_be_between`
- **Quantile validation** — `expect_column_quantile_values_to_be_between`
- **Proportion of unique values** — `expect_column_proportion_of_unique_values_to_be_between`
- **Anomaly detection** — [[dbt-anomaly-detection-tests]] using moving standard deviations

### UDF Testing Pattern

User-defined functions lack first-class dbt support but can be managed through a documented pattern: define the UDF as a macro, create a `CREATE OR REPLACE FUNCTION` macro, execute via `on-run-start` hook, and test with a singular test. See [[user-defined-function-testing]] for details.

### Test-Driven Development (TDD) with dbt

Write unit tests before model SQL to enforce early validation of business logic. See [[test-driven-development-with-dbt]] for the full workflow.

## Integration with Data Contracts

These testing patterns can be used to enforce constraints defined in [[dbt-data-contract-implementation]], providing runtime validation of schema and data quality expectations. The distributional and anomaly detection tests are particularly valuable for [[environmental-data-quality-hierarchy]] patterns.

## Best Practices

1. **Use built-in tests first** (`unique`, `not_null`, `accepted_values`, `relationships`) for basic data quality.
2. **Invest in generic tests** when the same validation logic applies across multiple models and columns.
3. **Add unit tests** for complex SQL logic (e.g., window functions, multiple joins).
4. **Employ a TDD cycle** for critical transformations.
5. **Automate test execution in CI/CD** — integrate `dbt test` as a merge gate and consider selective execution with [[dbt-slim-ci]].
6. **Extend with packages** like [[dbt-expectations]] for sophisticated tests such as anomaly detection and distribution checks.
7. **Separate test scopes** — run fast tests in pull requests and deeper nightly tests in staging.
8. **Log test results** via `on-run-end` hooks or by consuming [[dbt-artifacts]] for observability.
9. **Use distributional and anomaly detection tests** to support [[environmental-data-quality-hierarchy]] and data contract monitoring.

## Related Pages

- [[dbt-best-practices]]
- [[data-quality-dimensions]]
- [[dbt-expectations]]
- [[dbt-anomaly-detection-tests]]
- [[great-expectations-for-data-contracts]]
- [[dbt-data-contract-implementation]]
- [[environmental-data-quality-hierarchy]]
- [[dbt-unit-testing]]
- [[user-defined-function-testing]]
- [[test-driven-development-with-dbt]]
- [[dbt-utils]]
- [[dbt-macros]]
- [[dbt-slim-ci]]
- [[dbt-ci-testing-strategy]]
- [[dbt-observability-implementation]]
- [[dbt-artifacts]]
- [[singular-tests]]