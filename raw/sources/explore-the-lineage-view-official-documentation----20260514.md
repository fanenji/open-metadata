---
type: clip
title: "Explore the Lineage View | Official Documentation - OpenMetadata Documentation"
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/data-lineage/explore"
clipped: 2026-05-14
origin: web-clip
sources: []
tags: [web-clip]
---

# Explore the Lineage View | Official Documentation - OpenMetadata Documentation

Source: https://docs.open-metadata.org/v1.12.x/how-to-guides/data-lineage/explore

Skip to main contentOpenMetadata Documentation home pagev1.12.xSearch...⌘KSearch...NavigationData LineageExplore the Lineage View | Official DocumentationHomeQuickstartDeploymentConnectorsHow-to GuidesMCPAdmin GuideGuide for Data UsersData DiscoveryData ContractsData CollaborationData Quality and ObservabilityData Quality and ProfilerData Quality ObservabilityData LineageData InsightsData GovernanceReleasesDevelopersSDK & APIsData LineageOverviewHow to Deploy a Lineage WorkflowExplore the Lineage ViewHow Column-Level Lineage WorksHow to Manually Add or Edit LineageOn this pageExplore the Lineage ViewLineage LayersColumn LayerObservability LayerService LayerDomain LayerData Product LayerDocumentation IndexFetch the complete documentation index at: https://docs.open-metadata.org/llms.txtUse this file to discover all available pages before exploring further.​Explore the Lineage View

OpenMetadata UI displays end-to-end lineage traceability for the table and column levels. OpenMetadata supports lineage for Database, Dashboard, and Pipelines. Just search for an data asset and expand the graph to unfold lineage. It’ll display the upstreams and downstreams edges for each node. The lineage details specify the SQL query, pipeline information, and column lineage.

In the lineage view, in the example below, the table on the left is the parent or Source node. The table on the right is the Target node. You can also identify the target node by looking at the arrow attached to it. The arrow connecting the data assets or tables is the Edge. Clicking on an edge connecting a source and a destination will display all the edge information: the Source, Target, Description, and SQL Query. It displays the SQL query used to generate the view (The table is of the Type View). The SQL query provides information on how the target table was generated from the source table.

Tip: Metadata ingestion also brings in the View Lineage, if the database has views (Data assets of the Type View).

You can set up the Lineage Config to display the required number of Upstream and Downstream Nodes, as well as the Nodes per layer. You can set up to 3 Upstream and Downstream Nodes.

You can click on the data assets to view the data asset details.

Users can view the Source, Name of the Data Asset, Description, Owner (Team/User details), Tier, and Usage information for the data asset.

Based on the type of data asset (Table, Topic, Dashboard, Pipeline, ML Model, Container), the quick preview provides additional information. For example, for tables, the type of table, the number of queries, and columns are displayed.

The data quality and profiler metrics displays the details on the Tests Passed, Aborted, and Failed.

Users can view all the tags associated with the data asset.

The Schema provides the details on the column names, type of column, and column description.

Clicking on the tables will display the list of columns and column-level lineage.

In case of Pipelines, we first have the lineage ingested from the databases. Further, when setting up the pipeline ingestion, we specify the database service name. That way we display the lineage of the database tables connected via pipelines. If a lineage is created through a pipeline, the same is displayed in the Edge information.

Similarly for a Dashboard, we first have the lineage ingested from the databases. Further, when setting up the dashboard ingestion, the data models and charts are ingested. That way we display the lineage of the database tables connected using the dashboard data models.

​Lineage Layers

Lineage view supports multiple exploration layers that provide deeper insights into the structure, flow, and quality of data across your ecosystem. These layers help users visualize lineage not just at the dataset level, but also across services, domains, and business-critical data products.

​Column Layer

The Column layer enables detailed exploration of column-level lineage, allowing users to trace the flow and transformation of specific fields (e.g., customer_id, first_name) across tables and pipelines. This granularity helps in understanding data dependencies at the attribute level.

​Observability Layer

The Observability layer integrates data quality insights directly into lineage by displaying test outcomes such as passes, failures, and pending checks. This helps users identify potential issues and assess the trustworthiness of data as it moves through the pipeline.

​Service Layer

The Service layer visualizes how data flows across different platforms and services like Hive, Redshift, Power BI, and Tableau. It connects ingestion, transformation, and consumption points, offering a system-level view of the end-to-end data journey.

​Domain Layer

The Domain layer organizes datasets and assets into business-relevant categories such as “Ecommerce” or “Customer Data.” This classification provides contextual clarity and supports governance by aligning technical assets with business functions.

​Data Product Layer

The Data Product layer highlights curated outputs like Customer Registry or Superstore, representing the final, value-delivering datasets within a domain. It enables teams to track the lineage of trusted, consumption-ready data products across the organization.

How Column-Level Lineage WorksExplore and edit the rich column-level lineage.Was this page helpful?YesNoSuggest editsRaise issueHow to Deploy a Lineage WorkflowPreviousHow Column-Level Lineage Works | Official DocumentationNext⌘I
