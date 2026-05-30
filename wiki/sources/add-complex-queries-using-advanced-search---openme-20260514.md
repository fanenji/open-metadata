---
type: source
title: "Add Complex Queries using Advanced Search - OpenMetadata Documentation"
created: 2026-05-14
updated: 2026-05-14
tags: [data-discovery, advanced-search, elasticsearch, custom-properties]
related: [advanced-search, custom-properties, elasticsearch-7x, hierarchical-data-discovery]
sources: ["add-complex-queries-using-advanced-search---openme-20260514.md"]
---

# Add Complex Queries using Advanced Search - OpenMetadata Documentation

**Source:** https://docs.open-metadata.org/v1.12.x/how-to-guides/data-discovery/advanced

This official documentation page describes the **Advanced Search** feature in OpenMetadata v1.12.x, a UI-based query builder on the Explore page for constructing complex search queries with multiple and grouped conditions.

## Key Content

- **Advanced Search** is a quick and easy-to-use UI query builder for complex data discovery queries.
- **Supported search fields:** Deleted, Owner, Tags, Tier, Service, Database, Database Schema, Column.
- **Supported conditions:** Equal to, Not equal to, Any in, Not in, Contains, Does not contain. Conditions vary based on the selected field.
- **Grouping:** Multiple conditions can be added and grouped together using AND/OR logic.
- **Example:** A complex query with two groups — one for Owner (OR logic) and one for Service/Database/Schema/Column (AND logic).

## Custom Property Search Limitation

Elasticsearch does not support searching for custom properties with the following formats:
- Time
- DateTime
- Any date formats other than `yyyy-MM-dd`

This is a critical constraint for users planning to use custom properties for searchable metadata.