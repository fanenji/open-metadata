---
type: entity
title: Superset Connector
created: 2026-05-14
updated: 2026-05-14
tags: [connectors, dashboard, superset, ingestion]
related: [dashboard-connectors, dashboard-lineage, openmetadata-connectors, data-lineage, postgresql-ssl-modes, metadata-ingestion-workflow, service-connection, mysql-8x, postgresql-connector]
sources: ["Superset Connector  OpenMetadata Dashboard Integration.md"]
---
# Superset Connector

The Superset Connector is a turnkey [[dashboard-connectors|dashboard connector]] in OpenMetadata v1.12.x that ingests metadata from Apache Superset dashboards and charts. It supports Superset 2.0.0 and offers two distinct extraction methods.

## Extraction Methods

### API-based Extraction
Extracts metadata via Superset's REST API. Requires the Superset user to have at least `can read on Chart` and `can read on Dashboard` permissions. This is the simpler approach but may provide less metadata depth.

### Database-based Extraction
Extracts metadata directly from Superset's backend database (MySQL or PostgreSQL). Requires `SELECT` privilege on the `dashboards` and `slices` tables within the Superset schema. This method can yield richer metadata.

## SSL Configuration

The connector supports SSL for three connection types:

| Connection Type | SSL Options |
|-----------------|-------------|
| Superset API | `Certificate Path` in Advanced Config |
| Superset MySQL | `caCertificate` (server validation); `ssl_key` + `ssl_cert` + `ssl_ca` (mutual auth) |
| Superset PostgreSQL | SSL modes (`prefer`, `verify-ca`, `allow`, etc.) with CA certificate |

For PostgreSQL SSL details, see [[postgresql-ssl-modes]].

## Lineage

To establish [[dashboard-lineage|lineage from database tables to dashboards]], the corresponding database service name must be explicitly added during configuration. Without this step, dashboard-to-table lineage will not appear in the [[data-lineage|lineage graph]].

## Airflow Dependency Note

The SSL configuration section references the Airflow Server as the location where certificates must be accessible. Users who have migrated to the [[kubernetes-native-orchestrator]] should verify certificate accessibility in the K8s environment.