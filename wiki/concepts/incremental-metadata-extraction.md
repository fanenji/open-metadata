---
type: concept
title: Incremental Metadata Extraction (Beta)
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, ingestion, metadata, beta]
related: [postgresql-connector, metadata-ingestion-workflow, metadata-agent, filter-patterns]
sources: ["postgresql-connector-openmetadata-database-integra-20260514.md"]
---

# Incremental Metadata Extraction (Beta)

Incremental Metadata Extraction is a Beta feature in OpenMetadata that enables changed-table detection after the first execution. Instead of extracting metadata from all tables on every run, it only processes tables that have changed since the last successful pipeline run.

## How It Works

After the first full metadata extraction, subsequent runs use the timestamp of the last successful pipeline run as a base to search for updated entities. This reduces the load on the source system and speeds up ingestion.

## Configuration Parameters

- **Enabled**: If True, enables Metadata Extraction to be Incremental.
- **Lookback Days**: Number of days to search back for a successful pipeline run. The timestamp of the last found successful pipeline run will be used as a base to search for updated entities.
- **Safety Margin Days**: Number of days to add to the last successful pipeline run timestamp to search for updated entities.

## Availability

Incremental Metadata Extraction is currently only available for:

- BigQuery
- Redshift
- Snowflake

It is **not available** for PostgreSQL or most other database connectors.

## Related Pages

- [[postgresql-connector]] — PostgreSQL connector documentation noting this feature is not available.
- [[metadata-ingestion-workflow]] — The canonical UI-driven process for ingesting metadata.
- [[metadata-agent]] — Configurable, schedulable pipeline that extracts metadata.
- [[filter-patterns]] — Inclusion/exclusion rules to control ingestion scope.