---
type: entity
title: REST API Connector
created: 2026-05-14
updated: 2026-05-15
tags: ["openmetadata", "connector", "rest-api", "openapi", "ingestion", "beta", "connectors"]
related: ["openapi-specification", "rest-connector-yaml-config", "external-connector-execution", "metadata-cli", "filter-patterns", "ingestion-framework", "openmetadata-connectors", "service-connection", "openmetadata"]
sources: ["run-the-openapi-rest-connector-externally---openme-20260514.md", "rest-api-connector-openmetadata-integration-docume-20260514.md"]
---

# REST API Connector

The REST API Connector is a Beta connector in OpenMetadata v1.12.x that ingests metadata from any web service exposing an [[openapi-specification|OpenAPI Specification (OAS)]] document. It is part of the [[openmetadata-connectors]] library and operates within the [[ingestion-framework]]. The connector enables users to discover and document API endpoints, request schemas, and response schemas within the OpenMetadata platform, and supports both UI‑based and external (CLI) execution.

## Features

- **API Endpoint** discovery and metadata ingestion  
- **Request Schema** documentation  
- **Response Schema** documentation  
- Support for both UI‑based and external (CLI) execution  

## Requirements

- Python 3.9–3.11  
- OpenMetadata ingestion framework installed  
- Access to an OpenAPI Schema URL (hosted OAS document in JSON format, e.g., `https://petstore3.swagger.io/api/v3/openapi.json`)  
- Optional authentication token for protected API schemas  

## Connection Workflow (UI)

1. Create a new [[service-connection]] of type **REST** from the OpenMetadata UI.  
2. Provide a unique Service Name (immutable after creation) and Description.  
3. Enter the **OpenAPI Schema URL** and optional **Token**.  
4. Test the connection and save.  
5. Schedule ingestion at an hourly, daily, weekly, or manual cadence, then deploy.  

## Configuration

The connector requires the following configuration fields:

- **OpenAPI Schema URL** – URL to the OpenAPI Specification document.  
- **Authentication Token** – Optional token for protected API schemas.  
- **Source Config** – Set to `ApiMetadata` type with optional parameters:  
  - `markDeletedApiCollections`  
  - `overrideMetadata`  
  - `apiCollectionFilterPattern` – Filter pattern for API collections. For details on filter patterns, see [[filter-patterns]].

## External Execution

The REST API Connector can be run externally using a YAML configuration file and the `metadata ingest` CLI command. See [[rest-connector-yaml-config]] for the complete configuration reference and [[external-connector-execution]] for the general pattern.

### Quick Start

1. Create a YAML config file with the source, sink, and workflow configuration.  
2. Run: `metadata ingest -c <path-to-yaml>`  
3. Authenticate using a [[personal-access-token|JWT token]] (bot token).  

The [[metadata-cli]] tool is used for external execution.

## Beta Status

As a Beta feature, the REST API Connector may not be fully stable or feature‑complete. Users should test thoroughly in non‑production environments before relying on it for critical metadata workflows.

## AutoPilot Integration

When AutoPilot is enabled in OpenMetadata, the REST API Connector benefits from automated workflow handling. AutoPilot manages usage tracking, data lineage, and similar tasks without requiring manual setup, reducing operational overhead for metadata ingestion pipelines.