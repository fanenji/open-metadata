---
type: clip
title: "Bulk Export Data Assets via CSV in OpenMetadata - OpenMetadata Documentation"
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/data-discovery/export"
clipped: 2026-05-14
origin: web-clip
sources: []
tags: [web-clip]
---

# Bulk Export Data Assets via CSV in OpenMetadata - OpenMetadata Documentation

Source: https://docs.open-metadata.org/v1.12.x/how-to-guides/data-discovery/export

Skip to main contentOpenMetadata Documentation home pagev1.12.xSearch...⌘KSearch...NavigationData DiscoveryBulk Export Data Assets via CSV in OpenMetadataHomeQuickstartDeploymentConnectorsHow-to GuidesMCPAdmin GuideGuide for Data UsersData DiscoveryData ContractsData CollaborationData Quality and ObservabilityData Quality and ProfilerData Quality ObservabilityData LineageData InsightsData GovernanceReleasesDevelopersSDK & APIsData DiscoveryOverviewHow to Discover Assets of InterestSteps for Searching Using HierarchyGet a Quick Glance of the Data AssetsDetailed View of the Data AssetsAdd Complex Queries using Advanced SearchBulk Upload Data AssetsHow to Bulk Import Data AssetHow to Export Data AssetImport-Export TroubleshootingTable ConstraintOn this pageExport Data AssetHow to Bulk Export a Database ServiceHow to Bulk Export a DatabaseHow to Bulk Export a Database SchemaHow to Bulk Export a TablesDocumentation IndexFetch the complete documentation index at: https://docs.open-metadata.org/llms.txtUse this file to discover all available pages before exploring further.​Export Data Asset

Exporting a Data Asset is simple. Below are the steps to bulk export various data assets, such as Database Services, Databases, Schemas, and Tables.

​How to Bulk Export a Database Service

Navigate to the Database Service you want to export by going to Settings > Services > Database.

For this example, we are exporting in the Snowflake service.

Click on the ⋮ icon and select Export to download the Database Service CSV file.

You can also export the Database Service using the API with the following endpoint:/api/v1/services/databaseServices/name/{name}/export

Make sure to replace {name} with the Fully Qualified Name (FQN) of the Database Service.

​How to Bulk Export a Database

In this example, we are exporting in the DEMO database under Snowflake.

Click on the ⋮ icon and select Export to download the Database CSV file.

You can also export the Database using the API with the following endpoint:/api/v1/databases/name/{name}/export

Make sure to replace {name} with the Fully Qualified Name (FQN) of the Database.

​How to Bulk Export a Database Schema

In this example, we are exporting in the JAFFLE_SHOP schema under Snowflake > DEMO.

Click on the ⋮ icon and select Export to download the Database Schema CSV file.

You can also export the Database Schema using the API with the following endpoint:/api/v1/databaseSchemas/name/{name}/export

Make sure to replace {name} with the Fully Qualified Name (FQN) of the Database Schema.

​How to Bulk Export a Tables

In this example, we are exporting in the CUSTOMERS table under Snowflake > DEMO > JAFFLE_SHOP.

Click on the ⋮ icon and select Export to download the Table CSV file.

You can also export the Tables using the API with the following endpoint:/api/v1/tables/name/{name}/export

Make sure to replace {name} with the Fully Qualified Name (FQN) of the Table.

Data Asset ImportQuickly import a data assets as a CSV file.Was this page helpful?YesNoSuggest editsRaise issueBulk Import Data Assets via CSV in OpenMetadataPreviousTroubleshooting for Import-Export issueNext⌘I
