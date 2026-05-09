---
type: source
title: "Data Catalog - A Broken Promise"
created: 2026-05-07
updated: 2026-05-07
tags: [data-catalog, data-governance, metadata, data-contracts, knowledge-engine]
related: [data-catalog-critique, embedded-metadata, data-contract-platform, model-context-protocol, dbt-testing-patterns]
sources: ["Data Catalog - A Broken Promise.md"]
authors: [Ananth Packkildurai]
year: 2022
url: "https://www.dataengineeringweekly.com/p/data-catalog-a-broken-promise"
venue: "Data Engineering Weekly"
---
# Data Catalog - A Broken Promise

A critique of data catalogs arguing that they fail because they require users to learn a separate system that neither creates nor analyzes data. The author proposes two evolution paths: embedding metadata capture into data creation tools, and transforming passive catalogs into active knowledge engines.

## Key Arguments

- **The Broken Promise**: Data catalogs create an adoption barrier by requiring users to be aware of and trained on a separate tool that doesn't participate in data creation or analysis.
- **Evolution Path #1 — Lose the Interface**: Embed catalog functionality directly into data creation tools (e.g., dbt, Airflow) so metadata is captured automatically without a separate UI.
- **Evolution Path #2 — Data Catalog to Knowledge Engine**: Transform passive catalogs into active systems that integrate into data creation workflows via Data Contract platforms, and leverage ML/AI to auto-discover relationships between data assets.

## Connections

This source aligns with the wiki's emphasis on [[embedded-metadata]] patterns and [[dbt-testing-patterns]] as alternatives to standalone governance tools. The "Knowledge Engine" vision connects to [[model-context-protocol]] as an AI-driven approach to data discovery.