---
type: source
title: "Source: superset-connector-openmetadata-dashboard-integrat-20260514.md"
created: 2026-05-15
updated: 2026-05-15
sources: ["superset-connector-openmetadata-dashboard-integrat-20260514.md"]
tags: []
related: []
---

# Source: superset-connector-openmetadata-dashboard-integrat-20260514.md

## Analysis of: Superset Connector | OpenMetadata Dashboard Integration

### Key Entities

- **Superset** (Product/Platform) — Central entity. Apache Superset (2.0.0+) is the source system whose metadata (dashboards, charts, lineage) is being ingested. Role: source system.
- **OpenMetadata** (Platform) — The target metadata platform ingesting from Superset. Role: destination system.
- **Superset Connector** (Tool/Connector) — The turnkey integration component within OpenMetadata's connector library. Role: central — the entire document describes its configuration and use.
- **MySQL** (Database) — One of two supported backend databases for Superset; used as an alternative ingestion path when SSO is enabled on Superset. Role: peripheral but important alternative.
- **PostgreSQL** (Database) — The other supported backend database for Superset; alternative ingestion path. Role: peripheral but important alternative.
- **Airflow** (Orchestrator) — Mentioned as the server where SSL certificates must be accessible. Role: peripheral infrastructure reference.
- **Hybrid Ingestion Runner** (Component) — Mentioned in a note about secret management for sensitive credential fields. Role: peripheral.

**Wiki existence check:** Superset Connector already exists in the wiki index. The existing page is a stub/overview. This document provides the full detailed content.

### Key Concepts

- **API Connection vs. Database Connection** — Two distinct modes for ingesting Superset metadata. API mode (default) uses Superset REST APIs and requires basic/LDAP auth only (SSO breaks this). Database mode connects directly to Superset's MySQL or PostgreSQL backend, bypassing SSO limitations. This is the core architectural decision point for the connector.
- **Dashboard-to-Table Lineage** — The mechanism by which OpenMetadata traces from dashboards/charts back to underlying database tables. Requires explicit configuration of the Database Service Name in the ingestion pipeline. This is a critical feature for data provenance.
- **Filter Patterns** — Inclusion/exclusion rules at the dashboard, chart, and data model levels using regex. Also includes projectFilterPattern with dot-notation for nested project hierarchies. Standard OpenMetadata pattern applied to dashboard connectors.
- **SSL Configuration** — Three-tier approach: (1) API mode uses Verify SSL (validate/ignore/no-ssl) with optional Certificate Path; (2) MySQL mode uses caCertificate, sslCertificate, sslKey for mutual auth; (3) PostgreSQL mode uses SSL modes (prefer, verify-ca, etc.) with caCertificate only.
- **Soft Deletion** — The "Mark Deleted Dashboards" toggle flags absent dashboards as soft-deleted rather than permanently removing them, preserving lineage.

**Wiki existence check:** Filter Patterns, Soft Deletion, Dashboard Lineage, and SSL modes for PostgreSQL already have dedicated wiki pages. The concept of API vs. Database connection modes for dashboard connectors is not yet documented as a general pattern.

###
