---
type: source
title: "REST API Connector | OpenMetadata Integration Documentation"
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, rest-api, connector, openapi, beta]
related: [rest-api-connector, openapi-specification, service-connection, metadata-ingestion-workflow, openmetadata-connectors]
sources: ["rest-api-connector-openmetadata-integration-docume-20260514-2.md"]
---

# REST API Connector | OpenMetadata Integration Documentation

This source is the official OpenMetadata v1.12.x documentation for the REST API Connector (Beta). It covers the requirements, connection configuration, and metadata ingestion workflow for ingesting metadata from any REST API that exposes an OpenAPI Specification (OAS) document.

## Key Content

- **Requirements:** An OpenAPI Schema URL (JSON format) is required; an optional authentication token is needed if the schema is protected.
- **Metadata Ingestion:** The standard 8-step UI-driven workflow (select service → create → name → configure → test → schedule → deploy → view) is used to configure and deploy the connector.
- **Connection Options:** The primary parameter is the OpenAPI Schema URL (e.g., `https://petstore3.swagger.io/api/v3/openapi.json`). The optional Token parameter is for authenticated schemas.
- **AutoPilot:** The documentation mentions that if AutoPilot is enabled, workflows like usage tracking and data lineage are handled automatically.

## Status

This source is a duplicate of the same official documentation already captured in the existing `rest-api-connector` wiki page. It adds no new information beyond what is already documented.

## Open Questions

- The connector is marked as **Beta**, but no limitations, known issues, or unsupported OpenAPI features are documented.
- The "AutoPilot" concept is mentioned but not defined or explained elsewhere in the wiki.
- Performance characteristics, rate limiting, pagination handling, and authentication method support beyond token are not addressed.