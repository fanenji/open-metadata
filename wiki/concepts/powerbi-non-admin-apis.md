---
type: concept
title: PowerBI Non-Admin APIs
created: 2026-05-14
updated: 2026-05-14
tags: [powerbi, api, non-admin, ingestion, lineage]
related: [powerbi-connector, powerbi-admin-apis, powerbi-get-dataset-tables-api, push-dataset-limitation, data-lineage]
sources: ["PowerBI Connector  OpenMetadata Integration Documentation.md"]
---
# PowerBI Non-Admin APIs

The PowerBI Non-Admin APIs are the standard (non-administrative) PowerBI REST APIs used by the [[powerbi-connector|PowerBI Connector]] when Admin API mode is disabled. This mode provides a more restricted but potentially more secure approach to metadata ingestion.

## Capabilities

- **Limited Workspace Coverage**: Only fetches dashboard and chart metadata from workspaces where the service principal's security group is explicitly assigned.
- **Restricted Lineage**: Uses the [[powerbi-get-dataset-tables-api|Get Dataset Tables API]] to gather table and dataset information. This API is subject to the [[push-dataset-limitation|Push Dataset limitation]].

## Limitations

- **Push Dataset Only**: Lineage can only be generated for Push Datasets. Other dataset types will not have lineage information.
- **Workspace Assignment Required**: The service principal must be explicitly added to each workspace from which metadata should be ingested.
- **No Default Workspace Access**: Default user workspaces (e.g., "My Workspace") are not accessible.

## When to Use

Non-Admin APIs are appropriate when:

- Security policies restrict tenant-wide administrative access
- Only specific workspaces need to be ingested
- The service principal should operate with least-privilege principles

For complete metadata coverage, use [[powerbi-admin-apis]] instead.
