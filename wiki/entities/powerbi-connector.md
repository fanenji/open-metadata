---
type: entity
title: PowerBI Connector
created: 2026-05-14
updated: 2026-05-15
tags: [powerbi, connector, dashboard, ingestion, lineage, oauth, azure, dashboard-connector, microsoft, dashboard-connectors, connectors]
related: [openmetadata-connectors, data-lineage, metadata-ingestion-workflow, service-connection, powerbi-admin-apis, powerbi-non-admin-apis, oauth-service-principal, push-dataset-limitation, powerbi-usage-ingestion-limitation, dashboard-connectors, dashboard-lineage, ingestion-pipeline-troubleshooting, workflow-deployment-error, debug-logging-ingestion, filter-patterns, soft-deletion, owner-propagation, azure-ad-service-principal, superset-connector, powerbi-admin-vs-non-admin-apis, pbit-file-lineage-extraction, cli-ingestion-with-basic-auth]
sources: ["PowerBI Connector  OpenMetadata Integration Documentation.md", "powerbi-dashboard-troubleshooting-guide-openmetada-20260514.md", "powerbi-connector-openmetadata-integration-documen-20260514.md", "powerbi-dashboard-troubleshooting-guide-openmetada-20260514-2.md", "run-the-powerbi-connector-externally---openmetadat-20260514.md"]
---

# PowerBI Connector

## Overview

The PowerBI Connector is a turnkey [[dashboard-connectors|dashboard connector]] in the [[openmetadata-connectors]] library for ingesting metadata from Microsoft PowerBI into [[OpenMetadata]]. It extracts dashboards, charts, datasets, data models, projects, lineage, column lineage, and owners, providing full visibility into the Power BI data estate within the [[unified-metadata-graph]]. It supports both UI-driven and external (YAML/CLI) execution modes.

**Key Features:**
- Dashboards, charts, data models, and projects — full metadata ingestion.
- Lineage extraction via admin/non-admin APIs and via `.pbit` file-based extraction.
- Column lineage support.
- Owner extraction (use `includeOwners` toggle; matches owner emails with existing OpenMetadata users, does not overwrite existing owners – see [[owner-propagation]]).
- Tag ingestion is not supported; the `includeTags` toggle has no effect as PowerBI does not provide tags via its APIs.
- Usage ingestion is not supported.

## Requirements

- **PowerBI Pro License** — Required for API access.
- **Azure AD Application** — Must be registered with appropriate API permissions.
- **Tenant Settings** — A PowerBI Admin must enable service principal API access from the PowerBI Admin console.

## Authentication

The connector supports only **OAuth 2.0 Service Principal** authentication via Azure AD (see [[oauth-service-principal]]). The following credentials must be configured:

- `clientId` — Azure AD Application (Client) ID
- `clientSecret` — Azure AD Client Secret
- `tenantId` — Azure AD Directory (Tenant) ID
- `scope` — `https://analysis.windows.net/powerbi/api/.default`
- `authorityUri` — Default `https://login.microsoftonline.com/`
- `hostPort` — Default `https://app.powerbi.com`

In addition, **"Allow public client flows"** must be enabled in the Azure Authentication configuration.

### Required API Permissions

The Azure AD app must have `Dashboard.Read.All` (required) and `Dataset.Read.All` (optional but needed for dataset information and lineage). Tenant-related permissions must not be granted to the app.

## API Modes

A critical configuration choice, toggled by the **Use Admin APIs** setting, determines the scope and completeness of metadata ingestion:

| Feature | Admin APIs (Enabled) | Non-Admin APIs (Disabled) |
|---------|----------------------|---------------------------|
| **Workspace Coverage** | All workspaces in the PowerBI instance | Only workspaces with the service principal’s security group assigned |
| **Lineage Source** | [[powerbi-scan-result-api\|Scan Result API]] (no limitations) | [[powerbi-get-dataset-tables-api\|Get Dataset Tables API]] |
| **Lineage Completeness** | Full lineage for all datasets | Only for push datasets |
| **Permission Level** | Admin-level API access | Workspace-level access |

When Admin APIs are enabled, the connector fetches metadata from **all** workspaces and uses the Scan Result API for full lineage. When disabled, only workspaces where the service principal is assigned are accessible, and lineage is limited to push datasets via the Get Dataset Tables API (see [[push-dataset-limitation]]).

In addition to API-based lineage, the connector also supports lineage extraction from `.pbit` files (Power BI template files) when provided through the `pbitFilesSource` configuration (see [[pbit-file-lineage-extraction]]).

## Connection Parameters

- `clientId`, `clientSecret`, `tenantId`, `scope`, `authorityUri`, `hostPort` — As described in Authentication.
- `paginationEntityPerPage` (UI) / `pagination_entity_per_page` (YAML) — Pagination limit (default 100, max 100).
- `useAdminApis` — Boolean toggle for selecting Admin or Non-Admin mode.
- `pbitFilesSource` — (For external execution) Path or source configuration for `.pbit` files for lineage extraction.

## Filter Patterns

Regex-based include/exclude filters for selective ingestion:

- **Dashboard Filter Pattern** — Regex for dashboards.
- **Chart Pattern** — Regex for charts.
- **Data Model Pattern** — Regex for data models.
- **Project Filter Pattern** — Regex for project hierarchy using dot notation (e.g., `Project1.NestedProjectA`).

These patterns are configured in the `sourceConfig` section of the connector.

## Ingestion Options

The following options can be configured during ingestion pipeline setup (UI) or in the source configuration (external YAML). For external execution, the YAML uses an array of `dbServiceNames` and camelCase options.

- **Database Service Name(s)** / `dbServiceNames` — Required for establishing [[data-lineage|lineage]] between database tables and PowerBI dashboards (see [[dashboard-lineage]]).
- **Include Owners** / `includeOwners` — Matches owner emails with existing OpenMetadata users; does not overwrite existing owners (see [[owner-propagation]]).
- **Include Tags** / `includeTags` — Toggle for tag ingestion (currently not supported for PowerBI; see note above).
- **Include Data Models** / `includeDataModels` — Toggle for data model ingestion.
- **Mark Deleted Dashboards** / `markDeletedDashboards` — Soft-deletion toggle for removed dashboards (see [[soft-deletion]]).
- **Mark Deleted Data Models** / `markDeletedDataModels` — Soft-deletion toggle for removed data models.
- **Include Draft Dashboard** / `includeDraftDashboard` — Toggle for including draft dashboards (enabled by default).
- **Override Metadata** / `overrideMetadata` — Allow overriding existing metadata.
- **Override Lineage** / `overrideLineage` — Allow overriding existing lineage.
- **Enable Debug Log** / `loggerLevel` — Toggle for debug-level logging (see [[debug-logging-ingestion]]).

## Setup Procedure

1. **Enable API Permissions** (PowerBI Admin Console) — Allow service principals to use Power BI APIs, read-only admin APIs, and enhance API responses with detailed metadata.
2. **Create Azure AD App** — Register an application in Azure AD following the service principal setup guide.
3. **Grant API Permissions** — Add `Dashboard.Read.All` (required) and `Dataset.Read.All` (optional) with admin consent. Ensure no tenant-level permissions are granted.
4. **Create Workspaces** — Create new workspaces in PowerBI; the service principal does not access default user workspaces (e.g., "My Workspace").
5. **Configure Service Connection** — In the OpenMetadata UI, set up the connection with the required authentication and parameters. For external execution, create a YAML configuration file.

## External Execution (YAML/CLI)

The connector can be run externally using a YAML configuration file and the `metadata ingest -c <path-to-yaml>` CLI command. The YAML configuration covers:

- **Source Configuration** — `clientId`, `clientSecret`, `tenantId`, `scope`, `authorityUri`, `hostPort`, `pagination_entity_per_page`, `useAdminApis`, `pbitFilesSource`.
- **Source Config** — `dbServiceNames`, filter patterns, `includeOwners`, `includeTags`, `includeDataModels`, `markDeletedDashboards`, `markDeletedDataModels`, `includeDraftDashboard`, `overrideMetadata`, `overrideLineage`.
- **Sink Configuration** — `type: metadata-rest`.
- **Workflow Configuration** — `openMetadataServerConfig` (with `hostPort`, `authProvider`, `securityConfig`), `loggerLevel`, `storeServiceConnection`, SSL configuration.

See [[cli-ingestion-with-basic-auth]] for authentication details and [[pbit-file-lineage-extraction]] for `.pbt` extraction.

## Limitations

- **Dataflows** — PowerBI dataflows are not supported.
- **Usage Ingestion** — Not supported; the Power BI Usage API does not accept Service Principal authentication (see [[powerbi-usage-ingestion-limitation]]).
- **Non-Admin API Lineage** — When using Non-Admin APIs, lineage is restricted to push datasets only.
- **Default Workspaces** — The service principal ignores default user workspaces; workspaces must be created explicitly.
- **Tags** — Not supported (see Ingestion Options note).

## Troubleshooting

Common issues and recovery steps:

1. **Workflow Deployment Error** — The ingestion pipeline entity is created but no workflow runs. Recovery involves editing and redeploying the pipeline (see [[workflow-deployment-error]]).
2. **Debug Logging** — Enable verbose logging using the *Enable Debug Log* toggle in the ingestion edit dialog (Settings > Services > Service > Ingestion > Edit > Debug Log), or via the five-step UI procedure (Services → Select node → Ingestion tab → Edit → Enable Debug Log). This is a generic procedure applicable to all connectors (see [[debug-logging-ingestion]]). In external execution, set `loggerLevel: DEBUG`.
3. **Permission Issues** — Verify connector prerequisites and access configurations. The guide defers to connector-specific documentation for required permissions (see [[ingestion-pipeline-troubleshooting]]).

### Open Questions

The following questions were raised but not directly answered in the official troubleshooting guide (v1.12.x):

- What specific PowerBI permissions (e.g., workspace access, API scopes) are required for metadata ingestion?
- What root causes trigger the Workflow Deployment Error (network issues, invalid credentials, resource limits)?

## Related Pages

- [[dashboard-connectors]] — Category of connectors for BI/dashboard platforms.
- [[dashboard-lineage]] — Traceability from dashboards to underlying tables.
- [[data-lineage]] — General data lineage concepts.
- [[service-connection]] — Service connection configuration.
- [[filter-patterns]] — Using regex filters in ingestion.
- [[soft-deletion]] — Marking entities as deleted.
- [[owner-propagation]] — Propagating owners from source.
- [[ingestion-pipeline-troubleshooting]] — General troubleshooting.
- [[workflow-deployment-error]] — Partial failure mode.
- [[debug-logging-ingestion]] — Debug logging procedure.
- [[superset-connector]] — Another dashboard connector.
- [[powerbi-admin-vs-non-admin-apis]] — Detailed API mode comparison.
- [[pbit-file-lineage-extraction]] — pbit file lineage extraction.
- [[metadata-ingestion-workflow]] — UI-driven ingestion process.
- [[cli-ingestion-with-basic-auth]] — CLI ingestion authentication.