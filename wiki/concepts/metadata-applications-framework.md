---
type: concept
title: Metadata Applications Framework
created: 2026-05-14
updated: 2026-05-14
tags: [automation, applications, marketplace, framework]
related: [application-framework, change-events-system, unified-metadata-graph]
sources: ["OpenMetadata Community Meeting Oct 2023 Release 1 2 0 datamesh openmetadata.md"]
---
# Metadata Applications Framework

The Metadata Applications Framework is a pluggable system introduced in [[OpenMetadata]] 1.2.0 that enables installing, configuring, and scheduling automation applications that run within the OpenMetadata server. It fulfills the original 2021 vision of "automation" by allowing reactive and scheduled actions based on metadata changes.

## Architecture

- **Marketplace**: A catalog of available applications (first-party and eventually third-party) that administrators can browse and install.
- **Manifest**: Each application includes a manifest defining its identity, required metadata access, and configuration schema.
- **Configuration**: Applications expose their own configuration interface for customization during installation.
- **Scheduling**: Applications can be scheduled to run periodically (e.g., hourly) or triggered on-demand.
- **Execution history**: Each application maintains a run history with logs and audit trails.

## Built-in Applications (1.2.0)

- **Data Insights**: Collects and reports on metadata health, KPIs, and asset composition.
- **Data Insights Report**: Sends scheduled email reports on metadata health.
- **Search Indexing**: Reindexes all metadata into ElasticSearch/OpenSearch on a schedule.

## Example Use Cases

- **Tag propagation via lineage**: Automatically propagate descriptions and tags from columns/tables through lineage to downstream dashboards and reports.
- **Lifecycle policies**: Detect unused assets (based on last access time) and automatically tag them for garbage collection or archival.
- **Garbage collection**: Automatically delete or archive data in connected sources (Snowflake, Redshift, BigQuery) based on usage patterns.
- **Reactive automation**: Respond to [[change-events-system|metadata change events]] (schema changes, new assets) with automated actions.

## Relationship to Webhooks

Previously, automation was limited to webhooks — external systems receiving metadata change events. The Application Framework brings automation **inside** the OpenMetadata server, enabling richer, scheduled, and stateful automation without external infrastructure.