---
type: clip
title: "How to Discover Assets of Interest - OpenMetadata Documentation"
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/data-discovery/discover"
clipped: 2026-05-14
origin: web-clip
sources: []
tags: [web-clip]
---

# How to Discover Assets of Interest - OpenMetadata Documentation

Source: https://docs.open-metadata.org/v1.12.x/how-to-guides/data-discovery/discover

Skip to main contentOpenMetadata Documentation home pagev1.12.xSearch...⌘KSearch...NavigationData DiscoveryHow to Discover Assets of InterestHomeQuickstartDeploymentConnectorsHow-to GuidesMCPAdmin GuideGuide for Data UsersData DiscoveryData ContractsData CollaborationData Quality and ObservabilityData Quality and ProfilerData Quality ObservabilityData LineageData InsightsData GovernanceReleasesDevelopersSDK & APIsData DiscoveryOverviewHow to Discover Assets of InterestSteps for Searching Using HierarchyGet a Quick Glance of the Data AssetsDetailed View of the Data AssetsAdd Complex Queries using Advanced SearchBulk Upload Data AssetsHow to Bulk Import Data AssetHow to Export Data AssetImport-Export TroubleshootingTable ConstraintOn this pageHow to Discover Assets of InterestSearchKeyword SearchQuick FiltersFilter by the Type of Data AssetFilter by Asset OwnerFilter by DatabaseFilter based on Importance: TiersFilter based on Importance: UsageDiscover Data through AssociationDiscover Assets through RelationshipsAdvanced SearchDiscover Data EvolutionFilter by Deleted Data AssetsDocumentation IndexFetch the complete documentation index at: https://docs.open-metadata.org/llms.txtUse this file to discover all available pages before exploring further.​How to Discover Assets of Interest

OpenMetadata simplifies data discovery with the following strategies.

​Search

Search is at the front and center of OpenMetadata and is available in the top Menu bar across all the different pages. Users can also start searching by invoking the Keyboard shortcut Ctrl + K in Windows or Cmd + K in Mac OS.

The Search APIs are backed by Elasticsearch.

​Keyword Search

A simple yet powerful way to find assets by typing the name or description from the search interface. The search suggest will display matching data assets in several categories. Your query will retrieve all matching tables, topics, dashboards, pipelines, ML models, containers, glossaries, and tags. Your queries will match names for data assets and their components, such as column names for tables and chart names for dashboards. The queries will also match the descriptions used.

​Quick Filters

Multiple quick filter options further help to narrow down the search by Owner, Tag, Tier, Service, Service Type, and other filters relevant to the type of data asset like Database, Schema, Columns. You can also search by deleted data assets.

​Filter by the Type of Data Asset

The search results can be narrowed down by data assets such as Table, Topic, Dashboard, Pipeline, ML Model, Container, Glossary, or Tag.

Users can navigate to the Explore page for specific type of data assets and use the filter options relevant to that data asset to narrow down the search.

​Filter by Asset Owner

A team or a user can own the data asset in OpenMetadata. Users can filter data assets by the asset owner. With information on the data asset owners, you can direct your questions to the right person or team.

​Filter by Database

When searching while you are in a database page, you can narrow down your search to within the database or to include the overall search results within OpenMetadata.

​Filter based on Importance: Tiers

Using tiers, you can search for data based on importance.

​Filter based on Importance: Usage

OpenMetadata captures usage profiles for tables during metadata/profiler ingestion. This helps to learn how other data consumers are using the tables. You can use the quick filter to narrow down the search results by relevance by clicking on the down arrow on the top right of the Explore page. You can search for data by:

Last Updated - Filter data by the recent updates and changes.

Weekly Usage - Based on the data asset usage metrics.

Relevance

These details are based on the usage summary computations. Further, you can sort the results by ascending and descending order.

​Discover Data through Association

OpenMetadata provides the links to the frequently joined tables and columns as measured by the data profiler. You can also discover assets through relationships based on data lineage.

​Discover Assets through Relationships

OpenMetadata helps to locate assets of interest by tracing data lineage. You can view the upstream and downstream nodes to discover the sources of data and learn about the tables, pipelines, and more. The table and column descriptions help to decide if the data is helpful for your use case. Similarly, the pipeline description helps to uncover the transformation and more data of interest.

​Advanced Search

Users can find data assets matching strict criteria by multiple parameters on metadata properties, using the syntax editor with and/or conditions. Advanced search in OpenMetadata supports Boolean operators and faceted queries to search for specific facets of your data. Separate advanced search options are available for Tables, Topics, Dashboards, Pipelines, ML Models, Containers, Glossary, and Tags.

​Discover Data Evolution

By viewing lineage and metadata versioning, users can discover the data evolution of data assets.

​Filter by Deleted Data Assets

Users can also search for the soft-deleted data assets in OpenMetadata. Use the toggle bar to search for deleted assets. The deleted data assets are read-only.

Users can click on Clear to unselect all the filter options.

Get a Quick Glance of the Data AssetsQuick preview of the selected data asset.Was this page helpful?YesNoSuggest editsRaise issueData Discovery | OpenMetadata How-To GuidePreviousGuide to Searching Data Using Hierarchical ViewNext⌘I
