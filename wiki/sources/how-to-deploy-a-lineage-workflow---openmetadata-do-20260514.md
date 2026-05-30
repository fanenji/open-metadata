---
type: source
title: "Source: how-to-deploy-a-lineage-workflow---openmetadata-do-20260514.md"
created: 2026-05-15
updated: 2026-05-15
sources: ["how-to-deploy-a-lineage-workflow---openmetadata-do-20260514.md"]
tags: []
related: []
---

# Source: how-to-deploy-a-lineage-workflow---openmetadata-do-20260514.md

## Analysis: How to Deploy a Lineage Workflow

### Key Entities

| Name | Type | Role | In Wiki? |
|------|------|------|----------|
| **Lineage Agent** | Workflow component | Central — the primary mechanism for ingesting lineage from query logs | No |
| **Metadata Ingestion** | Workflow | Peripheral — prerequisite that brings in view lineage automatically | Yes ([[metadata-ingestion-workflow]]) |
| **dbt Ingestion** | Workflow | Peripheral — alternative lineage source via dbt artifacts | Yes ([[dbt-integration]], [[dbt-lineage-ingestion]]) |
| **BigQuery, Snowflake, MSSQL, Redshift, Clickhouse, PostgreSQL, Databricks** | Connectors | Peripheral — supported connectors for lineage workflow | Partial ([[postgresql-connector]] exists) |
| **Query Log Duration** | Configuration parameter | Central — controls time window for query log analysis | No |
| **Parsing Timeout Limit** | Configuration parameter | Central — timeout for SQL parsing during lineage analysis | No |
| **Result Limit** | Configuration parameter | Central — row limit for query log results | No |
| **Filter Condition** | Configuration parameter | Central — SQL condition to exclude queries from lineage analysis | No |
| **CSV File** | Data format | Peripheral — fallback method for unsupported connectors | No |

### Key Concepts

| Concept | Definition | Why It Matters | In Wiki? |
|---------|------------|----------------|----------|
| **View Lineage** | Automatic lineage generated from database views during metadata ingestion | Provides basic lineage without separate workflow; column-level included | No |
| **Query Log Lineage** | Lineage derived from parsing database query history logs | More comprehensive than view lineage; captures all table creation and transformation queries | No |
| **Lineage Agent** | Configurable pipeline that extracts query logs and creates lineage relationships | Primary method for deploying lineage workflows via UI | No |
| **Manual Lineage** | User-added or edited lineage relationships | Fallback for unsupported connectors or corrections | No (but [[data-lineage]] exists) |

### Main Arguments & Findings

- **Core claim**: Lineage can be deployed via three methods: (1) automatic view lineage from metadata ingestion, (2) a dedicated Lineage Agent from the UI, or (3) external CLI-based workflow.
- **Key distinction**: Metadata ingestion only captures view lineage; the Lineage Agent captures *all* queries that can generate lineage information.
- **Supported connectors**: Limited set (BigQuery, Snowflake, MSSQL, Redshift, Clickhouse, PostgreSQL, Databricks).
- **Fallback**: CSV file ingestion for unsupported connectors; manual lineage editing always available.
- **Evidence strength**: Official documentation; procedural with configuration details. No empirical validation.

### Connections to Existing Wiki

- **Strengthens**: [[data-lineage]] — provides the deployment procedure missing from the concept page.
- **Extends**: [[metadata-ingestion-workflow]] — clarif
