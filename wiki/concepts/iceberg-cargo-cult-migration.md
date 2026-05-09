---
type: concept
title: Iceberg Cargo Cult Migration
created: 2026-04-04
updated: 2026-04-04
tags: [anti-pattern, apache-iceberg, migration, architecture]
related: [apache-iceberg, data-lakehouse, iceberg-maintenance-operations]
sources: ["Is Apache Iceberg Melting?.md"]
---
# Iceberg Cargo Cult Migration

A warning pattern for blind adoption of Apache Iceberg without matching the original constraints that made it successful. A cargo cult migration typically involves an organization copying a reference architecture (e.g., Netflix's Iceberg deployment) without understanding the underlying problems being solved.

## Characteristics

- Adopting Iceberg for headline features (time travel, ACID) without changing the operating model
- Ending up with more moving parts, more cost, and no measurable reliability or performance win
- Treating Iceberg like a database rather than a table layer that requires active maintenance

## Prevention

- Name the specific bottleneck you're removing before migration
- Commit to the operating model: catalog strategy, maintenance, engineering standards
- Use real success criteria (fewer correctness incidents, lower scan costs, faster schema changes)
- If you can't name the bottleneck, you're at high risk of building a cargo cult lakehouse
