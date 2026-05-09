---
type: concept
title: Convergent Evolution in Data Engineering
created: 2026-05-07
updated: 2026-05-07
tags: [data-engineering, methodology, patterns, framework]
related: [data-engineering-design-patterns, cache-pattern-data-engineering, lindy-effect-data-engineering, data-engineering-lifecycle]
sources: ["Patterns of Data Engineering.md"]
---
# Convergent Evolution in Data Engineering

Convergent evolution occurs when different systems independently develop similar solutions to identical problems. In data engineering, the field repeatedly "reinvents" similar concepts under new terminology — "parlance evolves faster than technology."

## Core Principle

The author traces the evolution of a caching pattern through multiple iterations:
- **Materialized Views** (Oracle, 1998)
- **One Big Table / Wide Tables** (denormalization techniques)
- **Snapshotting** (temporal caching)
- **Semantic Layers** (modern metric-focused caching)

Each represents the same fundamental goal: rapid data retrieval.

## Key Arguments

1. **Avoiding Hype** — New terminology doesn't necessarily indicate new technology. Understanding historical context prevents chasing buzzwords.
2. **The Lindy Effect** — Older, battle-tested techniques likely remain relevant longer than trendy alternatives.
3. **Pattern Recognition** — Identifying convergent evolutions reveals underlying design patterns with enduring value.

## Relationship to Three-Level Framework

Convergent Evolutions form the bottom level of the book's three-tier hierarchy:
- **Convergent Evolutions (CE)** — Technologies and approaches used daily
- **Data Engineering Patterns (DEP)** — Common themes from similar technologies
- **Data Engineering Design Patterns (DEDP)** — Best-practice solutions to specific challenges

Multiple convergent evolutions feed into patterns, which subsequently inform design patterns.

## Examples in the Book

The book identifies several convergent evolutions:
- Orchestration approaches (bash → stored procedures → ETL tools → Python)
- Schema management (schema evolution → data contracts → NoSQL)
- Data storage (warehouses → MDM → data lakes → reverse ETL → CDP)
- Caching (materialized views → OBT → dbt tables → OLAP cubes → DWA)
- Data access (BI dashboards → semantic layers → modern OLAP → data virtualization)