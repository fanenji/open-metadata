---
type: concept
title: Dynamic API System
created: 2026-05-07
updated: 2026-05-07
tags: [api, architecture, routing, legacy]
related: [groovy-api-system, legacy-geospatial-api-layer]
sources: ["SISTEMA API - SCRIPT GROOVY.md"]
---
# Dynamic API System

An API architecture pattern where a single script or service generates responses dynamically based on path variables rather than exposing static endpoints for each resource. This approach reduces code duplication and simplifies deployment for hierarchical data structures.

## Characteristics

- **Path Variable Routing**: The API reads URL path segments to determine which resource to serve.
- **Single Entry Point**: A single script handles all resource types.
- **Content-Type Negotiation**: The response format (JSON, HTML, etc.) is determined by the request headers.

## Example: Groovy API System

The [[groovy-api-system]] implements this pattern with a four-level hierarchy:

- Landing page (no path)
- Swagger documentation (`/openapi`)
- Datasets list (`/datasets`)
- Dataset detail (`/datasets/{id}`)
- Items list (`/datasets/{id}/items`)
- Item data (`/datasets/{id}/items/{item_id}`)

## Related Concepts

- [[legacy-geospatial-api-layer]] — The full API consumption layer using this pattern.