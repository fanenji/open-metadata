---
type: concept
title: W3C Semantic Standards for Data Platforms
created: 2026-05-06
updated: 2026-05-06
tags: [w3c, semantic-web, rdf, owl, dcat, skos, provenance, metadata-standards]
related: [semantic-context-graph, openmetadata-knowledge-graph, openmetadata-ontology-explorer, data-catalog-tool-comparison]
sources: ["OpenMetadata - build-ai-you-can-trust-with-knowledge-graph.md"]
---
# W3C Semantic Standards for Data Platforms

The OpenMetadata Knowledge Graph and Ontology Explorer are built on a foundation of open W3C semantic web standards. These standards bring decades of research in knowledge representation into the data platform in a portable, interoperable way.

## Standards Used

| Standard | Full Name | Purpose |
|----------|-----------|---------|
| **RDF** | Resource Description Framework | Core data model for representing relationships as subject-predicate-object triples. The foundational graph data model. |
| **OWL** | Web Ontology Language | Formal ontology language for defining rich relationships, constraints, and class hierarchies between concepts. |
| **DCAT** | Data Catalog Vocabulary | Standard vocabulary for describing datasets and data catalogs. Enables catalog interoperability. |
| **DPROD** | Data Product Vocabulary | Vocabulary for describing data products as units of data exchange. Relevant to [[data-product-definition]]. |
| **SKOS** | Simple Knowledge Organization System | Standard for representing taxonomies, thesauri, and controlled vocabularies. Used for glossary terms. |
| **PROV-O** | Provenance Ontology | Standard for representing provenance information — who did what, when, and with what. Used for lineage and change history. |
| **Schema.org** | Schema.org | Broad vocabulary for structured data on the web. Provides common types for entities like organizations, people, and events. |

## Relevance to Data Platforms

- **Portability:** Because the graph is built on open standards, it is not locked into any vendor. Any tool that speaks RDF/OWL can consume the graph.
- **Interoperability:** Standards like DCAT and DPROD enable catalog-to-catalog and platform-to-platform data exchange.
- **Future-proofing:** The standards are mature, widely adopted, and maintained by the W3C, ensuring long-term stability.
- **AI readiness:** Semantic web standards were designed for machine reasoning, making them a natural fit for AI agent consumption.

## Connections

- These standards underpin the [[semantic-context-graph]] in OpenMetadata.
- They differentiate OpenMetadata from [[datahub]] and [[amundsen]] in the [[data-catalog-tool-comparison]], which may not use W3C standards as their core graph model.