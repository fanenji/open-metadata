---
type: clip
title: "How to Create a Custom Property for a Data Asset - OpenMetadata Documentation"
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/guide-for-data-users/custom"
clipped: 2026-05-14
origin: web-clip
sources: []
tags: [web-clip]
---

# How to Create a Custom Property for a Data Asset - OpenMetadata Documentation

Source: https://docs.open-metadata.org/v1.12.x/how-to-guides/guide-for-data-users/custom

Skip to main contentOpenMetadata Documentation home pagev1.12.xSearch...⌘KSearch...NavigationGuide for Data UsersHow to Create a Custom Property for a Data AssetHomeQuickstartDeploymentConnectorsHow-to GuidesMCPAdmin GuideGuide for Data UsersData DiscoveryData ContractsData CollaborationData Quality and ObservabilityData Quality and ProfilerData Quality ObservabilityData LineageData InsightsData GovernanceReleasesDevelopersSDK & APIsGuide for Data UsersOverviewUnderstanding the Basics of OpenMetadataOverview of Data AssetsHow to Add Description using MarkdownHow to Request for DescriptionHow to Assign or Change Data OwnershipHow to Follow a Data AssetHow to Add TagsHow to Request for TagsHow to Create a Personal Access TokenHow to Add Glossary TermsHow to Create a Custom Property for a Data AssetHow to Customize OpenMetadataOverview of AnnouncementsHow to Create an AnnouncementData Asset VersioningHow to Delete a Data AssetOpenMetadata Browser ExtensionOn this pageHow to Create a Custom Property for a Data AssetDocumentation IndexFetch the complete documentation index at: https://docs.open-metadata.org/llms.txtUse this file to discover all available pages before exploring further.​How to Create a Custom Property for a Data Asset

OpenMetadata uses a schema-first approach, and that’s why we support custom properties for all types of data assets. Organizations can extend the attributes as required to capture custom metadata. You can view the Custom Properties tab in the detailed view for all types of data assets.

Supported types:

Date

Date Time

Duration

Email

Entity Reference

Entity Reference List

Enum

Integer

Markdown

Number

SQL Query

String

Table

Time

Time Interval

Timestamp

To create a Custom Property in OpenMetadata:

Navigate to Settings >> Custom Properties

Click on the type of data asset you would like to create a custom property for.

Click on Add Property

Enter the required details: Name, Type, and Description. You can lookup for the details of the information asked on the right side panel.

Name: The name must start with a lowercase letter, as preferred in the camelCase format. Uppercase letters and numbers can be included in the field name; but spaces, underscores, and dots are not supported.

Type: Type of custom property like entityReference, email, etc.

Description: Describe your custom property to provide more information to your team.

Click on Create.

Once the custom property has been created for a type of data asset, you can add the values for the custom property from the Custom Property tab in the detailed view of the data assets.

To delete a Custom Property for a particular asset, such as tables, navigate to Settings >> Custom Properties >> Tables and

click on Delete Property

Overview of AnnouncementsLearn more about the announcements in OpenMetadataWas this page helpful?YesNoSuggest editsRaise issueHow to Add Glossary Terms | Official DocumentationPreviousHow to Customize OpenMetadataNext⌘I
