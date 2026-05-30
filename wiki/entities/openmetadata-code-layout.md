---
type: entity
title: OpenMetadata Code Layout
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, code-layout, developer-guide, architecture]
related: [openmetadata, schema-first-approach, change-events-system, ingestion-framework, openmetadata-connectors, unified-metadata-graph, dropwizard, flyway, elasticsearch, mysql, postgres, apache-airflow]
sources: ["understand-code-layout---openmetadata-documentatio-20260514.md"]
---
# OpenMetadata Code Layout

The OpenMetadata codebase is organized into two primary parts: a **Java backend** for the API and server, and a **Python framework** for metadata ingestion. This page consolidates the directory structure, build tooling, and key architectural components as documented in the official developer guide.

## Repository Structure

### Schema Definitions (Metadata Models)
- **Entities**: `OpenMetadata/openmetadata-spec/src/main/resources/json/schema/entity` — data, feed, policies, services, tags, teams
- **Types**: `OpenMetadata/openmetadata-spec/src/main/resources/json/schema/type`
- **API Request Objects**: `OpenMetadata/openmetadata-spec/src/main/resources/json/schema/api`
- **Generated Java POJOs**: `OpenMetadata/openmetadata-service/target/generated-sources/jsonschema2pojo`
- **Generated Python Types**: `OpenMetadata/ingestion/src/metadata/generated`

### Java Backend (API & Server)
- **REST API Resources**: `OpenMetadata/openmetadata-service/src/main/java/org/openmetadata/service/resources`
- **Event Handlers**: `OpenMetadata/openmetadata-service/src/main/java/org/openmetadata/service/events`
- **Database (JDBI3)**: `OpenMetadata/openmetadata-service/src/main/java/org/openmetadata/service/jdbi3`
- **Elasticsearch Publisher**: `OpenMetadata/openmetadata-service/src/main/java/org/openmetadata/service/elasticsearch/ElasticSearchEventPublisher.java`
- **Configuration**: `OpenMetadata/conf/openmetadata.yaml`

### Python Ingestion Framework
- **Source Connectors**: `OpenMetadata/ingestion/src/metadata/ingestion/source`
- **Processors**: `OpenMetadata/ingestion/src/metadata/ingestion/processor`
- **Sinks**: `OpenMetadata/ingestion/src/metadata/ingestion/sink`
- **Stages**: `OpenMetadata/ingestion/src/metadata/ingestion/stage`
- **BulkSinks**: `OpenMetadata/ingestion/src/metadata/ingestion/bulksink`
- **Workflow Examples**: `OpenMetadata/ingestion/examples/workflows`
- **Airflow DAGs**: `OpenMetadata/ingestion/examples/airflow/dags`

### Bootstrap & Migration
- **Database Setup**: `OpenMetadata/bootstrap/openmetadata-ops.sh`
- **Migration Tool**: Flyway manages database table versions.

## Key Build Tools
- **jsonschema2pojo-maven-plugin**: Converts JSON Schema definitions to Java POJOs (configured in `pom.xml`).
- **Makefile**: The `make generate` command generates Python types from JSON Schema definitions.
- **Swagger**: Generates API documentation following OpenAPI standards.

## Architectural Notes
- The codebase reflects a **schema-first** philosophy: JSON Schema is the source of truth, and code is generated from it.
- The Java backend uses **Dropwizard** as the REST API framework.
- **ContainerResponseFilter** applies event handlers globally to all outgoing API responses, ensuring consistent change event capture.
- Airflow DAG definitions exist in the codebase for backward compatibility, but the [[kubernetes-native-orchestrator]] provides an alternative orchestration method in v1.12+.