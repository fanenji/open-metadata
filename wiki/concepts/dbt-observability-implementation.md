---
type: concept
title: dbt Observability Implementation
created: 2026-04-07
updated: 2026-04-07
tags: [dbt, observability, monitoring, jinja, macros]
related: [on-run-end-hook, dbt-artifacts, data-observability-definition, dbt-testing-patterns, elementary-dbt-package, or-avidov, jonathan-talmi]
sources: ["dbt observability 101 How to monitor dbt run and test results.md"]
---
# dbt Observability Implementation

A lightweight, dbt-native pattern for monitoring dbt run and test results by logging execution metadata directly to the data warehouse using Jinja variables. This approach avoids the complexity of processing dbt artifact JSON files and meets four key criteria: storing results as simple tables, relying only on dbt functionality, integrating into routine runs, and having minimal performance impact.

## Motivation

In large dbt projects with parallel invocations, it is challenging to understand exactly which models and tests were executed and what the results were. Logging results over time enables detection of:
- Performance bottlenecks
- Models with deteriorating performance
- Flaky tests (by tracking test success rates over time)
- Test coverage gaps
- Problematic sources

## Implementation Steps

### Step 1: Identify Metadata to Collect

The dbt `results` Jinja variable (available only during an `on-run-end` hook) contains run result fields (status, execution time, rows affected) and node metadata (unique_id, database, schema, name, resource type). A unique `result_id` is created by concatenating `invocation_id` and node `unique_id`.

### Step 2: Create a Storage Table

Create an empty table (e.g., `dbt_results`) using a dbt model with an empty select query. This leverages dbt's full refresh, schema change strategies, and custom schema configuration.

### Step 3: Implement a Parsing Macro

Write a macro that flattens the nested result objects and extracts only the selected fields for insertion into the simple table.

### Step 4: Configure the on-run-end Hook

Create a macro that:
1. Receives the `results` variable as input
2. Flattens the results using the parsing macro
3. Inserts the flattened data into the storage table

Add the hook to `dbt_project.yml`:
```yaml
on-run-end:
  - "{{ my_observability_macro(results) }}"
```

## Limitations

- Captures less comprehensive metadata than full artifact processing (e.g., project metadata like model descriptions, test configurations are not included).
- The `results` Jinja variable is only available during `on-run-end` hooks, limiting when data can be collected.
- Tested primarily on Snowflake; other platforms may require minor adjustments.

## Relationship to Other Approaches

- **dbt artifacts:** The article critiques artifact processing as complex (nested, poorly documented, version-dependent). The Jinja approach avoids artifacts entirely.
- **Elementary dbt package:** Extends this basic pattern with richer metadata, dashboards, and alerts. However, Elementary itself processes artifacts, creating an internal tension.
- **Brooklyn Data dbt_artifacts package:** An alternative package for handling dbt artifacts.

## Connections

- [[data-observability-definition]] — Provides a concrete implementation of the "freshness" and "quality" dimensions.
- [[dbt-testing-patterns]] — Adds flaky test detection as a use case enabled by observability logging.
- [[on-run-end-hook]] — The dbt configuration mechanism central to this approach.
- [[dbt-artifacts]] — The alternative approach that this pattern avoids.
- [[elementary-dbt-package]] — The production-ready extension of this pattern.