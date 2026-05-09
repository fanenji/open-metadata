---
type: concept
title: Interactive Data Lineage
created: 2026-04-08
updated: 2026-04-08
tags: [data-lineage, visualization, openmetadata, data-governance]
related: [local-llm-openmetadata-extension, openmetadata, data-observability-three-pillars, data-root-cause-analysis]
sources: ["Local LLM for OpenMetadata - Visual Studio Marketplace.md"]
---
# Interactive Data Lineage

A visual representation of data flow showing upstream and downstream table relationships, rendered as an interactive graph. Implemented in the [[local-llm-openmetadata-extension]] via the `LineageService.ts` component.

## Features

- **Interactive Graph**: Users can click + buttons to expand relationships, - buttons to collapse, drag nodes to reposition, and zoom with the mouse wheel.
- **Upstream/Downstream Views**: Shows both sources (upstream) and dependents (downstream) of any table.
- **IDE Integration**: Lineage visualization appears directly in VS Code, eliminating the need to switch to a web-based catalog.

## Relevance to Wiki

Interactive data lineage is a key component of [[data-observability-three-pillars]] (Metrics, Metadata, Lineage). It supports [[data-root-cause-analysis]] by enabling engineers to trace data issues through dependency chains. This implementation demonstrates lineage visualization in an IDE context, complementing the wiki's existing coverage of lineage in [[openmetadata]] and [[datahub]].