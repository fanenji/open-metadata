---
type: concept
title: Data Ingestion Architectural Patterns
created: 2026-04-04
updated: 2026-04-04
tags: [data-ingestion, architecture, patterns, etl, elt, streaming]
related: [unified-data-repository-pattern, data-virtualization-pattern, etl-pattern, elt-pattern, push-vs-pull-ingestion, stream-processing-ingestion, janmeskens, data-federation-for-sensitive-data, ecl-framework, early-binding-vs-late-binding]
sources: ["Data Ingestion — Part 1 Architectural Patterns.md"]
---
# Data Ingestion Architectural Patterns

A framework for understanding the strategic choices in moving data from the operational plane (where data originates) to the analytical plane (where data is transformed into analytical products). The choice of pattern directly impacts organizational analytical capacity, scalability, governance, and real-time capabilities.

## Core Patterns

1. **[[unified-data-repository-pattern]]** — Single storage system (typically RDBMS) serving both operational and analytical needs. Simple but limited scalability and integration challenges.
2. **[[data-virtualization-pattern]]** — Specialized software layer that queries multiple underlying sources in real-time without moving data. Near-real-time access but network overhead and historical tracking challenges.
3. **[[etl-pattern]]** — Traditional Extract, Transform, Load paradigm where transformation occurs on a dedicated server. Centralized logic but vendor lock-in, performance bottlenecks, and limited scalability.
4. **[[elt-pattern]]** — Modern Extract, Load, Transform paradigm where raw data is loaded first, then transformed within the data platform. Enhanced flexibility and scalability but multi-tool governance and orchestration complexity.

## Emerging Patterns

5. **[[push-vs-pull-ingestion]]** — Distinction between analytical plane actively retrieving data (Pull) vs operational plane proactively sending data (Push). Push requires higher organizational maturity.
6. **[[stream-processing-ingestion]]** — Continuous flow of data enabling real-time processing. Two approaches: adapting ELT/ETL for streaming, or leveraging streaming caches analytically.

## Key Trade-offs

- **Simplicity vs Scalability**: Unified Repository is simplest but least scalable; ELT offers most flexibility but requires sophisticated orchestration.
- **Real-time vs Historical**: Data Virtualization and Stream Processing excel at near-real-time access but struggle with historical analysis ("time travel").
- **Control vs Flexibility**: ETL provides centralized control but risks vendor lock-in; ELT offers tool diversity but demands multi-tool governance.
- **Organizational Maturity**: Push patterns require high software development maturity; Pull patterns are more resilient to pipeline disruptions.

## Connections

- [[data-federation-for-sensitive-data]] shares the concept of querying across sources without moving data, similar to Data Virtualization.
- [[early-binding-vs-late-binding]] parallels the Push vs Pull distinction in terms of control flow.
- [[ECL-framework]] relates to ingestion patterns as foundational to the Extract phase.
- [[data-product-definition]] is downstream of ingestion architecture choices.
- [[CI-CD-for-data-pipelines]] is an operational concern for ingestion pipelines.