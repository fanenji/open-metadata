---
type: clip
title: "How to Assign or Change Data Ownership - OpenMetadata Documentation"
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/guide-for-data-users/data-ownership"
clipped: 2026-05-14
origin: web-clip
sources: []
tags: [web-clip]
---

# How to Assign or Change Data Ownership - OpenMetadata Documentation

Source: https://docs.open-metadata.org/v1.12.x/how-to-guides/guide-for-data-users/data-ownership

Skip to main contentOpenMetadata Documentation home pagev1.12.xSearch...⌘KSearch...NavigationGuide for Data UsersHow to Assign or Change Data OwnershipHomeQuickstartDeploymentConnectorsHow-to GuidesMCPAdmin GuideGuide for Data UsersData DiscoveryData ContractsData CollaborationData Quality and ObservabilityData Quality and ProfilerData Quality ObservabilityData LineageData InsightsData GovernanceReleasesDevelopersSDK & APIsGuide for Data UsersOverviewUnderstanding the Basics of OpenMetadataOverview of Data AssetsHow to Add Description using MarkdownHow to Request for DescriptionHow to Assign or Change Data OwnershipHow to Follow a Data AssetHow to Add TagsHow to Request for TagsHow to Create a Personal Access TokenHow to Add Glossary TermsHow to Create a Custom Property for a Data AssetHow to Customize OpenMetadataOverview of AnnouncementsHow to Create an AnnouncementData Asset VersioningHow to Delete a Data AssetOpenMetadata Browser ExtensionOn this pageHow to Assign or Change Data OwnershipData Asset OwnershipAssign Data OwnershipChange Data OwnershipOwner Propagation in OpenMetadataTeam Ownership is PreferredDocumentation IndexFetch the complete documentation index at: https://docs.open-metadata.org/llms.txtUse this file to discover all available pages before exploring further.​How to Assign or Change Data Ownership

​Data Asset Ownership

In OpenMetadata, either a team or multiple user can be the owner of a data asset. Owners have access to perform all the operations on a data asset. For example, edit description, tags, glossary terms, etc.

​Assign Data Ownership

Admin users have access to add or change data ownership.

Navigate to the data asset and click on the edit icon next to the Owner of the data asset.

Select a Team or a User as the Owner of the Data Asset.

​Change Data Ownership

If the data asset already has an owner, you can change the owner by clicking on the edit icon for Owner and simply selecting a team or user to change ownership.

If no owner is selected, and if the Database or Database Schema has a owner, then by default the same owner will be assigned to the Database Schema or Table respectively, based on the owner propagation in OpenMetadata.

​Owner Propagation in OpenMetadata

OpenMetadata supports Owner Propagation and the owner will be propagated based on a top-down hierarchy. The owner of the Database will be auto-propagated as the owner of the Database Schemas and Tables under it. Similarly, the owner of the Database Schema will be auto-propagated as the owner of the Tables under it.

Owner Propagation does not work for data assets that already have an Owner assigned to them. If there is no owner, then an Owner will be assigned based on the hierarchy.

If a Database or Database Schema has an Owner assigned, and you delete the owner from the Database Schema or Tables under it, then the Owner will be auto-assigned in this case based on the existing Owner details at the top hierarchy.

You can also assign a different owner manually.

​Team Ownership is Preferred

OpenMetadata is a data collaboration platform. We highly recommend Team Ownership of data assets, because individual users will only have part of the context about the data asset in question. Assigning team ownership will give access to all the members of a particular team. Only teams of the type ‘Groups’ can own data assets.

How to Follow a Data AssetLearn how to follow data assetsWas this page helpful?YesNoSuggest editsRaise issueHow to Request for DescriptionPreviousHow to Follow a Data Asset | Official DocumentationNext⌘I
