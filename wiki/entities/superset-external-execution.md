---
type: entity
title: Superset External Execution
created: 2026-05-14
updated: 2026-05-14
tags: [superset, connector, yaml, cli, ingestion, external]
related: [superset-connector, metadata-cli, personal-access-token, filter-patterns, soft-deletion, postgresql-ssl-modes, mysql-8x, postgresql-connector, ingestion-framework, store-service-connection]
sources: ["run-the-superset-connector-externally---openmetada-20260514-2.md"]
---

# Superset External Execution

The Superset External Execution pattern describes how to run the [[superset-connector]] metadata ingestion outside the OpenMetadata UI, using a YAML configuration file and the [[metadata-cli]] command-line tool. This approach is useful for environments where workflows are managed by an external orchestrator rather than the built-in Airflow or K8s-native scheduler.

## Connection Modes

The external execution supports three distinct connection modes, each with specific authentication constraints:

### 1. Superset API Connection (Default)

- Uses Superset REST APIs to fetch metadata
- **Only supports basic or LDAP authentication** — does not work with SSO-enabled Superset instances
- Requires the user to have at least `can read` on Chart and `can read on Dashboard` permissions
- Configuration fields: `hostPort`, `username`, `password`, `provider` (`db` or `ldap`)

### 2. MySQL Database Connection

- Connects directly to the MySQL database backing Superset
- Used when SSO is enabled on the Superset instance
- Requires `SELECT` privilege on `dashboards`, `tables`, and `slices` tables within the `superset` schema
- Configuration fields: `hostPort`, `username`, `password`, `databaseSchema`, optional SSL certificates
- Supports mutual SSL authentication with `caCertificate`, `sslCertificate`, and `sslKey`

### 3. PostgreSQL Database Connection

- Connects directly to the PostgreSQL database backing Superset
- Used when SSO is enabled on the Superset instance
- Requires `SELECT` privilege on `dashboards`, `tables`, and `slices` tables within the `superset` schema
- Configuration fields: `hostPort`, `username`, `password`, `database`, optional `sslMode` and `caCertificate`
- SSL modes: `disable`, `allow`, `prefer`, `require`, `verify-ca`, `verify-full`

## Source Configuration Options

The `sourceConfig` section of the YAML provides fine-grained control over what metadata is ingested:

| Option | Type | Description |
|--------|------|-------------|
| `dbServiceNames` | List | Database service names for ingesting lineage |
| `dashboardFilterPattern` | Regex | Include/exclude dashboards by name |
| `chartFilterPattern` | Regex | Include/exclude charts by name |
| `dataModelFilterPattern` | Regex | Include/exclude data models by name |
| `projectFilterPattern` | Regex | Include/exclude by project name |
| `includeOwners` | Boolean | Include owners; replaces null owners with source owner |
| `includeTags` | Boolean | Include tags in metadata ingestion |
| `includeDataModels` | Boolean | Include data models in metadata ingestion |
| `includeDraftDashboard` | Boolean | Include draft dashboards (default: true) |
| `markDeletedDashboards` | Boolean | Soft-delete dashboards missing from source |
| `markDeletedDataModels` | Boolean | Soft-delete data models missing from source |
| `overrideMetadata` | Boolean | Override existing metadata (description, tags, owner, displayName) |
| `overrideLineage` | Boolean | Override existing lineage |

## SSL Configuration Patterns

Three distinct SSL patterns are documented:

- **Superset API**: Only `caCertificate` is required under `sslConfig`
- **MySQL**: `caCertificate` for basic SSL validation; optionally add `sslCertificate` and `sslKey` for mutual authentication
- **PostgreSQL**: `sslMode` (e.g., `verify-ca`, `verify-full`) plus `caCertificate` under `sslConfig`

## Store Service Connection

The `storeServiceConnection` toggle (default: `true`) controls whether sensitive connection information is stored encrypted in the database (via Fernet Key) or in an external Secrets Manager. When set to `false`, the service connection is used only at runtime and is not sent to the OpenMetadata server.

## CLI Execution

After saving the YAML configuration file, run:

```bash
metadata ingest -c <path-to-yaml>
```

The workflow configuration requires:
- `hostPort` pointing to the OpenMetadata server API
- `authProvider` (e.g., `openmetadata`)
- `securityConfig` with a [[personal-access-token|JWT token]] for authentication
- Optional `verifySSL` and `sslConfig` for server-side SSL

## See Also

- [[superset-connector]] — The main connector page for UI-based ingestion
- [[metadata-cli]] — The CLI tool used for external execution
- [[filter-patterns]] — General filter pattern documentation
- [[soft-deletion]] — Soft-deletion concept and flags
- [[postgresql-ssl-modes]] — PostgreSQL SSL mode reference
- [[store-service-connection]] — The store service connection concept
