---
type: entity
title: Apache Superset
created: 2026-05-07
updated: 2026-05-07
tags: [bi, visualization, dashboard, open-source]
related: [dremio, jupyter, stack-cartografico, dremio-reflections]
sources: ["Sintesi Architettura (Claude).md"]
---
# Apache Superset

Apache Superset is an open-source BI and visualization platform used alongside Power BI in the Regione Liguria Data Platform. It provides interactive dashboards, chart building, and embedding capabilities.

## Connection to Dremio

Superset connects to [[dremio]] via:
- **sqlalchemy_dremio** (SQLAlchemy dialect)
- **ODBC** on port 31010
- **Arrow Flight** on port 32010 (high-performance data transfer protocol)

## Key Features

- **Dashboard**: Interactive, filterable dashboards
- **Chart Builder**: Drag-and-drop chart creation with SQL Lab for custom queries
- **Row-Level Security**: Fine-grained access control on dashboard data
- **Embedding**: Dashboard embedding in React applications via iframe/API
- **Authentication**: LDAP/OAuth integration

## Role in Architecture

Superset serves as the primary open-source BI tool for the platform, complementing [[Power BI]] for users who prefer an open-source stack. It queries data through Dremio's virtualization layer, benefiting from [[dremio-reflections]] for query acceleration.