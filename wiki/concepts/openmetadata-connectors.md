---
type: concept
title: OpenMetadata Connectors
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, connectors, ingestion, integration]
related: [openmetadata, ingestion-framework, unified-metadata-graph]
sources: ["OMD - Getting Started.md"]
---

# OpenMetadata Connectors

OpenMetadata provides a library of over 90 turnkey connectors for ingesting metadata from a wide variety of data sources. These connectors are a key differentiator, enabling rapid and comprehensive metadata ingestion without custom development.

## Supported Source Types

Connectors are available for:
- Data warehouses
- Data lakes
- Streaming platforms
- Dashboards
- ML models
- And many more

## Custom Sources

For data sources not covered by the turnkey connectors, OpenMetadata provides APIs to streamline custom metadata ingestion.

## Role in the Platform

Connectors are the primary mechanism for populating the [[unified-metadata-graph]]. They are managed by the [[ingestion-framework]], which handles the extraction, transformation, and loading of metadata from source systems into OpenMetadata.