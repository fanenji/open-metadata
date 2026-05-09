---
type: source
title: "Boost your dbt tests using Great Expectations in dbt"
created: 2026-04-04
updated: 2026-04-04
tags: [dbt, data-quality, testing]
related: [dbt-labs, great-expectations, dbt-best-packages]
sources: ["Boost your dbt tests using Great Expectations in dbt.md"]
authors: [Zoltan C. Toth]
year: 2022
url: "https://zoltanctoth.medium.com/boost-your-dbt-tests-using-great-expectations-in-dbt-1c2d33d53fb3"
venue: "Medium"
---
# Boost your dbt tests using Great Expectations in dbt

This article explores how to enhance standard dbt testing capabilities by integrating the `dbt-expectations` package, which brings advanced validation logic inspired by the [[great-expectations]] framework directly into the dbt workflow.

The author covers:
- **dbt Testing Basics**: Explaining singular, generic, and custom generic tests.
- **Advanced Validation**: Using `dbt-expectations` for regex matching, outlier detection (using standard deviation), and schema/shape integrity checks.
- **Implementation**: How to install the package via `packages.yml` and use it in `models.yml`.
