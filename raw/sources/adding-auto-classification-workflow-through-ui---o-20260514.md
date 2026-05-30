---
type: clip
title: "Adding Auto Classification Workflow through UI - OpenMetadata Documentation"
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/data-governance/classification/auto-classification/workflow"
clipped: 2026-05-14
origin: web-clip
sources: []
tags: [web-clip]
---

# Adding Auto Classification Workflow through UI - OpenMetadata Documentation

Source: https://docs.open-metadata.org/v1.12.x/how-to-guides/data-governance/classification/auto-classification/workflow

Skip to main contentOpenMetadata Documentation home pagev1.12.xSearch...⌘KSearch...NavigationAuto-Classification WorkflowAdding Auto Classification Workflow through UIHomeQuickstartDeploymentConnectorsHow-to GuidesMCPAdmin GuideGuide for Data UsersData DiscoveryData ContractsData CollaborationData Quality and ObservabilityData Quality and ProfilerData Quality ObservabilityData LineageData InsightsData GovernanceReleasesDevelopersSDK & APIsData GovernanceOverviewGlossaryClassificationOverviewOverview of ClassificationHow to Classify Data AssetsHow to Request for Classification TagsSample Data Handling Using PII TagsAuto-Classification WorkflowOverviewWorkflowExternal WorkflowAuto PII TaggingSample DataWhat are TiersBest Practices for ClassificationDomains & Data ProductMetricsColumn Bulk OperationsOn this pageAdding Auto Classification Agent through the UI1. Navigate to the Database Service2. Access the Agents Tab3. Configure Auto Classification Details4. Set the Schedule5. Add the Agent WorkflowDocumentation IndexFetch the complete documentation index at: https://docs.open-metadata.org/llms.txtUse this file to discover all available pages before exploring further.​Adding Auto Classification Agent through the UI

Follow these steps to configure Auto Classification Agent via the OpenMetadata UI:

​1. Navigate to the Database Service

Go to Settings > Services > Databases in the OpenMetadata UI.

Select the database for which you want to configure Auto Classification Agent.

​2. Access the Agents Tab

In the selected database, navigate to the Agents tab.

Click on the option to Add Auto Classification Agent, as shown in the example image.

​3. Configure Auto Classification Details

Fill in the details for your Auto Classification Agent workflow.

Each field’s purpose is explained directly in the UI, allowing you to customize the configuration based on your requirements.

By default, the store sample data option is enabled. If you prefer not to ingest sample data during a scheduled run, please ensure that this option is disabled in the Agent configuration.

​4. Set the Schedule

Specify the time interval at which the Auto Classification Agent should run.

​5. Add the Agent Workflow

Once all details are configured, click Add Auto Classification Agent to save and activate the workflow.

By following these steps, you can set up an Auto Classification Agent workflow to automatically identify and tag sensitive data in your databases.Was this page helpful?YesNoSuggest editsRaise issueAuto-Classification in OpenMetadataPreviousExternal Auto Classification WorkflowNext⌘I
