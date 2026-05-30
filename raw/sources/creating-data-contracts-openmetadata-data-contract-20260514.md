---
type: clip
title: "Creating Data Contracts | OpenMetadata Data Contracts Guide - OpenMetadata Documentation"
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/data-contracts/create"
clipped: 2026-05-14
origin: web-clip
sources: []
tags: [web-clip]
---

# Creating Data Contracts | OpenMetadata Data Contracts Guide - OpenMetadata Documentation

Source: https://docs.open-metadata.org/v1.12.x/how-to-guides/data-contracts/create

Skip to main contentOpenMetadata Documentation home pagev1.12.xSearch...⌘KSearch...NavigationData ContractsCreating Data Contracts | OpenMetadata Data Contracts GuideHomeQuickstartDeploymentConnectorsHow-to GuidesMCPAdmin GuideGuide for Data UsersData DiscoveryData ContractsData CollaborationData Quality and ObservabilityData Quality and ProfilerData Quality ObservabilityData LineageData InsightsData GovernanceReleasesDevelopersSDK & APIsData ContractsOverviewCreating Data ContractsData Contract SpecificationOn this pageCreate Data ContractDocumentation IndexFetch the complete documentation index at: https://docs.open-metadata.org/llms.txtUse this file to discover all available pages before exploring further.​Create Data Contract

Data contracts are currently available for tables ingested into OpenMetadata. The following guide shows how a data contract was created for a snowflake.DEMO_STAGE.JAFFLE_SHOP.CUSTOMERS table.

To create a Data Contract for a Table in OpenMetadata:

Go to the Table’s page, select Contract, then + Add Contract

In Contract Details, be sure to give your new data contract a name. Optionally, you can assign Owners and provide a description of your data contract. Then select Schema.

Select the columns of your table that you would like to add to your new data contract, or select all columns by checking the box at the top right. Then select Semantics

Add the business rules you would like to enforce in Semantics. For OpenMetadata Tables, rules can be created for:

Service

Owners

Display Name

Name

Description

Tags

Domain

Data Product

Tier

Once a rule is created, you can + Add New Rule to create more, or select Quality

Select + Add Test to add a Data Quality Test or tests to your new contract, then select Save

Once your new data contract has been created successfully, you can run it by selecting > Run now

Was this page helpful?YesNoSuggest editsRaise issueData Contracts | OpenMetadata Data ContractsPreviousCreating Data Contracts | OpenMetadata Data Contracts GuideNext⌘I
