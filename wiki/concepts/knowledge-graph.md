---
type: concept
title: Knowledge Graph
created: 2026-07-15
updated: 2026-07-15
tags: [knowledge-graph, semantic-web, agentic-ai, ontology]
related: [unified-metadata-graph, ontology-explorer, agentic-ai, mcp-server, openmetadata-features]
sources: ["https://blog.open-metadata.org/build-ai-you-can-trust-with-knowledge-graph-00ab12b3488a"]
---

# Knowledge Graph

An interactive, asset-centric visualization of the [[unified-metadata-graph]] in OpenMetadata 1.13. It renders the full relationship context surrounding any data asset — tables, dashboards, pipelines — with labeled edges making every connection explicit.

## Purpose

AI agents are only as reliable as the semantic foundation they reason from. If a business concept like "Revenue" maps to three different tables with no formal relationship, an AI agent (via [[mcp-server]]) will pick one definition and confidently return a wrong answer. Knowledge Graph lets teams **verify the graph before AI reasons from it**, finding and fixing semantic gaps.

## What It Shows

For any data asset, Knowledge Graph displays:

- **Ownership** — Teams and users responsible for the asset
- **Schema hierarchy** — From service down to table
- **Business semantics** — Glossary terms and definitions mapped to the asset
- **Downstream consumers** — Analysts, dashboards, ML models using the asset
- **Change history** — Last modification and by whom

## Key Features

- **Depth slider** — Controls graph expansion from immediate neighbors to entire ecosystem
- **Bidirectional queries** — From asset → connections, or from team/domain/glossary term → governed assets
- **Automatic inference** — Derives relationships from existing metadata (ownership chains, reverse relationships, pipeline associations) without manual declaration
- **Real-time updates** — Every metadata decision (owner assignment, domain, tagging) immediately reflects as a new relationship

## Relationship to Ontology Explorer

Knowledge Graph and [[ontology-explorer]] are complementary views of the same underlying semantic graph:

- **Knowledge Graph** — Asset-centric: starts from a table/dashboard/pipeline
- **Ontology Explorer** — Business-glossary-centric: starts from business concepts

Together they provide both directions: from data assets upward into business meaning, and from business concepts downward into implementing data.

## Version

Introduced in **OpenMetadata 1.13** (April 2026).