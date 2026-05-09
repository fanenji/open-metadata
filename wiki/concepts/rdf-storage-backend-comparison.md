---
type: concept
title: RDF Storage Backend Comparison
created: 2026-04-04
updated: 2026-04-04
tags: [rdf, sparql, storage, performance, openmetadata]
related: [openmetadata-rdf-integration, sparql-query-patterns]
sources: ["RDF Ontology.md"]
---
# RDF Storage Backend Comparison

The [[openmetadata-rdf-integration]] supports a pluggable storage backend architecture with two primary implementations: Apache Jena Fuseki (default) and QLever (high-performance alternative).

## Apache Jena Fuseki

- **Type**: Default backend
- **Description**: A SPARQL server from the Apache Jena project, providing HTTP access to RDF data
- **Strengths**:
  - Mature, well-documented project with active community
  - Full SPARQL 1.1 compliance (query, update, federation)
  - Supports RDFS and OWL reasoning
  - Easy to deploy (Java WAR file or standalone server)
  - Good for moderate-scale deployments
- **Weaknesses**:
  - Performance degrades at very large scale (billions of triples)
  - Limited distributed query capabilities
  - Memory-intensive for reasoning workloads

## QLever

- **Type**: High-performance alternative
- **Description**: A SPARQL engine optimized for large-scale RDF datasets, originally developed for Wikidata
- **Strengths**:
  - Significantly faster query performance on large datasets
  - Efficient indexing and compression
  - Designed for web-scale RDF data (billions of triples)
  - Lower memory footprint for equivalent workloads
- **Weaknesses**:
  - Smaller community and ecosystem
  - Less mature than Fuseki
  - May lack some advanced SPARQL features
  - More complex deployment

## Decision Framework

| Criterion | Choose Fuseki | Choose QLever |
|-----------|---------------|---------------|
| Dataset size | < 100M triples | > 100M triples |
| Query complexity | Moderate | High |
| Reasoning needs | RDFS/OWL required | Basic only |
| Deployment simplicity | Important | Less important |
| Community support | Important | Less important |
| Performance requirements | Standard | High-throughput |

## Configuration

In [[openmetadata-rdf-integration]], the backend is selected via the `storageType` configuration parameter:

```yaml
rdfConfiguration:
  enabled: true
  storageType: FUSEKI       # or QLEVER
  remoteEndpoint: http://fuseki:3030/openmetadata
```

## Open Questions

- Performance benchmarks comparing Fuseki vs. QLever in the context of OpenMetadata's workload patterns
- Operational costs (memory, CPU, storage) for each backend at scale
- Migration path between backends (data export/import)
