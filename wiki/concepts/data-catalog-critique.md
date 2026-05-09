---
type: concept
title: Data Catalog Critique
created: 2026-05-07
updated: 2026-05-07
tags: [data-catalog, data-governance, metadata, critique]
related: [embedded-metadata, data-contract-platform, model-context-protocol, dbt-testing-patterns, data-catalog-as-a-broken-promise]
sources: ["Data Catalog - A Broken Promise.md"]
---
# Data Catalog Critique

The argument that traditional data catalogs fail to deliver value because they require users to learn a separate system that neither creates nor analyzes data. This critique, articulated by [[Ananth Packkildurai]], identifies a fundamental adoption barrier: users must be aware of the catalog's existence and trained to use it, despite the catalog being disconnected from their primary workflows.

## Core Thesis

Data catalogs are a "broken promise" because they demand effort from users without being integrated into the tools where data is actually created (e.g., dbt, Airflow) or analyzed (e.g., BI tools, notebooks). This creates a friction that undermines adoption and data governance initiatives.

## Proposed Evolution Paths

1. **Lose the Interface (Embedded Catalog)**: Embed metadata capture directly into data creation tools so that documentation and discovery happen automatically as part of existing workflows.
2. **Data Catalog → Knowledge Engine**: Transform passive catalogs into active systems that integrate into data creation via [[data-contract-platform]] and leverage ML/AI to auto-discover relationships between data assets.

## Tensions and Open Questions

- How do non-technical business users discover data if the catalog is embedded into engineering tools like dbt?
- Can a Data Contract platform satisfy compliance and audit requirements that demand a separate catalog interface?
- What empirical evidence exists that embedded metadata capture improves adoption over standalone catalogs?

## Connections to Wiki

This critique provides a counterpoint to catalog-centric data governance approaches. It aligns with the wiki's emphasis on [[embedded-metadata]] patterns and [[dbt-testing-patterns]] as alternatives to standalone governance tools. The "Knowledge Engine" vision connects to [[model-context-protocol]] as an AI-driven approach to data discovery.