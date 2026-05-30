---
type: source
title: "What is a Glossary Term | Official Documentation - OpenMetadata Documentation"
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, glossary, data-governance, glossary-terms]
related: [glossary-terms, classification-tags, mutually-exclusive-glossary-terms, glossary-term-version-history, glossary-term-lifecycle, how-to-add-glossary-terms]
sources: ["what-is-a-glossary-term-official-documentation---o-20260514.md"]
authors: [OpenMetadata]
year: 2026
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/data-governance/glossary/glossary-term"
venue: "OpenMetadata Documentation v1.12.x"
---
# What is a Glossary Term | Official Documentation - OpenMetadata Documentation

This official documentation page defines a **Glossary Term** as a preferred terminology for a concept within OpenMetadata's data governance framework. It details the structure of a glossary term, including description, tags, synonyms, child terms, related terms, references, mutually exclusive configuration, reviewers, and associated assets. The page also covers the three-tab UI layout (Overview, Glossary Terms, Assets), tag propagation behavior, and version history rules (minor vs. major version changes).

## Key Points

- A Glossary Term is a preferred terminology for a concept, used to organize and discover data assets.
- Glossary terms can carry classification tags; when a term is applied to an asset, its tags propagate automatically.
- Terms support synonyms, child terms (for hierarchical relationships), and related terms (for associative relationships).
- The **Mutually Exclusive** configuration prevents assigning multiple terms from the same glossary/term to a single data asset.
- Each term has a life cycle status (e.g., Draft, Approved) and a set of reviewers.
- Version history: backward compatible changes → minor version (+0.1); backward incompatible changes → major version (+1.0).

## Connections

- Strengthens [[glossary-terms]] with detailed structural and behavioral definitions.
- Extends [[classification-tags]] by clarifying the tag propagation mechanism via glossary terms.
- Related to [[how-to-add-glossary-terms]] (procedural counterpart).
- Introduces concepts documented in [[mutually-exclusive-glossary-terms]], [[glossary-term-version-history]], and [[glossary-term-lifecycle]].