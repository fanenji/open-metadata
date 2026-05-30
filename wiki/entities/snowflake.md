---
type: entity
title: Snowflake
created: 2026-05-14
updated: 2026-05-14
tags: [connector, database, snowflake, data-warehouse]
related: [openmetadata, openmetadata-connectors, service-connection, metadata-agent, metadata-ingestion-workflow]
sources: ["how-to-ingest-metadata-official-documentation---op-20260514.md"]
---

# Snowflake

A cloud-based data warehouse platform and one of the supported database connectors in OpenMetadata. Snowflake is used as the primary example throughout the official [[metadata-ingestion-workflow|Metadata Ingestion Workflow]] documentation, demonstrating the end-to-end process of creating a service connection, configuring a metadata agent, and scheduling ingestion.

## In OpenMetadata

Snowflake is one of the 90+ turnkey connectors in the [[openmetadata-connectors|OpenMetadata connector library]]. It supports ingestion of:
- Databases, schemas, tables, and columns
- Views (when Include Views is enabled)
- Tags and classifications (when Include Tags is enabled)
- Query parsing for lineage analysis

## Connection Configuration

The Snowflake connector requires standard connection details (account, warehouse, database, schema, username, password/private key) configured through the [[service-connection|Service Connection]] UI. Required fields are documented in the connector-specific panel within the OpenMetadata UI.

## Usage in Documentation

The official "How to Ingest Metadata" guide uses Snowflake as the reference example, noting that the steps are identical for all other supported database services. This makes Snowflake the de facto reference implementation for understanding the ingestion workflow.