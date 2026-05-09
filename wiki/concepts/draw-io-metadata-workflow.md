---
type: concept
title: draw.io Metadata Workflow
created: 2026-05-07
updated: 2026-05-07
tags: [metadata, diagram-generation, duckdb, draw-io, vscode, automation]
related: [diagrams-as-view-pattern, duckdb, draw-io, vscode, jaco-van-der-laan, embedded-metadata]
sources: ["Metadata-Driven Data Architecture Leveraging draw.io and VSCode for Scalable Design.md"]
---
# draw.io Metadata Workflow

An automated pipeline for generating data model diagrams from metadata, using [[DuckDB]] as the metadata store and [[draw.io]] as the visualization layer. The workflow is tool-agnostic in principle but specifically demonstrated with DuckDB and draw.io.

## Pipeline

```
YAML Mapping → Metadata DB (DuckDB) → Python Script → draw.io XML → .drawio File
```

## Components

1. **Source of Truth**: YAML/JSON mapping files defining data flows, transformations, filters, and joins.
2. **Metadata Store**: [[DuckDB]] stores parsed metadata from mapping files.
3. **Generation Script**: Python scripts read metadata from DuckDB and produce draw.io XML structures.
4. **Diagram Files**: `.drawio` files organized in a Git repository alongside mapping and SQL files.
5. **Editing Environment**: [[VSCode]] with the Draw.io Integration plugin for visual editing and clickable navigation.
6. **Publishing**: Diagrams exported as SVG/PNG and embedded into Confluence pages.

## Key Features

- **Consistency**: Automated generation ensures uniform layout, styling, and component naming.
- **Reusability**: Diagram components (functions, filters, joins) can be reused across diagrams.
- **Bidirectional Parsing**: Diagrams can be parsed back into DuckDB metadata for business stakeholder input.
- **Version Control**: All artifacts (mappings, diagrams, scripts) live in a Git repository.

## Connections to Existing Wiki

- [[DuckDB]] serves as the metadata store — extends DuckDB's documented role beyond query engine to metadata management.
- Aligns with [[embedded-metadata]] — capturing metadata in creation tools (YAML/JSON) rather than separate catalog interfaces.
- Complements [[dbt-osmosis]] — both automate documentation generation, but this approach is tool-agnostic and not tied to dbt.
- The code-first approach implicitly supports the [[data-catalog-critique]].