---
type: concept
title: Push Dataset
created: 2026-05-14
updated: 2026-05-14
tags: [powerbi, dataset, lineage]
related: [powerbi-connector, admin-vs-non-admin-api-mode, dashboard-lineage]
sources: ["powerbi-connector-openmetadata-integration-documen-20260514.md"]
---

# Push Dataset

A Push Dataset is a type of PowerBI dataset where data is pushed into the dataset via the PowerBI REST API rather than imported from a data source. This is the **only dataset type** that supports lineage generation when using [[admin-vs-non-admin-api-mode|Non-Admin APIs]].

## Characteristics

- Data is pushed programmatically via the PowerBI REST API
- The dataset schema and data are defined at push time
- Supports lineage because the table structure is known to the API

## Lineage Implications

- With [[admin-vs-non-admin-api-mode|Admin APIs]]: All dataset types support lineage via the Scan Result API
- With [[admin-vs-non-admin-api-mode|Non-Admin APIs]]: Only push datasets support lineage via the Get Dataset Tables API
- Imported or DirectQuery datasets do not expose table information through the Non-Admin Get Dataset Tables API

## Usage

Push datasets are commonly used in custom application scenarios where data is generated or transformed externally and then pushed into PowerBI for visualization.