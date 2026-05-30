---
type: clip
title: "How to Create a Personal Access Token | Official Documentation - OpenMetadata Documentation"
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/guide-for-data-users/personal-access-token"
clipped: 2026-05-14
origin: web-clip
sources: []
tags: [web-clip]
---

# How to Create a Personal Access Token | Official Documentation - OpenMetadata Documentation

Source: https://docs.open-metadata.org/v1.12.x/how-to-guides/guide-for-data-users/personal-access-token

Skip to main contentOpenMetadata Documentation home pagev1.12.xSearch...⌘KSearch...NavigationGuide for Data UsersHow to Create a Personal Access Token | Official DocumentationHomeQuickstartDeploymentConnectorsHow-to GuidesMCPAdmin GuideGuide for Data UsersData DiscoveryData ContractsData CollaborationData Quality and ObservabilityData Quality and ProfilerData Quality ObservabilityData LineageData InsightsData GovernanceReleasesDevelopersSDK & APIsGuide for Data UsersOverviewUnderstanding the Basics of OpenMetadataOverview of Data AssetsHow to Add Description using MarkdownHow to Request for DescriptionHow to Assign or Change Data OwnershipHow to Follow a Data AssetHow to Add TagsHow to Request for TagsHow to Create a Personal Access TokenHow to Add Glossary TermsHow to Create a Custom Property for a Data AssetHow to Customize OpenMetadataOverview of AnnouncementsHow to Create an AnnouncementData Asset VersioningHow to Delete a Data AssetOpenMetadata Browser ExtensionOn this pageHow to Create a Personal Access TokenPrerequisitesSteps to Create a Personal Access TokenUsageDocumentation IndexFetch the complete documentation index at: https://docs.open-metadata.org/llms.txtUse this file to discover all available pages before exploring further.​How to Create a Personal Access Token

Personal Access Tokens (PATs) in OpenMetadata let you authenticate and interact with the OpenMetadata API securely. Follow the steps below to generate a new personal access token.

​Prerequisites

You have a valid OpenMetadata user account.

You have access to the OpenMetadata UI.

​Steps to Create a Personal Access Token

Log in to the OpenMetadata UI

Navigate to your OpenMetadata instance.

Enter your credentials to log in.

Access your profile

Click your profile icon in the top-right corner of the UI.

Select View Profile from the dropdown menu.

Open the Access Tokens tab

In your profile page, click the Access Tokens tab.

Generate a new token

Click Generate New Token.

Set token expiration

Choose an expiration period for the token. Available options typically include:

1 hour

1 day

7 days

30 days

60 days

Copy your token

After generation, the personal access token is displayed.

You can revoke a token at any time by selecting Revoke Token.

Copy and securely store the token, as you may not be able to view it again later.

​Usage

Use the generated token to authenticate API requests to OpenMetadata. Include it in the Authorization header as follows:

Authorization: Bearer <your_personal_access_token>

Was this page helpful?YesNoSuggest editsRaise issueHow to Request for Tags | Official DocumentationPreviousHow to Add Glossary Terms | Official DocumentationNext⌘I
