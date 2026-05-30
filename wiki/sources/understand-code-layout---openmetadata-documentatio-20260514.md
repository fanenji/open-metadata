---
type: source
title: "Understand Code Layout - OpenMetadata Documentation"
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, code-layout, architecture, developer-guide]
related: [openmetadata, openmetadata-code-layout, schema-first-approach, change-events-system, ingestion-framework, openmetadata-connectors, unified-metadata-graph, external-dependencies-configuration]
sources: ["understand-code-layout---openmetadata-documentatio-20260514.md"]
authors: ["OpenMetadata Contributors"]
year: 2026
url: "https://docs.open-metadata.org/v1.12.x/developers/architecture/code-layout"
venue: "OpenMetadata Official Documentation v1.12.x"
---
# Understand Code Layout - OpenMetadata Documentation

This source is the official developer onboarding guide for the OpenMetadata v1.12.x codebase. It provides a high-level map of the repository structure, covering the schema-first metadata model approach, the Java REST API layer (Dropwizard), the Python ingestion framework, and the supporting system components (events, database, Elasticsearch, authentication, and orchestration).

## Key Topics

- **Schema-First Approach**: Metadata models are defined using JSON Schema, then converted to Java POJOs via `jsonschema2pojo-maven-plugin` and to Python types via the Makefile.
- **Entity Types**: Core metadata objects — data, feed, policies, services, tags, teams — are defined under `json/schema/entity`.
- **API Layer**: REST APIs built with Dropwizard, documented with Swagger/OpenAPI, located under `openmetadata-service/src/main/java/org/openmetadata/service/resources`.
- **Change Events**: Entity changes are captured as events, stored in the database, and indexed in Elasticsearch via `ElasticSearchEventPublisher` and `ContainerResponseFilter`.
- **Database**: MySQL or Postgres for the metadata catalog; Flyway manages schema migrations; tables created via `bootstrap/openmetadata-ops.sh`.
- **Ingestion Framework**: A Python framework with Source, Processor, Sink, Stage, and BulkSink components; connectors located under `ingestion/src/metadata/ingestion/`.
- **Orchestration**: Apache Airflow is referenced for pull-based ingestion orchestration, with DAG definitions under `ingestion/examples/airflow/dags`.

This document is essential for developers contributing to OpenMetadata or building custom connectors.