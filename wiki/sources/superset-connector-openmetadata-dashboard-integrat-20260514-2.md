---
type: source
title: "Source: superset-connector-openmetadata-dashboard-integrat-20260514-2.md"
created: 2026-05-15
updated: 2026-05-15
sources: ["superset-connector-openmetadata-dashboard-integrat-20260514-2.md"]
tags: []
related: []
---

# Source: superset-connector-openmetadata-dashboard-integrat-20260514-2.md

## Analysis of: Superset Connector | OpenMetadata Dashboard Integration

### Key Entities

- **Superset** (Product/Platform) — Central entity. Apache Superset (2.0.0+) is the source system from which metadata is ingested. Role: central.
- **OpenMetadata** (Platform) — The metadata platform performing the ingestion. Role: central.
- **MySQL** (Database) — One of two supported backend databases for Superset; used as an alternative ingestion source when SSO is enabled. Role: peripheral.
- **PostgreSQL** (Database) — The other supported backend database for Superset; alternative ingestion source when SSO is enabled. Role: peripheral.
- **Superset API** (Interface) — Default ingestion method; supports basic and LDAP authentication only. Role: peripheral.
- **Airflow Server** (Orchestrator) — Referenced as the location where SSL certificates must be accessible. Role: peripheral.
- **Hybrid Ingestion Runner** (Component) — Mentioned in the context of secret management for credential fields. Role: peripheral.

All entities likely already exist in the wiki. The `[[superset-connector]]` page exists in the index.

### Key Concepts

- **API Connection vs. Database Connection** — Two mutually exclusive methods for ingesting Superset metadata. API is default but fails with SSO; database connection (MySQL or Postgres) is the workaround for SSO-enabled instances. Matters because it defines the primary architectural decision point for connector setup.
- **Dashboard Lineage** — Traceability from dashboards/charts back to database tables, enabled by specifying the Database Service Name. Matters because it connects BI metadata to the underlying data infrastructure.
- **Filter Patterns** — Inclusion/exclusion rules for dashboards, charts, data models, and projects using regex. Matters for controlling ingestion scope and reducing noise.
- **Soft Deletion (Mark Deleted Dashboards)** — Flag to mark absent dashboards as deleted rather than permanently removing them. Matters for preserving lineage and historical metadata.
- **SSL Configuration** — Three distinct SSL setups: Superset API (verify/ignore/no-ssl with certificate path), MySQL (caCertificate, ssl_cert, ssl_key for mutual auth), PostgreSQL (SSL modes like `prefer`, `verify-ca` with caCertificate). Matters for production security.
- **AutoPilot** — Mentioned as handling usage tracking, data lineage, and similar tasks automatically. Matters as a convenience feature reducing manual pipeline management.

All concepts likely already exist in the wiki, though `AutoPilot` may not be documented.

### Main Arguments & Findings

- **Core claim**: The Superset connector provides a turnkey solution for ingesting dashboards, charts, lineage, owners, and datamodels from Apache Superset.
- **Supported features**: Dashboards ✓, Charts ✓, Lineage ✓, Owners ✓, Datamodels ✓, Column Lineage ✓. Tags ✕, Projects ✕.
- **Two ingestion paths**: API (default, basic/LDAP only) or direct database (MySQL/Postgres, required when SSO is enabl
