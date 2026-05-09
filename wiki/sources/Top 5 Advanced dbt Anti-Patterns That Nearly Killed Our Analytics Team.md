---
type: source
title: "Top 5 Advanced dbt Anti-Patterns That Nearly Killed Our Analytics Team"
created: 2026-04-04
updated: 2026-04-04
tags: [dbt, anti-patterns, analytics-engineering, best-practices]
related: [dbt-anti-patterns, dbt-incremental-strategy-guide, dbt-macro-minimalism, dbt-materialization-strategy-matrix, dbt-business-logic-testing, dbt-3-layer-architecture, dbt-testing-patterns, dbt-insert-by-period, data-quality-dimensions, shift-left-data-quality]
sources: ["Top 5 Advanced dbt Anti-Patterns That Nearly Killed Our Analytics Team.md"]
authors: [Reliable Data Engineering]
year: 2025
url: "https://medium.com/@reliabledataengineering/top-5-advanced-dbt-anti-patterns-that-nearly-killed-our-analytics-team-7e303a9fcaf1"
venue: "Medium"
---
# Top 5 Advanced dbt Anti-Patterns That Nearly Killed Our Analytics Team

A detailed account from the team at Reliable Data Engineering of five advanced dbt anti-patterns that caused significant production issues, along with the "boring but correct" solutions that fixed them. The article covers 18 months of mature dbt usage across 340 models, 89 macros, and 8 analytics engineers.

## Key Anti-Patterns

1. **The "Clever" Incremental Strategy** — Using `append` strategy with `unique_key` (which append ignores), filtering on wrong columns, and missing late-arriving data. Fix: `merge` strategy with a lookback window.
2. **Macro Over-Engineering Madness** — Creating complex, multi-parameter macros that call other macros, making debugging nearly impossible. Fix: single-purpose macros ("Macro Minimalism").
3. **The "Everything is Incremental" Obsession** — Making small tables (15-365 rows) incremental for "performance," adding complexity without benefit. Fix: Materialization Strategy Matrix (View <1M, Table <10M, Incremental >10M).
4. **Testing Theatre vs. Actual Quality** — Having 400+ schema-only tests that pass while data is completely wrong. Fix: Business Logic Testing (reasonableness, freshness, cross-model consistency).
5. **The "Sophisticated" Architecture** — Creating 7-layer architectures that nobody can navigate. Fix: Practical 3-Layer Architecture (Staging → Intermediate → Marts).

## Reported Results

- dbt run time: 23 min → 8 min (-65%)
- Data quality incidents: 3-4/week → 0.5/week (-85%)
- Snowflake compute: $8,400/month → $3,100/month (-63%)
- Incremental model failures: 12/month → 1/month (-92%)

## Key Philosophy

"Boring but correct" patterns outperform clever, sophisticated ones in production. The article emphasizes that advanced anti-patterns are more dangerous than beginner mistakes because they fail silently and spectacularly.