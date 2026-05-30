---
type: source
title: "Source: how-to-manually-add-or-edit-lineage---openmetadata-20260514.md"
created: 2026-05-15
updated: 2026-05-15
sources: ["how-to-manually-add-or-edit-lineage---openmetadata-20260514.md"]
tags: []
related: []
---

# Source: how-to-manually-add-or-edit-lineage---openmetadata-20260514.md

## Analysis: How to Manually Add or Edit Lineage

### Key Entities
- **OpenMetadata** (platform) — Central entity; the system providing the no-code lineage editor.
- **Lineage Editor** (UI tool) — Drag-and-drop interface for manually creating/editing lineage edges between data assets.
- **Data Assets** (tables, topics, dashboards, ML models, containers, pipelines) — Nodes in the lineage graph; the entities being connected.
- **Columns** (sub-entities) — Used for column-level lineage; visible when expanding a table node.

All entities likely already exist in the wiki (OpenMetadata, data-lineage, data-asset-ownership, etc.). The Lineage Editor as a specific UI tool may not have a dedicated page.

### Key Concepts
- **Manual Lineage Editing** — The ability to add or delete lineage edges via a drag-and-drop UI, supplementing automated lineage ingestion.
- **Column-Level Lineage** — Tracing data flow at the column granularity by linking columns between source and destination tables.
- **Edge Creation** — The fundamental operation: connecting a source data asset to a destination data asset to represent data flow.

These concepts likely exist in the wiki under [[data-lineage]] and [[data-lineage]] pages, but the manual editing workflow is not explicitly documented.

### Main Arguments & Findings
- **Core Claim**: OpenMetadata provides a no-code, drag-and-drop lineage editor for manually adding or editing lineage.
- **Supported Scope**: Both table-level and column-level lineage can be manually edited.
- **Supported Asset Types**: Tables, topics, dashboards, ML models, containers, and pipelines can be connected as nodes.
- **Workflow**: Select a data asset → navigate to Lineage Tab → click Edit → select destination asset type → search and select → create edge → optionally expand for column-level linking.
- **Evidence**: The source is official documentation; no empirical evidence is provided. The claim is a feature description, not a research finding.

### Connections to Existing Wiki
- **Directly related to**: [[data-lineage]] (the core concept page), [[data-lineage]] (overview page), [[how-column-level-lineage-works]] (if it exists).
- **Extends**: The existing lineage documentation by adding the manual editing workflow, which is complementary to automated lineage ingestion.
- **Strengthens**: The wiki's coverage of lineage capabilities by documenting the manual editing feature.

### Contradictions & Tensions
- **No contradictions** with existing wiki content.
- **Internal tension**: The source mentions "tables, topics, pipelines, dashboards, ML models, containers, and pipelines" — pipelines are listed twice, likely a typo.
- **Caveat**: Manual lineage editing is a supplementary feature; it does not replace automated lineage ingestion. The source does not discuss conflict resolution if both manual and automated lineage exist for the same edge.

### Recommendations
- **Create new page**: [[manual-lineage-editing]] — Document the drag-and-drop workflow, su
