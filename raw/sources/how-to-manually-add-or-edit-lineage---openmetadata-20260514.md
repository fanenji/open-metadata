---
type: clip
title: "How to Manually Add or Edit Lineage - OpenMetadata Documentation"
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/data-lineage/manual"
clipped: 2026-05-14
origin: web-clip
sources: []
tags: [web-clip]
---

# How to Manually Add or Edit Lineage - OpenMetadata Documentation

Source: https://docs.open-metadata.org/v1.12.x/how-to-guides/data-lineage/manual

Skip to main contentOpenMetadata Documentation home pagev1.12.xSearch...⌘KSearch...NavigationData LineageHow to Manually Add or Edit LineageHomeQuickstartDeploymentConnectorsHow-to GuidesMCPAdmin GuideGuide for Data UsersData DiscoveryData ContractsData CollaborationData Quality and ObservabilityData Quality and ProfilerData Quality ObservabilityData LineageData InsightsData GovernanceReleasesDevelopersSDK & APIsData LineageOverviewHow to Deploy a Lineage WorkflowExplore the Lineage ViewHow Column-Level Lineage WorksHow to Manually Add or Edit LineageOn this pageHow to Manually Add or Edit LineageDocumentation IndexFetch the complete documentation index at: https://docs.open-metadata.org/llms.txtUse this file to discover all available pages before exploring further.​How to Manually Add or Edit Lineage

Edit lineage to provide a richer understanding of the provenance of data. The OpenMetadata no-code editor provides a drag and drop interface. Drop tables, topics, pipelines, dashboards, ML models, containers, and pipelines onto the lineage graph. You may add new edges or delete existing edges to better represent data lineage.

OpenMetadata supports manual editing of both table and column level lineage. We can build the lineage by creating edges. You can connect the source of the lineage to the destination by connecting the nodes.

Once you have ingested your database and dashboard services.

Start by picking one database service, and select a table. In the data asset details page, navigate to the Lineage Tab.

Click on the Edit option to enable the lineage editor.

Select the type of data asset (table, topic, dashboard, ML model, container, pipeline) to connect to as the destination.

Search and select the relevant data asset.

Create an edge between these two data assets.

You can also expand a table to view the available columns

Link the relevant columns together by connecting the column edges to trace column-level lineage.

Here’s a quick video on manually adding lineage.

Watch the recording of the Webinar on Lineage (13:30 to 15:50)

Was this page helpful?YesNoSuggest editsRaise issueHow Column-Level Lineage Works | Official DocumentationPrevious⌘I
