---
type: clip
title: "How to Add Tags | OpenMetadata User Tagging Guide - OpenMetadata Documentation"
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/guide-for-data-users/tags"
clipped: 2026-05-14
origin: web-clip
sources: []
tags: [web-clip]
---

# How to Add Tags | OpenMetadata User Tagging Guide - OpenMetadata Documentation

Source: https://docs.open-metadata.org/v1.12.x/how-to-guides/guide-for-data-users/tags

Skip to main contentOpenMetadata Documentation home pagev1.12.xSearch...⌘KSearch...NavigationGuide for Data UsersHow to Add Tags | OpenMetadata User Tagging GuideHomeQuickstartDeploymentConnectorsHow-to GuidesMCPAdmin GuideGuide for Data UsersData DiscoveryData ContractsData CollaborationData Quality and ObservabilityData Quality and ProfilerData Quality ObservabilityData LineageData InsightsData GovernanceReleasesDevelopersSDK & APIsGuide for Data UsersOverviewUnderstanding the Basics of OpenMetadataOverview of Data AssetsHow to Add Description using MarkdownHow to Request for DescriptionHow to Assign or Change Data OwnershipHow to Follow a Data AssetHow to Add TagsHow to Request for TagsHow to Create a Personal Access TokenHow to Add Glossary TermsHow to Create a Custom Property for a Data AssetHow to Customize OpenMetadataOverview of AnnouncementsHow to Create an AnnouncementData Asset VersioningHow to Delete a Data AssetOpenMetadata Browser ExtensionOn this pageHow to Add TagsAuto-Classification in OpenMetadataDocumentation IndexFetch the complete documentation index at: https://docs.open-metadata.org/llms.txtUse this file to discover all available pages before exploring further.​How to Add Tags

From the Explore page, select a data asset and click on the edit icon or + Add for Tags.

Search for the relevant tags. You can either type and search, or scroll to select from the options provided.

Click on the checkmark to save the changes.

The tagged data assets can be discovered right from the Classification page.

Navigate to Govern >> Classification.

The list of tags is displayed along with the details of Usage in various data assets.

Click on the Usage number to view the tagged assets.

You can view all the tags in the right panel.

Data assets can also be classified using Tiers. Learn more about Tiers.

Among the Classification Tags, OpenMetadata has some System Classification. Learn more about the System Tags.

​Auto-Classification in OpenMetadata

OpenMetadata identifies PII data and auto tags or suggests the tags. The data profiler automatically tags the PII-Sensitive data. The addition of tags about PII data helps consumers and governance teams identify data that needs to be treated carefully.

In the example below, the columns ‘user_name’ and ‘social security number’ are auto-tagged as PII-sensitive. This works using NLP as part of the profiler during ingestion.

In the below example, the column ‘dwh_x10’ is also auto-tagged as PII Sensitive, even though the column name does not provide much information.

When we look at the content of the column ‘dwh_x10’ in the Sample Data tab, it becomes clear that the auto-classification is based on the data in the column.

How to Request for TagsRequest for tags and discuss about the same, all within OpenMetadata.Was this page helpful?YesNoSuggest editsRaise issueHow to Follow a Data Asset | Official DocumentationPreviousHow to Request for Tags | Official DocumentationNext⌘I
