---
type: source
title: "Source: DBT Tests That Catch Real Bugs and How to Wire CI.md"
created: 2026-05-07
updated: 2026-05-07
sources: ["DBT Tests That Catch Real Bugs and How to Wire CI.md"]
tags: []
related: []
---

# Source: DBT Tests That Catch Real Bugs and How to Wire CI.md

## Key Entities

- **Sai Kumar Devulapelli** (Author) — Central role. Senior Data Engineer, author of the guide. Likely does not exist in the wiki.
- **dbt** (Tool) — Central. The entire article is about dbt testing and CI. Already exists in the wiki (e.g., [[dbt-testing-patterns]], [[dbt-slim-ci]], [[dbt-cloud]]).
- **dbt-utils** (Package) — Peripheral. Referenced for `expression_is_true` test. Already exists in the wiki (via [[dbt-insert-by-period]]).
- **GitHub Actions** (CI Platform) — Peripheral. Used as example CI runner. Not in the wiki.
- **dbt Cloud** (Platform) — Peripheral. Mentioned as alternative CI pattern. Already exists in the wiki ([[dbt-cloud]]).
- **BigQuery / Snowflake / Redshift / Postgres** (Warehouses) — Peripheral. Mentioned as adapter examples. Some exist in the wiki ([[snowflake-zero-copy-clone]], [[snowflake-manual-clustering]]).

## Key Concepts

- **Real-bug-catching tests** — Tests targeting actual failure modes (duplicate business keys, orphan facts, future timestamps, SCD2 overlaps, row-count explosions) rather than just `unique` and `not_null`. Central to the article. Likely does not exist as a named concept in the wiki.
- **Slim CI** — CI/CD strategy running only changed models and their dependencies using `state:modified+`. Already exists in the wiki ([[dbt-slim-ci]]).
- **Drift guards** — Tests that fail on abnormal changes in row counts or key cardinality. Not explicitly in the wiki, but related to [[dbt-ci-testing-strategy]].
- **SCD2 invariants** — Tests ensuring no overlapping or gap validity ranges in slowly changing dimensions. Not in the wiki.
- **Source freshness** — Monitoring that source data arrives within expected time windows. Already exists in the wiki ([[data-observability-definition]]).
- **Exposures** — dbt feature tying models to dashboards/apps for impact analysis. Not in the wiki.
- **Deterministic tests** — Tests that produce consistent results by bounding time windows and avoiding non-deterministic functions. Not in the wiki.

## Main Arguments & Findings

- **Core claim**: Most dbt projects rely on insufficient default tests (`unique`, `not_null`) that miss real-world failure modes. A targeted test suite covering keys, integrity, enums, ranges, time sanity, SCD2 invariants, and drift guards catches actual bugs.
- **Evidence**: The article provides copy-paste SQL macros for each test type (composite uniqueness, recent_enough, scd2_no_overlaps, volume_didnt_jump, key_cardinality_guard) and a complete CI workflow (GitHub Actions YAML).
- **Evidence strength**: Moderate. The article is a practical guide with working code examples, but no empirical data or case studies demonstrating bug catch rates. The arguments are logical and based on common data engineering failure modes.

## Connections to Existing Wiki

- **Strengthens**: [[dbt-testing-patterns]] — Provides concrete, copy-paste examples of advanced tests beyond the categorization in the existing page.
- **Strengthens**: [[dbt-slim-ci]] —
