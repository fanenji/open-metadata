---
type: concept
title: Tiers
created: 2026-05-14
updated: 2026-05-14
tags: ["data-governance", "classification", "tiers", "data-importance", "system-classification"]
related: ["classification-tags", "system-classification", "tag-based-access-control", "openmetadata-insights", "data-insights-application-troubleshooting", "how-to-classify-data-assets-official-documentation-20260514"]
sources: ["how-to-classify-data-assets-official-documentation-20260514.md", "what-are-tiers-openmetadata-classification-tiers-g-20260514.md"]
---

# Tiers

Tiers are specialized [[classification-tags|classification tags]] in OpenMetadata used for ranking data importance and criticality. They are [[system-classification|System Classification]] tags — pre-built and provided out of the box — accessed via **Govern > Classification > Tier**. Tiers enable data producers and owners to define the importance of data assets to the organization, supporting data prioritization, resource allocation, and decluttering efforts.

## Five-Tier System

OpenMetadata provides a five-tier classification system, ranging from Tier 1 (highest importance) to Tier 5 (lowest importance, unused data).

| Tier | Impact | Used for | Type of Impact | Usage |
|------|--------|----------|----------------|-------|
| **Tier 1** | High | External & Internal Decisions | Revenue, Regulatory, & Reputational | Highly used |
| **Tier 2** | Moderate | Some External & Mostly Internal Decisions | Some Regulatory | Highly used |
| **Tier 3** | Low | Internal Decisions | — | Highly used (Top N percentile) |
| **Tier 4** | Low | Internal Team Decisions | — | — |
| **Tier 5** | Individual owned | Unused Datasets | — | — |

### Tier Descriptions

- **Tier 1**: The most critical data assets. These directly impact revenue, regulatory compliance, or organizational reputation. They are used for both external and internal decision-making and are highly used across the organization. Once identified, organizations should prioritize improving descriptions and [[data-quality|data quality]] for Tier 1 assets.
- **Tier 2**: Moderately important data with some external impact and mostly internal decision-making use. May have some regulatory implications. Highly used.
- **Tier 3**: Data used for internal decisions only. Highly used, typically representing the top N percentile of usage.
- **Tier 4**: Data used for internal team decisions. Lower priority than Tier 3.
- **Tier 5**: Individually owned datasets that are unused. These are candidates for periodic deletion to declutter the data estate.

## Operational Methodology

### Start with Extremes

The recommended approach is to identify the most important (Tier 1) and least important (Tier 5) data first. This establishes clear boundaries and makes it easier to classify the intermediate tiers (Tier 2, 3, 4) according to organizational needs.

### Tier 1 Prioritization

Once Tier 1 data is identified, organizations should focus on:
- Improving descriptions and documentation
- Enhancing [[data-quality|data quality]] measures
- Ensuring robust [[data-lineage|data lineage]] tracking
- Applying appropriate governance controls

### Tier 5 Decluttering

[[openmetadata-insights|Data Insights]] in OpenMetadata helps identify unused datasets as Tier 5 candidates. These datasets can be deleted periodically to declutter the data estate. This practice keeps the metadata catalog clean and focused on valuable data assets.

## How to Apply Tiers

1. Navigate to the **Explore** page.
2. Select a data asset (table, topic, dashboard, etc.).
3. Click the **edit icon** next to the Tier field.
4. Select the appropriate tier from the dropdown.
5. Click the **arrow** next to a tier to view its description before selecting.

Tiers can also be applied programmatically via the [[metadata-cli|Metadata CLI]] or API during [[metadata-ingestion-workflow|metadata ingestion]].

## Relationship to Other Classification Systems

Tiers are a subset of [[classification-tags|classification tags]] and are specifically [[system-classification|System Classification]] tags — meaning they are pre-built by OpenMetadata and not user-created. They complement other classification tags (such as PII, sensitivity labels) and [[glossary-tags|glossary tags]] to provide a multi-dimensional governance framework. While glossary tags define *what* data means, tiers define *how important* it is.

## Open Questions

- Are Tiers customizable beyond the five default levels, or is the system fixed at five?
- Can organizations rename tiers or modify their descriptions?
- How does Data Insights algorithmically determine "unused" for Tier 5 classification?
- Is Tier 5 deletion automated or manual?