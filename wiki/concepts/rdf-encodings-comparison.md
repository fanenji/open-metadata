---
type: concept
title: RDF Encodings Comparison
created: 2026-04-29
updated: 2026-04-29
tags: [rdf, encoding, serialization, semantic-web]
related: [semantic-metadata-overview, dcat-ontology]
sources: ["FOSS4GE 2024  Towards better data platforms with semantic metadata - Summary.md"]
---
# RDF Encodings Comparison

RDF data can be serialised in multiple encodings. The same knowledge graph can be expressed in any of these formats — encoding is a matter of tooling preference, not semantic meaning.

| Encoding | Notes |
|---|---|
| **Turtle** | Human-readable, concise — common for authoring |
| **JSON-LD** | JSON with a `@context` block — web-friendly, ideal for APIs |
| **RDF/XML** | The classic W3C format — verbose but widely supported |
| **N-Triples** | Line-by-line, one triple per line — easy to process |

## When to Use Each

- **Turtle**: Authoring and editing semantic metadata by hand
- **JSON-LD**: Web APIs, embedding in HTML pages for search engine indexing
- **RDF/XML**: Legacy systems, tools that require XML input
- **N-Triples**: Large-scale data processing, streaming, import/export

## Tooling

Semantic data has mature tooling in all major languages:
- **Python:** `rdflib`, `pyLD`
- **Java:** Apache Jena, RDF4J
- **JavaScript:** `jsonld.js`, `n3.js`

With these libraries, you handle the knowledge graph directly — you do not need to write parsers for each encoding separately.