---
type: query
title: "Research: verifica esistenza di un end-point sparql o api per interrogare il grafo rdf in openmetadata"
created: 2026-06-23
updated: 2026-06-23
origin: deep-research
tags: [research]
sources: []
related: []
---

# Research: verifica esistenza di un end-point sparql o api per interrogare il grafo rdf in openmetadata

## Risposta sintetica

**Sì, OpenMetadata espone endpoint SPARQL e API REST per interrogare il suo grafo RDF.** La feature è documentata in una issue di progettazione su GitHub (issue #22853) e nell'architettura degli standard OpenMetadata. Non si tratta di un endpoint SPARQL pubblico standard (tipo Fuseki/GraphDB) ma di una serie di endpoint REST che includono l'esecuzione di query SPARQL e operazioni sul knowledge graph RDF.

## API REST per RDF

Secondo la issue GitHub open-metadata/OpenMetadata#22853 [1], il modulo RDF espone i seguenti endpoint REST (`/api/v1/rdf/`):

### Endpoint di Query

| Metodo | Endpoint                                       | Descrizione                                                              |
| ------ | ---------------------------------------------- | ------------------------------------------------------------------------ |
| `POST` | `/api/v1/rdf/sparql`                           | Esegue una query SPARQL (SELECT, ASK, CONSTRUCT, DESCRIBE) sul grafo RDF |
| `POST` | `/api/v1/rdf/sparql/update`                    | Esegue operazioni SPARQL Update (INSERT, DELETE) sul grafo               |
| `GET`  | `/api/v1/rdf/entity/{entityType}/{id}`         | Recupera una singola entità in formato RDF                               |
| `GET`  | `/api/v1/rdf/graph/explore/{entityType}/{id}`  | Esplora il sottografo attorno a un'entità                                |
| `GET`  | `/api/v1/rdf/search/semantic`                  | Ricerca semantica sul grafo RDF                                          |
| `GET`  | `/api/v1/rdf/search/similar/{entityType}/{id}` | Trova entità simili nel grafo                                            |
| `GET`  | `/api/v1/rdf/recommendations/user/{userId}`    | Raccomandazioni personalizzate basate sul grafo                          |
| `POST` | `/api/v1/rdf/lineage/infer`                    | Inferenza di lineage tramite ragionamento RDF                            |
| `GET`  | `/api/v1/rdf/status`                           | Stato del modulo RDF                                                     |

### Architettura Sottostante

Il modulo RDF si basa su [1]:

- **`RdfRepository`** (`org.openmetadata.service.rdf.RdfRepository`) — orchestratore centrale delle operazioni RDF
- **`RdfUpdater`** (`org.openmetadata.service.rdf.RdfUpdater`) — sincronizzazione entità → RDF tramite hook nel ciclo di vita
- **SPARQL Query Engine** — traduzione SQL → SPARQL per query ibride
- **JSON-LD Context** — ogni tipo entità ha un context JSON-LD per la conversione in RDF
- **Ontologia** — file Turtle (`resources/rdf/openmetadata.ttl`) che definisce il modello RDF/OWL

## Standard OpenMetadata e SPARQL

Il sito openmetadatastandards.org [2] descrive un'architettura a layer che include esplicitamente uno **SPARQL Query Layer** posizionato sopra SHACL Validation e JSON-LD Mapping:

```
Applications (Knowledge Graphs, Semantic Search, Reasoning)
         ↑
   SPARQL Query Layer
         ↑
   SHACL Validation Layer
         ↑
   JSON-LD Mapping Layer
```

La documentazione mostra esempi di query SPARQL usando la libreria Python `rdflib` [2]:

```python
from rdflib import Graph
g = Graph()
g.parse('rdf/ontology/openmetadata.ttl', format='turtle')

query = """
PREFIX om: <http://open-metadata.org/ontology/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?table ?owner
WHERE {
  ?table a om:Table ;
         om:owner ?owner ;
         om:database ?db .
  ?db om:name "production" .
}
"""
results = g.query(query)
```

Questo indica che l'ontologia RDF di OpenMetadata è interrogabile via SPARQL usando triple store standard compatibili con RDFlib.

## Altre API di Query (Non-RDF)

OpenMetadata offre anche API di query che non usano SPARQL ma operano sul [[unified-metadata-graph]]:

### Ricerca Semantica (Vector Search)

`POST /api/v1/search/vector/query` [3] — ricerca vettoriale basata su embedding, non su RDF. Usa OpenSearch come backend e richiede un provider di embedding (OpenAI, Bedrock, DJL).

### MCP Server

Attraverso l'[[mcp-server]] [4], OpenMetadata espone il grafo a LLM e agent AI via Model Context Protocol, permettendo query in linguaggio naturale.

### API REST Standard

Le API REST standard di OpenMetadata (`/api/v1/`) [5] coprono tutte le operazioni CRUD su entità, ricerca, lineage e governance, ma non usano SPARQL.

### SDK

Python, Java e Go SDK [5] offrono accesso programmatico tipizzato a tutte le entità del catalogo.

## Stato della Feature RDF/SPARQL

**Importante**: l'endpoint SPARQL descritto nella issue #22853 è una **feature in fase di progettazione/implementazione**, non ancora parte delle release stabili (la issue è aperta). La documentazione su openmetadatastandards.org descrive l'architettura prevista. In produzione (v1.12.x), le API REST standard e la ricerca semantica vettoriale sono le interfacce di query disponibili.

La tabella seguente riassume lo stato:

| Interfaccia | Stato | Tipo Query |
|-------------|-------|------------|
| `POST /api/v1/rdf/sparql` | In sviluppo (issue #22853) | SPARQL |
| `POST /api/v1/search/vector/query` | Disponibile (v1.12+) | Vettoriale/Semantica |
| API REST CRUD (`/api/v1/`) | Disponibile | REST/JSON |
| MCP Server | Disponibile (v1.12+) | Linguaggio naturale via LLM |
| SDK (Python/Java/Go) | Disponibile | Programmatica tipizzata |

## Relazione con la Wiki Esistente

- [[semantic-web-support]] — descrive gli standard RDF/OWL, SHACL, JSON-LD, PROV-O nel contesto OpenMetadata. L'endpoint SPARQL sarebbe l'interfaccia di query per questo layer semantico.
- [[unified-metadata-graph]] — il concetto architetturale centrale. Le API RDF/SPARQL operano su una rappresentazione RDF di questo grafo.
- [[metadata-standard]] — il progetto ombrello che include sia JSON Schema che gli standard semantici.
- [[mcp-server]] — interfaccia alternativa per interrogare il grafo, orientata ad AI/LLM anziché a query SPARQL formali.
- [[openmetadata-system-architecture]] — l'architettura complessiva dove il modulo RDF si inserisce come layer aggiuntivo.

## Conclusioni

OpenMetadata sta costruendo un'infrastruttura RDF completa con endpoint SPARQL come parte della sua strategia semantic web [1][2]. Allo stato attuale:

1. **L'ontologia RDF/OWL esiste** (`openmetadata.ttl`) ed è interrogabile offline con tool come rdflib/SPARQL [2].
2. **Gli endpoint REST per SPARQL** sono in fase di sviluppo (issue #22853) [1].
3. **In produzione**, le alternative per interrogare il grafo sono: API REST standard, ricerca semantica vettoriale, e MCP Server per query in linguaggio naturale [3][4][5].
4. Per chi necessita di query SPARQL oggi, è possibile caricare l'ontologia in un triple store esterno (es. GraphDB, Fuseki) ed esporre un endpoint SPARQL indipendente.

## References

1. [RDF Ontology Integration in OpenMetadata: Architecture and Implementation · Issue #22853 · open-metadata/OpenMetadata](https://github.com/open-metadata/OpenMetadata/issues/22853) — github.com
2. [RDF & Ontologies Overview - OpenMetadata Standards](https://openmetadatastandards.org/rdf/overview) — openmetadatastandards.org
3. [Enable Semantic Search | OpenMetadata Deployment Guide](https://docs.open-metadata.org/v1.12.x/deployment/semantic-search) — docs.open-metadata.org
4. [Semantic Search MCP Tool - OpenMetadata Documentation](https://docs.open-metadata.org/v1.12.x/how-to-guides/mcp/semantic-search) — docs.open-metadata.org
5. [OpenMetadata SDKs & APIs - OpenMetadata Documentation](https://docs.open-metadata.org/v1.12.x/api-reference) — docs.open-metadata.org
6. [Metadata Standard | OpenMetadata Core Schema Guide](https://docs.open-metadata.org/v1.12.x/api-reference/main-concepts/metadata-standard) — docs.open-metadata.org
7. [OpenMetadata GitHub Repository](https://github.com/open-metadata/openmetadata) — github.com
