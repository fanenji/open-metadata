---
type: entity
title: OpenMetadata 1.13 Features
created: 2026-05-05
updated: 2026-05-05
tags: [openmetadata, release-notes, semantic-layer]
related: [openmetadata-1.12-release-notes, knowledge-graph, ontology-explorer, data-goverance]
sources: ["announcing-openmetadata-1-13.md"]
---
# OpenMetadata 1.13 Features

OpenMetadata 1.13 introduces a semantic context layer designed to provide AI agents with the business context necessary for trustworthy reasoning.

## Core Capabilities

### Knowledge Graph
A feature that unifies technical metadata (schemas, lineage, ownership) with semantic metadata (glossary terms, classifications) into a single interactive, navigable graph. It supports W3C standards (RDF, OWL, DCAT, etc.) to ensure interoperability with AI agents via [[model-context-protocol-mcp]].

### Ontology Explorer
An interactive visual map for navigating and governing business ontologies. It allows users to trace business terms directly to physical data assets like tables, dashboards, and pipelines.

### Glossary Terms & Relations
Introduces a configurable schema layer for typed, RDF-compatible relationships between glossary terms (e.g., "calculated from", "is equivalent to"). This allows AI agents to reason over the relationships between business concepts rather than just guessing based on schema.

### Columns as Assets
A structural change where columns are treated as first-class, discoverable entities. This improves visibility for column-level governance, classifications, and quality rules.

## New Connectors
- **BurstIQ**: Blockchain-based healthcare/life sciences data.
- **SSRS**: SQL Server Reporting Services metadata and lineage.
- **Google Pub/Sub**: Messaging metadata (topics, subscriptions, schemas).
- **Matillion Data Cloud**: ETL pipeline metadata.
- **Airflow REST API**: Expanded integration for DAG and pipeline metadata.
- **Microsoft Fabric**: Support for Data Warehouse and Data Factory pipelines.