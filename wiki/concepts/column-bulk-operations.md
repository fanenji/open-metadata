---
type: concept
title: "Column Bulk Operations"
created: 2026-07-07
updated: 2026-07-07
tags: [openmetadata, governance, columns, metadata-management]
related: [openmetadata, custom-properties, data-governance, classification-tags, glossary-terms]
sources: ["Announcing OpenMetadata 1.12 1.md"]
---
# Column Bulk Operations

**Column Bulk Operations** is a feature introduced in OpenMetadata 1.12 that aggregates identical column names across all asset types (tables, topics, containers, APIs, search indexes) into a single management view, enabling unified governance at scale.

## Core Capabilities

- **Cross-Asset Aggregation**: Find all instances of a column name (e.g., `customer_id`) across every asset type in the platform — tables, topics, containers, APIs, and search indexes
- **Bulk Updates**: Set descriptions, tags, and glossary terms for all instances simultaneously in a single operation
- **Flexible Filtering**: Narrow operations by domain, tier, tags, or metadata status before applying changes

## Why It Matters

In enterprise environments, a column like `customer_id` may appear in 50+ tables with inconsistent documentation, tags, and ownership. Column Bulk Operations treats identical column names as a single governance entity, allowing data stewards to:

1. Find every instance of a column name
2. Apply consistent descriptions, tags, and glossary terms
3. Filter by domain or tier for targeted updates

This transforms governance from a per-asset manual process to an enterprise-wide automated one.

## Relationship to Other Features

- **[[custom-properties]]**: Column custom properties (also new in 1.12) can be managed through bulk operations
- **[[classification-tags]]**: Tags applied via bulk operations follow tag inheritance and propagation rules
- **[[glossary-terms]]**: Glossary terms can be bulk-assigned to columns across all assets
- **[[data-governance]]**: Column Bulk Operations is a key governance scalability feature

## See Also

- [[openmetadata]] — Platform overview
- [[custom-properties]] — Custom property management
- [[data-governance]] — Governance framework