---
type: clip
title: "Advanced Guide for Roles and Policies - OpenMetadata Documentation"
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/admin-guide/roles-policies"
clipped: 2026-05-14
origin: web-clip
sources: []
tags: [web-clip]
---

# Advanced Guide for Roles and Policies - OpenMetadata Documentation

Source: https://docs.open-metadata.org/v1.12.x/how-to-guides/admin-guide/roles-policies

Skip to main contentOpenMetadata Documentation home pagev1.12.xSearch...⌘KSearch...NavigationAdvanced Guide for Roles and PoliciesAdvanced Guide for Roles and PoliciesHomeQuickstartDeploymentConnectorsHow-to GuidesMCPAdmin GuideGuide for Data UsersData DiscoveryData ContractsData CollaborationData Quality and ObservabilityData Quality and ProfilerData Quality ObservabilityData LineageData InsightsData GovernanceReleasesDevelopersSDK & APIsAdmin GuideOverviewHow to Ingest MetadataHow to Delete a Service ConnectionManage Teams and UsersAdvanced Guide for Roles and PoliciesOverviewBuilding Blocks of Authorization - Rules, Policies, and RolesUse Cases - Creating Roles & Policies in OpenMetadataCLI Ingestion with Basic AuthHow to Add Custom LogoReindexing SearchData InsightsPermission DebuggerPersona and Landing Page CustomizationAudit LogsOn this pageAdvanced Guide for Roles and PoliciesUsers and TeamsAccess Control Design: Roles and PoliciesAuthentication FlowAuthorization FrameworkDifference Between ViewBasic and ViewAll in OpenMetadataViewBasicKey Points:ViewAllKey Points:Summary TableOverview:Documentation IndexFetch the complete documentation index at: https://docs.open-metadata.org/llms.txtUse this file to discover all available pages before exploring further.​Advanced Guide for Roles and Policies

​Users and Teams

OpenMetadata introduces a versatile hierarchical team structure that aligns with your organization’s setup. Administrators can mirror their organizational hierarchy by creating various team types.

Organization serves as the foundation of the team hierarchy representing the entire company. Under Organization, you can add Business Units, Divisions, Departments, Groups, and Users. For instance, if your company is Facebook, then the Organization represents entire Facebook itself, which further houses diverse teams like Engineering, Sales, Finance, and Marketing.

BusinessUnit is positioned one level below the Organization and can contain other Business Units, Divisions, Departments, and Groups. To illustrate, the Engineering Business Unit could be one of the top-tier Business Units in the Organization. It contains other teams like Groups and additional Business Units.

Division is positioned below Business Unit and can include Divisions, Departments, and Groups. For example, a Division named ‘Product Development’ under the Engineering Business Unit. It can have teams like ‘Software Division,’ ‘Hardware Division,’ and ‘QA Division.’

Department is positioned below Division and can include other Departments and Groups. For example, a ‘Data Engineering Department could include specialized teams like ‘Infrastructure,’ ‘Data Science,’ and ‘Platform.’

Group represents the final tier in this hierarchy. It contains a group of users that reflect finite teams within your organization.

Notably, only Groups have the privilege of owning Data Assets within the OpenMetadata platform.

This structured hierarchy enhances your control over team management and resource ownership. By creating a dynamic model mirroring your organization’s functions, OpenMetadata empowers you to effortlessly manage permissions, access controls, and data ownership at different levels of granularity.

​Access Control Design: Roles and Policies

OpenMetadata incorporates a robust Access Control framework that merges Role-Based Access Control (RBAC) with Attribute-Based Access Control (ABAC) in a powerful hybrid model. This security design is reinforced by

Authentication with SSO Integration: OpenMetadata seamlessly integrates with various Single Sign-On (SSO) providers, including Azure AD, Google, Okta, Auth0, OneLogin, and more. This ensures a unified and secure authentication experience for users.

Team Hierarchy: OpenMetadata offers a structured team hierarchy that mirrors your organization’s structure, enhancing manageability and granularity in access control.

Roles and Policies: Policies and Roles are pivotal in determining who can access what resources and perform what actions. These policies are based on a combination of user attributes, roles, and resource attributes.

User and Bots Authentication: OpenMetadata accommodates human users and automated applications (bots). For human users, logging into the OpenMetadata UI mandates SSO authentication. Upon successful authentication, a JWT token is issued.

Bots, on the other hand, are equipped with a JWT token generated based on SSL certificates. This token serves as their identity and authorization mechanism when interacting with the OpenMetadata server APIs.

​Authentication Flow

User Authentication: When users access the OpenMetadata UI, they authenticate with their SSO provider. Upon successful authentication, a JWT token is generated. This token validates the user’s session and permits them to authenticate requests to the OpenMetadata server.

Bot Authentication: Automated applications like the ingestion connector are equipped with a pre-generated JWT Token. OpenMetadata, with its configured SSL Certificates, authenticates the JWT token, establishing the bot’s identity. This token authorizes the bot to interact with OpenMetadata server APIs.

​Authorization Framework

OpenMetadata’s authorization is a result of evaluating three crucial factors:

Who is the User (Authentication): This aspect is determined by the authentication process – whether it a user or a bot – ensuring that only authorized entities access the system.

What Resource (Resource Attributes): Based on the API calls being made, OpenMetadata identifies the target resource and its associated attributes.

Below is a list of resources that correspond to Entities such as Table, Topic, Pipeline, etc.

What Operation (API Call): Each API call is linked to a specific operation, such as editing descriptions, deleting tags, changing ownership, etc.

There are common operations such as Create, Delete, and ViewAll that apply to all the resources. Each resource can also have its specific operation, such as ViewTests, ViewQueries for Table.

​Difference Between ViewBasic and ViewAll in OpenMetadata

The operations ViewBasic and ViewAll in OpenMetadata differ in the level of detail they provide access to. Below is a detailed explanation of each operation:

​ViewBasic

Provides access to the basic details of an asset.

Includes information such as:

Description

Tags

Owner

Fundamental metadata

Excludes more detailed information, including:

Profile data

Sample data

Data profile

Tests

Queries

​Key Points:

Suitable for viewing foundational asset metadata.

Limited access for users who do not require in-depth technical details.

​ViewAll

Provides access to all details of an asset.

Includes everything available in ViewBasic, along with:

Profile data

Sample data

Data profile

Tests

Queries

​Key Points:

Designed for users who need a complete view of the asset.

Offers comprehensive insights and detailed metadata.

​Summary Table

FeatureViewBasicViewAllBasic Details✅ Included✅ IncludedProfile Data❌ Not Included✅ IncludedSample Data❌ Not Included✅ IncludedData Profile❌ Not Included✅ IncludedTests & Queries❌ Not Included✅ Included

​Overview:

ViewBasic: Focused on essential metadata.

ViewAll: Provides a complete view, including advanced details.

Choose the appropriate operation based on the level of access required.

By synthesizing these components, OpenMetadata dynamically ascertains whether a user or bot can perform a particular action on a specific resource. This fusion of RBAC and ABAC in the hybrid model contributes to a robust and flexible access control mechanism, bolstering the security and control of your OpenMetadata environment.

Building Blocks of Authorization: Rules, Policies, and RolesLearn all the details of Rules, Policies, and Roles

Use Cases: Creating Roles & Policies in OpenMetadataTailor you policies to meet your organizational and team needs.Was this page helpful?YesNoSuggest editsRaise issueHow to Change the Team Type | Official DocumentationPreviousBuilding Blocks of Authorization - Rules, Policies, and RolesNext⌘I
