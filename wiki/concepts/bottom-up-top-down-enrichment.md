---
type: concept
title: "Bottom Up Top Down Enrichment"
created: 2026-05-30
updated: 2026-05-30
tags: []
related: []
---

type: concept
title: Bottom-Up and Top-Down Enrichment
created: 2026-05-14
updated: 2026-05-14
tags: [knowledge-graph, metadata, enrichment]
related: [unified-metadata-graph, mcp-server, data-lineage, data-quality]
sources: ["Embedding an MCP Server into OpenMetadata.md"]
---

# Bottom-Up and Top-Down Enrichment

The unified knowledge graph in OpenMetadata is enriched through two complementary flows:

## Bottom-Up Enrichment

Metadata flows upward from the data infrastructure:

- **Physical metadata** from 90+ connectors — schemas, tables, pipelines, dashboards
- **Lineage** — column-level transformation tracking
- **Data profiling** — uniqueness, null counts, value distributions
- **Data quality test results** — pass/fail status of defined tests

## Top-Down Enrichment

Metadata flows downward from user interactions:

- **Documentation** — descriptions, comments, announcements
- **Ownership** — assignment of teams and users to assets
- **Tags and glossary terms** — business semantics and classification
- **Questions and conversations** — collaborative discussions about data
- **Policies** — governance rules applied to assets

## Significance

This dual-direction enrichment makes the knowledge graph "living and breathing" — it reflects both the technical reality of the data infrastructure and the human understanding of what the data means. This richness is what enables the embedded [[mcp-server|MCP server]] to provide LLMs with context that goes far beyond simple schema information, including quality signals, usage patterns, and business semantics.