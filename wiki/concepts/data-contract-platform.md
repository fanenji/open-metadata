---
type: concept
title: Data Contract Platform
created: 2026-05-07
updated: 2026-05-07
tags: [data-contract, data-governance, metadata, data-quality]
related: [data-catalog-critique, embedded-metadata, dbt-testing-patterns, model-context-protocol]
sources: ["Data Catalog - A Broken Promise.md"]
---
# Data Contract Platform

A system that enforces agreements between data producers and consumers, integrated into the data creation process rather than being a post-hoc documentation tool. Proposed by [[Ananth Packkildurai]] as an evolution path for data catalogs, transforming passive metadata repositories into active governance systems.

## Key Characteristics

- **Proactive Enforcement**: Data contracts define expectations (schema, quality, freshness) that are validated at creation time, not documented after the fact.
- **Workflow Integration**: Contracts are defined and enforced within the tools that produce data (dbt, Airflow, streaming platforms).
- **Machine-Readable**: Contracts are expressed in a format that can be automatically validated and monitored.

## Relationship to Data Catalogs

A Data Contract platform addresses the core critique of traditional data catalogs: it doesn't require users to learn a separate system. Instead, it embeds governance into the creation workflow. This aligns with the [[embedded-metadata]] pattern.

## Connections to Wiki

- [[dbt-testing-patterns]] — dbt tests and contracts (e.g., `dbt_project.yml` contracts) are a form of data contract enforcement.
- [[model-context-protocol]] — MCP could expose data contracts to AI agents for automated compliance checking.
- [[data-catalog-critique]] — This concept is proposed as a solution to the "broken promise" of data catalogs.