---
type: source
title: "Patterns of Data Engineering: Timeless Practices from Convergent Evolution"
created: 2026-05-07
updated: 2026-05-07
tags: [data-engineering, design-patterns, architecture, convergent-evolution, reference]
related: [convergent-evolution-data-engineering, data-engineering-design-patterns, cache-pattern-data-engineering, dynamic-querying-pattern, semantic-layer-evolution, orchestration-evolution, workspace-packaging-pattern, data-asset-reusability-pattern, lindy-effect-data-engineering, data-engineering-lifecycle]
sources: ["Patterns of Data Engineering.md"]
authors: [Simon Späti]
year: 2025
url: "https://dedp.online"
venue: ""
---
# Patterns of Data Engineering

An evolving online book by Simon Späti that explores fundamental design patterns in data engineering discovered through the lens of convergent evolution. The book argues that different systems independently develop similar solutions to identical problems, and recognizing these patterns helps practitioners avoid chasing hype and focus on fundamentals.

## Core Framework

The book organizes knowledge into a three-level hierarchy:

1. **Convergent Evolutions (CE)** — Technologies and approaches used daily (e.g., dbt, Data Lake, Message Queue)
2. **Data Engineering Patterns (DEP)** — Common themes from similar technologies (e.g., Caching, ELT, Data Lineage)
3. **Data Engineering Design Patterns (DEDP)** — Best-practice solutions to specific challenges (e.g., Dynamic Querying, Open Data Platform)

## Key Arguments

- **Caching is the universal underlying pattern** — Materialized views, OBT, dbt tables, OLAP cubes, semantic layers, and data virtualization all fundamentally implement caching
- **The Lindy Effect applies** — Older, battle-tested techniques likely remain relevant longer than trendy alternatives
- **Declarative approaches dominate** — Modern data engineering is moving from imperative to intent-driven approaches
- **AI reinforces fundamentals** — Rather than replacing data engineers, AI will increase focus on data quality, modeling, and presentation

## Major Design Patterns

- **Dynamic Querying** — Enabling ad-hoc analysis without full pipeline re-runs, with four pillars: no-code interface, reusable templates, logical data model, materialization/caching
- **Stratified Data Flow Modeling** — Layered data flow design
- **Open Data Platform (Lakehouse)** — Unified analytics and data science workloads
- **Asset-based Governance** — Data products as discoverable, trusted resources
- **Declarative Pipelines** — Intent-driven pipeline definition

## Convergent Evolution Examples

The book traces multiple convergent evolutions including:
- Bash scripts → Stored Procedures → ETL Tools → Python Scripts (orchestration)
- Schema Evolution → Data Contracts → NoSQL (schema management)
- Data Warehouses → MDM → Data Lakes → Reverse ETL → CDP (data storage)
- Materialized Views → OBT → dbt Tables → OLAP Cubes → DWA (caching)
- BI Dashboards → Semantic Layers → Modern OLAP → Data Virtualization (data access)

## Author

Simon Späti is a data engineer with 20+ years of experience, creator of the Data Engineering Vault and ssp.sh, which ranks as a top Google result for Data Engineering content.