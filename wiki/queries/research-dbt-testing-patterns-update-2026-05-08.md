---
type: query
title: "Research: dbt-testing-patterns update"
created: 2026-05-08
origin: deep-research
tags: [research]
---

# Research: dbt-testing-patterns update

# dbt-testing-patterns (Update)

`dbt-testing-patterns` is a core concept in the [[dbt]] ecosystem, referring to the categorization and strategies for implementing tests in dbt projects. This page provides an updated synthesis of current practices, including [[dbt-unit-testing|unit testing]], [[dbt-custom-tests|custom (generic) tests]], [[singular-tests|singular tests]], and the integration of [[dbt-macros|macros]] and packages for extended test coverage. It also covers emerging patterns like [[user-defined-function-testing|UDF testing]] and [[test-driven-development-with-dbt|test-driven development (TDD)]].

---

## Categories of dbt Tests

dbt tests are broadly divided into three categories:

### 1. Singular Tests
Singular tests are one-off SQL queries stored in the `tests/` directory. They return failing records when data integrity checks fail. They are ideal for business‑rule validations that do not need reuse. [6][7]

**Example** (no negative order quantities):  
```sql
SELECT transaction_id
FROM {{ ref('fact_transactions') }}
WHERE quantity < 0
```

### 2. Generic (Custom) Tests
Generic tests are reusable SQL templates defined as macros (using Jinja) and are applied to multiple models via YAML configuration. They allow parametrization and can reference external packages (e.g., `dbt_utils`, `dbt_expectations`). [4][6] They are defined in the `tests/generic/` directory or included via packages.

**Example YAML application** using `dbt_utils.expression_is_true`:
```yaml
models:
  - name: my_model
    tests:
      - dbt_utils.expression_is_true:
          expression: "sales_empire + sales_rebellion = total_sales_galaxy"
```

The `dbt_utils` and `dbt_expectations` packages provide many pre‑built generic tests such as `unique_combination_of_columns`, `expect_sum_between`, and `anomaly_detection`. [4][5]

### 3. Unit Tests
Introduced as a first‑class feature in dbt v1.8, unit tests validate model logic with mock inputs and expected outputs, isolated from upstream data sources. [5][1] They are defined in the `unit_tests:` section of a YAML file and can directly test both SQL models and UDFs.

**Example unit test for a UDF** (from dbt Developer Hub) [1]:
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

Unit tests enable a [[test-driven-development-with-dbt|TDD approach]]: tests are written before the model SQL, ensuring the transformation logic is correct from the start. [4][8]

---

## Managing and Testing User‑Defined Functions (UDFs)

dbt has no native `ref()` or `source()` for UDFs, but they can be deployed using `on‑run‑start` hooks or macros. [2][3] The typical pattern involves:

1. **Define the UDF as a macro** that accepts a schema parameter (e.g., `{{ target.schema }}`).  
2. **Create a macro that calls `CREATE OR REPLACE FUNCTION`** – this is placed in `macros/udfs/`.  
3. **Execute the macro via a hook** in `dbt_project.yml` under `on‑run‑start`.  
4. **Test the UDF** with a singular test that calls the function and expects no results. [2]

This approach works on Redshift, BigQuery, Snowflake, and Databricks, though some warehouses (e.g., BigQuery) require fully qualified UDF references using `{{ target.project }}`. [3]

**Example UDF macro** (BigQuery) [3]:
```sql
{% macro make_func_math_radian() %}
CREATE OR REPLACE FUNCTION f_math.radian() RETURNS FLOAT64 AS (
  `{{ target.project }}`.f_math.pi() / 180
);
{% endmacro %}
```

The **volatility** attribute is accepted for both SQL and Python UDFs but handled differently per warehouse (BigQuery ignores it, Snowflake applies it). [1]

---

## Test‑Driven Development (TDD) with dbt

TDD in dbt involves writing a unit test *before* writing the model SQL. The test provides mock input rows and expected output rows, then the model must be written to produce that output. [4][8] This workflow reduces debug cycles and enforces early validation of business logic.

The `dbt_utils` and `dbt_expectations` packages are heavily used in TDD to provide expressive test macros like `expect_sum_between` or `expression_is_true`. [4] Multi‑column row‑by‑row tests (e.g., `dbt_utils.unique_combination_of_columns`) help detect duplicate records without aggregation. [4]

---

## Best Practices

The following best practices are synthesised from the community and official documentation:

1. **Use built‑in tests first** (`unique`, `not_null`, `accepted_values`, `relationships`) for basic data quality. [6][7]  
2. **Invest in generic tests** when the same validation logic applies across models. [6]  
3. **Add unit tests for complex SQL logic** (e.g., window functions, multiple joins) to isolate model correctness from source data issues. [5]  
4. **Employ a TDD cycle** for critical transformations. [4]  
5. **Automate test execution in CI/CD** – integrate `dbt test` as a merge gate to prevent failures in production. [7]  
6. **Extend with packages** like `dbt_expectations` for sophisticated tests (anomaly detection, distribution checks). [5][6]  
7. **Separate test scopes** – fast tests in pull requests, deeper nightly tests in staging. (Related: [[dbt-ci-testing-strategy]], [[dbt-slim-ci]])  
8. **Log test results** via `on‑run‑end` hooks or by consuming [[dbt-artifacts]] for observability. [7]

---

## Contradictions and Gaps

- **UDF testing maturity**: While UDFs can be tested via singular tests or unit tests (when used within models), there is no first‑class `dbt test` command for UDFs alone. Some practitioners rely on pre‑hooks, which can clutter console output. [2]  
- **Unit test support**: Although dbt now offers native unit tests, the feature is relatively new (v1.8+) and may not yet be adopted across all projects. Older patterns that rely on custom equality macros are still widely used. [8]  
- **Tooling gaps**: None of the sources provide a comprehensive comparison of native dbt unit tests versus external package‑based equality tests. A formal framework for choosing between them is missing.

---

## Suggested Additional Sources

The following sources would strengthen a complete understanding of current patterns:

- Official dbt documentation on [unit tests](https://docs.getdbt.com/docs/build/unit-tests) and migration guides.  
- A hands‑on comparison of native unit test syntax (dbt v1.8) vs. the older `dbt_utils.equality` macro approach.  
- Case studies of testing UDFs at scale, especially concerning Python UDFs on Snowflake/BigQuery.  
- Performance benchmarks for different test execution strategies (singular vs. generic vs. unit) on large datasets.  
- Deep dives into integrating [[dbt-expectations]] with CI/CD for anomaly detection and schema drift.

---

## Related Concepts

- [[dbt-expectations]] – Port of Great Expectations to dbt test macros.  
- [[dbt_utils]] – Utility package with many generic tests.  
- [[dbt-macros]] – Reusable Jinja code for dynamic SQL and test logic.  
- [[dbt-anomaly-detection-tests]] – Time‑series tests in dbt-expectations.  
- [[dbt-schema-synchronization]] – Automating schema + test definitions.  
- [[dbt-observability-implementation]] – Monitoring test run results.  
- [[dbt-slim-ci]] – Selective execution of tests in CI.  
- [[dbt-unit-testing]] – (Future dedicated page)  
- [[user-defined-function-testing]] – (Future dedicated page)  

---

## References

[1] dbt Developer Hub – User‑defined functions.  
[2] Equal Experts – Testing and deploying UDFs with dbt.  
[3] dbt Community Forum – Using dbt to manage UDFs.  
[4] Beyond Measure – Test Driven Development with dbt.  
[5] Datafold – 7 dbt testing best practices.  
[6] Monte Carlo – Understanding dbt Custom Tests.  
[7] Metaplane – Everything you need to know about dbt tests.  
[8] Start Data Engineering – How to unit test SQL transforms in dbt.

## References

1. [User-defined functions | dbt Developer Hub](https://docs.getdbt.com/docs/build/udfs) — docs.getdbt.com
2. [Testing and deploying UDFs with dbt | Equal Experts](https://www.equalexperts.com/blog/our-thinking/testing-and-deploying-udfs-with-dbt/) — equalexperts.com
3. [Using dbt to manage user defined functions - Show and Tell - dbt Community Forum](https://discourse.getdbt.com/t/using-dbt-to-manage-user-defined-functions/18) — discourse.getdbt.com
4. [Test Driven Development (TDD) with dbt: Test First, SQL Later | Beyond Measure](https://www.dumky.net/posts/test-driven-development-tdd-with-dbt-test-first-sql-later/) — dumky.net
5. [7 dbt testing best practices](https://www.datafold.com/blog/7-dbt-testing-best-practices/) — datafold.com
6. [Understanding Dbt Custom Tests (Without Losing Your Mind)](https://www.montecarlodata.com/blog-dbt-custom-tests/) — montecarlodata.com
7. [Everything you need to know about dbt tests: How to write them, examples, and best practices | Metaplane](https://www.metaplane.dev/blog/dbt-test-examples-best-practices) — metaplane.dev
8. [How to unit test sql transforms in dbt – Start Data Engineering](https://www.startdataengineering.com/post/how-to-test-sql-using-dbt/) — startdataengineering.com
