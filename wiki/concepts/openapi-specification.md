---
type: concept
title: "Openapi Specification"
created: 2026-05-30
updated: 2026-05-30
tags: []
related: []
---

type: concept
title: OpenAPI Specification
created: 2026-05-14
updated: 2026-05-14
tags: [openapi, rest, api, schema, standards]
related: [rest-api-connector, openmetadata-connectors, ingestion-framework]
sources: ["rest-api-connector-openmetadata-integration-docume-20260514.md"]
---

# OpenAPI Specification

The OpenAPI Specification (OAS) is a standard, language-agnostic interface description for REST APIs. It defines a web service's API in a machine-readable document (typically JSON or YAML), including available endpoints, request/response formats, authentication methods, and data schemas.

## Role in OpenMetadata

The [[rest-api-connector]] relies entirely on the OpenAPI Specification to dynamically discover and ingest API metadata. By providing only an OpenAPI Schema URL, users enable the connector to:

- Discover all available API endpoints
- Extract request and response schemas
- Document the API structure within OpenMetadata's [[unified-metadata-graph]]

This standards-based approach makes the REST API Connector highly generic — it can ingest metadata from any service that publishes an OAS document, without requiring a service-specific connector implementation.

## Common Formats

- **JSON**: `https://api.example.com/v3/openapi.json`
- **YAML**: `https://api.example.com/v3/openapi.yaml`

## Security

If the OAS document is hosted behind authentication, the REST API Connector supports passing an authentication Token to access the protected schema URL.