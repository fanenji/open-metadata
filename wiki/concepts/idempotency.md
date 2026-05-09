---
type: concept
title: Idempotency
created: 2026-04-29
updated: 2026-04-29
tags: [data-engineering, reliability, pipelines, architecture]
related: [ci-cd-for-data-pipelines, dbt-data-contract-implementation, fan-out-trap, network-shuffle, medallion-architecture]
sources: ["if-you-understand-these-5-data-engineering-terms-youre-ahead-of-90-of-the.md"]
---
# Idempotency

Idempotency is a property of a data pipeline where running it multiple times produces the **same final state** as running it once. It is the foundational reliability pattern that distinguishes junior from senior data engineering.

## Why It Matters

Data pipelines fail constantly — APIs go down, clusters run out of memory, source data arrives late. When a pipeline fails halfway through and must be rerun, an idempotent pipeline ensures the database state remains correct regardless of how many times it executes.

## Implementation Patterns

- **MERGE (Upsert):** Checks if a row already exists; if so, updates it; if not, inserts it. This is the most common idempotency pattern.
- **Drop-and-Replace Partitions:** Safely drops specific partitions and re-writes them, avoiding duplication.
- **Full Refresh:** Truncates the target table and re-writes all data (safe for small tables or batch windows).

## Anti-Pattern

Using plain `INSERT` without deduplication logic. Running an `INSERT`-only pipeline twice duplicates all data, corrupting dashboards and reports.

## Connection to Existing Wiki

- [[ci-cd-for-data-pipelines]] — Idempotency is a prerequisite for safe CI/CD in data workflows.
- [[dbt-data-contract-implementation]] — dbt's materializations (incremental, table, view) are designed with idempotency in mind.
- [[fan-out-trap]] — Non-idempotent joins can trigger Cartesian explosions that compound the problem.
