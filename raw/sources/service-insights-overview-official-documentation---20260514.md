---
type: clip
title: "Service Insights Overview | Official Documentation - OpenMetadata Documentation"
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/data-insights/service-insights"
clipped: 2026-05-14
origin: web-clip
sources: []
tags: [web-clip]
---

# Service Insights Overview | Official Documentation - OpenMetadata Documentation

Source: https://docs.open-metadata.org/v1.12.x/how-to-guides/data-insights/service-insights

Skip to main contentOpenMetadata Documentation home pagev1.12.xSearch...⌘KSearch...NavigationData InsightsService Insights Overview | Official DocumentationHomeQuickstartDeploymentConnectorsHow-to GuidesMCPAdmin GuideGuide for Data UsersData DiscoveryData ContractsData CollaborationData Quality and ObservabilityData Quality and ProfilerData Quality ObservabilityData LineageData InsightsData GovernanceReleasesDevelopersSDK & APIsData InsightsOverviewWhat is TieringSet Up Data Insights IngestionKey Performance Indicators (KPI)Elasticsearch reindexData Insights ReportConfigure the Data Insights ReportHow to Transform the Data Culture of Your CompanyService InsightsOn this pageService InsightsTotal Data AssetsDescription CoveragePII CoverageTier CoverageOwnership coverageGenerated Data with OpenMetadata AI (OpenMetadata Only)PII DistributionTier DistributionMost Used Data AssetsMost Expensive QueriesData QualityDocumentation IndexFetch the complete documentation index at: https://docs.open-metadata.org/llms.txtUse this file to discover all available pages before exploring further.​Service Insights

Users can view insights for individual services using the Service Insights tab. This guide provides an overview of the available charts and outlines troubleshooting steps when no data is displayed.

​Total Data Assets

This chart displays the total number of data assets within a service, categorized by asset type. For example, in a database service, it shows the count of tables, databases, database schemas, and stored procedures.

If no data is displayed, ensure that the metadata ingestion pipeline has been executed successfully.

​Description Coverage

This chart shows the percentage of data assets that have a populated description field.

If no data is displayed, verify that both the metadata ingestion pipeline and the data insights pipeline have been executed successfully.

​PII Coverage

This chart displays the percentage of data assets containing columns tagged with Personally Identifiable Information (PII) tags.

If the chart does not show any data, ensure that both the Auto Classification pipeline and the Data Insights pipeline have been successfully executed.

​Tier Coverage

This chart displays the percentage of data assets where tier classification has been populated.

If the chart shows no data, verify that the Auto Tiering pipeline (OpenMetadata only) and the Data Insights pipeline have been executed successfully.

​Ownership coverage

This chart shows the percentage of data assets that have a populated owner field.

If no data is displayed, verify that both the metadata ingestion pipeline and the data insights pipeline have been executed successfully.

​Generated Data with OpenMetadata AI (OpenMetadata Only)

This table displays a breakdown of metadata populated by the OpenMetadata AI agent versus metadata populated manually.

If the table shows no data, ensure that the Auto Classification pipeline, Auto Data Quality (DQ) pipeline, Auto Tiering pipeline, OpenMetadata AI application, and Data Insights application have been executed successfully.

​PII Distribution

This table displays a breakdown of data assets categorized by their associated PII (Personally Identifiable Information) tags.

If the table shows no data, verify that both the Auto Classification pipeline and the Data Insights application have been executed successfully.

​Tier Distribution

This table provides a breakdown of data assets based on their assigned Tier classification.

If the table displays no data, ensure that the Auto Tiering pipeline (OpenMetadata only) and the Data Insights application have been executed successfully.

​Most Used Data Assets

This table displays the top five most frequently accessed data assets, determined by their usage percentile.

If the table shows no data, verify that the usage pipeline has been executed successfully.

​Most Expensive Queries

This table displays the top queries based on the cost of query execution.

If the table shows no data, verify that the usage pipeline has been executed successfully. Additionally, not all connectors support extracting query cost—ensure that your connector supports this feature.

​Data Quality

This chart shows the percentage of data assets that have one or more data quality tests configured.

If no data is displayed, verify that the data quality pipeline and the data insights pipeline have been executed successfully.

Was this page helpful?YesNoSuggest editsRaise issueHow to Transform the Data Culture of Your CompanyPrevious⌘I
