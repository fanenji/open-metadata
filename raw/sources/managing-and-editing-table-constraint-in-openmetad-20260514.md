---
type: clip
title: "Managing and Editing Table Constraint in OpenMetadata - OpenMetadata Documentation"
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/data-discovery/table-constraint"
clipped: 2026-05-14
origin: web-clip
sources: []
tags: [web-clip]
---

# Managing and Editing Table Constraint in OpenMetadata - OpenMetadata Documentation

Source: https://docs.open-metadata.org/v1.12.x/how-to-guides/data-discovery/table-constraint

Skip to main contentOpenMetadata Documentation home pagev1.12.xSearch...⌘KSearch...NavigationData DiscoveryManaging and Editing Table Constraint in OpenMetadataHomeQuickstartDeploymentConnectorsHow-to GuidesMCPAdmin GuideGuide for Data UsersData DiscoveryData ContractsData CollaborationData Quality and ObservabilityData Quality and ProfilerData Quality ObservabilityData LineageData InsightsData GovernanceReleasesDevelopersSDK & APIsData DiscoveryOverviewHow to Discover Assets of InterestSteps for Searching Using HierarchyGet a Quick Glance of the Data AssetsDetailed View of the Data AssetsAdd Complex Queries using Advanced SearchBulk Upload Data AssetsHow to Bulk Import Data AssetHow to Export Data AssetImport-Export TroubleshootingTable ConstraintOn this pageTable ConstraintViewing table constraintNavigate to the Table Details Page:Explore Table Constraints:Editing table constraint:Ensure Appropriate Permissions:Access the Table’s Schema:Modify Constraints:Documentation IndexFetch the complete documentation index at: https://docs.open-metadata.org/llms.txtUse this file to discover all available pages before exploring further.​Table Constraint

​In OpenMetadata, table constraint are integral to understanding the relationships between tables, enhancing data discovery, and facilitating comprehensive data lineage tracking. By default, the ingestion process captures these constraints, allowing users to visualize and manage table relationships effectively.​

​Viewing table constraint

Once the metadata ingestion is complete, foreign key relationships can be explored within the OpenMetadata UI:​

​Navigate to the Table Details Page:

Access the desired table within the OpenMetadata interface.

​Explore Table Constraints:

Table constraint are displayed, detailing the relationships between the current table and its related tables. OpenMetadata referred column for foreign key

This visualization aids in understanding data dependencies and supports effective data governance.​

​Editing table constraint:

To modify table constraint:​GitHub

​Ensure Appropriate Permissions:

Confirm that you have the necessary edit permissions for the table.​

​Access the Table’s Schema:

Navigate to the table’s schema view within the OpenMetadata UI.​

​Modify Constraints:

Edit the table constraint as required.​

If the editing options are unavailable, it may indicate insufficient permissions or that the feature is not supported in your current OpenMetadata version. In such cases, consider upgrading to the latest version or consulting your administrator.​Was this page helpful?YesNoSuggest editsRaise issueTroubleshooting for Import-Export issuePrevious⌘I
