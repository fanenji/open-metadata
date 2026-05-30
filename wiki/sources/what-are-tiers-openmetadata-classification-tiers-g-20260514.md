---
type: source
title: "What are Tiers | OpenMetadata Classification Tiers Guide"
created: 2026-05-14
updated: 2026-05-14
tags: [classification, tiers, data-governance, openmetadata]
related: [tiers, classification-tags, system-classification, openmetadata-insights, data-insights-application-troubleshooting, how-to-classify-data-assets-official-documentation-20260514]
sources: ["what-are-tiers-openmetadata-classification-tiers-g-20260514.md"]
authors: ["OpenMetadata Documentation Team"]
year: 2026
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/data-governance/classification/tiers"
venue: "OpenMetadata Official Documentation v1.12.x"
---

# What are Tiers | OpenMetadata Classification Tiers Guide

Official documentation page explaining the concept of Tiers as System Classification tags in OpenMetadata. Tiers are importance-based classification tags used to rank data assets according to their criticality to the organization.

## Key Content

- **Tiering concept**: Data producers or owners define the importance of data using a five-tier system.
- **Five-tier structure**: Tier 1 (highest impact: revenue, regulatory, reputational) through Tier 5 (individual-owned, unused datasets).
- **Impact/Usage matrix**: Structured mapping of each tier to impact type, regulatory implications, and usage frequency.
- **Start with extremes methodology**: Identify Tier 1 (most important) and Tier 5 (least important) first, then fill in intermediate tiers.
- **Tier 5 decluttering**: Data Insights identifies unused datasets as Tier 5 candidates for periodic deletion.
- **UI procedure**: From the Explore page, select a data asset, click the edit icon for Tier, and select the appropriate tier. The arrow next to the tier provides a description.
- **Access path**: Govern > Classification > Tier.