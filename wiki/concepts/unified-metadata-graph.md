---
type: concept
title: Unified Metadata Graph
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, metadata, graph, architecture]
related: [openmetadata, openmetadata-connectors, data-lineage, data-quality]
sources: ["OMD - Getting Started.md"]
---

# Unified Metadata Graph

The Unified Metadata Graph is a core architectural concept in [[OpenMetadata]]. It is a single graph database that organizes all metadata ingested from source systems into a comprehensive, interconnected representation of an organization's entire data estate.

## Purpose

The Unified Metadata Graph serves as the single source of truth for all metadata, eliminating the need for practitioners to switch between multiple catalogs, quality, or governance tools. It enables:

- **Discovery:** Finding data assets through natural language search, filtering, and faceting.
- **Lineage:** Tracking table and column-level lineage across the data estate.
- **Quality:** Mapping quality test results to data assets and lineage.
- **Governance:** Applying business glossaries, classification tags, and automated PII classification.

## Relationship to Other Components

- Metadata is ingested from 90+ source systems via [[openmetadata-connectors]] and custom APIs.
- The graph is accessible through a unified user interface.
- It underpins features like [[data-lineage]], [[data-quality]], and governance automation.

## Open Questions

- What is the actual relationship between the Unified Metadata Graph and the underlying database (e.g., Elasticsearch, Neo4j)?
- How do "quality lineage maps" technically integrate with the existing lineage tracking in the graph?