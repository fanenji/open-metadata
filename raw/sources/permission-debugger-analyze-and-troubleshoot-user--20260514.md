---
type: clip
title: "Permission Debugger | Analyze and Troubleshoot User Access - OpenMetadata Documentation"
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/admin-guide/permission-debugger"
clipped: 2026-05-14
origin: web-clip
sources: []
tags: [web-clip]
---

# Permission Debugger | Analyze and Troubleshoot User Access - OpenMetadata Documentation

Source: https://docs.open-metadata.org/v1.12.x/how-to-guides/admin-guide/permission-debugger

Skip to main contentOpenMetadata Documentation home pagev1.12.xSearch...⌘KSearch...NavigationAdmin GuidePermission Debugger | Analyze and Troubleshoot User AccessHomeQuickstartDeploymentConnectorsHow-to GuidesMCPAdmin GuideGuide for Data UsersData DiscoveryData ContractsData CollaborationData Quality and ObservabilityData Quality and ProfilerData Quality ObservabilityData LineageData InsightsData GovernanceReleasesDevelopersSDK & APIsAdmin GuideOverviewHow to Ingest MetadataHow to Delete a Service ConnectionManage Teams and UsersAdvanced Guide for Roles and PoliciesCLI Ingestion with Basic AuthHow to Add Custom LogoReindexing SearchData InsightsPermission DebuggerPersona and Landing Page CustomizationAudit LogsOn this pagePermission DebuggerHow It WorksHow to Use the Permission Debugger1. Select a User2. Define the Permission Check3. Evaluate PermissionExample 1: DENIED (EditAll on Table)Example 2: ALLOWED (ViewAll on Table)📄 Scenario🔍 Evaluation Result📊 Evaluation SummaryUse CasesDocumentation IndexFetch the complete documentation index at: https://docs.open-metadata.org/llms.txtUse this file to discover all available pages before exploring further.​Permission Debugger

The Permission Debugger allows administrators to analyze and debug user permissions across roles, teams, and policies. This feature is critical for troubleshooting access issues, verifying policy behavior, and ensuring users have the correct level of access.

​How It Works

The Permission Debugger simulates permission checks for a given user on a selected resource and operation. It provides detailed insight into:

Which policies and rules were evaluated

The final allow/deny decision

Matching rule count

Evaluation time

​How to Use the Permission Debugger

​1. Select a User

First navigate to settings > Access Control > Permission Debugger

Use the input field to search for and select the user whose permissions you want to inspect.

​2. Define the Permission Check

Resource: Select a resource type.

Options include: user, team, table, database, glossary, tag, glossaryTerm, searchIndex, mlModel, container, topic, pipeline, dashboard, databaseSchema

Operation: Choose the operation to check against the selected resource.

Examples: ViewAll, EditAll, Deploy, Trigger, Kill, GenerateToken, etc.

Resource FQN or ID (Optional): Provide a Fully Qualified Name (FQN) or unique ID of a specific resource if you want to debug at the resource instance level.

​3. Evaluate Permission

Click the Evaluate button to perform the permission check.

​Example 1: DENIED (EditAll on Table)

User: prajwal.pp44

Resource: table

Operation: EditAll

Resource FQN: sample_data.ecommerce_db.shopify.dim_address_clean

Result:

Decision: DENIED

User prajwal.pp44 is Denied to perform EditAll on

table (sample_data.ecommerce_db.shopify.dim_address_clean)

Evaluation Summary:

MetricValuePolicies Evaluated2Rules Evaluated1048Matching Rules0Allow Rules0Deny Rules0Time354ms

​Example 2: ALLOWED (ViewAll on Table)

This example demonstrates a successful permission evaluation for a user attempting to view a specific table resource using the ViewAll operation.

​📄 Scenario

User: prajwal.pp44

Resource: table

Operation: ViewAll

Resource FQN: sample_data.ecommerce_db.shopify.dim_address_clean

​🔍 Evaluation Result

Decision: ALLOWED

User prajwal.pp44 is Allowed to perform ViewAll on

table (sample_data.ecommerce_db.shopify.dim_address_clean)

​📊 Evaluation Summary

DetailValuePolicies Evaluated2Rules Evaluated1048Matching Rules1046Allow Rules0Deny Rules0Evaluation Time363ms

​Use Cases

Debug permission issues for a specific user.

Validate that newly created policies are functioning as expected.

Understand why a user has or doesn’t have access to specific resources.

Was this page helpful?YesNoSuggest editsRaise issueResolving Data Insights and KPI Display Issues in OpenMetadataPreviousPersona and Landing Page Customization in OpenMetadataNext⌘I
