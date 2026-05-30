---
type: concept
title: Schema-First Approach
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, architecture, json-schema, code-generation]
related: [openmetadata, openmetadata-code-layout, unified-metadata-graph, ingestion-framework]
sources: ["understand-code-layout---openmetadata-documentatio-20260514.md"]
---
# Schema-First Approach

The schema-first approach is a core architectural principle of OpenMetadata. Metadata models — including entities, types, API request objects, and relationships — are defined first using **JSON Schema**, which serves as the single source of truth. Code artifacts (Java POJOs and Python types) are then generated from these schema definitions, ensuring consistency across the API, storage, and ingestion layers.

## How It Works

1. **Define**: Metadata models are authored as JSON Schema files under `openmetadata-spec/src/main/resources/json/schema/`.
2. **Generate (Java)**: The `jsonschema2pojo-maven-plugin` (configured in `pom.xml`) converts schemas into Plain Old Java Objects (POJOs), placed under `openmetadata-service/target/generated-sources/jsonschema2pojo`.
3. **Generate (Python)**: The `make generate` command produces Python types from the same schemas, output to `ingestion/src/metadata/generated`.

## Schema Categories

| Category | Directory | Purpose |
|----------|-----------|---------|
| Entities | `json/schema/entity` | Core metadata objects: data, feed, policies, services, tags, teams |
| Types | `json/schema/type` | Reusable type definitions |
| API Requests | `json/schema/api` | Request/response object shapes |

## Benefits

- **Consistency**: The API, database layer, and ingestion framework all derive from the same schema definitions, eliminating drift.
- **Type Safety**: Generated POJOs and Python types provide compile-time guarantees.
- **Documentation**: JSON Schema serves as living documentation for the metadata model.
- **Extensibility**: Adding a new entity or property starts with updating the schema, and code generation propagates the change.

This approach is fundamental to understanding how [[openmetadata-code-layout|the codebase is organized]] and how the [[unified-metadata-graph]] maintains a coherent model across all integrated services.