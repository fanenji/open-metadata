---
type: concept
title: OpenMetadata Unified Knowledge Graph
created: 2026-02-13
updated: 2026-02-13
tags: [openmetadata, knowledge-graph, metadata, data-catalog, governance]
related: [openmetadata, openmetadata-data-quality, openmetadata-integration-patterns, data-catalog-tool-comparison, data-discovery-tools, data-catalog-critique, datahub, amundsen]
sources: ["Openmetadata Unified Knowledge Graph.md"]
---
# OpenMetadata Unified Knowledge Graph

The OpenMetadata Unified Knowledge Graph is a centralized, graph-based repository that structures metadata as interconnected nodes and edges. It is the foundational architecture of [[openmetadata]], enabling discovery, observability, and governance across data ecosystems.

## Core Concept

Unlike traditional metadata storage (relational tables or flat files), the Unified Knowledge Graph represents:
- **Nodes (Entities)**: Datasets, tables, models, dashboards, pipelines, and other data assets.
- **Edges (Relationships)**: Lineage, ownership, joins, dependencies, and other connections between entities.

This graph structure creates a single source of truth for data teams, supporting interconnected insights and avoiding silos.

## Architecture

The graph is built on a **schema-first architecture** where metadata structure is defined first via schemas, then implemented. This design supports:
- **Scalability**: The graph can grow to thousands of assets without performance degradation.
- **Customization**: Custom entities and relationships can be added via APIs.
- **Extensibility**: New connectors and integrations can be developed without modifying core graph logic.

The graph is stored and queried through OpenMetadata's four-component system: API, ingestion, search, and UI.

## Metadata Ingestion

Metadata is ingested via a **pull-based mechanism** using over 100 connectors. The platform retrieves data from sources (databases, pipelines, dashboards) rather than relying on pushes, ensuring consistency and reliability. Connectors support:
- Scheduled ingestion for periodic updates
- Real-time updates via webhooks or APIs
- Bidirectional synchronization with existing catalogs

## Key Operations

- **Lineage Tracking**: Visualizes data flow across assets with manual drag-and-drop editing for accuracy.
- **Search and Discovery**: Combines advanced filters, profiling, and relationships for contextual asset location.
- **Governance Features**: Enforces versioning, tags, and compliance through the interconnected graph.
- **Federation**: Integrates with existing data catalogs ([[datahub]], [[amundsen]], Atlas, Alation, Collibra) without forced migration, enabling cross-catalog query and unified lineage.

## Benefits

- **Enhanced Discovery**: Complete context and lineage visualization for all assets.
- **Collaboration**: Streamlined UI for both technical and non-technical users.
- **Governance**: Versioning, tags, and compliance enforcement.
- **Interoperability**: Coexistence with existing catalogs via federation.

## Connections to Existing Wiki

- [[openmetadata]] — The platform that hosts the Unified Knowledge Graph.
- [[openmetadata-data-quality]] — Data quality features powered by the graph.
- [[openmetadata-integration-patterns]] — Integration with existing data catalogs.
- [[data-catalog-tool-comparison]] — Comparison with other catalog tools.
- [[data-discovery-tools]] — Graph-based discovery approach.
- [[data-catalog-critique]] — How the graph approach addresses catalog limitations.