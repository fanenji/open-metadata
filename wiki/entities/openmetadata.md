---
sources: [sources.md, OMD - Getting Started.md, Announcing OpenMetadata 1.12 1.md]
tags: [openmetadata, metadata-platform, data-governance, platform, data-catalog, metadata]
related: [ingestion-framework, data-profiling, data-lineage, data-quality, glossary-tags, elasticsearch, mysql-postgresql, unified-metadata-graph, openmetadata-connectors, openmetadata-features, collate-inc, knowledge-graph, mcp-server, openmetadata-ai-sdk, schema-first-approach]
type: entity
title: OpenMetadata
created: 2024-05-24
updated: 2026-07-07
---
# OpenMetadata

OpenMetadata is an open-source, all-in-one platform for data discovery, lineage, data quality, observability, and governance. It centralizes all data context to help organizations build high-quality data and AI assets. It follows a [[schema-first-approach|schema-first architecture]] and provides a [[unified-metadata-graph]] that powers search, collaboration, and AI-driven automation.

## Architecture

OpenMetadata is composed of three main components: the [[ingestion-framework|Ingestion Framework]], the **OpenMetadata Server**, and the **OpenMetadata UI**. The platform ingests metadata from over 90 source systems via turnkey connectors or custom APIs. All metadata is organized into the [[unified-metadata-graph]], providing a single, comprehensive source of truth.

**Core Dependencies:**
- **Application Framework**: [[dropwizard|Dropwizard]] with [[jetty|Jetty]]
- **Database**: [[mysql-8x|MySQL 8.x]] or PostgreSQL
- **Search**: [[elasticsearch-7x|Elasticsearch 7.x]] or OpenSearch
- **Deployment**: [[kubernetes|Kubernetes]] via [[helm-charts|Helm Charts]]

See [[openmetadata-system-architecture]] for detailed architecture documentation.

## Key Features

OpenMetadata provides a comprehensive set of features organized into seven categories:

- **Discovery:** Integrated catalog, data quality, and glossary; natural language search; 90+ [[openmetadata-connectors|turnkey data connectors]].
- **Lineage:** Table and [[column-level-lineage]]; automated data estate mapping with APIs; governance and PII automation.
- **Observability:** Alerting and notifications; [[incident-manager|incident management]]; pipeline monitoring; root cause analysis; anomaly detection; [[data-profiling|data profiler]].
- **Quality:** Table and column-level test cases; no-code and SQL-based tests; [[test-suite|test suites]]; [[data-quality-as-code|quality as code]].
- **Collaboration:** Announcements, tasks, and team conversations; Slack/Teams integration; [[activity-feed|activity feed]] and team dashboards.
- **Governance:** Business [[glossary-terms|glossary]] and [[classification-tags]]; automated PII classification and description generation.
- **Insights:** Data asset analytics; app usage metrics; coverage KPIs; ownership dashboards; data health and governance reports.

## Version History

| Version | Release Date | Key Features |
|---------|-------------|--------------|
| 1.9 | ~2025 | Data Contracts, Agentic AI foundations |
| 1.10 | ~2025 | Profiler Agent, MCP Server improvements |
| 1.11 | ~2025 | Data Quality as Code |
| **1.12** | **Feb 2026** | **AI SDK, Data Quality Test Library, Kubernetes Orchestrator, ODCS 3.1, OpenLineage, Semantic Search, Column Bulk Operations, Audit Logs for AI** |

## 1.12 Highlights

Release 1.12 delivers four strategic capabilities:

1. **[[openmetadata-ai-sdk|AI SDK]]** — Programmatic access to the knowledge graph via MCP, enabling embedding metadata intelligence into any application
2. **[[test-library|Data Quality Test Library]]** — Reusable, parameterized SQL-based test templates with centralized governance
3. **[[kubernetes-native-orchestrator|Kubernetes Orchestrator]]** — Native K8s scheduler replacing Airflow, reducing deployment components from 4 to 3
4. **Open Standards** — [[odcs-open-data-contract-standard|ODCS 3.1]] for data contracts and [[openlineage-integration|OpenLineage]] for lineage ingestion

Additional 1.12 features include:
- [[semantic-search-openmetadata|Semantic Search]] with vector embeddings (Bedrock, OpenAI, HuggingFace)
- [[column-bulk-operations|Column Bulk Operations]] for cross-asset governance
- Lineage improvements: column-only filtering, edge highlighting, stored procedure support, SQLglot integration
- [[audit-logs|User & AI Audit Logs]] with AI agent accountability
- Data Contracts at Data Product level with auto-inheritance
- Column Custom Properties with side panel drawer UI
- Distributed Search Indexing for scalability
- Timezone-Aware Freshness Tests
- New connectors: StarRocks, SFTP, Redshift Serverless
- Snowflake Dynamic Table Metrics

## User Roles

OpenMetadata supports collaboration among diverse teams:
- Data platform engineers
- Governance professionals
- Data scientists and analysts
- Business users

## See Also

- [[collate-inc]] — Managed OpenMetadata service
- [[unified-metadata-graph]] — Core architectural concept
- [[openmetadata-connectors]] — The 90+ connector library
- [[openmetadata-features]] — Detailed feature descriptions
- [[ingestion-framework]] — The metadata ingestion backbone
- [[data-quality]] — Quality testing capabilities
- [[data-lineage]] — Lineage tracking
- [[glossary-tags]] — Business glossary and tags
- [[knowledge-graph]] — Knowledge graph layer
- [[openmetadata-code-layout]] — Codebase structure
