---
type: entity
title: Python SDK
created: 2026-05-14
updated: 2026-05-14
tags: [python-sdk, sdk, code-generation, json-schema]
related: [schema-first-approach, jsonschemas, custom-connectors, ingestion-framework, integration-approaches-comparison]
sources: ["Mini-Webinar on Custom Connectors dataintegration connectors ingestion datacatalog metadata.md"]
---
# Python SDK

The Python SDK is a generated library of Python classes that mirror the OpenMetadata standard definitions. It is automatically generated from the [[jsonschemas|JSON Schema]] definitions that serve as the single source of truth for all metadata entity structures.

## Generation

The Python SDK is generated from the same JSON Schema repository that produces:
- Java code powering the server
- TypeScript code for the UI
- Database storage schemas
- Documentation

This ensures all platform components stay synchronized across languages.

## Key Features

- **Type validation** — Python classes enforce type constraints at development time (IDE support in PyCharm, VS Code)
- **Helper methods** — Built-in utilities for common operations, such as patching descriptions on tables and columns
- **Standard objects** — Classes for all OpenMetadata entities (Table, Column, Database, Schema, etc.) with proper relationships

## Usage

The Python SDK is used in two primary contexts:
1. **CI/CD scripts** — Automating metadata updates (e.g., updating ML model metadata on push)
2. **Custom connectors** — The ingestion framework is powered by the Python SDK; the same objects used in scripts are used in [[custom-connectors]]

## Example

```python
from metadata.ingestion.connections import create_connection
from metadata.ingestion.models.table_queries import CreateTableRequest
from metadata.generated.schema.entity.data.table import Column, DataType

# Create connection
connection = create_connection(server_host, server_port, jwt_token)

# Create table request with type validation
table_request = CreateTableRequest(
    name="my_table",
    databaseSchema=EntityReference(id=schema_id),
    columns=[
        Column(name="id", dataType=DataType.INT),
        Column(name="name", dataType=DataType.VARCHAR),
    ]
)
```

## Relationship to Ingestion Framework

The ingestion framework is built on top of the Python SDK. Custom connectors use the same SDK objects and helpers, meaning the learning curve for SDK usage transfers directly to custom connector development.

## Limitations

- Language-specific — requires a Python environment
- For simple, one-off operations, raw API calls may be more lightweight