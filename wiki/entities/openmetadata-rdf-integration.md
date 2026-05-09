---
type: entity
title: OpenMetadata RDF Integration
created: 2026-04-04
updated: 2026-04-04
tags: [openmetadata, rdf, sparql, knowledge-graph, ontology]
related: [openmetadata, sparql-query-patterns, rdf-storage-backend-comparison, semantic-search-in-data-catalogs, data-catalog-tool-comparison, data-observability-three-pillars, custom-connector-openmetadata]
sources: ["RDF Ontology.md"]
---
# OpenMetadata RDF Integration

The OpenMetadata RDF Integration is a feature that adds a semantic knowledge graph layer to the [[openmetadata]] metadata catalog. It enables semantic search, graph-based analytics, reasoning, and standards-compliant data catalog federation using W3C standards (RDF, SPARQL, DCAT).

## Architecture

The integration follows a layered architecture:

1. **REST API Layer** — Exposes RDF-specific endpoints alongside existing entity APIs
2. **Service Layer** — Contains the `RdfRepository` orchestrator and `RdfUpdater` for entity lifecycle synchronization
3. **RDF Translation Layer** — Handles JSON-LD context processing, entity-to-RDF conversion, and SQL-to-SPARQL translation via Apache Calcite
4. **Storage Layer** — Pluggable backends: Apache Jena Fuseki (default) and QLever (high-performance)

## Core Components

### RDF Repository
Central orchestrator (`org.openmetadata.service.rdf.RdfRepository`) providing:
- Entity CRUD operations (create, update, delete)
- SPARQL query and update execution
- Semantic search (embedding-based similarity)
- Similar entity and user recommendations

### Entity to RDF Conversion
- **Ontology Mapping**: A Turtle file (`openmetadata.ttl`) defines class hierarchy mapping OpenMetadata entities to DCAT standards (e.g., `om:Service` → `dcat:DataService`, `om:Table` → `om:DataAsset` → `dcat:Dataset`)
- **JSON-LD Context**: Maps entity fields to RDF properties (e.g., `name` → `dcterms:title`)

### RDF Updater
Hooks into `EntityRepository` lifecycle methods (`postCreate`, `postUpdate`, `postDelete`) to synchronize RDF state with entity changes.

### SPARQL Query Engine
- Native SPARQL execution
- SQL-to-SPARQL translation using Apache Calcite for users familiar with SQL

## REST API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/rdf/status` | RDF service status |
| GET | `/api/v1/rdf/entity/{entityType}/{id}` | Get entity as RDF |
| POST | `/api/v1/rdf/sparql` | Execute SPARQL query |
| POST | `/api/v1/rdf/sparql/update` | Execute SPARQL update |
| GET | `/api/v1/rdf/graph/explore/{entityType}/{id}` | Graph exploration |
| GET | `/api/v1/rdf/search/semantic` | Semantic search |
| GET | `/api/v1/rdf/search/similar/{entityType}/{id}` | Find similar entities |
| GET | `/api/v1/rdf/recommendations/user/{userId}` | User recommendations |
| POST | `/api/v1/rdf/lineage/infer` | Lineage inference |

## Configuration

```yaml
rdfConfiguration:
  enabled: true
  storageType: FUSEKI       # or QLEVER
  remoteEndpoint: http://fuseki:3030/openmetadata
  username: admin
  password: ${RDF_PASSWORD}
  dataset: openmetadata
  baseUri: https://metadata.company.com/
  queryTimeout: 30000
  maxResultSize: 10000
  enableInference: true
  reasonerType: RDFS        # or OWL
```

## Use Cases

- **Semantic Data Discovery**: Natural language queries, concept-based search, cross-domain discovery
- **Advanced Lineage**: Transitive queries, multi-hop impact analysis, pattern detection
- **Compliance & Governance**: Tag-based asset discovery, regulatory tracking, automated enforcement
- **Recommendation Engine**: Similar dataset suggestions, collaborative filtering, usage pattern analysis
- **Federation & Integration**: Multi-instance queries, external knowledge graph linking, standards-based exchange

## Design Principles

- **Non-intrusive**: RDF operates alongside existing functionality
- **Pluggable**: Multiple RDF storage backends supported
- **Standards-based**: Full W3C specification compliance
- **Performance-conscious**: Asynchronous updates, caching, query optimization
- **Extensible**: Easy ontology mapping and reasoning rule additions

## Connections to Wiki

- Strengthens [[openmetadata]] as a platform with semantic web capabilities
- Adds a new evaluation dimension to [[data-catalog-tool-comparison]] (semantic web support)
- Extends [[data-observability-three-pillars]] by enabling transitive lineage inference via SPARQL
- Related to [[custom-connector-openmetadata]] as a pattern for extending OpenMetadata
