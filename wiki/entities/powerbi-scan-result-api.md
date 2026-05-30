---
type: entity
title: PowerBI Scan Result API
created: 2026-05-14
updated: 2026-05-14
tags: [powerbi, api, scan-result, lineage, admin]
related: [powerbi-connector, powerbi-admin-apis, data-lineage]
sources: ["PowerBI Connector  OpenMetadata Integration Documentation.md"]
---
# PowerBI Scan Result API

The PowerBI Scan Result API is a Microsoft PowerBI Admin REST API endpoint used by the [[powerbi-connector|PowerBI Connector]] when operating in [[powerbi-admin-apis|Admin API]] mode. It is the primary mechanism for gathering table and dataset information needed to generate [[data-lineage|lineage]].

## Endpoint

`POST https://api.powerbi.com/v1.0/myorg/admin/workspaces/getInfo`

Reference: [Workspace Info Get Scan Result](https://learn.microsoft.com/en-us/rest/api/power-bi/admin/workspace-info-get-scan-result)

## Key Characteristics

- **No Dataset Type Limitations**: Unlike the [[powerbi-get-dataset-tables-api|Get Dataset Tables API]], the Scan Result API works with all dataset types (imported, DirectQuery, Push, etc.).
- **Admin-Only**: Requires administrative API permissions and the "Allow service principals to use read-only Power BI admin APIs" tenant setting.
- **Full Coverage**: Provides complete table and dataset metadata across all workspaces.

## Role in Lineage Generation

When Admin APIs are enabled, the connector uses this API to extract the detailed table and column information necessary to construct lineage relationships between source database tables and PowerBI dashboards.
