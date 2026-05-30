---
type: entity
title: OpenMetadata
created: 2024-05-24
updated: 2026-05-14
tags: ["openmetadata", "metadata-platform", "data-governance", "platform", "data-catalog"]
related: ["ingestion-framework", "data-profiling", "data-lineage", "data-quality", "glossary-tags", "elasticsearch", "mysql-postgresql", "unified-metadata-graph", "openmetadata-connectors", "openmetadata-features"]
sources: ["sources.md", "OMD - Getting Started.md"]
---

# OpenMetadata

OpenMetadata is an open-source, all-in-one platform for data discovery, lineage, data quality, observability, and governance. It centralizes all data context to help organizations build high-quality data and AI assets. The platform provides a unified metadata store, a powerful ingestion framework, and an intuitive user interface.

## Architecture

OpenMetadata is composed of three main components: the **Ingestion Framework**, the **OpenMetadata Server**, and the **OpenMetadata UI**. The platform ingests metadata from over 90 source systems via turnkey connectors or custom APIs. All metadata is organized into a [[unified-metadata-graph]], providing a single, comprehensive source of truth. The platform can be extended with applications like OpenMetadata AI or custom-built workflows.

## Key Features

OpenMetadata provides a comprehensive set of features organized into seven categories:

- **Discovery:** Integrated catalog, data quality, and glossary; natural language search; 90+ turnkey data connectors.
- **Lineage:** Table and column-level lineage; automated data estate mapping with APIs; governance and PII automation. Tracks the origin and transformation of data across systems.
- **Observability:** Alerting and notifications; incident management; pipeline monitoring; root cause analysis; anomaly detection; data profiler that analyzes data to understand its structure, content, and quality.
- **Quality:** Table and column-level test cases; no-code and SQL-based tests; test suites; quality lineage maps. Defines and runs tests to ensure data reliability.
- **Collaboration:** Announcements, tasks, and team conversations; Slack/Teams integration; activity feed and team dashboards.
- **Governance:** Business glossary and classification tags; automated PII classification and description generation. Provides business metadata for classifying and organizing data assets.
- **Insights:** Data asset analytics; app usage metrics; coverage KPIs; ownership dashboards; data health and governance reports.

## Dependencies

- **Elasticsearch**: Powers the search and discovery capabilities.
- **MySQL/PostgreSQL**: Serves as the metadata store database.
- **Airflow**: Commonly used to orchestrate ingestion pipelines.

## User Roles

OpenMetadata supports collaboration among diverse teams:
- Data platform engineers
- Governance professionals
- Data scientists and analysts
- Business users

## Related Pages

- [[unified-metadata-graph]] — Core architectural concept
- [[openmetadata-connectors]] — The 90+ connector library
- [[openmetadata-features]] — Detailed feature descriptions
- [[ingestion-framework]] — The metadata ingestion backbone
- [[data-quality]] — Quality testing capabilities
- [[data-lineage]] — Lineage tracking
- [[glossary-tags]] — Business glossary and tags