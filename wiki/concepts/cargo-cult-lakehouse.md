---
type: concept
title: Cargo Cult Lakehouse
created: 2026-04-04
updated: 2026-04-04
tags: [anti-pattern, lakehouse, architecture, migration]
related: [data-lakehouse, iceberg-cargo-cult-migration, iceberg-maintenance-operations]
sources: ["Is Apache Iceberg Melting?.md"]
---
# Cargo Cult Lakehouse

A warning pattern where organizations adopt a lakehouse architecture without a clear bottleneck to solve, leading to increased complexity without measurable payoff.

## Characteristics

- Adopting lakehouse as a "badge" rather than to solve a specific problem
- Not committing to the operating model (catalog, maintenance, engineering standards)
- Expecting Iceberg to be a "free upgrade" rather than an infrastructure investment

## Prevention

- Name the specific bottleneck you're removing before migration
- Use real success criteria: fewer correctness incidents, lower scan costs, faster schema changes
- If you can't name the bottleneck, you're at high risk of building a cargo cult lakehouse
