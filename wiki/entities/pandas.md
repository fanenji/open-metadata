---
type: entity
title: Pandas
created: 2026-05-06
updated: 2026-05-06
tags: [python, data-analysis]
related: [data-quality-dimensions, ai-driven-data-quality]
sources: ["Automate Data Quality Checks with AI Agents-20260506.md"]
---
# Pandas

**Pandas** is a high-performance, open-source Python library used for data manipulation and analysis. It provides data structures like DataFrames that are essential for performing data quality checks.

## Use in Data Quality
Pandas is frequently used for basic, rule-based DQ checks, such as:
*   **Completeness**: Identifying missing values using `.isna().sum()`.
*   **Uniqueness**: Detecting duplicates using `.duplicated()`.
*   **Filtering**: Removing invalid entries using `.dropna()` or boolean indexing.
