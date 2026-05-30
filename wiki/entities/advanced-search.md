---
type: entity
title: Advanced Search
created: 2026-05-14
updated: 2026-05-15
tags: [search, data-discovery, openmetadata, ui-feature]
related: [data-discovery, elasticsearch-7x, usage-metrics, tiers, soft-deletion, hierarchical-data-discovery, custom-properties, guide-to-searching-data-using-hierarchical-view, reindexing-search]
sources: ["how-to-discover-assets-of-interest---openmetadata--20260514.md", "add-complex-queries-using-advanced-search---openme-20260514.md"]
---

# Advanced Search

**Advanced Search** is a power-user discovery feature in OpenMetadata that provides a UI-based query builder on the Explore page. It enables finding data assets matching strict criteria across multiple metadata properties, supporting Boolean operators, faceted queries, and a syntax editor for constructing complex search expressions. It is designed to help narrow down search results in voluminous data estates.

## Capabilities

- **Boolean Operators**: Combine search terms with AND, OR, NOT logic.
- **Faceted Queries**: Search for specific facets of data assets (e.g., by column name, schema, database).
- **Syntax Editor / Query Builder**: Write and/or conditions directly using the UI-based query builder, or construct complex queries with multiple grouped conditions.
- **Per-Asset-Type Options**: Separate advanced search interfaces are available for Tables, Topics, Dashboards, Pipelines, ML Models, Containers, Glossary, and Tags.

## Supported Search Fields

Advanced Search allows filtering on the following fields:

- Deleted
- Owner
- Tags
- Tier
- Service
- Database
- Database Schema
- Column

## Supported Conditions

The available conditions vary based on the selected field:

- Equal to
- Not equal to
- Any in
- Not in
- Contains
- Does not contain

## Query Building

Users can add multiple conditions and group them together using AND/OR logical operators:

- **AND**: All conditions must be satisfied.
- **OR**: Any one of the conditions must be satisfied.

### Example

A complex query can be constructed with two groups:

1. **Owner group**: Multiple owners defined with OR logic (any one owner matches).
2. **Service/Database/Schema/Column group**: Specific data location criteria with AND logic.

## Custom Property Search Limitation

Elasticsearch does not support searching for custom properties with the following formats:

- Time
- DateTime
- Any date formats other than `yyyy-MM-dd`

This is a critical constraint for users planning to use custom properties for searchable metadata. See [[custom-properties]] for more details.

## Relationship to Other Discovery Methods

Advanced Search complements [[data-discovery|keyword search]] and [[usage-metrics|quick filters]] by providing strict multi-parameter criteria that cannot be expressed through simple filters alone. It is the most precise discovery method in the OpenMetadata toolkit.

Alternative discovery methods include:

- [[hierarchical-data-discovery]] — Explore data assets via a tree-like structure.
- [[guide-to-searching-data-using-hierarchical-view]] — Procedural guide for the Hierarchy View.
- [[reindexing-search]] — Maintenance operation to rebuild the search index.

## Open Questions

- Does Advanced Search support saved searches or search history?
- What is the exact syntax for the Boolean query language?