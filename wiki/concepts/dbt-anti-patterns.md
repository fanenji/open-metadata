---
type: concept
title: dbt Anti-Patterns
created: 2026-04-04
updated: 2026-04-04
tags: [dbt, anti-patterns, best-practices, analytics-engineering]
related: [dbt-incremental-strategy-guide, dbt-macro-minimalism, dbt-materialization-strategy-matrix, dbt-business-logic-testing, dbt-3-layer-architecture, dbt-testing-patterns, dbt-insert-by-period]
sources: ["Top 5 Advanced dbt Anti-Patterns That Nearly Killed Our Analytics Team.md"]
---
# dbt Anti-Patterns

A catalog of common dbt anti-patterns that can cause silent failures, performance degradation, and loss of trust in data. Advanced anti-patterns are particularly dangerous because they fail silently and spectacularly, unlike beginner mistakes which are usually caught quickly.

## The Five Advanced Anti-Patterns

### 1. Wrong Incremental Strategy
Using `append` strategy with `unique_key` (which append ignores), filtering on wrong columns, and missing late-arriving data. This causes silent data corruption through duplicates and missed updates.

**Fix:** Use `merge` strategy with a lookback window to catch late-arriving updates. Filter on source table date columns, not derived timestamps.

### 2. Macro Over-Engineering
Creating complex, multi-parameter macros that call other macros, making debugging nearly impossible. Error messages point to generated SQL, not source code.

**Fix:** Single-purpose macros ("Macro Minimalism") that are immediately readable. Macros should be used in 3+ models and should not call other macros.

### 3. Everything Incremental
Making small tables (15-365 rows) incremental for "performance," adding complexity without benefit. This creates debugging overhead and requires frequent `--full-refresh` runs.

**Fix:** Materialization Strategy Matrix: View for <1M rows, Table for <10M rows, Incremental only for >10M rows AND mostly append-only data.

### 4. Testing Theatre
Having many schema-only tests (unique, not_null, accepted_range) that pass while data is completely wrong. Tests catch schema violations but miss business logic failures.

**Fix:** Business Logic Testing — test reasonableness of metrics, data freshness, and cross-model consistency. Test what stakeholders actually care about.

### 5. Over-Architected Layers
Creating 7+ layer architectures that nobody can navigate. Simple changes take days instead of hours due to unclear layer boundaries.

**Fix:** Practical 3-Layer Architecture: Staging (1:1 with source, clean + rename), Intermediate (optional, only for reused logic), Marts (final business entities, wide and denormalized).

## Key Philosophy

"Boring but correct" patterns outperform clever, sophisticated ones in production. The goal is maintainability, debuggability, and reliability — not elegance or reusability.