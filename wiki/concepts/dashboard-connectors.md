---
type: concept
title: Dashboard Connectors
created: 2026-05-14
updated: 2026-05-14
tags: [connectors, dashboard, ingestion, bi]
related: [superset-connector, dashboard-lineage, openmetadata-connectors, data-lineage, metadata-ingestion-workflow, service-connection]
sources: ["Superset Connector  OpenMetadata Dashboard Integration.md"]
---
# Dashboard Connectors

Dashboard connectors are a distinct category of [[openmetadata-connectors|OpenMetadata connectors]] that ingest metadata from Business Intelligence (BI) and dashboard platforms. Unlike database connectors that extract schema, profiling, and query-level metadata, dashboard connectors focus on dashboards, charts, and the lineage between visualizations and underlying data sources.

## Supported Platforms

OpenMetadata v1.12.x includes the [[superset-connector|Superset Connector]] as a supported dashboard connector. Other BI platforms (Tableau, Power BI, Looker) may have their own connectors in the broader connector library.

## Extraction Patterns

Dashboard connectors typically support two extraction methods:

1. **API-based**: Uses the BI platform's REST API with user-level permissions to read dashboard and chart metadata.
2. **Database-based**: Queries the BI platform's backend database directly for richer metadata extraction.

## Lineage

Dashboard connectors enable [[dashboard-lineage|dashboard-to-table lineage]], establishing traceability from visualizations back to the underlying database tables. This requires explicit configuration of the corresponding database service name.

## Relationship to Other Connector Types

Dashboard connectors complement database connectors ([[oracle-connector]], [[postgresql-connector]], [[snowflake]]) and transformation connectors ([[dbt]]) to provide a complete metadata picture spanning from raw data through transformation to business-facing dashboards.