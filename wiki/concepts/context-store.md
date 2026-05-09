---
type: concept
title: Context Store
created: 2026-03-14
updated: 2026-03-14
tags: [data-engineering, infrastructure, semantics, context, metadata]
related: [ecl-framework, contextualize-pipeline, early-binding-vs-late-binding, context-propagation, context-architect-role, data-product-definition, data-contract-versioning-strategy]
sources: ["Data Engineering After AI.md"]
---
# Context Store

The **Context Store** is a new infrastructure component proposed by [[Ananth Packkildurai]] as part of the [[ECL-framework]]. It is a dedicated, versioned, queryable store of semantic definitions, entity classifications, and relationship maps.

## Purpose

The Context Store is where business definitions live — not as documentation in a wiki, not as logic baked into a Gold table, but as versioned, validated artifacts that downstream systems can query and trust. It distinguishes queryable data from trustworthy data.

## Key Properties

- **Versioned** — Context artifacts track changes over time, enabling auditability and rollback
- **Queryable** — Downstream systems (including AI agents) can query the store for grounded context
- **Validated** — Only artifacts that pass the [[contextualize-pipeline]] validation workflow are stored
- **Lineage-aware** — Context artifacts are linked to the lineage of the data they describe

## Relationship to Other Concepts

- **vs. [[data-product-definition]]**: The Context Store formalizes the semantics of data products
- **vs. [[data-contract-versioning-strategy]]**: Extends contract versioning to cover all semantic artifacts
- **vs. [[data-catalog-critique]]**: The Context Store is embedded in pipeline infrastructure, not a separate catalog interface
- **vs. [[embedded-metadata]]**: The Context Store is the destination for context propagated via metadata

## Open Questions

- How to govern ownership of the Context Store across teams
- How to adjudicate conflicts between competing semantic definitions
- How discovered context graduates to prescribed context
- Tooling for the Context Store is still maturing