---
type: concept
title: PowerBI Admin APIs
created: 2026-05-14
updated: 2026-05-14
tags: [powerbi, api, admin, ingestion, lineage]
related: [powerbi-connector, powerbi-non-admin-apis, powerbi-scan-result-api, data-lineage]
sources: ["PowerBI Connector  OpenMetadata Integration Documentation.md"]
---
# PowerBI Admin APIs

The PowerBI Admin APIs are a set of Microsoft PowerBI REST APIs that provide administrative-level access to PowerBI metadata. When the [[powerbi-connector|PowerBI Connector]] is configured to use Admin APIs, it can fetch dashboard and chart metadata from **all workspaces** in the PowerBI instance.

## Capabilities

- **Full Workspace Coverage**: Access to metadata from every workspace, regardless of service principal assignment.
- **Unrestricted Lineage**: Uses the [[powerbi-scan-result-api|Scan Result API]] to gather table and dataset information for lineage generation, with no limitations on dataset types.
- **Enhanced Metadata**: Admin API responses can include detailed metadata when the "Enhance admin APIs responses with detailed metadata" tenant setting is enabled.

## Requirements

- The PowerBI Admin must enable "Allow service principals to use read-only Power BI admin APIs" in the Tenant settings.
- The Azure AD application must have appropriate API permissions with admin consent.

## Comparison with Non-Admin APIs

See [[powerbi-non-admin-apis]] for the alternative API mode. The Admin APIs provide complete metadata coverage but require higher privilege levels. The Non-Admin APIs are more restricted but may be preferred for security boundaries where the service principal should not have tenant-wide access.
