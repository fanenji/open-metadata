---
type: concept
title: ELT Pattern (Extract, Load, Transform)
created: 2026-04-04
updated: 2026-04-04
tags: [data-ingestion, architecture, pattern, elt]
related: [data-ingestion-architectural-patterns, etl-pattern, unified-data-repository-pattern, data-virtualization-pattern, CI-CD-for-data-pipelines]
sources: ["Data Ingestion — Part 1 Architectural Patterns.md"]
---
# ELT Pattern (Extract, Load, Transform)

A modern data processing paradigm that restructures the traditional ETL process. In ELT, Extract and Load operations transfer raw data directly to the data platform without immediate transformation. Transformation occurs subsequently, converting raw data into actionable insights, and can operate independently and on different schedules from extraction and loading.

## Benefits

- **Enhanced Flexibility** — Separation of extraction/loading from transformation enables selection of diverse tools for different data types and transformation standards.
- **Aligned Performance** — Transformation leverages the full computational power of the data platform, effective for massive datasets with distributed computing engines.
- **Improved Scalability** — Flexibility facilitates choice of transformation tools that excel in automation and scalability.

## Drawbacks

- **Governance of Multiple Tools** — Using different tools for extraction, loading, and transformation necessitates stringent governance for licensing, pricing, update cycles, and support.
- **Orchestration Challenges** — A more varied toolkit requires sophisticated orchestration (often DAG-based) to ensure transformations proceed only after successful data extraction and loading.

## Notes

The ELT pattern is often favored for its flexibility but demands a commitment to managing a multi-tool landscape and a complex orchestration strategy. It is a personal favorite of [[janmeskens]] for its adaptability.