---
type: source
title: "Metadata-Driven Data Architecture: Leveraging draw.io and VSCode for Scalable Design"
created: 2026-05-07
updated: 2026-05-07
tags: [metadata, diagram-generation, draw-io, duckdb, vscode, data-modeling]
related: [jaco-van-der-laan, diagrams-as-view-pattern, draw-io-metadata-workflow, duckdb, embedded-metadata, dbt-osmosis, data-catalog-critique]
sources: ["Metadata-Driven Data Architecture Leveraging draw.io and VSCode for Scalable Design.md"]
authors: [Jaco van der Laan]
year: 2025
url: "https://medium.com/towards-data-engineering/metadata-driven-data-architecture-leveraging-draw-io-and-vscode-for-scalable-design-a785e96b0e4e"
venue: "Towards Data Engineering (Medium)"
---
# Metadata-Driven Data Architecture: Leveraging draw.io and VSCode for Scalable Design

A conceptual article proposing a metadata-driven workflow where diagrams are generated artifacts, not the source of truth. The approach uses [[DuckDB]] as a metadata store, Python scripts to generate [[draw.io]] XML, and [[VSCode]] as the primary editing environment for YAML/JSON mapping files.

## Summary

The article advocates for a **code-first** approach to data modeling and mapping maintenance. YAML/JSON files serve as the single source of truth for data flows, transformations, filters, and joins. From these files, diagrams are automatically generated via a pipeline: YAML Mapping → Metadata DB → Python Script → draw.io XML → .drawio File.

## Key Principles

- **Diagrams as a View, Not Source of Truth**: All diagrams are generated from metadata and can be parsed back when necessary.
- **Code-First Mapping Maintenance**: YAML/JSON files enable diffs, reviews, scripting, and testability.
- **Bidirectional Metadata-Diagram Parsing**: The workflow supports extracting metadata back from .drawio XML into DuckDB for business stakeholder input and reverse engineering.

## Workflow

1. Maintain mappings in YAML/JSON files within a Git repository.
2. Store metadata in DuckDB.
3. Run Python scripts to generate draw.io XML from metadata.
4. Open and edit `.drawio` files in VSCode using the Draw.io Integration plugin.
5. Optionally parse diagrams back into metadata for business input.
6. Publish diagrams to Confluence as SVG/PNG.

## Tooling

- [[draw.io]] (diagramming)
- [[DuckDB]] (metadata store)
- [[VSCode]] (IDE with Draw.io Integration plugin)
- YAML Language Server, JSON Schema validator, GitHub Copilot (validation and authoring)

## Connections to Existing Wiki

- Strongly aligns with [[embedded-metadata]] — capturing metadata in creation tools.
- Complements [[dbt-osmosis]] — both automate documentation generation from metadata, but this approach is tool-agnostic.
- Implicitly supports the [[data-catalog-critique]] by advocating code-as-source-of-truth over visual-first tools.

## Open Questions

- How does this workflow handle diagram layout and positioning at scale (hundreds of tables)?
- What happens when business users edit diagrams and those changes conflict with code-based mappings?
- How does this compare to existing data modeling tools (Erwin, ER/Studio, Hackolade) that already offer bidirectional model-diagram sync?