---
type: entity
title: PowerBI Get Dataset Tables API
created: 2026-05-14
updated: 2026-05-14
tags: [powerbi, api, dataset, lineage, non-admin]
related: [powerbi-connector, powerbi-non-admin-apis, push-dataset-limitation, data-lineage]
sources: ["PowerBI Connector  OpenMetadata Integration Documentation.md"]
---
# PowerBI Get Dataset Tables API

The PowerBI Get Dataset Tables API is a PowerBI REST API endpoint used by the [[powerbi-connector|PowerBI Connector]] when operating in [[powerbi-non-admin-apis|Non-Admin API]] mode. It retrieves table information from datasets for lineage generation.

## Endpoint

`GET https://api.powerbi.com/v1.0/myorg/datasets/{datasetId}/tables`

Reference: [Datasets Get Tables](https://learn.microsoft.com/en-us/rest/api/power-bi/push-datasets/datasets-get-tables)

## Key Limitation

This API is part of the **Push Datasets** API group and only returns table information if the dataset is a [[push-dataset-limitation|Push Dataset]]. For all other dataset types (imported, DirectQuery, etc.), no table data is returned, making lineage generation impossible for those datasets.

## Role in Lineage Generation

When Non-Admin APIs are enabled, this is the only mechanism available for extracting table-level metadata. The [[push-dataset-limitation]] means lineage coverage will be incomplete unless all datasets in scope are Push Datasets.
