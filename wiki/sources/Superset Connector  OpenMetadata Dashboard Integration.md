---
type: source
title: "Superset Connector: OpenMetadata Dashboard Integration"
created: 2026-05-14
updated: 2026-05-14
tags: [connectors, dashboard, superset, ingestion]
related: [superset-connector, dashboard-connectors, dashboard-lineage, openmetadata-connectors, data-lineage, postgresql-ssl-modes, metadata-ingestion-workflow, service-connection]
sources: ["Superset Connector  OpenMetadata Dashboard Integration.md"]
authors: []
year: 2026
url: "https://docs.open-metadata.org/v1.12.x/connectors/dashboard/superset"
venue: "OpenMetadata Official Documentation"
---
# Superset Connector: OpenMetadata Dashboard Integration

Official documentation for the Apache Superset connector in OpenMetadata v1.12.x. Covers requirements, connection details, SSL configuration for API and database backends, and lineage setup from database tables to dashboards.

## Requirements

- **Superset Version**: Compatible with Superset 2.0.0.
- **API Connection**: User must have at least `can read on Chart` and `can read on Dashboard` permissions.
- **Database Connection**: Database user must have `SELECT` privilege on `dashboards` and `slices` tables within the Superset schema (MySQL or PostgreSQL).

## Connection Details

The connector supports two extraction methods:
1. **API-based**: Extracts metadata via Superset's REST API.
2. **Database-based**: Extracts metadata directly from Superset's backend database.

## SSL Configuration

Three distinct SSL configuration paths are documented:
- **Superset API SSL**: Configure `Certificate Path` in Advanced Config; certificates must be accessible from the Airflow Server.
- **Superset MySQL SSL**: `caCertificate` for server validation; `ssl_key` + `ssl_cert` + `ssl_ca` for mutual authentication.
- **Superset PostgreSQL SSL**: SSL modes (`prefer`, `verify-ca`, `allow`, etc.) with CA certificate for validation.

## Lineage

To establish lineage from database tables to dashboards, the corresponding database service name must be explicitly added during configuration.