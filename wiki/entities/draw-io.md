---
type: entity
title: draw.io
created: 2026-05-07
updated: 2026-05-07
tags: [tool, diagramming, visualization]
related: [diagrams-as-view-pattern, draw-io-metadata-workflow, jaco-van-der-laan, vscode]
sources: ["Metadata-Driven Data Architecture Leveraging draw.io and VSCode for Scalable Design.md"]
---
# draw.io

An open-source diagramming application used for creating ERDs, mapping diagrams, and other visual representations of data architecture. In the [[draw-io-metadata-workflow]], draw.io serves as the **visualization layer** — diagrams are generated from metadata stored in [[DuckDB]] and can be parsed back into metadata when needed.

## Key Features in the Workflow

- **XML-based file format** (.drawio) that can be programmatically generated and parsed.
- **VSCode Integration**: The Draw.io Integration plugin allows editing `.drawio` files directly within [[VSCode]].
- **Confluence Publishing**: Diagrams can be exported as SVG/PNG and embedded into Confluence pages.

## Role in the Architecture

- Diagrams are **views**, not the source of truth.
- Generated automatically from YAML/JSON mapping files via a Python → DuckDB → draw.io XML pipeline.
- Support bidirectional parsing: metadata can be extracted from diagrams back into DuckDB.