---
type: entity
title: OpenMetadata 1.12 Release Notes
created: 2026-02-26
updated: 2026-02-26
tags: [release, openmetadata, software-update]
related: [openmetadata-ai-sdk, openmetadata-kubernetes-orchestrator, openmetadata-data-quality-library]
sources: ["Announcing OpenMetadata 1.12.md"]
---
# OpenMetadata 1.12 Release Notes

The 1.12 release of OpenMetadata focuses on three core pillars: **Standardizing Quality**, **Simplifying Deployment**, and **Supporting Open Standards**.

## Key Features

### 1. AI & Semantic Intelligence
- **OpenMetadata AI SDK**: Enables developers to embed metadata intelligence (lineage, quality, ownership) into external applications like Slack, GitHub, or n8n.
- **Semantic Search**: Uses vector embeddings in [[opensearch-monitoring]] to support natural language discovery via OpenAI, Bedrock, and HuggingFace.
- **MCP Tooling**: New capabilities within the [[model-context-protocol-mcp]] server for lineage creation, test definitions, and Root Cause Analysis (RCA).

### 2. Data Quality & Governance
- **Data Quality Test Library**: A GUI-driven, parameterized approach to SQL-based testing. It allows administrators to create reusable templates, providing a "no-code" alternative to [[dbt]]'s YAML-based testing.
- **Column Bulk Operations**: Allows for unified governance by aggregating identical column names across all assets (tables, topics, APIs) for bulk updates.
- **AI Agent Audit Logs**: Provides transparency by tracking actions taken by both humans and AI agents.

### 3. Infrastructure & Standards
- **Kubernetes Orchestrator**: A major architectural shift that removes the [[apache-airflow]] dependency, reducing the deployment footprint to just the App Server, Database, and Search Index.
- **Open Standards**: Implementation of **ODCS 3.1** for data contracts and **OpenLineage** for seamless lineage ingestion from producers like Spark and Flink.