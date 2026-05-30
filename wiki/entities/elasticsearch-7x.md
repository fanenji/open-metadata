---
type: entity
title: ElasticSearch 7.x
created: 2026-05-14
updated: 2026-05-14
tags: [search-engine, openmetadata, indexing, infrastructure]
related: [openmetadata, openmetadata-system-architecture, external-dependencies-configuration, change-events-system]
sources: ["openmetadata-system-architecture-developer-guide---20260514.md"]
---

# ElasticSearch 7.x

ElasticSearch 7.x is the search and analytics engine used by OpenMetadata to index metadata and power full-text search, discovery, and activity feeds. It is one of the four core architectural dependencies identified in the [[openmetadata-system-architecture]].

## Role in OpenMetadata

- Indexes all metadata entities for fast, relevance-ranked search
- Powers the activity feed by indexing [[change-events-system|change events]]
- Enables data discovery across the entire metadata catalog

## Version and Compatibility

The official v1.12.x architecture documentation specifies ElasticSearch 7.x. In practice, OpenMetadata also supports OpenSearch, as documented in [[external-dependencies-configuration]]. This version-specific reference reflects the documentation snapshot and may not represent the full range of supported search backends in all deployment scenarios.