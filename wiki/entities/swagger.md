---
type: entity
title: Swagger
created: 2026-05-14
updated: 2026-05-14
tags: [api, documentation, openapi, tooling, openmetadata]
related: [openmetadata, openmetadata-code-layout, dropwizard, openapi-specification, rest-api-connector]
sources: ["understand-code-layout---openmetadata-documentatio-20260514.md"]
---
# Swagger

Swagger is the API documentation tool used by OpenMetadata to generate interactive API documentation following the [[openapi-specification|OpenAPI Specification]] standards. It is integrated with the [[dropwizard|Dropwizard]] framework to auto-generate documentation from the REST API resource definitions.

## Role in OpenMetadata

- **API Documentation**: Automatically produces browsable, interactive API docs from the Java REST resource classes under `openmetadata-service/.../resources`.
- **OpenAPI Compliance**: Generates documentation in the OpenAPI format, which is the same specification format required by the [[rest-api-connector]] for ingesting metadata from external REST APIs.
- **Developer Experience**: Enables developers to explore and test API endpoints directly from the documentation UI.

## Significance

Swagger-generated documentation is the bridge between OpenMetadata's internal API implementation and external consumers, including:
- The Python [[ingestion-framework]] clients that call the API
- Custom integrations built by users
- The [[rest-api-connector]], which relies on OpenAPI specs for metadata ingestion

Swagger is a peripheral tool in the [[openmetadata-code-layout|codebase]] but essential for API discoverability and integration.