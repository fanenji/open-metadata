---
type: entity
title: Hierarchy View
created: 2026-05-14
updated: 2026-05-14
tags: [data-discovery, ui, navigation]
related: [data-discovery, unified-metadata-graph, openmetadata-features]
sources: ["guide-to-searching-data-using-hierarchical-view----20260514.md"]
---

# Hierarchy View

The Hierarchy View is a UI feature in [[openmetadata|OpenMetadata]] that organizes data assets in a structured, layered manner based on their relationships and dependencies. It provides an alternative to search-based discovery by allowing users to navigate a tree-like structure of the metadata graph.

## Usage

1. **Access**: Navigate to the Hierarchy View within the OpenMetadata interface.
2. **Navigate**: Expand or collapse different levels of the hierarchy to drill down into more specific data assets or to view higher-level parent assets.
3. **Inspect**: Click on a data asset within the hierarchy to view detailed information, metadata, or related data connections.

## Relationship to Other Features

- The Hierarchy View is one of several data discovery methods in OpenMetadata, complementing search and the [[unified-metadata-graph]].
- It is part of the broader [[openmetadata-features|OpenMetadata features]] for data discovery and exploration.

## Open Questions

- What determines the hierarchy structure? (Service → Database → Schema → Table, or something else?)
- How does the hierarchy relate to the unified metadata graph?
- Are there filtering or search capabilities within the hierarchy view?
- Does it support custom hierarchies or only the default organizational structure?