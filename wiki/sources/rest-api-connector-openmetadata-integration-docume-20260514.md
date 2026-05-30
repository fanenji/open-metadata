---
type: source
title: "Rest Api Connector Openmetadata Integration Docume 20260514"
created: 2026-05-30
updated: 2026-05-30
tags: []
related: []
authors: []
year: 2026
url: ""
venue: ""
---

type: source
title: "REST API Connector | OpenMetadata Integration Documentation"
created: 2026-05-14
updated: 2026-05-14
tags: [connectors, rest-api, openapi, ingestion, beta]
related: [rest-api-connector, openapi-specification, openmetadata-connectors, ingestion-framework, service-connection]
sources: ["rest-api-connector-openmetadata-integration-docume-20260514.md"]
authors: ["OpenMetadata"]
year: 2025
url: "https://docs.open-metadata.org/v1.12.x/connectors/api/rest"
venue: "OpenMetadata Documentation v1.12.x"
---

# REST API Connector | OpenMetadata Integration Documentation

Official documentation for the REST API Connector, a Beta connector in OpenMetadata v1.12.x that enables metadata ingestion from any service exposing an OpenAPI Specification (OAS). The connector ingests API Endpoints, Request Schemas, and Response Schemas.

## Key Points

- **Beta Status**: The connector is marked as BETA, indicating it may not be fully stable or feature-complete.
- **Requirements**: Only an OpenAPI Schema URL (pointing to a hosted OAS document, typically JSON) and an optional authentication Token if the schema is protected.
- **Feature List**: API Endpoint, Request Schema, Response Schema.
- **AutoPilot Integration**: When AutoPilot is enabled, workflows like usage tracking and data lineage are handled automatically without user configuration.

## Configuration Steps

1. Select the REST service type from the Services page.
2. Provide a unique Service Name and Description.
3. Configure the connection with the OpenAPI Schema URL and optional Token.
4. Test the connection and save.
5. Schedule ingestion (hourly, daily, weekly, or manual) and deploy.

The source also references troubleshooting guidance and the ability to run the connector externally.