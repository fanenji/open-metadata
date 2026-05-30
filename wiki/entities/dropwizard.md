---
type: entity
title: Dropwizard
created: 2026-05-14
updated: 2026-05-14
tags: [java, framework, rest-api, openmetadata]
related: [openmetadata, openmetadata-code-layout]
sources: ["understand-code-layout---openmetadata-documentatio-20260514.md"]
---
# Dropwizard

Dropwizard is the Java REST API framework used by OpenMetadata to build its backend services. It provides a lightweight, production-ready foundation for the OpenMetadata API layer.

## Role in OpenMetadata

- **REST API Host**: All OpenMetadata API resources are defined under `openmetadata-service/src/main/java/org/openmetadata/service/resources` using Dropwizard's JAX-RS integration.
- **Event Filtering**: The `ContainerResponseFilter` (a JAX-RS filter supported by Dropwizard) applies event handlers globally to all outgoing API responses, enabling the [[change-events-system]].
- **Configuration**: Dropwizard manages the application configuration defined in `conf/openmetadata.yaml`.

## Key Integrations

- **Swagger**: Dropwizard integrates with Swagger to auto-generate OpenAPI-compliant API documentation.
- **JDBI3**: Database access is handled through JDBI3, with code located under `openmetadata-service/.../jdbi3`.

Dropwizard is a peripheral but essential component of the [[openmetadata-code-layout|OpenMetadata codebase]], providing the HTTP and REST infrastructure that external clients and the ingestion framework interact with.