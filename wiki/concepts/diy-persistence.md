---
type: concept
title: DIY Persistence
created: 2026-05-07
updated: 2026-05-07
tags: [architecture, modern-data-stack, trend]
related: [data-observability-definition, fivetran, airbyte, monte-carlo]
sources: ["The Modern Data Stack in 2025 What Actually Won.md"]
---
# DIY Persistence

DIY persistence is the finding that custom-built solutions remain common in the modern data stack, defying predictions that SaaS tools would eliminate custom development. Depending on the category, 19–42% of teams use custom solutions.

## Categories with Strong DIY Presence

- **Data ingestion:** 19% use custom scripts (average team size: 8+ data engineers)
- **Data observability:** 42% use dbt tests + custom alerts (dominant approach)
- **Reverse ETL:** 5% use custom scripts

## Why DIY Persists

- Complex transformations during extraction
- Proprietary APIs not supported by vendors
- Cost savings (especially at scale)
- Control and customization requirements
- Observability tools expensive ($30–50K/year typical) with false positive issues

## Implications

The DIY persistence trend challenges the [[platformization]] narrative. While vendors expand their platforms, many teams still prefer custom solutions for specific use cases, particularly in observability and ingestion.
