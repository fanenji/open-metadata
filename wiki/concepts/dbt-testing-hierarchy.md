---
type: concept
title: dbt Testing Hierarchy
created: 2026-04-07
updated: 2026-04-07
tags: [testing, dbt, strategy]
related: [dbt, dbt-unit-testing, data-diff]
sources: ["7 dbt testing best practices.md"]
---
# dbt Testing Hierarchy

An effective dbt testing strategy utilizes a multi-layered approach, balancing implementation effort against the type of coverage provided.

| Test Type | Effort | Coverage | Use Case |
| :--- | :--- | :--- | :--- |
| **Generic dbt Tests** | Medium | Medium | Fundamental integrity (nulls, uniqueness, relationships) |
| **dbt Unit Tests** | High | Low (Logic-specific) | Complex business logic validation |
| **Data Diffing** | Low | High (Unknown unknowns) | Detecting unforeseen impacts of code changes |

### Strategy Recommendation
1. **Foundation:** Use generic tests for essential quality checks.
2. **Precision:** Apply unit tests to a small share of critical/complex logic.
3. **Safety Net:** Use data diffing to catch the "long tail" of unexpected regressions.