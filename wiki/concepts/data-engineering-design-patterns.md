---
type: concept
title: Data Engineering Design Patterns (DEDP)
created: 2026-05-07
updated: 2026-05-07
tags: [data-engineering, design-patterns, architecture, framework]
related: [convergent-evolution-data-engineering, cache-pattern-data-engineering, dynamic-querying-pattern, data-lakehouse, data-asset-reusability-pattern, workspace-packaging-pattern]
sources: ["Patterns of Data Engineering.md"]
---
# Data Engineering Design Patterns (DEDP)

Data Engineering Design Patterns represent higher-level architectural solutions to common data engineering challenges. Unlike Data Engineering Patterns (DEPs), these are conceptual frameworks rather than ready-to-implement code.

## Three-Level Framework

The book organizes knowledge from bottom-up:

| Level | Description | Examples |
|---|---|---|
| **Convergent Evolutions (CE)** | Technologies and approaches used daily | dbt, Data Lake, Message Queue, Microservices |
| **Patterns (DEP)** | Common themes from similar technologies | Caching, ELT, Data Lineage, Observability |
| **Design Patterns (DEDP)** | Best-practice solutions to specific challenges | Dynamic Querying, Real-Time Platform, Cost Management |

## Key Design Patterns

| Pattern | Description |
|---|---|
| **Dynamic Querying** | Ad-hoc query capability without reprocessing |
| **Stratified Data Flow Modeling** | Layered data flow design |
| **Open Data Platform (Lakehouse)** | Unified analytics and data science workloads |
| **Asset-based Governance** | Data products as discoverable, trusted resources |
| **Declarative Pipelines** | Intent-driven rather than implementation-driven pipeline definition |

## What DEDPs Provide

- Architecture blueprints and conceptual integration guidance
- Examples of similar implementations
- Best practices for specific problems
- Framework for long-term, sustainable data architecture

DEDPs operate beyond typical industry hype cycles, providing sustainable guidance for navigating data engineering decisions and building robust, long-term data platforms.