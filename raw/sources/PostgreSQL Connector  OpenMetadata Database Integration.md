---
title: "PostgreSQL Connector | OpenMetadata Database Integration"
source: "https://docs.open-metadata.org/v1.12.x/connectors/database/postgres"
author:
published:
created: 2026-05-14
description: "Connect PostgreSQL to OpenMetadata with our comprehensive database connector guide. Step-by-step setup, configuration examples, and metadata extraction tips."
tags:
  - "clippings"
topic:
type: "note"
---
## PostgreSQL

PROD

In this section, we provide guides and references to use the PostgreSQL connector. Configure and schedule PostgreSQL metadata and profiler workflows from the OpenMetadata UI:

- [Requirements](#requirements)
- [Metadata Ingestion](#metadata-ingestion)
- [Query Usage](https://docs.open-metadata.org/v1.12.x/connectors/ingestion/workflows/usage)
- [Data Profiler](https://docs.open-metadata.org/v1.12.x/how-to-guides/data-quality-observability/profiler/profiler-workflow)
- [Data Quality](https://docs.open-metadata.org/v1.12.x/how-to-guides/data-quality-observability/quality)
- [Lineage](https://docs.open-metadata.org/v1.12.x/connectors/ingestion/lineage)
- [dbt Integration](https://docs.open-metadata.org/v1.12.x/connectors/database/dbt)
- [Enable Security](#securing-postgres-connection-with-ssl-in-openmetadata)
- [Troubleshooting](https://docs.open-metadata.org/v1.12.x/connectors/database/postgres/troubleshooting)

## Requirements

Note that we only support officially supported PostgreSQL versions. You can check the version list [here](https://www.postgresql.org/support/versioning/).

### Usage & Lineage

For the usage and lineage workflow, OpenMetadata relies on the [`pg_stat_statements`](https://www.postgresql.org/docs/current/pgstatstatements.html) extension to read query history. You need to enable the extension and grant your user read access to query statistics.

**1\. Load the extension at server startup** by adding the following to your `postgresql.conf`:

```ini
shared_preload_libraries = 'pg_stat_statements'
```

After making this change, restart the PostgreSQL server.

**2\. Enable the extension and grant access** by running the following SQL as a superuser:

```sql
CREATE EXTENSION IF NOT EXISTS pg_stat_statements;

-- Grant read access to the OpenMetadata user
GRANT pg_read_all_stats TO your_user;
```

You can find more information on the usage workflow [here](https://docs.open-metadata.org/v1.12.x/connectors/ingestion/workflows/usage) and the lineage workflow [here](https://docs.open-metadata.org/v1.12.x/connectors/ingestion/lineage).

`pg_stat_statements` is **not a query log** — it is a fixed-size, in-memory statistics collector. This has important implications for lineage and usage completeness:

- **Entry eviction**: It stores entries in a hash table controlled by `pg_stat_statements.max` (default: **5000**). When full, the least-executed entries are silently evicted. Queries can disappear before OpenMetadata reads them.
- **Query normalization**: Queries are deduplicated by shape — literal values are replaced with placeholders (e.g., `SELECT * FROM users WHERE id = $1`). Individual executions are not stored.
- **No timestamps**: There is no time data. Only cumulative `calls` count and `total_exec_time` since the last reset are tracked. The **query log duration** setting in OpenMetadata will have no impact — only the **query limit** matters.
- **Resets clear everything**: A server restart or `pg_stat_statements_reset()` wipes all entries.

To get the most complete lineage and usage data, we recommend:

- **Increase `pg_stat_statements.max`** to at least `10000` (or higher) in `postgresql.conf` to reduce entry eviction.
- **Set `pg_stat_statements.track = 'all'`** in `postgresql.conf` to capture queries inside functions and procedures.
- **Schedule frequent ingestion runs** (e.g., every 1–2 hours) to capture queries before they are evicted.
- **Avoid calling `pg_stat_statements_reset()`** before ingestion. If periodic resets are needed, schedule them after ingestion completes.

If your organization restricts direct access to `pg_stat_statements`, or if you need more control over query retention, you can set the **Query Statement Source** connection property to a custom view or table (e.g., `my_schema.custom_query_history`). The custom source must expose the same columns that OpenMetadata reads from `pg_stat_statements`: `userid` (oid), `dbid` (oid), `query` (text), and either `total_exec_time` (double precision, PostgreSQL 13+) or `total_time` (double precision, PostgreSQL < 13). If not set, OpenMetadata defaults to `pg_stat_statements`.

### IAM Authentication

In order to be able to connect via IAM, you need to have the following:

1. Database is configured to use IAM authentication Ensure that the RDS has IAM DB authentication enabled. Otherwise, you can click on Modify to enable it.
2. The user has the necessary IAM permissions Even if you use IAM to connect to postgres, you need to specify a user to prepare the connection. You need to create a user as follows:

```sql
CREATE USER iam_user WITH LOGIN;
GRANT rds_iam TO iam_user;
```

3. The AWS Role has the necessary permissions The role that is going to be used to perform the ingestion, needs to have the following permissions:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "rds-db:connect"
            ],
            "Resource": [
                "arn:aws:rds-db:eu-west-1:<aws_account_number>:dbuser:<rds_db_resource_id>/<postgres_user>"
            ]
        }
    ]
}
```

Otherwise, you might be finding issues such as PAM authentication failed for user “<user>“

## Stored Procedures

When executing stored procedures in PostgreSQL, lineage extraction relies on capturing the SQL queries executed within the procedure. However, by default, PostgreSQL does not track the internal queries of a stored procedure in `pg_stat_statements`.

### Enabling Query Tracking for Lineage

To ensure OpenMetadata captures lineage from stored procedures, follow these steps:

1. **Enable Logging for All Statements** Modify the `postgresql.conf` file and set: `ini    log_statement = 'all'    ` This will log all executed SQL statements, including those inside stored procedures.
2. **Configure `pg_stat_statements` to Track Nested Queries** By default, `pg_stat_statements` may only capture top-level procedure calls and not the internal queries. To change this behavior, update: `ini    pg_stat_statements.track = 'all'    ` This ensures that statements executed within procedures are recorded.

## Metadata Ingestion

To ingest metadata from your sources, you need to create a service connection. The service connects your source system with OpenMetadata. Once you create a service, you can use it to configure your ingestion workflows.  
  
To create a service connection and ingest your metadata, follow the steps below:

## Connection Details

## Securing PostgreSQL Connection with SSL in OpenMetadata

To establish secure connections between OpenMetadata and a PostgreSQL database, you can configure SSL using different SSL modes provided by PostgreSQL, each offering varying levels of security. Under `Advanced Config`, specify the SSL mode appropriate for your connection, such as `prefer`, `verify-ca`, `allow`, and others. After selecting the SSL mode, provide the CA certificate used for SSL validation (`caCertificate`). Note that PostgreSQL requires only the CA certificate for SSL validation.

For IAM authentication, it is recommended to choose the `allow` mode or another SSL mode that fits your specific requirements.

![SSL Configuration](https://mintcdn.com/openmetadata/zq8wMYJ70mT1Pi3x/public/images/connectors/ssl_connection.png?w=2500&fit=max&auto=format&n=zq8wMYJ70mT1Pi3x&q=85&s=9c82accb90c0700523b4523398995ed9)

SSL Configuration

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