---
type: entity
title: Oracle Connector
created: 2026-05-14
updated: 2026-05-15
tags: [oracle, connector, ingestion, database, openmetadata, oracle-troubleshooting-guide-openmetadata-support--20260514, workflow-deployment-error, ingestion-pipeline-troubleshooting, debug-logging, oracle-schema-select-limitation]
related: [openmetadata-connectors, service-connection, metadata-ingestion-workflow, data-profiling, data-quality, dbt-integration, data-lineage, filter-patterns, ingestion-scheduling, oracle-troubleshooting-guide-openmetadata-support--20260514, workflow-deployment-error, ingestion-pipeline-troubleshooting, debug-logging, oracle-schema-select-limitation]
sources: ["Oracle Connector  OpenMetadata Enterprise Database Guide.md", "oracle-troubleshooting-guide-openmetadata-support--20260514.md"]
---
# Oracle Connector

The Oracle Connector is a turnkey connector within OpenMetadata's [[openmetadata-connectors|ingestion framework]] that extracts metadata from Oracle databases. It supports Oracle versions 12c, 18c, 19c, and 21c through the `python-oracledb` library. This document covers permission models, driver details, the schema-level SELECT limitation, and troubleshooting tips.

## Supported Workflows

- **Metadata Ingestion**: Extracts schema, table, and structural metadata.
- **Profiler & Data Quality**: Requires additional `SELECT` permissions beyond basic metadata ingestion.
- **Usage & Lineage**: Captures query logs and transformation lineage.
- **dbt Integration**: Ingests dbt model definitions and lineage for Oracle sources.

## Permission Requirements

### Minimum for Metadata Ingestion

The Oracle user must have:

- `CREATE SESSION` — allows the user to connect to the database.
- `SELECT_CATALOG_ROLE` — grants read-only access to data dictionary views.

These can be assigned via a role or granted directly to the user.

### Additional for Profiler & Data Quality

Profiling and data quality tests require `SELECT` on the specific tables being analyzed. Options:

- `SELECT ANY TABLE` — broad access to all tables (use with caution).
- `SELECT ON {schema}.{table}` — granular, per-table grants.

**Oracle Limitation**: There is no built-in Oracle routine to grant `SELECT` on an entire schema. Administrators must either grant `SELECT ANY TABLE` or enumerate individual table grants. This differs from PostgreSQL and MySQL, which support schema-level `SELECT` grants.

## Permission Models

### Role-Based (Recommended)

```sql
CREATE USER user_name IDENTIFIED BY admin_password;
CREATE ROLE new_role;
GRANT new_role TO user_name;
GRANT CREATE SESSION TO new_role;
GRANT SELECT_CATALOG_ROLE TO new_role;
-- For Profiler/Quality:
GRANT SELECT ANY TABLE TO new_role;
-- Or per-table:
GRANT SELECT ON ADMIN.EXAMPLE_TABLE TO new_role;
```

### Direct User Grants

```sql
CREATE USER my_user IDENTIFIED BY my_password;
GRANT CREATE SESSION TO my_user;
GRANT SELECT_CATALOG_ROLE TO my_user;
-- For Profiler/Quality:
GRANT SELECT ANY TABLE TO my_user;
-- Or per-table:
GRANT SELECT ON ADMIN.EXAMPLE_TABLE TO my_user;
```

## Connection to OpenMetadata

The Oracle Connector integrates with the standard [[metadata-ingestion-workflow]]. Users first create a [[service-connection]] encapsulating Oracle credentials and connection details, then configure a [[metadata-agent]] with appropriate [[filter-patterns]] and [[ingestion-scheduling]].

## Troubleshooting

The official troubleshooting guide ([[oracle-troubleshooting-guide-openmetadata-support--20260514]]) documents three common scenarios:

### Workflow Deployment Error

If errors occur during workflow deployment, the Ingestion Pipeline Entity is still created, but no workflow runs. To recover, Edit the Ingestion Pipeline and Deploy it again. This follows the general [[workflow-deployment-error]] pattern.

### Debug Logging

To enable debug logging for the Oracle connector (or any ingestion):
1. Navigate to **Settings > Services > Database**.
2. Select the Oracle service.
3. Go to the **Ingestion** tab, click the three-dot menu, and select **Edit**.
4. Enable the **Debug Log** option and click **Next**.
5. Configure the schedule and click **Submit**.

See [[debug-logging]] for the generic procedure.

### Permission Issues

Ensure all prerequisites and access configurations for the Oracle connector are properly implemented. Refer to the Permission Requirements section above and the [[oracle-schema-select-limitation]] page for a known Oracle-specific permission constraint.

## See Also

- [[data-profiling]] — Profiler workflow documentation
- [[data-quality]] — Data quality test configuration
- [[dbt-integration]] — dbt integration overview
- [[data-lineage]] — Lineage ingestion workflows
- [[oracle-troubleshooting-guide-openmetadata-support--20260514]] — Troubleshooting guide