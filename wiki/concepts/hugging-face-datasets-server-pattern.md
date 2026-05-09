---
type: concept
title: Hugging Face Datasets Server Pattern
created: 2026-05-07
updated: 2026-05-07
tags: [api, pattern, reference, hugging-face]
related: [api-design-principles, cql-filtering, data-download-service]
sources: ["SISTEMA API.md"]
---
# Hugging Face Datasets Server Pattern

A reference API pattern from the Hugging Face Datasets Server, used as a concrete implementation model for the Data Platform's API system. This pattern demonstrates a clean, RESTful approach to serving dataset content with three core endpoints.

## Core Endpoints

### 1. ROWS — Paginated Row Retrieval
```
GET /rows?dataset={dataset}&config={config}&split={split}&offset={offset}&length={length}
```
Returns a paginated slice of dataset rows. Parameters:
- `dataset`: Dataset identifier (e.g., `jamescalam/world-cities-geo`)
- `config`: Configuration name
- `split`: Dataset split (train, test, validation)
- `offset`: Starting row index (0-based)
- `length`: Number of rows to return

### 2. SEARCH — Text Search
```
GET /search?dataset={dataset}&config={config}&split={split}&query={query}
```
Full-text search across all fields in the dataset. Returns matching rows.

### 3. FILTER — Structured Filtering
```
GET /filter?dataset={dataset}&config={config}&split={split}&where={condition}
```
Structured filtering using a SQL-like `where=` parameter. Example: `where=country='Italy'`

## Relevance to Data Platform

This pattern is directly applicable to the [[data-download-service]] subsystem, which prepares and serves data to consumers. The three-endpoint pattern provides:
- A simple, discoverable API surface
- Consistent pagination semantics
- Both search and structured filtering capabilities
- A proven model used at scale by Hugging Face

## Design Considerations

- The `where=` parameter uses SQL-like syntax, not full CQL — simpler but less expressive
- Offset-based pagination is suitable for moderate dataset sizes; cursor-based may be needed at scale
- The pattern assumes a single dataset per endpoint; the Data Platform may need multi-dataset or cross-dataset querying

## Related Pages
- [[api-design-principles]]
- [[cql-filtering]]
- [[data-download-service]]
- [[SISTEMA API]]