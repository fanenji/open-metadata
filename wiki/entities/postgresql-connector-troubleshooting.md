---
type: entity
title: PostgreSQL Connector Troubleshooting
created: 2026-05-14
updated: 2026-05-14
tags: [postgresql, connector, troubleshooting, ingestion, lineage]
related: [postgresql-connector, pg-stat-statements, ingestion-pipeline-troubleshooting, workflow-deployment-error, postgresql-iam-authentication, stored-procedure-lineage]
sources: ["postgresql-connector-troubleshooting---openmetadat-20260514.md"]
---

# PostgreSQL Connector Troubleshooting

This page consolidates all known troubleshooting scenarios for the [[postgresql-connector]] in OpenMetadata. It is derived from the official troubleshooting documentation and extends the general [[ingestion-pipeline-troubleshooting]] reference with PostgreSQL-specific error patterns.

## Workflow Deployment Error

If errors occur during workflow deployment, the Ingestion Pipeline Entity is still created, but no workflow runs in the ingestion container. This is a recoverable partial failure.

**Resolution**: Edit the Ingestion Pipeline and re-deploy it. From the Connection tab, you can also edit the Service if needed.

This pattern is also documented for the [[powerbi-connector]] and is a general behavior of the ingestion framework. See [[workflow-deployment-error]] for the general pattern.

## Debug Logging

To enable debug logging for any ingestion workflow:
1. Navigate to **Settings > Services > Service Type (e.g., Database)**.
2. Select the service.
3. Go to the **Ingestion** tab, click the three-dot menu, and select **Edit**.
4. Enable the **Debug Log** option and click **Next**.
5. Configure the schedule and click **Submit**.

## Permission Issues

If permission-related errors occur during connector setup or metadata ingestion, verify that all prerequisites and access configurations specified for the connector are properly implemented. Refer to the [[postgresql-connector]] page for the required permissions.

## pg_stat_statements: Relation Does Not Exist

**Error**: `(psycopg2.errors.UndefinedTable) relation "pg_stat_statements" does not exist`

**Cause**: The [[pg-stat-statements]] extension is not enabled.

**Solution**:
```sql
CREATE EXTENSION IF NOT EXISTS pg_stat_statements;
```
Also ensure the extension is loaded at server startup by setting `shared_preload_libraries = 'pg_stat_statements'` in `postgresql.conf`, then restart the PostgreSQL server.

## Incomplete or Missing Lineage/Usage Data

**Issue**: Lineage or usage data appears incomplete — some queries or tables are missing, or the number of tracked queries decreases over time.

**Cause**: [[pg-stat-statements]] is a fixed-size, in-memory hash table (default 5000 entries). When full, least-executed entries are silently evicted. Server restarts also clear all entries.

**Solutions**:
1. **Increase `pg_stat_statements.max`** to at least 10000 (or higher) in `postgresql.conf`.
2. **Run ingestion more frequently** — schedule usage and lineage pipelines every 1–2 hours instead of daily.
3. **Do not reset stats before ingestion** — avoid calling `pg_stat_statements_reset()` before an ingestion run.
4. **Use a custom query source** — periodically snapshot `pg_stat_statements` contents into a persistent table and point OpenMetadata to it using the `queryStatementSource` connection property. See the Usage & Lineage section for details.

## Column XYZ Does Not Exist (Unsupported PostgreSQL Version)

**Error**: `psycopg2.errors.UndefinedColumn: column "relispartition" does not exist`

**Cause**: The PostgreSQL version is below the minimum supported by OpenMetadata. The error occurs when the connector attempts to check `relispartition` in the `pg_class` table, a column only available in PostgreSQL 12+.

**Resolution**: Upgrade to a supported PostgreSQL version. Refer to the official PostgreSQL version list.

## Error: no pg_hba.conf entry for host

**Error**: `(psycopg2.OperationalError) FATAL: no pg_hba.conf entry for host "x.xx.xxx.x", user "xxxxxx", database "xxxxx", no encryption`

**Cause**: The connecting host is not permitted by the server's `pg_hba.conf` configuration.

**Solutions**:
1. **Whitelist the IP address** — ensure the IP from the OpenMetadata Service wizard is allowed in the database firewall rules (Azure Firewall rules for Azure-managed PostgreSQL).
2. **Verify network access** — ensure the PostgreSQL server is accessible from the internet for the allowed IP addresses. Adjust VPN or private network settings if needed.
3. **Adjust SSL mode** — set **SSL Mode** to `Allow` in the OpenMetadata Service configuration.

## Error: PAM authentication failed for user

**Error**: `PAM authentication failed for user "<user>"`

**Cause**: The user lacks the necessary IAM permissions for AWS RDS IAM authentication.

**Resolution**: Ensure three conditions are met:
1. **Database configured for IAM authentication** — RDS has IAM DB authentication enabled.
2. **User has necessary IAM permissions** — create the user and grant `rds_iam`:
   ```sql
   CREATE USER iam_user WITH LOGIN;
   GRANT rds_iam TO iam_user;
   ```
3. **AWS Role has necessary permissions** — the role used for ingestion must have the following IAM policy:
   ```json
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Effect": "Allow",
         "Action": ["rds-db:connect"],
         "Resource": ["arn:aws:rds-db:eu-west-1:<aws_account_number>:dbuser:<rds_db_resource_id>/<postgres_user>"]
       }
     ]
   }
   ```

See [[postgresql-iam-authentication]] for more details.
