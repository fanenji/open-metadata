---
type: clip
title: "Team Structure in OpenMetadata | Official Documentation - OpenMetadata Documentation"
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/admin-guide/teams-and-users/team-structure-openmetadata"
clipped: 2026-05-14
origin: web-clip
sources: []
tags: [web-clip]
---

# Team Structure in OpenMetadata | Official Documentation - OpenMetadata Documentation

Source: https://docs.open-metadata.org/v1.12.x/how-to-guides/admin-guide/teams-and-users/team-structure-openmetadata

Skip to main contentOpenMetadata Documentation home pagev1.12.xSearch...⌘KSearch...NavigationManage Teams and UsersTeam Structure in OpenMetadata | Official DocumentationHomeQuickstartDeploymentConnectorsHow-to GuidesMCPAdmin GuideGuide for Data UsersData DiscoveryData ContractsData CollaborationData Quality and ObservabilityData Quality and ProfilerData Quality ObservabilityData LineageData InsightsData GovernanceReleasesDevelopersSDK & APIsAdmin GuideOverviewHow to Ingest MetadataHow to Delete a Service ConnectionManage Teams and UsersOverviewTeam Structure in OpenMetadataHow to Add a TeamHow to Invite Users to OpenMetadataHow to Add Users to TeamsHow to Change the Team TypeAdvanced Guide for Roles and PoliciesCLI Ingestion with Basic AuthHow to Add Custom LogoReindexing SearchData InsightsPermission DebuggerPersona and Landing Page CustomizationAudit LogsOn this pageTeam Structure in OpenMetadataDocumentation IndexFetch the complete documentation index at: https://docs.open-metadata.org/llms.txtUse this file to discover all available pages before exploring further.​Team Structure in OpenMetadata

OpenMetadata supports a hierarchical team structure with teamType that can be Organization, Business Unit, Division, Department, and Group (default team type). Organization serves as the foundation of the team hierarchy representing the entire company. The other team types under Organization are Business Units, Divisions, Departments, and Groups.

Organization is the root team in the hierarchy. It cannot have a parent. It can have children of the type Business Unit, Division, Department, Group along with Users directly as children (who are without teams).

BusinessUnit is the next level of the team in the hierarchy. It can have Business Unit, Division, Department, and Group as children. It can only have one parent either of the type Organization, or Business Unit.

Division is the next level of the team in the hierarchy below Business Unit. It can have Division, Department, and Group as children. It can only have one parent of the type Organization, Business Unit, or Division.

Department is the next level of the team in the hierarchy below Division. It can have Department and Group as children. It can have Organization, Business Unit, Division, or Department as parents. It can have multiple parents.

Group is the last level of the team in the hierarchy. It can only have Users as children and not any other teams. It can have all the team types as parents. It can have multiple parents.

Once created, the teamType for Group cannot be changed later.

Only the Teams of the type Group can own data assets.

OpenMetadata supports flexible nested team hierarchies under organizational structures such as Business Unit, Division, and Department. While there is no hardcoded limit to the depth of hierarchy, leaf nodes such as “Group” cannot have child teams. Additionally, certain team types like “Department” cannot be nested within “Group.” To extend the hierarchy, consider using other team types where appropriate.

How to Add a TeamCreating a Team in OpenMetadata is easy for different team types.Was this page helpful?YesNoSuggest editsRaise issueManage Teams and UsersPreviousHow to Add a Team | OpenMetadata Admin GuideNext⌘I
