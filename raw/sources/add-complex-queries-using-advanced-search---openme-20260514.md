---
type: clip
title: "Add Complex Queries using Advanced Search - OpenMetadata Documentation"
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/data-discovery/advanced"
clipped: 2026-05-14
origin: web-clip
sources: []
tags: [web-clip]
---

# Add Complex Queries using Advanced Search - OpenMetadata Documentation

Source: https://docs.open-metadata.org/v1.12.x/how-to-guides/data-discovery/advanced

Skip to main contentOpenMetadata Documentation home pagev1.12.xSearch...⌘KSearch...NavigationData DiscoveryAdd Complex Queries using Advanced SearchHomeQuickstartDeploymentConnectorsHow-to GuidesMCPAdmin GuideGuide for Data UsersData DiscoveryData ContractsData CollaborationData Quality and ObservabilityData Quality and ProfilerData Quality ObservabilityData LineageData InsightsData GovernanceReleasesDevelopersSDK & APIsData DiscoveryOverviewHow to Discover Assets of InterestSteps for Searching Using HierarchyGet a Quick Glance of the Data AssetsDetailed View of the Data AssetsAdd Complex Queries using Advanced SearchBulk Upload Data AssetsHow to Bulk Import Data AssetHow to Export Data AssetImport-Export TroubleshootingTable ConstraintOn this pageAdd Complex Queries using Advanced SearchNote on Custom Properties in Elasticsearch SearchDocumentation IndexFetch the complete documentation index at: https://docs.open-metadata.org/llms.txtUse this file to discover all available pages before exploring further.​Add Complex Queries using Advanced Search

In case of voluminous data, the advanced search option helps to narrow down the search results for data discovery. The query builder supports multiple conditions as well as grouped conditions to simplify search.

The advanced search option is a quick and easy to use UI query builder to support complex queries for data discovery.

To use the advanced search for complex queries:

Navigate to the Explore page and click on the Advanced option on the top right

Using the Syntax Editor, select the Field you would like like to search by. Currently, the following fields are supported: Deleted, Owner, Tags, Tier, Service, Database, Database Schema, and Column.

Select the required Conditions for your query. The following fields are supported: Equal to, Not equal to, Any in, Not in, Contains, and Does not contain. The conditions will vary based on the field selected.

Add in the values for the Criteria.

You can add multiple conditions and group the conditions together.

Use the AND/OR conditions. Select AND to ensure that all the conditions are satisfied. Select OR to ensure that any one of the conditions is satisfied.

For example, we can set up a complex query as follows:

Group one set of conditions together by defining the Owner. You can add multiple conditions to define different owners and use the OR condition to ensure that the owner is any one among them.

​Note on Custom Properties in Elasticsearch SearchElasticsearch does not support searching for custom properties with the following formats:

Time

DateTime

Any date formats other than yyyy-MM-dd

Please ensure that custom properties adhere to these constraints for compatibility with Elasticsearch search functionality.

Next, you can add another set of conditions specific to the data based on the Service, Database, Schema, or Columns. Apply the conditions to search.

Was this page helpful?YesNoSuggest editsRaise issueDetailed View of the Data AssetsPreviousBulk Upload Data Assets with CSV in OpenMetadataNext⌘I
