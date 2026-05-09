---
type: concept
title: dremioframe Data Quality Expectations
created: 2026-04-04
updated: 2026-04-04
tags: [dremio, data-quality, validation, expectations]
related: [dremioframe, dbt-expectations, data-quality-dimensions, great-expectations-for-data-contracts]
sources: ["Introducing dremioframe - A Pythonic DataFrame Interface for Dremio.md"]
---

# dremioframe Data Quality Expectations

**dremioframe** includes built-in data quality validation methods, called "expectations," that allow users to validate data directly within the DataFrame pipeline. This feature provides a lightweight alternative to dedicated data quality tools.

## Available Methods

- **`.expect_not_null("column")`**: Asserts that a column contains no null values.
- **`.expect_column_values_to_be_between("column", min, max)`**: Asserts that all values in a column fall within a specified range.

## Usage

```python
df = client.table("sales") \
           .select("product", "price", "quantity") \
           .collect()

df.quality.expect_not_null("price")
df.quality.expect_column_values_to_be_between("quantity", min=1, max=10000)
```

## Comparison to Other Tools

| Feature | dremioframe Expectations | [[dbt-expectations]] | [[great-expectations-for-data-contracts]] |
|---------|------------------------|----------------------|-------------------------------------------|
| Integration | Built into DataFrame pipeline | dbt package | Standalone library |
| Coverage | Basic (null, range) | 60+ tests | Extensive |
| Execution | In-memory after collect | SQL-based | SQL/Python |
| Maturity | Alpha | Mature | Mature |

## Limitations

- Limited to basic null and range checks in the current Alpha version.
- Runs after data is collected (in-memory), not as a pushdown validation.
- No integration with alerting or observability pipelines.
- Feature overlap with [[dbt-expectations]] and [[dbt-testing-patterns]] is not addressed by the library.

## Relationship

This feature connects to the broader [[data-quality-dimensions]] framework, specifically addressing Accuracy (range checks) and Completeness (null checks). It represents a lightweight, developer-friendly approach to data quality that complements more comprehensive tools like [[dbt-expectations]].