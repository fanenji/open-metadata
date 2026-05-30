---
type: source
title: "How to Ingest Metadata | Official Documentation - OpenMetadata Documentation"
created: 2026-05-14
updated: 2026-05-14
tags: [metadata-ingestion, administration, connectors, scheduling]
related: [metadata-ingestion-workflow, metadata-agent, service-connection, filter-patterns, ingestion-scheduling, soft-deletion]
sources: ["how-to-ingest-metadata-official-documentation---op-20260514.md"]
authors: [OpenMetadata]
year: 2026
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/admin-guide/how-to-ingest-metadata"
venue: "OpenMetadata Documentation v1.12.x"
---

# How to Ingest Metadata | Official Documentation - OpenMetadata Documentation

Official step-by-step guide for integrating third-party data sources with OpenMetadata and running ingestion workflows from the UI. Covers the complete workflow: creating a service connection, configuring a metadata agent with filter patterns, scheduling ingestion pipelines, and managing deployed agents.

The guide uses Snowflake as the primary example but notes that the steps are identical for all supported database services. Key topics include:

- **Service Connection creation**: navigating Settings → Services → Databases → Add New Service
- **Connector selection**: choosing from available database, dashboard, pipeline, ML model, messaging, storage, and metadata service connectors
- **Connection configuration**: entering credentials and testing connectivity
- **Metadata Agent deployment**: configuring database/schema/table filter patterns, toggles for FQN filtering, views, tags, debug logging, and soft deletion
- **Scheduling**: preset intervals (hourly, daily, weekly, monthly) or custom cron expressions with configurable retries
- **Agent management**: viewing run status, triggering immediate runs, killing running pipelines, redeploying after config changes, editing, and deleting agents

Prerequisite: Admin access on the source tool is required to add a connector and ingest metadata.