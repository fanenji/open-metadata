---
type: concept
title: Push Dataset Limitation
created: 2026-05-14
updated: 2026-05-14
tags: [powerbi, lineage, push-dataset, api, limitation]
related: [powerbi-connector, powerbi-non-admin-apis, powerbi-get-dataset-tables-api, data-lineage]
sources: ["PowerBI Connector  OpenMetadata Integration Documentation.md"]
---
# Push Dataset Limitation

The Push Dataset limitation is a critical constraint affecting [[data-lineage|lineage]] generation when the [[powerbi-connector|PowerBI Connector]] is configured to use [[powerbi-non-admin-apis|Non-Admin APIs]].

## What It Is

The PowerBI [Get Dataset Tables API](https://learn.microsoft.com/en-us/rest/api/power-bi/push-datasets/datasets-get-tables), used in Non-Admin mode to retrieve table information for lineage, only returns data for **Push Datasets**. A Push Dataset is a specific type of PowerBI dataset where data is programmatically pushed into PowerBI via the REST API, rather than being imported or connected via DirectQuery.

## Impact

- **Incomplete Lineage**: Datasets that are not Push Datasets (e.g., imported datasets, DirectQuery datasets) will not have table information available, and therefore no lineage can be generated for them.
- **Silent Gaps**: Users may expect full lineage coverage but only receive partial results without explicit errors.
- **Decision Point**: This limitation should be a primary factor when choosing between Admin and Non-Admin API modes.

## Mitigation

To avoid this limitation, use [[powerbi-admin-apis|Admin APIs]], which leverage the [[powerbi-scan-result-api|Scan Result API]] — an API with no dataset type restrictions.
