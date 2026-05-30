---
type: entity
title: JsonSchemas
created: 2026-05-14
updated: 2026-05-14
tags: [json-schema, metadata-modeling, code-generation, openmetadata]
related: [openmetadata, schema-first-approach, openmetadata-code-layout, openmetadata-system-architecture]
sources: ["openmetadata-system-architecture-developer-guide---20260514.md"]
---

# JsonSchemas

JsonSchemas (JSON Schema) is the formal schema definition language used by OpenMetadata to define all metadata entity structures. It is one of the four core architectural dependencies identified in the [[openmetadata-system-architecture]].

## Role in OpenMetadata

JSON Schema serves as the single source of truth for the platform's data model. This [[schema-first-approach]] means:

- Every metadata entity (tables, dashboards, pipelines, ML models, etc.) is defined as a JSON Schema document
- Java POJOs for the backend API are generated from these schemas
- Python types for the ingestion framework are generated from the same schemas
- API documentation via [[swagger]] is derived from the schema-driven resource definitions

## Location

The JSON Schema definitions reside in the `openmetadata-spec/src/main/resources/json/schema/` directory of the [[openmetadata-code-layout|OpenMetadata repository]].