---
type: query
title: "Overview API OpenMetadata per leggere metadati di una tabella"
created: 2026-06-24
origin: chat
query: "fammi una overview delle api di openmetadata nell'ottica di leggere i metadati relativi ad un asset (tavola)"
tags: [openmetadata, api, rest, sdk, search, metadata]
---

# Overview API OpenMetadata per leggere metadati di una tabella

OpenMetadata espone **quattro** strade per leggere i metadati di un asset (es. tabella), più una in sviluppo. Dalla più diretta alla più integrata:

## 1. REST API diretta — `GET /api/v1/tables/{id}` o `GET /api/v1/tables/name/{fqn}`

Tutte le operazioni CRUD su entità sono esposte via REST, con pattern standard: collection, istanza per ID, istanza per FQN [[apis-openmetadata-metadata-standard-apis---openmet-20260514]]. La piattaforma è **schema-first**: 700+ JSON Schema definiscono ogni entità — incluse tabelle, colonne, database, schemi [[metadata-standard]].

**Pro**: massima flessibilità, qualsiasi HTTP client basta [[integration-approaches-comparison]].
**Contro**: nessuna validazione lato client, devi conoscere lo schema JSON a menadito [[integration-approaches-comparison]].

```
GET /api/v1/tables/{id}
GET /api/v1/tables/name/{fullyQualifiedName}
GET /api/v1/tables?database={db_fqn}&limit=10
```

## 2. SDK Python / Java / Go

Client library generate automaticamente dagli schema JSON, con classi type-safe e helper method [[integration-approaches-comparison]]. Offrono validazione IDE-level e interfacce tipizzate per tutte le operazioni.

```python
# Esempio concettuale (Python SDK)
from metadata.ingestion.ometa.openmetadata_rest import OpenMetadataAPIClient
client = OpenMetadataAPIClient(config)
table = client.get_by_name(entity=Table, fqn="my_db.my_schema.my_table")
```

**Best for**: pipeline CI/CD, aggiornamenti automatici, script [[integration-approaches-comparison]].

## 3. API di Ricerca

Tre livelli, tutti operativi in v1.12.x:

| Meccanismo | Endpoint / Modalità | Descrizione |
|---|---|---|
| **Keyword Search** | Elasticsearch-backed | Match su nome, colonne, descrizioni [[data-discovery]] |
| **Advanced Search** | Query booleane con filtri | Filtri per owner, tag, tier, service, database, schema [[data-discovery]] |
| **Semantic (Vector) Search** | `POST /api/v1/search/vector/query` | Ricerca per similarità semantica via embedding; richiede provider embedding configurato [[research-verifica-esistenza-di-un-end-point-sparql-o-api-pe-2026-06-23]] |

## 4. MCP Server (per LLM / AI agent)

Espone il grafo dei metadati via Model Context Protocol, permettendo query in linguaggio naturale da LLM [[research-verifica-esistenza-di-un-end-point-sparql-o-api-pe-2026-06-23]]. Disponibile in v1.12.x [[openmetadata]].

## 5. SPARQL/RDF (in sviluppo)

In fase di progettazione (issue #22853), non ancora in release stabile [[research-verifica-esistenza-di-un-end-point-sparql-o-api-pe-2026-06-23]]. Esporrà:

- `POST /api/v1/rdf/sparql` — query SPARQL (SELECT, CONSTRUCT, ASK, DESCRIBE)
- `GET /api/v1/rdf/entity/{entityType}/{id}` — singola entità in RDF
- `GET /api/v1/rdf/graph/explore/{entityType}/{id}` — esplorazione sottografo

L'ontologia RDF/OWL (`openmetadata.ttl`) esiste già ed è interrogabile offline con rdflib [[research-verifica-esistenza-di-un-end-point-sparql-o-api-pe-2026-06-23]].

## Scelta rapida (decision matrix)

| Scenario | Approccio |
|---|---|
| Operazione one-shot semplice | REST API diretta [[integration-approaches-comparison]] |
| Automazione / pipeline CI/CD | SDK Python/Java [[integration-approaches-comparison]] |
| Ricerca esplorativa ("trova tabelle che...") | Search API (keyword → advanced → semantic) [[data-discovery]] |
| Interrogazione da LLM/agente AI | MCP Server [[research-verifica-esistenza-di-un-end-point-sparql-o-api-pe-2026-06-23]] |
| Query SPARQL formali | **Non ancora disponibile** — in sviluppo [[research-verifica-esistenza-di-un-end-point-sparql-o-api-pe-2026-06-23]] |

La wiki **non documenta** endpoint REST specifici con esempi di request/response per `GET /api/v1/tables` (URL esatti, payload, autenticazione dettagliata). _(deduzione: sono recuperabili dalla [doc ufficiale API Reference](https://docs.open-metadata.org/v1.12.x/api-reference) o dallo Swagger UI dell'istanza)._

## Fonti consultate

- [[integration-approaches-comparison]]
- [[metadata-standard]]
- [[data-discovery]]
- [[openmetadata]]
- [[research-verifica-esistenza-di-un-end-point-sparql-o-api-pe-2026-06-23]]
- [[apis-openmetadata-metadata-standard-apis---openmet-20260514]]
- [[metadata-standard-openmetadata-core-schema-guide---20260514]]
