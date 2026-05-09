---
type: concept
title: Surrogate Key Generation
created: 2024-05-22
updated: 2024-05-22
tags: [data-engineering, dbt, primary-key]
related: [dbt_utils, dbt]
sources: ["A comprehensive guide to automated data testing in dbt.md"]
---
# Surrogate Key Generation

**Surrogate key generation** is the process of creating a unique, artificial identifier for a record, typically by hashing a combination of one or more natural columns.

## Purpose

In many modern data warehouse environments, source tables may lack a single, unique primary key. Surrogate keys are used to:
- **Ensure Uniqueness**: Create a reliable primary key for downstream modeling.
- **Simplify Joins**: Provide a single, consistent column to join on, rather than multiple columns.
- **Handle Changing Attributes**: Maintain identity even when natural keys (like names or addresses) change.

## Implementation in dbt

The most common way to implement this in [[dbt]] is via the `generate_surrogate_key` macro provided by the [[dbt_utils]] package. This macro takes a list of columns, handles null values (often by coalescing them), and applies a hashing function (like MD5) to produce a unique string.

## Example

If a table lacks a `user_id` but has `email` and `signup_date`, a surrogate key can be generated:

```sql
{{ dbt_utils.generate_surrogate_key(['email', 'signup_date']) }} AS user_pk
```