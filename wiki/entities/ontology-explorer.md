type: entity
title: Ontology Explorer
created: 2026-05-05
updated: 2026-05-05
tags: [openmetadata, ontology, ai-grounding, knowledge-graph, governance]
related: [openmetadata, semantic-context-graph, ontology-vs-similarity-ai-grounding, data-catalog-critique, shawn-gordon]
sources: ["ground-your-ai-in-standards-based-knowledge-with-ontology-explorer.md"]
---
# Ontology Explorer

Ontology Explorer is a feature shipping in **OpenMetadata 1.13** (Collate 1.13) that provides a dedicated interface for navigating and enriching the [[semantic-context-graph]] at the business concept level. It is built on open W3C standards including RDF, OWL, DCAT, DPROD, SKOS, PROV-O, and Schema.org.

## Key Capabilities

- **Formally modeled relationships:** Unlike similarity-based approaches, Ontology Explorer uses explicit, machine-readable relationships between business concepts (e.g., CAC → governedBy → GDPR, CAC → dependsOn → Conversion Rate).
- **Governance propagation:** A single ontology relationship automatically propagates compliance context to all assets implementing a concept, eliminating manual tag maintenance.
- **Isolated term counter:** Metrics showing concepts with no formal relationships, providing a gap signal for AI reasoning uncertainty.
- **Cross-glossary relationship surfacing:** Isolates relationships spanning multiple glossaries to reveal domain overlap or conflict.
- **Ambiguity handling:** When the ontology is incomplete, the system surfaces ambiguity by asking for clarification rather than silently guessing.

## Views

- **Overview:** Interactive graph of the entire business vocabulary, color-coded by glossary, with labeled edges.
- **Hierarchy View:** Tree view revealing parent-child structures and ontological depth.
- **Cross Glossary View:** Isolates relationships spanning multiple glossaries.
- **Data View:** Expands each term node to show tables, dashboards, and pipelines it governs, with quality scores, lineage, and ownership.

## Relationship to Knowledge Graph

Ontology Explorer and the [[openmetadata|Knowledge Graph]] are complementary views of the same underlying semantic context graph. Ontology Explorer starts from business concepts and maps how they relate to one another. Knowledge Graph starts from a data asset and shows everything connected to it.

## Target Users

- **Data stewards and governance teams:** Build and maintain the semantic graph, create relationships directly on the canvas, save graph states as named views.
- **Analysts and data scientists:** Navigate from a known concept to the assets that implement it, confirm governed canonical definitions.
