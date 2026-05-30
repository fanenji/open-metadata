---
type: clip
title: "Custom Metrics - OpenMetadata Documentation"
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/data-quality-observability/profiler/custom-metrics"
clipped: 2026-05-14
origin: web-clip
sources: []
tags: [web-clip]
---

# Custom Metrics - OpenMetadata Documentation

Source: https://docs.open-metadata.org/v1.12.x/how-to-guides/data-quality-observability/profiler/custom-metrics

Skip to main contentOpenMetadata Documentation home pagev1.12.xSearch...⌘KSearch...NavigationData ProfilerCustom MetricsHomeQuickstartDeploymentConnectorsHow-to GuidesMCPAdmin GuideGuide for Data UsersData DiscoveryData ContractsData CollaborationData Quality and ObservabilityData Quality and ProfilerData Quality ObservabilityData LineageData InsightsData GovernanceReleasesDevelopersSDK & APIsData Quality and ObservabilityOverviewData QualityData ProfilerOverviewProfiler WorkflowMetricsCustom MetricsExternal workflowAlerts & NotificationsIncident ManagerOn this pageCustom MetricsTable-Level MetricsColumn-Level MetricsDocumentation IndexFetch the complete documentation index at: https://docs.open-metadata.org/llms.txtUse this file to discover all available pages before exploring further.​Custom Metrics

Custom metrics in OpenMetadata enhance profiling capabilities by enabling users to define and compute unique business metrics using custom SQL queries. These metrics can be added at both the table and column levels, allowing tailored analysis specific to organizational needs. Once defined, custom metrics are incorporated into the profiler workflow, and their computed values are displayed alongside system metrics in the table and column profiles. This feature provides a flexible way to track specific data insights, empowering users to gain deeper visibility into their datasets.

​Table-Level Metrics

Navigate to the Database and switch to the Data Observability tab. Click on Table Profile, and on the right-hand side, select the Add option to access the custom metric feature.

Enter a meaningful name for the custom metric and input the required SQL query based on your data requirements.

Once the custom metric is defined, run the Profiler Agent in the Database Services.

After running the profiler agent, return to the same dataset to view the computed custom metric within the table profile.

​Column-Level Metrics

Navigate to the Database and switch to the Data Observability tab. Click on Column Profile, and on the right-hand side, select the Add option to access the custom metric feature.

After clicking on Custom Metric, provide a name, select column name, and define the SQL query.

Save and run the profiler workflow to generate the metric.

After running the profiler agent, return to the same dataset to view the computed custom metric within the column profile.

Was this page helpful?YesNoSuggest editsRaise issueMetrics | OpenMetadata Profiler Metrics GuidePreviousExternal Profiler Workflow | Official DocumentationNext⌘I
