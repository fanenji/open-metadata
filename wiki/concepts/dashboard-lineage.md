---
type: concept
title: Dashboard Lineage
created: 2026-05-14
updated: 2026-05-14
tags: [lineage, dashboard, bi, governance]
related: [data-lineage, superset-connector, dashboard-connectors, dbt-lineage-ingestion]
sources: ["Superset Connector  OpenMetadata Dashboard Integration.md"]
---
# Dashboard Lineage

Dashboard lineage is the traceability path from business-facing dashboards and charts back to the underlying database tables that supply their data. It extends the [[data-lineage|data lineage]] concept into the BI layer, enabling end-to-end visibility from raw data to business consumption.

## Configuration Requirement

To establish dashboard lineage in OpenMetadata, the corresponding database service name must be explicitly added during connector configuration. This is a critical step — without it, the lineage graph will not show connections between dashboards and database tables.

## Lineage Flow

The typical lineage flow is:
```
Database Tables → Dashboards → Charts
```

When combined with [[dbt-lineage-ingestion|dbt lineage]], the full path becomes:
```
Raw Sources → dbt Models → Database Tables → Dashboards → Charts
```

## Supported Connectors

Dashboard lineage is enabled through [[dashboard-connectors|dashboard connectors]] such as the [[superset-connector|Superset Connector]]. Each dashboard connector requires the database service name to be specified for lineage to function.