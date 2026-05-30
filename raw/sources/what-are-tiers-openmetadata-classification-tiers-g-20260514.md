---
type: clip
title: "What are Tiers | OpenMetadata Classification Tiers Guide - OpenMetadata Documentation"
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/data-governance/classification/tiers"
clipped: 2026-05-14
origin: web-clip
sources: []
tags: [web-clip]
---

# What are Tiers | OpenMetadata Classification Tiers Guide - OpenMetadata Documentation

Source: https://docs.open-metadata.org/v1.12.x/how-to-guides/data-governance/classification/tiers

Skip to main contentOpenMetadata Documentation home pagev1.12.xSearch...⌘KSearch...NavigationClassificationWhat are Tiers | OpenMetadata Classification Tiers GuideHomeQuickstartDeploymentConnectorsHow-to GuidesMCPAdmin GuideGuide for Data UsersData DiscoveryData ContractsData CollaborationData Quality and ObservabilityData Quality and ProfilerData Quality ObservabilityData LineageData InsightsData GovernanceReleasesDevelopersSDK & APIsData GovernanceOverviewGlossaryClassificationOverviewOverview of ClassificationHow to Classify Data AssetsHow to Request for Classification TagsSample Data Handling Using PII TagsAuto-Classification WorkflowWhat are TiersBest Practices for ClassificationDomains & Data ProductMetricsColumn Bulk OperationsOn this pageWhat are TiersHow to Add TiersDocumentation IndexFetch the complete documentation index at: https://docs.open-metadata.org/llms.txtUse this file to discover all available pages before exploring further.​What are Tiers

Tiering is an important concept of data classification in OpenMetadata. Tiers should be based on the importance of data. Using Tiers, data producers or owners can define the importance of data to an organization.

In OpenMetadata, Tiers are System Classification tags and can be accessed from Govern > Classification > Tier.

In case of tiering, it is easiest to start with the most important (Tier 1) and the least important (Tier 5) data. Once the Tier 1 or most important data is identified, organizations can focus on improving the descriptions and data quality. The Data Insights in OpenMetadata helps identify the unused datasets as Tier 5. The Tier 5 datasets can be deleted periodically to declutter. Other tiers can be added as per your organizational needs. Tags can be added to further mark the data assets.

TierImpactUsed forType of ImpactUsageTier 1HighExternal & Internal DecisionsRevenue, Regulatory, & ReputationalHighly usedTier 2ModerateSome External & Mostly Internal DecisionsSome RegulatoryHighly usedTier 3LowInternal Decisions-Highly used (Top N percentile)Tier 4LowInternal Team Decisions--Tier 5Individual ownedUnused Datasets--

​How to Add Tiers

From the Explore page, select a data asset and click on the edit icon for Tier. Select the appropriate tier. Clicking on the arrow next to the tier will provide a description of the tier.

Best Practices for ClassificationHere are the Best Practices around Classification.Was this page helpful?YesNoSuggest editsRaise issueExternal Storage for Sample DataPreviousBest Practices for Classification | Official DocumentationNext⌘I
