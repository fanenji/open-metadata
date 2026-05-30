---
type: concept
title: Metadata Ingestion Workflow
created: 2026-05-14
updated: 2026-05-14
tags: [metadata-ingestion, administration, workflow, ui]
related: [openmetadata, ingestion-framework, metadata-agent, service-connection, filter-patterns, ingestion-scheduling, openmetadata-administration, openmetadata-connectors, cli-ingestion-with-basic-auth]
sources: ["how-to-ingest-metadata-official-documentation---op-20260514.md"]
---

# Metadata Ingestion Workflow

The canonical UI-driven process for ingesting metadata from third-party sources into OpenMetadata. This workflow is the primary method for administrators to connect external data systems and automate metadata extraction.

## Prerequisites

- **Admin access on the source tool**: You must have administrative privileges on the external system (database, dashboard, pipeline, etc.) to create a connector and ingest metadata.
- **OpenMetadata Admin role**: Access to the Settings and Services pages within OpenMetadata.

## The 8-Step Workflow

### Step 1: Create a Service Connection
Navigate to **Settings → Services → Databases** (or the appropriate service category) and click **Add New Service**.

### Step 2: Select a Connector
Choose the specific connector for your source system (e.g., Snowflake, BigQuery, Redshift) from the available options and click **Next**.

### Step 3: Configure the Service
Enter a unique **Service Name** (no spaces; allowed special characters: `_ - . & ( )`) and an optional **Description** to document the service.

### Step 4: Enter Connection Details
Provide the connection credentials and parameters required by the selected connector. Required fields vary by service type. Connector-specific documentation is available in the right-side panel within the UI.

### Step 5: Test the Connection
Click **Test Connection** to verify connectivity and confirm which data assets are accessible with the provided credentials. The Connection Status panel displays access results. After a successful test, click **Save**.

### Step 6: Save the Service and Add an Agent
Configure default database, schema, and table filter patterns, then save. The Database Service page appears with Insights, Databases, Agents, and Connection tabs. Navigate to the **Agents** tab and click **Add Agent → Add Metadata Agent**.

> **Note**: The Agents tab is visible only to Admins, direct owners of the service, or members of an owner team.

### Step 7: Configure the Metadata Agent
Set up the [[metadata-agent|Metadata Agent]] with:
- **Name**: auto-generated with a unique suffix
- **Filter Patterns**: database, schema, and table inclusion/exclusion rules
- **Toggles**: FQN filtering, Include Views, Include Tags, Debug Log, Mark Deleted Tables
- **Query Parsing Timeout Limit**: timeout for view definition SQL parsing (default: 300 seconds)

### Step 8: Schedule and Deploy
Define the pipeline schedule (preset intervals or custom cron), set the number of retries on failure, and click **Add & Deploy**.

## Post-Deployment

After successful deployment, you can:
- View agent run status (queued, running, failed, successful) on the Agents tab
- Trigger immediate runs, kill running pipelines, redeploy after config changes, edit, or delete agents
- Browse ingested databases, schemas, and tables on the Databases tab
- Create additional pipelines for Usage, Lineage, dbt, or Profiler ingestion

## Relationship to Other Ingestion Methods

This UI-based workflow is the primary ingestion method. An alternative [[cli-ingestion-with-basic-auth|CLI Ingestion with Basic Auth]] approach exists for automation or environments without OAuth. The underlying orchestration backend (Airflow or [[kubernetes-native-orchestrator|Kubernetes-native orchestrator]]) is transparent to this UI workflow, though specific deployment behaviors may vary.