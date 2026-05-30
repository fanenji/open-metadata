---
type: concept
title: Faceted Search
created: 2026-05-14
updated: 2026-05-14
tags: [search, data-discovery, openmetadata, user-interface]
related: [data-discovery, advanced-search, classification-tags, glossary-terms]
sources: ["data-discovery-openmetadata-how-to-guide---openmet-20260514.md"]
---

# Faceted Search

Faceted search is a search interface that allows users to filter results by multiple dimensions or attributes simultaneously. In OpenMetadata, faceted search is the primary mechanism for narrowing down data assets among thousands of datasets.

## How It Works

Users can apply filters across different facets (categories) to progressively narrow search results. Common facets in OpenMetadata include:
- **Asset Type** — Table, Topic, Dashboard, Pipeline, ML Model, Container, Glossary, Tag
- **Service** — The source system (e.g., Snowflake, PostgreSQL, Superset)
- **Database / Schema** — For database assets
- **Owner** — Team or user responsible for the asset
- **Tags** — [[classification-tags]] applied to the asset
- **Glossary Terms** — [[glossary-terms]] associated with the asset
- **Tier** — Importance or criticality ranking

## Purpose

Faceted search addresses the core challenge of [[data-discovery]]: finding the right data among thousands of assets. Without rich metadata and faceted filtering, users would need to browse through large lists or rely solely on keyword matches, which is inefficient for large data estates.

## Relationship to Other Search Modes

Faceted search complements [[keyword-search]] (basic text search) and [[advanced-search]] (complex queries). Users typically start with a keyword search and then use facets to refine results, or use facets directly to browse by category.

## See Also

- [[data-discovery]] — The overall data discovery framework
- [[advanced-search]] — Complex query syntax for precise searches
- [[classification-tags]] — Tags used as facets for filtering