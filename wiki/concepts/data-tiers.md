---
type: concept
title: Data Tiers
created: 2026-04-05
updated: 2026-04-05
tags: [openmetadata, data-quality, governance, classification]
related: [openmetadata, openmetadata-governance, data-quality-certification-vs-usability-certification]
sources: ["OpenMetadata - The Complete Guide Every Data Engineer Needs to Read.md"]
---
# Data Tiers

Data Tiers in [[OpenMetadata]] are a classification system that signals to consumers which assets are production-grade versus experimental. The standard tiers are:

- **Tier.Gold** → Production, well-tested, documented
- **Tier.Silver** → Stable but less critical
- **Tier.Bronze** → Experimental, use with caution

Tiers are searchable and filterable in the catalog, helping users quickly identify trusted data sources. This concept is related to [[data-quality-certification-vs-usability-certification]], which distinguishes between "how good" and "how ready" data is.