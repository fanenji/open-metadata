---
type: concept
title: Service Connection
created: 2026-05-14
updated: 2026-05-14
tags: [metadata-ingestion, connectors, configuration, administration]
related: [openmetadata, metadata-ingestion-workflow, metadata-agent, openmetadata-connectors, ingestion-framework]
sources: ["how-to-ingest-metadata-official-documentation---op-20260514.md"]
---

# Service Connection

A configured link between OpenMetadata and an external data source, encapsulating connection credentials, endpoint details, and access parameters. The Service Connection is the foundational prerequisite for all metadata ingestion — without it, no metadata can be pulled from a source system.

## Creation

Service Connections are created through the OpenMetadata UI under **Settings → Services**. The process involves:

1. Selecting the service category (Databases, Dashboards, Pipelines, ML Models, Messaging, Storage, Metadata)
2. Choosing a specific connector from the [[openmetadata-connectors|library of 90+ connectors]]
3. Providing a unique Service Name and optional Description
4. Entering connection details (credentials, host, port, etc.) specific to the chosen connector
5. Testing the connection to verify access

## Connection Testing

The **Test Connection** feature validates:
- Network connectivity to the source system
- Authentication with the provided credentials
- Which data assets are accessible and can be ingested

The Connection Status panel displays granular access results for the service and its constituent data assets.

## Service Page

Once saved, each Service Connection has a dedicated page with four tabs:

- **Insights**: Usage and health metrics for the service
- **Databases**: Lists all ingested databases (for database services) with drill-down to schemas and tables
- **Agents**: Manages deployed [[metadata-agent|Metadata Agents]] and other ingestion pipelines
- **Connection**: Displays connection details and a summary of ingestible data assets

## Access Control

The Agents tab — where ingestion pipelines are deployed and managed — is visible only to:
- Admin users
- Direct owners of the service
- Members of an owner team

## Lifecycle

Service Connections can be created, edited, or deleted by Admin users. Deleting a service connection permanently removes it and its associated metadata. For temporary removal of specific assets while preserving lineage, use the [[soft-deletion|Mark Deleted Tables]] option on the Metadata Agent instead.