---
type: source
title: SISTEMA API
created: 2026-02-21
updated: 2026-02-21
tags: [data-platform, api, design]
related: [api-design-principles, hugging-face-datasets-server-pattern, cql-filtering, data-download-service, sistema-api-configuratore-api, sistema-api-script-groovy]
sources: ["SISTEMA API.md"]
---
# SISTEMA API

A Map of Content (MOC) note documenting the key architectural concerns for the Data Platform's API system. The note identifies five core design areas — content-type management, API versioning, HATEOAS, pagination, and CQL-based filtering — and references the Hugging Face Datasets Server as a concrete implementation pattern.

## Key Concerns

- **Content-Type Management**: Handling HTML vs JSON response formats.
- **API Versioning**: Strategy for managing API changes over time.
- **HATEOAS**: Hypermedia as the Engine of Application State — links drive API navigation.
- **Pagination**: Splitting large result sets into pages.
- **CQL Filtering**: Standardized filter syntax for API queries.

## Reference Implementation

The Hugging Face Datasets Server provides a working pattern with three core endpoints:
- `/rows` — paginated row retrieval
- `/search` — text search across dataset
- `/filter` — structured filtering with `where=` parameter

## Related Pages

- [[SISTEMA API - CONFIGURATORE API]]
- [[SISTEMA API - SCRIPT GROOVY]]
- [[api-design-principles]]
- [[hugging-face-datasets-server-pattern]]
- [[cql-filtering]]
- [[data-download-service]]