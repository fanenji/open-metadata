---
type: source
title: "dbt observability 101: How to monitor dbt run and test results"
created: 2026-04-07
updated: 2026-04-07
tags: [dbt, observability, monitoring, jinja, macros]
related: [dbt-observability-implementation, or-avidov, elementary-dbt-package, data-observability-definition, dbt-testing-patterns, dbt-artifacts, on-run-end-hook]
sources: ["dbt observability 101 How to monitor dbt run and test results.md"]
---
# dbt observability 101: How to monitor dbt run and test results

**Author:** Or Avidov  
**Published:** 2022-08-10  
**URL:** https://medium.com/@oravidov/dbt-observability-101-how-to-monitor-dbt-run-and-test-results-f7e5f270d6b6

## Summary

This article presents a lightweight, dbt-native approach to monitoring dbt run and test results by leveraging Jinja variables (`results`, `graph`, `invocation_id`) within an `on-run-end` hook. The author argues that processing dbt artifact JSON files is unnecessarily complex (nested, poorly documented, version-dependent) and proposes instead a macro-based pattern that flattens result objects and inserts them directly into a warehouse table. The approach meets four criteria: storing results as simple tables, relying only on dbt functionality, integrating into routine runs, and having minimal performance impact.

## Key Contributions

- Introduces the concept of **dbt observability** (coined by Jonathan Talmi at Snap) as a distinct practice from general data observability.
- Provides a step-by-step implementation guide for logging dbt execution metadata to the warehouse using only built-in dbt features.
- Demonstrates how to create a unique `result_id` by concatenating `invocation_id` and node `unique_id`.
- Identifies practical use cases: detecting performance bottlenecks, flaky tests, test coverage gaps, and problematic sources.

## Caveats

- The code was tested only on Snowflake; minor adjustments may be needed for other platforms.
- The Jinja-based approach captures less comprehensive metadata than full artifact processing (e.g., project metadata like model descriptions, test configurations are not included).
- The article promotes the Elementary dbt package as a more feature-rich alternative, creating an internal tension: the article criticizes artifact processing, but Elementary itself processes artifacts.

## Connections

- [[dbt-observability-implementation]] — The concrete implementation pattern documented in this wiki.
- [[data-observability-definition]] — Provides a concrete implementation of the "freshness" and "quality" dimensions.
- [[dbt-testing-patterns]] — Adds flaky test detection as a use case enabled by observability logging.
- [[on-run-end-hook]] — The dbt configuration mechanism central to this approach.
- [[dbt-artifacts]] — The alternative approach that the article critiques.
- [[elementary-dbt-package]] — The recommended package for richer observability.