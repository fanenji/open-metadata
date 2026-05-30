---
type: concept
title: Admin vs. Non-Admin API Mode
created: 2026-05-14
updated: 2026-05-14
tags: [powerbi, api, lineage, metadata-ingestion]
related: [powerbi-connector, dashboard-lineage, powerbi-admin-apis, powerbi-non-admin-apis]
sources: ["powerbi-connector-openmetadata-integration-documen-20260514.md"]
---

# Admin vs. Non-Admin API Mode

The PowerBI connector supports two API modes that determine the scope of metadata retrieval and lineage capabilities. This is the most critical configuration decision for the [[powerbi-connector|PowerBI Connector]].

## Admin APIs (Enabled)

- Fetches dashboard and chart metadata from **all workspaces** in the PowerBI instance
- Uses the **PowerBI Scan Result API** for table/dataset information
- No limitations on lineage generation
- Requires PowerBI Admin to enable "Allow service principals to use read-only PowerBI admin APIs"

## Non-Admin APIs (Disabled)

- Fetches metadata only from workspaces where the service principal's security group is assigned
- Uses the **PowerBI Get Dataset Tables API** for table/dataset information
- Lineage is **only available for push datasets** (datasets where data is pushed via API)
- Significantly restricts lineage capabilities

## Recommendation

Use Admin APIs whenever possible to ensure full workspace coverage and complete lineage. Non-Admin mode should only be used when organizational policies restrict admin API access.