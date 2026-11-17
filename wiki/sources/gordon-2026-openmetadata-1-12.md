---
type: source
title: "Announcing OpenMetadata 1.12"
created: 2026-07-07
updated: 2026-07-07
tags: [openmetadata, release, changelog, version-1-12]
related: [openmetadata, openmetadata-ai-sdk, data-quality, test-library, kubernetes-native-orchestrator, data-lineage, data-contracts, openlineage-integration, semantic-search-openmetadata, column-bulk-operations, audit-logs, collate-inc, odcs-open-data-contract-standard]
sources: ["https://blog.open-metadata.org/announcing-openmetadata-1-12-9e15b66e7748"]
source_path: "[[raw/sources/Announcing OpenMetadata 1.12 1]]"
---
# Announcing OpenMetadata 1.12

**Author:** Shawn Gordon | **Published:** 2026-02-24 | **Source:** [OpenMetadata Blog](https://blog.open-metadata.org/announcing-openmetadata-1-12-9e15b66e7748)

## Summary

OpenMetadata 1.12 delivers four strategic capabilities: **AI SDK** for programmatic access to the knowledge graph via MCP, a centralized **Data Quality Test Library** for reusable SQL-based test templates, a **Kubernetes Orchestrator** that removes the Airflow dependency, and **Open Standards** support (ODCS 3.1 for data contracts, OpenLineage for lineage metadata).

Additional features include User & AI Audit Logs, Column Bulk Operations, lineage improvements (column filtering, edge highlighting, SQLglot integration), and nine new connectors. The Collate 1.12 managed service adds AI Studio, Custom Auto Classification, Data Diff, GitHub Metadata Sink, and enhanced AskCollate.

## Key Features

### AI SDK
Programmatic access to OpenMetadata's [[unified-metadata-graph|Unified Metadata Graph]] via MCP. Enables embedding metadata intelligence into any application — chatbots, AI agents, CI/CD pipelines. See [[openmetadata-ai-sdk]].

### Data Quality Test Library
Reusable, parameterized SQL-based test templates managed through a GUI. Administrators define tests centrally; users apply via no-code forms. See [[test-library]].

### Kubernetes Orchestrator
Native K8s scheduler replaces Airflow for ingestion workflows. Simplifies deployment from 4 components to 3 (app server, database, search index). See [[kubernetes-native-orchestrator]].

### Open Standards
- **ODCS 3.1**: Import/export data contracts in Open Data Contract Standard format
- **OpenLineage**: Native API ingestion of lineage metadata from Flink, Spark, Airflow, dbt

### Lineage Improvements
Column-only filtering, edge highlighting, stored procedure support, column pagination, and SQLglot integration for faster query parsing.

### Collate 1.12 (Enterprise)
AI Studio, Custom Auto Classification, Data Diff, GitHub Metadata Sink (beta), enhanced AskCollate, SQL Studio extensions (Postgres, Redshift), Metadata Exporter, and new connectors (Microsoft Fabric, Dremio, MuleSoft).