---
type: concept
title: API Design Principles
created: 2026-05-07
updated: 2026-05-07
tags: [api, design, data-platform]
related: [hugging-face-datasets-server-pattern, cql-filtering, data-download-service, sistema-api-configuratore-api, sistema-api-script-groovy]
sources: ["SISTEMA API.md"]
---
# API Design Principles

A structured framework for the Data Platform's API design, consolidating five core concerns identified in the [[SISTEMA API]] Map of Content. These principles guide the design of APIs that serve dataset access, search, and filtering capabilities to internal and potentially external consumers.

## Core Concerns

### 1. Content-Type Management
The API must support content negotiation to serve both HTML (for browser-based exploration) and JSON (for programmatic access) responses. This is typically implemented via the `Accept` header or a `format` query parameter.

### 2. API Versioning
A versioning strategy is essential for managing breaking changes over time. Common approaches include:
- **URL path versioning** (`/v1/`, `/v2/`) — simple, explicit, but can lead to URL proliferation
- **Header-based versioning** (`Accept: application/vnd.api+json;version=1`) — cleaner URLs but harder to discover
- **Query parameter versioning** (`?version=1`) — simple but pollutes query space

The choice depends on consumer identification (internal vs. external) and deployment model.

### 3. HATEOAS (Hypermedia as the Engine of Application State)
API responses include links that drive navigation, enabling discoverability and reducing client-side URL construction. While powerful for external APIs, HATEOAS adds complexity that may be unnecessary for internal data platform APIs with well-known endpoints.

### 4. Pagination
Large result sets must be split into pages. Two primary strategies:
- **Offset-based pagination** (`offset=0&length=100`) — simple, consistent with Hugging Face pattern, but inefficient for large offsets
- **Cursor-based pagination** (`cursor=abc123`) — more efficient for large datasets, handles real-time data better, but more complex

### 5. CQL Filtering
Standardized filter syntax using Contextual Query Language (CQL) or a simpler SQL-like `where=` parameter (as in the Hugging Face pattern). See [[cql-filtering]] for details.

## Decision Framework

| Concern | Internal API | External API |
|---------|-------------|-------------|
| Content-Type | JSON only | JSON + HTML |
| Versioning | Header-based | URL path |
| HATEOAS | Optional | Recommended |
| Pagination | Offset-based | Cursor-based |
| Filtering | Simple where= | Full CQL |

## Related Pages
- [[hugging-face-datasets-server-pattern]]
- [[cql-filtering]]
- [[data-download-service]]
- [[SISTEMA API]]