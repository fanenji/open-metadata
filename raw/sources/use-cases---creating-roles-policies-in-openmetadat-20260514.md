---
type: clip
title: "Use Cases - Creating Roles & Policies in OpenMetadata - OpenMetadata Documentation"
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/admin-guide/roles-policies/use-cases"
clipped: 2026-05-14
origin: web-clip
sources: []
tags: [web-clip]
---

# Use Cases - Creating Roles & Policies in OpenMetadata - OpenMetadata Documentation

Source: https://docs.open-metadata.org/v1.12.x/how-to-guides/admin-guide/roles-policies/use-cases

Skip to main contentOpenMetadata Documentation home pagev1.12.xSearch...⌘KSearch...NavigationAdvanced Guide for Roles and PoliciesUse Cases - Creating Roles & Policies in OpenMetadataHomeQuickstartDeploymentConnectorsHow-to GuidesMCPAdmin GuideGuide for Data UsersData DiscoveryData ContractsData CollaborationData Quality and ObservabilityData Quality and ProfilerData Quality ObservabilityData LineageData InsightsData GovernanceReleasesDevelopersSDK & APIsAdmin GuideOverviewHow to Ingest MetadataHow to Delete a Service ConnectionManage Teams and UsersAdvanced Guide for Roles and PoliciesOverviewBuilding Blocks of Authorization - Rules, Policies, and RolesUse Cases - Creating Roles & Policies in OpenMetadataCLI Ingestion with Basic AuthHow to Add Custom LogoReindexing SearchData InsightsPermission DebuggerPersona and Landing Page CustomizationAudit LogsOn this pageUse Cases: Creating Roles & Policies in OpenMetadataUse Case 1: We want our teams to be able to create services and extract metadataUse Case 2: Roles for Data StewardUse Case 3: Only the team that owns the data asset should be able to access itUse Case 4: Deny all the access if the data asset is tagged with PII.Sensitive and allow only the ownersDocumentation IndexFetch the complete documentation index at: https://docs.open-metadata.org/llms.txtUse this file to discover all available pages before exploring further.​Use Cases: Creating Roles & Policies in OpenMetadata

OpenMetadata comes with default configurations such as the Organization Policy and Data Consumer Roles. These roles are setup to foster data collaboration.

We advise retaining the Organization policy, which enables everyone to view the assets and claim ownership when no owner is specified.

For individual teams, tailor your policies according to the specific needs of both the organization and the team. You may choose to adopt stricter policies as detailed in the previous sections.

​Use Case 1: We want our teams to be able to create services and extract metadata

You can create a policy with DatabaseService, Ingesiton Pipeline, and Workflow resources with All operations set to allow.

You can create a Role such as ServiceOwner role and assign the above policy. Once the role is created, you can assign it to users to enable service creation by themselves without the need for an Admin.

​Use Case 2: Roles for Data Steward

A data steward in OpenMetadata should be able to create Glossaries and Glossary Terms and be able to view all data and manage it for governance purposes.

Here is an example of a policy to enable it for Data Stewards using two rules.

Allow Glossary Operations: Enables the policy to allow operations on all Glossary related actions.

Edit Rule: Grants access to the Data Steward to edit description, edit tags on all entities; enabling the user to manage the data.

You can fine tune these permissions to suit your organizational needs.

​Use Case 3: Only the team that owns the data asset should be able to access it

To safeguard the data owned by a specific team, you can prevent external access.

The above rule specifies to deny all operations if the logged-in user is not the owner, or if the logged-in user’s team is not the owner of an asset.

​Use Case 4: Deny all the access if the data asset is tagged with PII.Sensitive and allow only the owners

Just like the above policy, you can create a rule with complex conditions as shown below

In this rule, we are specifying to deny operations if the table tag contains PII.Sensitive tag and if the logged-in user is not the owner, or their team is not the owner of the Table.Was this page helpful?YesNoSuggest editsRaise issueBuilding Blocks of Authorization - Rules, Policies, and RolesPreviousHow To Run Ingestion Pipeline Via CLI with Basic AuthNext⌘I
