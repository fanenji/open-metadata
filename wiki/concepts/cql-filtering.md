---
type: concept
title: CQL Filtering
created: 2026-05-07
updated: 2026-05-07
tags: [api, filtering, cql, query-language]
related: [api-design-principles, hugging-face-datasets-server-pattern, data-download-service]
sources: ["SISTEMA API.md"]
---
# CQL Filtering

Contextual Query Language (CQL) is a standardized syntax for expressing filters in API queries. It is identified as a core design concern for the Data Platform's API system in [[SISTEMA API]].

## Overview

CQL provides a formal grammar for filter expressions, supporting:
- **Comparison operators**: `=`, `<`, `>`, `<=`, `>=`, `<>`
- **Logical operators**: `AND`, `OR`, `NOT`
- **String matching**: `LIKE`, wildcards
- **Set membership**: `IN`, `NOT IN`
- **Range queries**: `BETWEEN`
- **Spatial operators**: `WITHIN`, `INTERSECTS`, `CONTAINS` (if applicable)

## CQL vs. Simple Filtering

| Aspect | CQL | Simple `where=` (Hugging Face) |
|--------|-----|-------------------------------|
| Expressiveness | High — full boolean logic | Low — single conditions |
| Standardization | OGC standard | Ad-hoc SQL-like |
| Complexity | Higher learning curve | Simple, intuitive |
| Spatial support | Yes (OGC CQL) | No |
| Use case | External APIs, complex queries | Internal APIs, simple filters |

## Integration with Data Platform

CQL filtering would integrate with:
- [[data-download-service]] — enabling consumers to request filtered subsets
- [[api-design-principles]] — as the recommended filter syntax for external-facing APIs
- [[hugging-face-datasets-server-pattern]] — as an alternative to the simpler `where=` parameter

## Open Questions

1. Is full CQL necessary, or would a simpler `where=` parameter suffice for the Data Platform's consumers?
2. Should CQL be supported alongside a simpler filter syntax, or replace it entirely?
3. How does CQL integrate with the underlying query engine (Dremio, DuckDB, Iceberg)?

## Related Pages
- [[api-design-principles]]
- [[hugging-face-datasets-server-pattern]]
- [[data-download-service]]
- [[SISTEMA API]]