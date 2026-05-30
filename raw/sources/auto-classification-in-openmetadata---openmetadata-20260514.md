---
type: clip
title: "Auto-Classification in OpenMetadata - OpenMetadata Documentation"
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/data-governance/classification/auto-classification"
clipped: 2026-05-14
origin: web-clip
sources: []
tags: [web-clip]
---

# Auto-Classification in OpenMetadata - OpenMetadata Documentation

Source: https://docs.open-metadata.org/v1.12.x/how-to-guides/data-governance/classification/auto-classification

Skip to main contentOpenMetadata Documentation home pagev1.12.xSearch...⌘KSearch...NavigationAuto-Classification WorkflowAuto-Classification in OpenMetadataHomeQuickstartDeploymentConnectorsHow-to GuidesMCPAdmin GuideGuide for Data UsersData DiscoveryData ContractsData CollaborationData Quality and ObservabilityData Quality and ProfilerData Quality ObservabilityData LineageData InsightsData GovernanceReleasesDevelopersSDK & APIsData GovernanceOverviewGlossaryClassificationOverviewOverview of ClassificationHow to Classify Data AssetsHow to Request for Classification TagsSample Data Handling Using PII TagsAuto-Classification WorkflowOverviewWorkflowExternal WorkflowAuto PII TaggingSample DataWhat are TiersBest Practices for ClassificationDomains & Data ProductMetricsColumn Bulk OperationsOn this pageAuto-Classification WorkflowTag MappingDocumentation IndexFetch the complete documentation index at: https://docs.open-metadata.org/llms.txtUse this file to discover all available pages before exploring further.​Auto-Classification Workflow

OpenMetadata identifies PII data and auto tags or suggests the tags. It automatically detects sensitive data and assigns relevant tags such as ‘PII Sensitive’. The addition of tags about PII data helps consumers and governance teams identify data that needs to be treated carefully.

In the example below, the columns ‘last_name’ and ‘social security number’ are auto-tagged as PII-sensitive. This works using NLP as part of the profiler during ingestion.

In the below example, the column ‘number_of_orders’ is also auto-tagged as Sensitive, even though the column name does not provide much information.

When we look at the content of the column ‘number_of_orders’ in the Sample Data tab, it becomes clear that the auto-classification is based on the data in the column.

You can read more about Auto PII Tagging here.

​Tag Mapping

Tag mapping is supported in the backend and not in the OpenMetadata UI. When two related tags are associated with each other, applying one tag, automatically applies the other tag. For example, when the tag Personal Data.Personal is applied, it automatically applies another tag Data Classification.Confidential. That way, applying the tag Personal automatically applies the tag Confidential.

What are TiersTiers helps to define the importance of data to an organization.Was this page helpful?YesNoSuggest editsRaise issueSample Data Handling Using PII TagsPreviousAdding Auto Classification Workflow through UINext⌘I
