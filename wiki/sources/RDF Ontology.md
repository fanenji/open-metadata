---
type: source
title: RDF Ontology Integration in OpenMetadata
created: 2026-04-04
updated: 2026-04-04
tags: [openmetadata, rdf, sparql, knowledge-graph, ontology]
related: [openmetadata, openmetadata-rdf-integration, sparql-query-patterns, rdf-storage-backend-comparison, semantic-search-in-data-catalogs, data-catalog-tool-comparison, data-observability-three-pillars]
sources: ["RDF Ontology.md"]
authors: [@harshach]
year: 2025
url: "https://github.com/open-metadata/OpenMetadata/issues/22853"
venue: GitHub Issue
---
# RDF Ontology Integration in OpenMetadata

This source is an official OpenMetadata GitHub issue (closed/completed) detailing the architecture and implementation of RDF (Resource Description Framework) ontology integration into the OpenMetadata platform. It describes a sophisticated knowledge graph layer that enriches the metadata catalog with semantic capabilities, enabling semantic search, graph-based analytics, reasoning, and standards-compliant data catalog federation.

## Key Contributions

- **Architecture**: A layered design with REST API → Service Layer → RDF Translation Layer → Storage Layer, with pluggable backends (Apache Jena Fuseki default, QLever for high-performance)
- **Entity-to-RDF Conversion**: Mapping OpenMetadata's JsonSchema entities to RDF triples using a custom ontology (Turtle file) that aligns with W3C DCAT standards
- **SPARQL Query Engine**: Native SPARQL execution plus SQL-to-SPARQL translation via Apache Calcite
- **Advanced Features**: Semantic search (embedding-based), transitive lineage inference, similar entity recommendations, user recommendations
- **Non-intrusive Design**: RDF operates alongside existing functionality via hooks in EntityRepository

## SPARQL Query Examples

The source provides concrete SPARQL queries for:
- Finding all tables with PII data (tag-based discovery)
- Data asset discovery by domain
- Impact analysis via transitive lineage (multi-hop)

## Configuration

Includes a YAML configuration block with parameters for enabling RDF, selecting storage backend (Fuseki/QLever), authentication, query timeout, result size limits, and reasoner type (RDFS/OWL).

## Status

Closed (completed) — indicates production implementation in OpenMetadata.
