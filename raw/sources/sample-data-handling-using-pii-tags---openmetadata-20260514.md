---
type: clip
title: "Sample Data Handling Using PII Tags - OpenMetadata Documentation"
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/data-governance/classification/sample-data-using-pii-tag"
clipped: 2026-05-14
origin: web-clip
sources: []
tags: [web-clip]
---

# Sample Data Handling Using PII Tags - OpenMetadata Documentation

Source: https://docs.open-metadata.org/v1.12.x/how-to-guides/data-governance/classification/sample-data-using-pii-tag

Skip to main contentOpenMetadata Documentation home pagev1.12.xSearch...⌘KSearch...NavigationClassificationSample Data Handling Using PII TagsHomeQuickstartDeploymentConnectorsHow-to GuidesMCPAdmin GuideGuide for Data UsersData DiscoveryData ContractsData CollaborationData Quality and ObservabilityData Quality and ProfilerData Quality ObservabilityData LineageData InsightsData GovernanceReleasesDevelopersSDK & APIsData GovernanceOverviewGlossaryClassificationOverviewOverview of ClassificationHow to Classify Data AssetsHow to Request for Classification TagsSample Data Handling Using PII TagsAuto-Classification WorkflowWhat are TiersBest Practices for ClassificationDomains & Data ProductMetricsColumn Bulk OperationsOn this pageSample Data Handling Using PII TagsHow It WorksExampleHow to Apply PII TagsDocumentation IndexFetch the complete documentation index at: https://docs.open-metadata.org/llms.txtUse this file to discover all available pages before exploring further.​Sample Data Handling Using PII Tags

In OpenMetadata, sensitive information is protected through automatic masking of sample data when PII (Personally Identifiable Information) tags are applied.

​How It Works

If a PII tag is applied to a specific column:

Only that column’s sample data will be masked and displayed as ****** in the UI.

If a PII tag is applied at the table level:

All columns within that table will have their sample data masked automatically.

This behavior ensures that sensitive data is not exposed through sample data views in OpenMetadata.

​Example

Column NameTagSample Data DisplayedemailPII.Sensitive******phoneNumberPII.Sensitive******age(None)25

When the tag is applied at the table level, the result would be:

Column NameTagSample Data DisplayedemailInherited from Table******phoneNumberInherited from Table******ageInherited from Table******

​How to Apply PII Tags

Navigate to the column or table in the OpenMetadata UI.

Apply the PII.Sensitive tag via the tagging options.

Ensure auto-classification or manual tagging captures the correct columns during ingestion.

Was this page helpful?YesNoSuggest editsRaise issueHow to Request for Classification Tags | Official DocumentationPreviousAuto-Classification in OpenMetadataNext⌘I
