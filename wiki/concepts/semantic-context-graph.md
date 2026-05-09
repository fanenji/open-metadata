---
type: concept
title: Semantic Context Graph
created: 2026-05-05
updated: 2026-05-07
tags: ["semantic-graph", "knowledge-graph", "ontology", "w3c", "metadata", "governance", "lineage"]related:
  - ontology-explorer
  - openmetadata
  - ontology-vs-similarity-ai-grounding
  - data-catalog-critique
  - ECL-framework
  - openmetadata-knowledge-graph
  - openmetadata-ontology-explorer
  - w3c-semantic-standards-for-data-platforms
  - context-store
  - contextualize-pipeline
sources: ["OpenMetadata - build-ai-you-can-trust-with-knowledge-graph.md", "ground-your-ai-in-standards-based-knowledge-with-ontology-explorer.md"]
related: ["openmetadata-knowledge-graph", "openmetadata-ontology-explorer", "w3c-semantic-standards-for-data-platforms", "context-store", "contextualize-pipeline"]
---
# Semantic Context Graph

## Introduction

A semantic context graph is a graph structure that connects business concepts, data assets, lineage, ownership, governance, teams, domains, and governance artifacts into a unified, machine-readable representation. It captures all formal relationships between these elements in a data platform. Built on open W3C semantic web standards (RDF, OWL, DCAT, DPROD, SKOS, PROV-O, Schema.org), it is portable, interoperable, and accessible to any tool that speaks the same standards. It is the foundation of Collate's approach to AI grounding and the basis on which AI agents reason.

## Components

- **Business concepts:** Formal definitions of terms (e.g., Customer Acquisition Cost, Revenue) with explicit relationships between them.
- **Data assets:** Tables, dashboards, pipelines, and other assets that implement business concepts.
- **Lineage:** How data flows between assets and how concepts depend on each other.
- **Ownership:** Who is responsible for each concept and asset.
- **Teams:** Organizational groups responsible for managing assets and concepts.
- **Domains:** Logical groupings of assets and concepts aligned with business functions.
- **Governance artifacts:** Compliance rules, policies, and regulations that apply to concepts and propagate to their implementing assets.

## Key Properties

- **Standards-based formal modeling:** Uses W3C standards (RDF, OWL, SKOS, PROV-O, DCAT, DPROD, Schema.org) for machine-readable knowledge representation, ensuring portability and interoperability.
- **Bidirectional navigation:** Relationships can be traversed from business concepts to data assets (via [[ontology-explorer]]) and from data assets to business concepts (via [[openmetadata|Knowledge Graph]]).
- **Real-time updates:** The graph updates immediately as metadata decisions are made (ownership assignments, domain additions, glossary term mappings).
- **Inference-capable:** Relationships that were never manually declared (ownership chains, reverse relationships, pipeline associations) can be automatically derived from existing metadata.
- **Automatic propagation:** Governance context defined at the concept level automatically applies to all implementing assets.
- **Gap detection:** The isolated term counter reveals concepts with no formal relationships.

## Concrete Implementations

The semantic context graph is the underlying structure that both [[ontology-explorer]] and the [[openmetadata|Knowledge Graph]] provide views into. More specific implementations in OpenMetadata 1.13 include:

- [[openmetadata-knowledge-graph]] — Asset‑centric view.
- [[openmetadata-ontology-explorer]] — Business‑glossary‑centric view.

## Role in AI Grounding and Trust

The semantic context graph is the foundation on which AI agents reason. If the graph is ambiguous or incomplete (e.g., "Revenue" maps to three different tables with no formal relationship), AI agents will not flag the ambiguity and will confidently return wrong answers. The graph provides the mechanism to find and fix gaps before AI reasons from the data, and it is the basis of Collate’s approach to AI grounding. The gap‑detection property (isolated term counter) helps identify concepts lacking formal relationships.

## Related Concepts and Connections

- Extends the [[ECL-framework]]’s emphasis on structured context by providing a concrete implementation mechanism.
- Addresses the [[data-catalog-critique]] by transforming passive catalogs into active, relationship-rich knowledge systems.
- Is a concrete implementation of a [[context-store]] for business semantics.
- Is the output store that a [[contextualize-pipeline]] would populate.
- Is a prerequisite for effective [[data-contract-platform]] enforcement.