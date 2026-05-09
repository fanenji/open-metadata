---
type: concept
title: Referential Integrity
created: 2024-05-22
updated: 2024-05-22
tags: [data-quality, database, dbt]
related: [dbt]
sources: ["A comprehensive guide to automating data testing in dbt.md"]
---
# Referential Integrity

**Referential integrity** is a fundamental concept in database design and data quality. It ensures that the relationship between tables remains consistent, specifically that a foreign key in a "child" table always points to a valid, existing primary key in a "parent" table.

## Implementation in dbt

In [[dbt]], referential integrity is enforced using the `relationships` generic test. This test validates that all values in a specific column of a child model exist in the referenced column of a parent model.

## Importance

Maintaining referential integrity is crucial for:
- **Data Accuracy**: Preventing "orphan" records that belong to non-existent entities.
- **Join Reliability**: Ensuring that downstream joins between tables produce expected results without losing data due to missing keys.
- **Downstream Trust**: Building confidence in the accuracy of complex, multi-layered data models.