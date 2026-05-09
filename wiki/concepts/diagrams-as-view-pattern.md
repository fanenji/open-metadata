---
type: concept
title: Diagrams as a View, Not Source of Truth
created: 2026-05-07
updated: 2026-05-07
tags: [metadata, diagram-generation, data-modeling, governance]
related: [draw-io-metadata-workflow, embedded-metadata, data-catalog-critique, dbt-osmosis, jaco-van-der-laan, draw-io, duckdb, vscode]
sources: ["Metadata-Driven Data Architecture Leveraging draw.io and VSCode for Scalable Design.md"]
---
# Diagrams as a View, Not Source of Truth

A core principle in metadata-driven data architecture: diagrams should be **generated artifacts** derived from a code-based source of truth, not the primary design mechanism.

## Rationale

- **Version Control**: Code (YAML/JSON) enables diffs, reviews, and traceability that binary diagram formats cannot.
- **Automation**: Diagrams can be regenerated consistently whenever metadata changes.
- **Consistency**: Automated generation ensures uniform layout, styling, and component naming across all diagrams.
- **Testability**: Mapping files can be validated with schemas, linters, and custom scripts.

## Workflow

1. Maintain mappings in YAML/JSON files (single source of truth).
2. Store metadata in a database (e.g., [[DuckDB]]).
3. Run Python scripts to generate draw.io XML from metadata.
4. Open generated `.drawio` files in [[VSCode]] for review.
5. Optionally parse diagrams back into metadata for business stakeholder input.

## Bidirectional Parsing (Pragmatic Compromise)

While code is the primary source of truth, the workflow supports parsing diagrams back into metadata. This enables:
- Early conceptual design sessions
- Business stakeholder input
- Diagram reverse engineering

This creates a potential tension: if business users edit diagrams and those changes propagate to metadata, diagrams become a de facto source of truth. The workflow treats this as a pragmatic compromise, not a contradiction.

## Connections to Existing Wiki

- Aligns with [[embedded-metadata]] — capturing metadata in creation tools rather than separate catalog interfaces.
- Complements [[dbt-osmosis]] — both automate documentation generation from metadata, but this approach is tool-agnostic.
- Supports the [[data-catalog-critique]] by advocating code-as-source-of-truth over visual-first tools.
- Contrasts with traditional data modeling tools (Erwin, ER/Studio) that use diagrams as primary design surfaces.