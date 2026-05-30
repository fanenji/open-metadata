---
type: entity
title: dbt Troubleshooting
created: 2026-05-14
updated: 2026-05-14
tags: [dbt, troubleshooting, openmetadata, ingestion]
related: [dbt, dbt-integration, dbt-artifacts, dbt-lineage-ingestion, dbt-artifact-storage, openmetadata]
sources: ["dbt-troubleshooting-openmetadata-integration-suppo-20260514.md"]
---

# dbt Troubleshooting

Consolidated reference for diagnosing and resolving common failures in the [[dbt]]-[[openmetadata|OpenMetadata]] integration. Covers three primary scenarios: the dbt tab not displaying, lineage not appearing, and S3 AccessDenied errors.

## 1. dbt Tab Not Displaying in the UI

After the dbt workflow completes, check the logs for validation errors. Missing keys in `manifest.json` or `catalog.json` are logged and must be added.

### Required Keys in manifest.json Nodes

The following keys must be present in each node of `manifest.json`:

| Key | Requirement | Purpose |
|-----|-------------|---------|
| `resource_type` | Required | Identifies the node type (model, source, etc.) |
| `alias` / `name` | At least one required | Identifies the table/view |
| `schema` | Required | Database schema name |
| `description` | Required if description needs to be updated | Model description |
| `compiled_code` / `compiled_sql` | Required if dbt model query should be shown in dbt tab and for query lineage | Compiled SQL query |
| `depends_on` | Required if lineage information needs to be extracted | Model dependencies |
| `columns` | Required if column descriptions are to be processed | Column metadata |

### Name/Alias/Schema/Database Matching

The `name`/`alias`, `schema`, and `database` values from `manifest.json` must exactly match the `name`, `schema`, and `database` of the table/view already ingested in OpenMetadata. **dbt will only be processed if these values match.** This is the most common root cause of the dbt tab not displaying.

### Sample manifest.json Node

```json
{
  "model.jaffle_shop.customers": {
    "resource_type": "model",
    "depends_on": {
      "nodes": [
        "model.jaffle_shop.stg_customers",
        "model.jaffle_shop.stg_orders",
        "model.jaffle_shop.stg_payments"
      ]
    },
    "database": "dev",
    "schema": "dbt_jaffle",
    "name": "customers",
    "alias": "customers",
    "description": "sample description",
    "columns": {
      "customer_id": {
        "name": "customer_id",
        "description": "This is a unique identifier for a customer"
      },
      "first_name": {
        "name": "first_name",
        "description": "Customer's first name. PII."
      }
    },
    "compiled_code": "sample query"
  }
}
```

## 2. Lineage Not Displaying from dbt

### Prerequisite Ordering

For dbt lineage to work, tables must be ingested **before** dbt ingestion runs. The correct process is:

1. **Ingest tables first**: Run metadata ingestion on the database service so that all tables (models) are ingested into OpenMetadata.
2. **Run dbt ingestion**: Run the dbt workflow on the same service. This adds dbt-related metadata (model definitions, descriptions) and draws lineage from model dependencies in `manifest.json`.

### Debugging Steps

If lineage is not appearing:

1. **Verify table ingestion**: Ensure all tables involved in the lineage are ingested in OpenMetadata.
2. **Check manifest.json**: Confirm that `depends_on` and `compiled_code`/`compiled_sql` keys are present in the relevant nodes. See [[dbt-artifacts]] for details.
3. **Search logs**: Search for the string `Processing dbt lineage for` in the dbt workflow logs to identify errors causing lineage creation to fail.

## 3. S3 AccessDenied Error

### Error Message

```
An error occurred (AccessDenied) when calling the ListBuckets operation: Access Denied
```

### Cause

The IAM policy for the user running ingestion does not grant sufficient permissions on the S3 bucket and its contents.

### Required IAM Policy

The user must have at least the following permissions:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::MyBucket",
        "arn:aws:s3:::MyBucket/*"
      ]
    }
  ]
}
```

**Important**: It is not enough to point the resource only to `arn:aws:s3:::MyBucket`. Both the bucket ARN and the contents ARN (`MyBucket/*`) must be included.

## Related Pages

- [[dbt-integration]] — Overview of the dbt-OpenMetadata integration
- [[dbt-artifacts]] — Detailed reference for dbt artifact files
- [[dbt-lineage-ingestion]] — How dbt transformation lineage is extracted
- [[dbt-artifact-storage]] — Configuration guide for storage backends