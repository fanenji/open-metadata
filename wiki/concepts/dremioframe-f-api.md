---
type: concept
title: dremioframe F Function Builder API
created: 2026-04-04
updated: 2026-04-04
tags: [dremio, python, api, expression-builder]
related: [dremioframe, dremio]
sources: ["Introducing dremioframe - A Pythonic DataFrame Interface for Dremio.md"]
---

# dremioframe F Function Builder API

The **F function builder API** is a module within [[dremioframe]] that enables programmatic construction of SQL expressions using Python objects, similar to PySpark's `F` module or R's dplyr. It allows developers to build dynamic queries without writing raw SQL strings.

## Core Functions

- **`F.col("column_name")`**: References a column by name.
- **`F.lit("value")`**: Injects a literal value into an expression.
- **`F.case()`**: Builds a SQL `CASE WHEN` expression via `.when(condition, value).else_(default).end()`.
- **Arithmetic operators**: Standard Python operators (`+`, `-`, `/`, `*`) work on `F.col()` objects.
- **Comparison operators**: `==`, `!=`, `>`, `<`, `>=`, `<=` produce SQL conditions.
- **`.alias("name")`**: Assigns an alias to an expression.

## Example

```python
from dremioframe import F

df = client.table("Samples.samples.dremio.com.zips.json") \
           .select(
               F.col("city"),
               F.col("state"),
               F.col("pop"),
               (F.col("pop") / 1000).alias("pop_thousands"),
               F.case()
                 .when(F.col("pop") > 100000, F.lit("large"))
                 .else_(F.lit("small"))
                 .end()
                 .alias("pop_label")
           ) \
           .filter(F.col("state") == F.lit("TX")) \
           .limit(10) \
           .collect()
```

## Use Cases

- Building queries dynamically based on user input or configuration.
- Creating reusable expression components.
- Avoiding SQL injection risks by using structured expressions.
- Mixing with standard string expressions in `.select()` and `.mutate()`.

## Relationship

The F API is the programmatic counterpart to the string-based expressions used in [[dremioframe]]'s `.select()` and `.mutate()` methods. Both approaches compile to the same optimized SQL under the hood.