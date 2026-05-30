---
type: concept
title: Advanced Search
created: 2026-05-14
updated: 2026-05-14
tags: ["search", "data-discovery", "openmetadata", "query-syntax", "query-builder"]
related: ["data-discovery", "faceted-search", "keyword-search", "advanced-search", "custom-properties", "elasticsearch-7x", "hierarchical-data-discovery"]
sources: ["data-discovery-openmetadata-how-to-guide---openmet-20260514.md", "add-complex-queries-using-advanced-search---openme-20260514.md"]
---

# Advanced Search

**Advanced Search** is a UI query builder on the Explore page in OpenMetadata that supports multiple conditions, grouped conditions, AND/OR logic, and field-specific operators. It is used for narrowing down search results in voluminous data.

## Key Characteristics

- **UI-based:** No need to write Elasticsearch queries; the interface provides a visual query builder.
- **Field-specific operators:** Conditions vary based on the selected field (e.g., "Any in" for tags, "Contains" for column names).
- **Grouping:** Conditions can be grouped to create complex boolean logic (e.g., (Owner = A OR Owner = B) AND (Service = X AND Database = Y)).
- **Complementary to Hierarchy View:** While [[hierarchical-data-discovery]] provides a tree-based navigation, Advanced Search offers a condition-based filtering approach.

## Custom Property Search Limitation

A critical constraint documented alongside this feature: [[elasticsearch-7x|Elasticsearch]] does not support searching for custom properties with Time, DateTime, or any date format other than `yyyy-MM-dd`. This limitation affects users who want to use [[custom-properties]] as searchable metadata fields.