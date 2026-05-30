---
type: clip
title: "Auto Pii Tagging Guide | Official Documentation - OpenMetadata Documentation"
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/data-governance/classification/auto-classification/auto-pii-tagging"
clipped: 2026-05-14
origin: web-clip
sources: []
tags: [web-clip]
---

# Auto Pii Tagging Guide | Official Documentation - OpenMetadata Documentation

Source: https://docs.open-metadata.org/v1.12.x/how-to-guides/data-governance/classification/auto-classification/auto-pii-tagging

Skip to main contentOpenMetadata Documentation home pagev1.12.xSearch...⌘KSearch...NavigationAuto-Classification WorkflowAuto Pii Tagging Guide | Official DocumentationHomeQuickstartDeploymentConnectorsHow-to GuidesMCPAdmin GuideGuide for Data UsersData DiscoveryData ContractsData CollaborationData Quality and ObservabilityData Quality and ProfilerData Quality ObservabilityData LineageData InsightsData GovernanceReleasesDevelopersSDK & APIsData GovernanceOverviewGlossaryClassificationOverviewOverview of ClassificationHow to Classify Data AssetsHow to Request for Classification TagsSample Data Handling Using PII TagsAuto-Classification WorkflowOverviewWorkflowExternal WorkflowAuto PII TaggingSample DataWhat are TiersBest Practices for ClassificationDomains & Data ProductMetricsColumn Bulk OperationsOn this pageAuto PII TaggingTagging logicTroubleshootingSSL: CERTIFICATE_VERIFY_FAILEDDocumentation IndexFetch the complete documentation index at: https://docs.open-metadata.org/llms.txtUse this file to discover all available pages before exploring further.​Auto PII Tagging

Auto PII tagging for Sensitive/NonSensitive at the column level is performed based on the two approaches described below.

​Tagging logic

Column Name Scanner: We validate the column names of the table against a set of regex rules that help us identify

common English patterns to identify email addresses, SSN, bank accounts, etc.

Entity Recognition: If the sample data ingestion is enabled, we’ll validate the sample rows against an Entity

Recognition engine that will bring up any sensitive information from a list of supported entities.

In that case, the confidence parameter lets you tune the minimum score required to tag a column as PII.Sensitive.

Note that if a column is already tagged as PII, we will ignore its execution.

​Troubleshooting

In OpenMetadata, the auto-classification feature primarily applies the PII classification, tagging data as either Sensitive or Non-Sensitive. The General classification, which includes tags like Address, Name, etc., is not available in the OpenMetadata. This functionality is present in the OpenMetadata and is expected to be included in the open-source release starting from version 1.7.1.

​SSL: CERTIFICATE_VERIFY_FAILED

If you see an error similar to:

Unexpected error while processing sample data for auto pii tagging - HTTPSConnectionPool(host='raw.githubusercontent.com', port=443):

Max retries exceeded with url: /explosion/spacy-models/master/compatibility.json

(Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to

get local issuer certificate (_ssl.c:1129)')))

This is a scenario that we identified on some corporate Windows laptops. The bottom-line here is that the profiler

is trying to download the Entity Recognition model but having certificate issues when trying the request.

A solution here is to manually download the model on the ingestion container / Airflow host by running:

pip --trusted-host github.com --trusted-host objects.githubusercontent.com install https://github.com/explosion/spacy-models/releases/download/en_core_web_md-3.5.0/en_core_web_md-3.5.0.tar.gz

If using Docker, you might want to customize the OpenMetadata-ingestion image to have this command run there by default.Was this page helpful?YesNoSuggest editsRaise issueExternal Auto Classification WorkflowPreviousExternal Storage for Sample DataNext⌘I
