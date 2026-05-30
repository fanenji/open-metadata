---
type: clip
title: "Data Asset Versioning | OpenMetadata Version Control Guide - OpenMetadata Documentation"
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/guide-for-data-users/versions"
clipped: 2026-05-14
origin: web-clip
sources: []
tags: [web-clip]
---

# Data Asset Versioning | OpenMetadata Version Control Guide - OpenMetadata Documentation

Source: https://docs.open-metadata.org/v1.12.x/how-to-guides/guide-for-data-users/versions

Skip to main contentOpenMetadata Documentation home pagev1.12.xSearch...⌘KSearch...NavigationGuide for Data UsersData Asset Versioning | OpenMetadata Version Control GuideHomeQuickstartDeploymentConnectorsHow-to GuidesMCPAdmin GuideGuide for Data UsersData DiscoveryData ContractsData CollaborationData Quality and ObservabilityData Quality and ProfilerData Quality ObservabilityData LineageData InsightsData GovernanceReleasesDevelopersSDK & APIsGuide for Data UsersOverviewUnderstanding the Basics of OpenMetadataOverview of Data AssetsHow to Add Description using MarkdownHow to Request for DescriptionHow to Assign or Change Data OwnershipHow to Follow a Data AssetHow to Add TagsHow to Request for TagsHow to Create a Personal Access TokenHow to Add Glossary TermsHow to Create a Custom Property for a Data AssetHow to Customize OpenMetadataOverview of AnnouncementsHow to Create an AnnouncementData Asset VersioningHow to Delete a Data AssetOpenMetadata Browser ExtensionOn this pageData Asset VersioningDocumentation IndexFetch the complete documentation index at: https://docs.open-metadata.org/llms.txtUse this file to discover all available pages before exploring further.​Data Asset Versioning

OpenMetadata maintains the version history for all data assets using a number with the format major.minor, starting with 0.1 as the initial version of an entity. Changes in metadata result in version changes as follows:

Backward compatible changes result in a Minor version change. A change in the description, tags, or ownership will increase the version of the data asset metadata by 0.1 (e.g., from 0.1 to 0.2).

Backward incompatible changes result in a Major version change. For example, when a column in a table is deleted, the version increases by 1.0 (e.g., from 0.2 to 1.2).

Metadata versioning helps simplify debugging processes. View the version history to see if a recent change led to a data issue. Data owners and admins can review changes and revert if necessary.

Versioning also helps in broader collaboration among consumers and producers of data. Admins can provide access to more users in the organization to change certain fields. Crowd-sourcing makes metadata the collective responsibility of the entire organization.

OpenMetadata versions all the changes to the metadata to capture the evolution of data over time in the Versions History. This is tracked for all the data assets. OpenMetadata also captures the metadata changes at the source. Click on the Versions icon to see the Version History of your data.

If a user adds a description to a column that is recorded as a Minor version change by incrementing the version number by 0.1. When description, owner, or tags are added, updated, or removed the minor version changes are recorded. These are backward-compatible changes. When a column is deleted at the source, OpenMetadata captures it as backward-incompatible change. To indicate that, the major version is changed by incrementing the version number by 1.0.

All the changes that have happened to your data and metadata are at your fingertips to understand the evolution of your data over time. This is also key for Data Governance.

How to Delete a Data AssetSoft, or hard delete data assetsWas this page helpful?YesNoSuggest editsRaise issueHow to Create an Announcement | Official DocumentationPreviousHow to Delete a Data Asset | Official DocumentationNext⌘I
