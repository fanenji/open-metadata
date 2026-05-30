---
type: concept
title: Hierarchical Data Discovery
created: 2026-05-14
updated: 2026-05-14
tags: [data-discovery, navigation, ui]
related: [hierarchy-view, data-discovery, unified-metadata-graph]
sources: ["guide-to-searching-data-using-hierarchical-view----20260514.md"]
---

# Hierarchical Data Discovery

Hierarchical Data Discovery is a method of exploring data assets in [[openmetadata|OpenMetadata]] by navigating a tree-like structure that reflects relationships and dependencies between assets. It provides an alternative to search-based discovery, enabling users to browse the metadata catalog in a structured, layered manner.

## Core Interaction Pattern

- **Drill-down Navigation**: Expanding hierarchy levels to move from higher-level parent assets to more specific child assets.
- **Collapse**: Contracting hierarchy levels to return to broader views.
- **Asset Selection**: Clicking an asset in the hierarchy to open its detailed view, including metadata, connections, and related information.

## Relationship to the Unified Metadata Graph

The hierarchical view is a visual representation of the [[unified-metadata-graph]], presenting the graph's structure in a navigable tree format. It leverages the same relationship data that powers lineage and discovery features.

## Comparison with Search-Based Discovery

| Aspect | Hierarchical Discovery | Search-Based Discovery |
|--------|------------------------|------------------------|
| Approach | Browse by structure | Query by keyword |
| Best for | Understanding relationships and context | Finding specific assets quickly |
| User action | Navigate and expand | Type and filter |
| Learning curve | Low for structured exploration | Requires knowledge of asset names |