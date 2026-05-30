---
type: concept
title: PowerBI Admin vs Non-Admin APIs
created: 2026-05-14
updated: 2026-05-14
tags: [powerbi, api, lineage, metadata-ingestion]
related: [powerbi-connector, dashboard-lineage, pbit-file-lineage-extraction]
sources: ["run-the-powerbi-connector-externally---openmetadat-20260514.md"]
---
# PowerBI Admin vs Non-Admin APIs

The PowerBI connector supports two API modes that fundamentally change what metadata is available during ingestion. The choice is controlled by the `useAdminApis` toggle in the YAML configuration.

## Admin APIs (Enabled by Default)

- **Workspace Scope:** Fetches dashboard and chart metadata from **all workspaces** in the PowerBI instance.
- **Lineage:** Uses the PowerBI **Scan Result API**, which has no limitations. Full lineage is available for all datasets.
- **Prerequisites:** Requires PowerBI Admin console permissions: "Allow service principals to use read-only PowerBI admin APIs" and "Enhance admin APIs responses with detailed metadata".

## Non-Admin APIs

- **Workspace Scope:** Only fetches metadata from workspaces where the service principal's security group is explicitly assigned.
- **Lineage:** Uses the PowerBI **Get Dataset Tables API**, which only retrieves table information for **Push Datasets**. Lineage is only available for Push Datasets.
- **Use Case:** Suitable when Admin API access is not granted or when only specific workspaces need to be ingested.

## Key Implications

- The Admin API mode is strongly recommended for comprehensive metadata ingestion and full lineage.
- The Non-Admin API mode is significantly limited in both scope and lineage capabilities.
- The choice should be made early in the connector setup, as it affects all subsequent metadata.

## Related

- [[powerbi-connector]] — The parent connector page.
- [[dashboard-lineage]] — General dashboard lineage concepts.
- [[pbit-file-lineage-extraction]] — Alternative lineage extraction method using .pbit files.