---
type: entity
title: VSCode
created: 2026-05-07
updated: 2026-05-07
tags: [tool, ide, development-environment]
related: [draw-io, diagrams-as-view-pattern, draw-io-metadata-workflow, jaco-van-der-laan]
sources: ["Metadata-Driven Data Architecture Leveraging draw.io and VSCode for Scalable Design.md"]
---
# VSCode

Visual Studio Code, the primary integrated development environment in the [[draw-io-metadata-workflow]]. It serves as the central workspace for maintaining mapping files, editing diagrams, and validating metadata.

## Role in the Workflow

- **Code-First Mapping Maintenance**: YAML/JSON mapping files are authored and validated in VSCode.
- **Diagram Editing**: The Draw.io Integration plugin enables opening and editing `.drawio` files directly.
- **Clickable Navigation**: Diagram components can link to YAML/JSON or SQL files, bridging visual and code layers.
- **Validation**: YAML Language Server, JSON Schema validator, and custom linters ensure mapping file correctness.
- **AI Assistance**: GitHub Copilot assists in authoring mapping files.

## File Structure

```
/data-models
  /mappings
    orders_to_dwh.yaml
  /diagrams
    orders_mapping.drawio
  /sql
    orders_to_dwh.sql
```