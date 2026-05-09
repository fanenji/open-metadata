---
type: concept
title: Generic vs. Singular Tests
created: 2024-05-22
updated: 2024-05-22
tags: [dbt, testing, data-quality]
related: [dbt]
sources: ["A comprehensive guide to automating data testing in dbt.md"]
---
# Generic vs. Singular Tests

In [[dbt]], data testing is primarily implemented through two distinct architectural patterns: Generic Tests and Singular Tests.

## Generic Tests

Generic tests are reusable, parameterizable tests defined in YAML files. They are applied to columns and are highly efficient for standard data quality checks.

- **Implementation**: Defined in `.yml` files under the `tests` key for a specific column.
- **Standard Examples**: `not_null`, `unique`, `relationships` (for **refertainable integrity**), and `accepted_values`.
- **Pros**: Highly reusable across different models and columns; low maintenance.

## Singular Tests

Singular tests are custom, one-off SQL queries designed for specific, complex business logic assertions.

- **Implementation**: Written as standard `.sql` files located in the `tests/` directory of a dbt project.
- **Mechanism**: A singular test passes if the query returns **zero** rows. If the query returns any rows, those rows represent the data that failed the assertion.
- **Pros**: Capable of expressing complex, multi-column, or multi-table logic that cannot be easily captured by a generic test.

## Comparison Summary

| Feature | Generic Tests | Singular Tests |
| :--- | :--- | :--- |
| **Location** | YAML configuration | `.sql` files in `tests/` |
| **Reusability** | High (can be applied to any column) | Low (specific to one logic/model) |

| **Complexity** | Best for simple, standard checks | Best for complex business rules |