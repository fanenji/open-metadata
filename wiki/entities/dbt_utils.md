---
type: entity
title: dbt_utils
created: 2024-05-22
updated: 2024-05-22
tags: [dbt, package, sql]
related: [dbt, surrogate-key-generation]
sources: ["A comprehensive guide to automating data testing in dbt.md"]
---
# dbt_utils

`dbt_utils` is a widely used package for [[dbt]] maintained by dbt Labs. It provides a collection of SQL generators, Jinja helpers, and generic tests that extend the core functionality of dbt.

## Key Features

- **SQL Generators**: Macros that automate the creation of complex SQL structures.
- **Jinja Helpers**: Utilities to simplify complex logic within dbt models.
- **Surrogate Key Generation**: One of its most critical features is the `generate_surrogate_key` macro, which allows engineers to create unique identifiers by hashing multiple columns. This is particularly useful for models that lack a natural primary key.

## Usage Example

Using the `generate_surrogate_key` macro to create a unique ID from multiple columns:

```sql
SELECT 
  {{ dbt_utils.generate_surrogate_key(['full_name', 'gender', 'acquired_at']) }} AS surrogate_key,
  ...
FROM {{ ref('users') }}
```