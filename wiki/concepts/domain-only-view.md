---
type: concept
title: Domain-Only View
created: 2026-05-14
updated: 2026-05-14
tags: [data-mesh, domains, ui, filtering]
related: [domains, domain-inheritance, data-mesh-openmetadata]
sources: ["OpenMetadata Community Meeting Oct 2023 Release 1 2 0 datamesh openmetadata.md"]
---
# Domain-Only View

Domain-Only View is a UI filter in [[OpenMetadata]] that restricts visibility to data assets belonging to a single [[domains|domain]]. It reduces cognitive load for users who only need to work within their organizational domain.

## Purpose

In the default flat view, all data assets across the entire organization are visible, which can be overwhelming. A data scientist working in the Marketing domain, for example, can switch to the Marketing domain-only view and see only assets relevant to their work.

## Current and Planned Scope

- **1.2.0 (initial)**: Domain-only view for browsing data assets.
- **Planned**: Domain-only view for [[data-quality|data quality]] (tests and failures within a domain).
- **Planned**: Domain-only view for [[openmetadata-insights|Data Insights]] (asset growth and usage within a domain).

## Interaction with Data Products

[[data-products|Data products]] are designed as public-facing assets and remain discoverable even when domain-only view is active. Implementation details (ETL pipelines, raw data) should remain internal to the domain and are hidden in this view.