---
type: source
title: Openmetadata Unified Knowledge Graph
created: 2026-02-13
updated: 2026-02-13
tags: [openmetadata, metadata, knowledge-graph, data-catalog]
related: [openmetadata, openmetadata-data-quality, openmetadata-unified-knowledge-graph, openmetadata-integration-patterns, data-catalog-tool-comparison, data-discovery-tools, data-catalog-critique]
sources: ["Openmetadata Unified Knowledge Graph.md"]
authors: []
year: 2026
url: ""
venue: ""
---
# Openmetadata Unified Knowledge Graph

This source document describes OpenMetadata's Unified Knowledge Graph, a centralized, graph-based repository that unifies metadata from diverse data assets, enabling discovery, observability, and governance across data ecosystems. It covers the core concept of structuring metadata as a graph with entities (datasets, tables, models) as nodes and relationships (lineage, ownership) as edges, creating a single source of truth for data teams.

## Key Points

- **Graph-based architecture**: Metadata is stored as interconnected nodes and edges, enabling scalable queries for discovery, lineage tracing, and governance.
- **Pull-based ingestion**: Over 100 connectors retrieve metadata from sources (databases, pipelines, dashboards) via pull mechanism, ensuring consistency and reliability.
- **Schema-first design**: Metadata structure is defined first via schemas, then implemented, supporting scalability and customization.
- **Four-component system**: API, ingestion, search, and UI components for simple deployment and upgrade.
- **Federation capability**: Integrates with existing data catalogs (DataHub, Amundsen, Atlas, Alation, Collibra) without forced migration, enabling cross-catalog query and unified lineage.
- **Lineage tracking**: Visualizes data flow across assets with manual drag-and-drop editing for accuracy.
- **Governance features**: Versioning, tags, compliance enforcement through the interconnected graph.

## Connections to Existing Wiki

- Strengthens [[openmetadata]] with detailed architectural description.
- Contextualizes [[openmetadata-data-quality]] as a feature powered by the graph.
- Provides integration details for [[data-catalog-tool-comparison]].
- Extends [[data-discovery-tools]] with graph-based discovery approach.
- May address some critiques in [[data-catalog-critique]] via graph-based federation.