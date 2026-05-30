---
type: entity
title: Search Indexes
created: 2026-05-14
updated: 2026-05-14
tags: [entity-type, elasticsearch, opensearch, ingestion]
related: [elasticsearch-7x, unified-metadata-graph, stored-procedures]
sources: ["OpenMetadata Community Meeting Oct 2023 Release 1 2 0 datamesh openmetadata.md"]
---
# Search Indexes

Search Indexes are a new entity type introduced in [[OpenMetadata]] 1.2.0, representing ElasticSearch or OpenSearch indexes as ingestible and viewable metadata entities. This feature exposes the internal search infrastructure as first-class citizens in the [[unified-metadata-graph]].

## Capabilities

- **Ingestion**: Indexes can be ingested from connected ElasticSearch or OpenSearch services.
- **Metadata display**: Shows field mappings, analyzers, normalizers, and index-specific settings.
- **Standard operations**: Supports the full suite of entity operations — descriptions, tags, glossary terms, ownership, and tier assignment.
- **Sample data**: Can display sample data from the index for UI exploration.

## Relationship to Platform

This feature makes the search backend transparent to users, allowing them to understand how OpenMetadata structures its search indexes and what mappings are in use. It also enables governance and documentation of the search infrastructure itself.