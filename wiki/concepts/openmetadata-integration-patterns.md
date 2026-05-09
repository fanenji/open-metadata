---
type: concept
title: OpenMetadata Integration Patterns
created: 2026-02-13
updated: 2026-02-13
tags: [openmetadata, integration, data-catalog, federation, connectors]
related: [openmetadata, openmetadata-unified-knowledge-graph, datahub, amundsen, data-catalog-tool-comparison, data-catalog-critique]
sources: ["Openmetadata Unified Knowledge Graph.md"]
---
# OpenMetadata Integration Patterns

OpenMetadata integrates with existing data catalogs and metadata sources through a library of over 100 pre-built connectors. These connectors support bidirectional metadata ingestion, enabling coexistence and federation without forced migration.

## Supported Catalogs

OpenMetadata provides connectors for major data catalogs:
- [[datahub]] — Event-based open-source metadata platform.
- [[amundsen]] — Open-source data catalog (originally by Lyft).
- **Atlas** — Apache Atlas, open-source metadata and governance platform.
- **Alation** — Commercial data catalog platform.
- **Collibra** — Commercial data governance platform.

## Integration Process

1. **Configure the connector**: Via YAML or UI, specifying credentials and filters for entities to import.
2. **Run ingestion**: Populate the [[openmetadata-unified-knowledge-graph]] with existing metadata, preserving ownership and glossaries.
3. **Enable federation**: Enable cross-catalog query and unified lineage, with options for push-back of updates.

## Integration Modes

- **Pull-based ingestion**: OpenMetadata retrieves metadata from source catalogs via connectors, ensuring consistency and reliability.
- **Scheduled ingestion**: Periodic updates to keep metadata synchronized.
- **Real-time updates**: Via webhooks or APIs for immediate synchronization.
- **Bidirectional sync**: Updates made in OpenMetadata can be pushed back to source catalogs.

## Federation Benefits

- **Single pane of glass**: Unified view across multiple catalogs without forced migration.
- **Unified lineage**: Lineage tracking across assets from different catalogs.
- **Cross-catalog query**: Search and discover assets across all integrated catalogs.
- **Reduced operational complexity**: Manage multiple catalogs through a single interface.

## Extensibility

For catalogs not natively supported, OpenMetadata allows custom connector development via plugins. This enables integration with proprietary or legacy systems.

## Connections to Existing Wiki

- [[openmetadata]] — The platform that provides these integration capabilities.
- [[openmetadata-unified-knowledge-graph]] — The graph that stores integrated metadata.
- [[data-catalog-tool-comparison]] — Comparison of OpenMetadata with other catalog tools.
- [[data-catalog-critique]] — How federation addresses catalog fragmentation.
- [[datahub]] — One of the supported integration targets.
- [[amundsen]] — Another supported integration target.