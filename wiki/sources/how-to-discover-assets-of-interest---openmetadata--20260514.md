---
type: source
title: How to Discover Assets of Interest - OpenMetadata Documentation
created: 2026-05-14
updated: 2026-05-14
tags: [data-discovery, search, openmetadata]
related: [advanced-search, data-discovery, metadata-versioning, usage-metrics, elasticsearch-7x, tiers, data-lineage, data-profiling, soft-deletion]
sources: ["how-to-discover-assets-of-interest---openmetadata--20260514.md"]
---

# How to Discover Assets of Interest - OpenMetadata Documentation

This official OpenMetadata v1.12.x how-to guide describes the multiple complementary strategies for discovering data assets within the platform. It covers keyword search, quick filters (by owner, tag, tier, service, database, and deleted assets), filtering by importance (tiers and usage), discovering data through association (frequently joined tables and lineage relationships), advanced search with Boolean operators and faceted queries, and discovering data evolution via lineage and metadata versioning. The guide emphasizes that search APIs are backed by Elasticsearch and that usage metrics are captured during metadata/profiler ingestion.

## Key Topics

- **Keyword Search**: Matching names, descriptions, column names, and chart names across all asset types.
- **Quick Filters**: Pre-defined filter categories (Owner, Tag, Tier, Service, Service Type, Database, Schema, Columns) and the toggle for soft-deleted assets.
- **Filter by Importance**: Tiers for importance-based filtering; Usage (Last Updated, Weekly Usage, Relevance) for activity-based sorting.
- **Discover through Association**: Frequently joined tables/columns from the data profiler; upstream/downstream nodes from data lineage.
- **Advanced Search**: Boolean operators, faceted queries, syntax editor with and/or conditions, per-asset-type search options.
- **Discover Data Evolution**: Viewing lineage and metadata versioning to track asset changes over time.
- **Soft-Deleted Assets**: Searchable via toggle; read-only after deletion.