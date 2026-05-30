---
type: source
title: "Source: get-a-quick-glance-of-the-data-assets---openmetada-20260514.md"
created: 2026-05-15
updated: 2026-05-15
sources: ["get-a-quick-glance-of-the-data-assets---openmetada-20260514.md"]
tags: []
related: []
---

# Source: get-a-quick-glance-of-the-data-assets---openmetada-20260514.md

## Analysis of: Get a Quick Glance of the Data Assets - OpenMetadata Documentation

### Key Entities

- **Explore page** — Central UI page in OpenMetadata where data assets are displayed as cards. Central to the source.
- **Data Asset Card** — UI component showing basic info (Source, Name, Description, Owner, Tier, Usage). Central.
- **Quick Preview (right side panel)** — UI panel providing a quick glance at a data asset upon clicking empty space next to it. Central.
- **Data Asset Types** — Table, Topic, Dashboard, Pipeline, ML Model, Container, Glossary, Tag. Central; each has a distinct preview.
- **Data Quality and Profiler Metrics** — Metrics displayed in preview (Tests Passed, Aborted, Failed). Central.
- **Tags** — Classification tags associated with a data asset, viewable in preview. Central.
- **Schema** — Column names, types, and descriptions viewable in preview. Central.

**Wiki Status:** All entities likely already exist in the wiki (e.g., [[data-profiling]], [[data-quality]], [[classification-tags]], [[glossary-terms]], [[hierarchy-view]]). The "Explore page" and "Quick Preview" are UI features not yet explicitly documented as standalone pages.

### Key Concepts

- **Preview based on Data Asset Type** — The quick preview panel dynamically shows type-specific information (e.g., partitions for topics, algorithm for ML models, reviewers for glossaries). Matters because it demonstrates context-aware UI design.
- **Data Asset Card** — A compact summary view for each asset in the Explore page. Matters as the primary discovery interface.
- **Quick Preview Panel** — A right-side panel providing a richer, type-specific preview without navigating to the full detail view. Matters for efficient data discovery.

**Wiki Status:** These are UI/UX concepts not yet documented as standalone wiki pages. They relate to [[hierarchy-view]] and [[data-discovery]] concepts.

### Main Arguments & Findings

- **Core Claim:** OpenMetadata provides a two-tier preview system: (1) basic info on data asset cards in the Explore page, and (2) a richer, type-specific quick preview in a right-side panel.
- **Evidence:** The source is official documentation; it describes the feature with examples for each data asset type.
- **Strength:** High — official documentation for v1.12.x.

### Connections to Existing Wiki

- **Related Pages:** [[hierarchy-view]] (alternative discovery method), [[data-profiling]] (profiler metrics), [[data-quality]] (test metrics), [[classification-tags]] (tags in preview), [[glossary-terms]] (glossary preview), [[teams-and-users]] (owner display), [[tiers]] (tier display).
- **Relationship:** This source **extends** existing knowledge by documenting the UI preview layer — a feature that surfaces the metadata described in other pages (profiling, quality, tags, ownership) in a compact, discoverable format.

### Contradictions & Tensions

- **No contradictions** with existing wiki content.
- **No internal tensions** — the source is straightforward
