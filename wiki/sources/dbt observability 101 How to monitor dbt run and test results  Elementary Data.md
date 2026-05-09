---
type: source
title: "Source: dbt observability 101 How to monitor dbt run and test results  Elementary Data.md"
created: 2026-05-07
updated: 2026-05-07
sources: ["dbt observability 101 How to monitor dbt run and test results  Elementary Data.md"]
tags: []
related: []
---

# Source: dbt observability 101 How to monitor dbt run and test results  Elementary Data.md

# Analysis: "dbt observability 101: How to monitor dbt run and test results | Elementary Data"

## Key Entities

| Entity | Type | Role | In Wiki? |
|--------|------|------|----------|
| **Or Avidov** | Person (Author) | Central — author of the guide, likely affiliated with Elementary Data | No |
| **Elementary Data** | Organization/Product | Central — provides the dbt observability package and platform | No (only `elementary-data` referenced in sources) |
| **Jonathan Talmi** | Person | Peripheral — credited for coining "dbt observability" at Snap | No |
| **dbt** | Tool/Platform | Central — the subject being monitored | Yes (multiple pages) |
| **dbt artifacts** | Concept/File format | Central — JSON files storing run results and metadata | No |
| **dbt Jinja variables** (graph, results, invocation_id) | Feature | Central — mechanism for extracting metadata | Partially (dbt-dispatch-pattern, dbt-testing-patterns) |
| **dbt on-run-end hook** | Feature | Central — execution context for logging | No |
| **dbt_results table** | Artifact/Table | Central — storage table for logged results | No |
| **Brooklyn Data dbt_artifacts package** | Tool/Package | Peripheral — alternative implementation | No |
| **Elementary dbt package** | Tool/Package | Central — production-ready implementation | No |

## Key Concepts

| Concept | Definition | Importance | In Wiki? |
|---------|------------|------------|----------|
| **dbt observability** | Monitoring dbt run results, test outcomes, and project metadata over time | Core thesis — enables detection of performance bottlenecks, flaky tests, coverage gaps | No |
| **dbt artifacts** | JSON files (manifest, run_results, catalog) produced by dbt commands | Foundation — contain all execution metadata but are hard to process programmatically | No |
| **Jinja variable extraction** | Using `results`, `graph`, and `invocation_id` Jinja variables to access metadata during hooks | Key implementation technique — avoids separate artifact processing pipeline | No |
| **on-run-end hook** | dbt configuration that executes macros after each command | Essential — only context where `results` variable is available | No |
| **Result object structure** | Nested dictionary with run result fields + graph node fields | Technical detail — must be flattened for table storage | No |
| **Incremental table pattern** | Using dbt incremental models with unique_key for storing run results | Implementation pattern — enables historical tracking | No |

## Main Arguments & Findings

### Core Claims
1. **dbt artifacts are insufficient for monitoring** — They are hard to process (nested, poorly documented, version-dependent) and require separate orchestration.
2. **Jinja variables provide a better approach** — `results`, `graph`, and `invocation_id` expose the same metadata within dbt's execution context, enabling simpler integration.
3. **A self-contained monitoring solution is achievable** — Using only dbt functionality (macros, hooks, incremental
