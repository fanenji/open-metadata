---
title: "Oracle Connector | OpenMetadata Enterprise Database Guide"
source: "https://docs.open-metadata.org/v1.12.x/connectors/database/oracle"
author:
published:
created: 2026-05-14
description: "Connect Oracle OpenMetadata to OpenMetadata effortlessly. Complete setup guide, configuration steps, and troubleshooting tips for seamless data catalog integration."
tags:
  - "clippings"
topic:
type: "note"
---
## Oracle

PROD

In this section, we provide guides and references to use the Oracle connector. Configure and schedule Oracle metadata and profiler workflows from the OpenMetadata UI:

- [Requirements](#requirements)
- [Metadata Ingestion](#metadata-ingestion)
- [Data Profiler](https://docs.open-metadata.org/v1.12.x/how-to-guides/data-quality-observability/profiler/profiler-workflow)
- [Data Quality](https://docs.open-metadata.org/v1.12.x/how-to-guides/data-quality-observability/quality)
- [Lineage](https://docs.open-metadata.org/v1.12.x/connectors/ingestion/lineage)
- [dbt Integration](https://docs.open-metadata.org/v1.12.x/connectors/database/dbt)
- [Troubleshooting](https://docs.open-metadata.org/v1.12.x/connectors/database/oracle/troubleshooting)

## Requirements

**Note**: To retrieve metadata from an Oracle database, we use the `python-oracledb` library, which provides support for versions 12c, 18c, 19c, and 21c. To ingest metadata from oracle user must have `CREATE SESSION` privilege for the user.

```sql
-- CREATE USER
CREATE USER user_name IDENTIFIED BY admin_password;
-- CREATE ROLE
CREATE ROLE new_role;
-- GRANT ROLE TO USER
GRANT new_role TO user_name;
-- Grant CREATE SESSION Privilege.
--   This allows the role to connect.
GRANT CREATE SESSION TO new_role;
-- Grant SELECT_CATALOG_ROLE Privilege.
--   This allows the role ReadOnly Access to Data Dictionaries
GRANT SELECT_CATALOG_ROLE TO new_role;
```

If you don’t want to create a role, and directly give permissions to the user, you can take a look at an example given below.

```sql
-- Create a New User
CREATE USER my_user IDENTIFIED by my_password;
-- Grant CREATE SESSION Privilege.
--   This allows the user to connect.
GRANT CREATE SESSION TO my_user;
-- Grant SELECT_CATALOG_ROLE Privilege.
--   This allows the user ReadOnly Access to Data Dictionaries
GRANT SELECT_CATALOG_ROLE to my_user;
```

**Note**: With just these permissions, your user should be able to ingest the metadata, but not the `Profiler & Data Quality`, you should grant `SELECT` permissions to the tables you are interested in for the `Profiler & Data Quality` features to work.

```sql
-- If you are using a role and do not want to specify a specific table, but any
GRANT SELECT ANY TABLE TO new_role;
-- If you are not using a role, but directly giving permission to the user and do not want to specify a specific table, but any
GRANT SELECT ANY TABLE TO my_user;
-- if you are using role
GRANT SELECT ON ADMIN.EXAMPLE_TABLE TO new_role;
-- if you are not using role, but directly giving permission to the user
GRANT SELECT ON ADMIN.EXAMPLE_TABLE TO my_user;
-- if you are using role
GRANT SELECT ON {schema}.{table} TO new_role;
-- if you are not using role, but directly giving permission to the user
GRANT SELECT ON {schema}.{table} TO my_user;
```

You can find further information [here](https://docs.oracle.com/javadb/10.8.3.0/ref/rrefsqljgrant.html). Note that there is no routine out of the box in Oracle to grant SELECT to a full schema.

## Metadata Ingestion

To ingest metadata from your sources, you need to create a service connection. The service connects your source system with OpenMetadata. Once you create a service, you can use it to configure your ingestion workflows.  
  
To create a service connection and ingest your metadata, follow the steps below:

## Connection Details

## Related

## [Usage Workflow](https://docs.open-metadata.org/v1.12.x/connectors/ingestion/workflows/usage)

Learn more about how to configure the Usage Workflow to ingest Query information from the UI.

## [Lineage Workflow](https://docs.open-metadata.org/v1.12.x/connectors/ingestion/workflows/lineage)

Learn more about how to configure the Lineage from the UI.

## [Profiler Workflow](https://docs.open-metadata.org/v1.12.x/how-to-guides/data-quality-observability/profiler/profiler-workflow)

Learn more about how to configure the Data Profiler from the UI.

## [Data Quality Workflow](https://docs.open-metadata.org/v1.12.x/how-to-guides/data-quality-observability/quality/configure)

Learn more about how to configure the Data Quality tests from the UI.

## [dbt Integration](https://docs.open-metadata.org/v1.12.x/connectors/database/dbt)

Learn more about how to ingest dbt models’ definitions and their lineage.