---
type: source
title: PowerBI Connector | OpenMetadata Integration Documentation
created: 2026-05-14
updated: 2026-05-14
tags: [powerbi, dashboard-connector, oauth, azure-ad, metadata-ingestion]
related: [powerbi-connector, dashboard-connectors, dashboard-lineage, filter-patterns, soft-deletion, owner-propagation, service-connection, metadata-ingestion-workflow]
sources: ["powerbi-connector-openmetadata-integration-documen-20260514.md"]
---

# PowerBI Connector | OpenMetadata Integration Documentation

Official OpenMetadata v1.12.x documentation for the PowerBI dashboard connector. Covers requirements, OAuth 2.0 Service Principal authentication setup, Admin vs. Non-Admin API modes, connection details, filter patterns, lineage configuration, and known limitations (no dataflows, no usage ingestion).

## Key Points

- **Authentication**: OAuth 2.0 Service Principal (Client ID, Client Secret, Tenant ID) is the only supported auth type.
- **API Modes**: Admin APIs provide full workspace coverage and complete lineage via Scan Result API. Non-Admin APIs are limited to assigned workspaces and push-dataset-only lineage.
- **Limitations**: PowerBI dataflows not supported. Usage ingestion not supported due to Service Principal auth limitation.
- **Lineage**: Requires database service name configuration. Full lineage only with Admin APIs.
- **Filters**: Dashboard, chart, data model, and project filter patterns supported. Project filters use dot notation for hierarchy.
- **Soft Deletion**: "Mark Deleted Dashboards" toggle flags removed dashboards as soft-deleted.
- **Owner Propagation**: "Include Owners" toggle matches owner emails with existing OpenMetadata users; does not overwrite existing owners.

## Connection Parameters

- `clientId`, `clientSecret`, `tenantId` — Azure AD app credentials
- `scope` — `https://analysis.windows.net/powerbi/api/.default`
- `authorityUri` — Default `https://login.microsoftonline.com/`
- `hostPort` — Default `https://app.powerbi.com`
- `paginationEntityPerPage` — Default 100, max 100

## Azure AD Setup Steps

1. Enable API permissions in PowerBI Admin console (Allow service principals to use PowerBI APIs, Allow service principals to use read-only PowerBI admin APIs, Enhance admin APIs responses with detailed metadata)
2. Create Azure AD app and service principal
3. Grant API permissions: `Dashboard.Read.All` (required), `Dataset.Read.All` (optional, for datamodel/lineage)
4. Create PowerBI workspaces (service principal ignores "My Workspace")

## Source URL

https://docs.open-metadata.org/v1.12.x/connectors/dashboard/powerbi