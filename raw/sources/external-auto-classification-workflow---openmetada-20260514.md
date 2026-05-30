---
type: clip
title: "External Auto Classification Workflow - OpenMetadata Documentation"
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/data-governance/classification/auto-classification/external-workflow"
clipped: 2026-05-14
origin: web-clip
sources: []
tags: [web-clip]
---

# External Auto Classification Workflow - OpenMetadata Documentation

Source: https://docs.open-metadata.org/v1.12.x/how-to-guides/data-governance/classification/auto-classification/external-workflow

Skip to main contentOpenMetadata Documentation home pagev1.12.xSearch...⌘KSearch...NavigationAuto-Classification WorkflowExternal Auto Classification WorkflowHomeQuickstartDeploymentConnectorsHow-to GuidesMCPAdmin GuideGuide for Data UsersData DiscoveryData ContractsData CollaborationData Quality and ObservabilityData Quality and ProfilerData Quality ObservabilityData LineageData InsightsData GovernanceReleasesDevelopersSDK & APIsData GovernanceOverviewGlossaryClassificationOverviewOverview of ClassificationHow to Classify Data AssetsHow to Request for Classification TagsSample Data Handling Using PII TagsAuto-Classification WorkflowOverviewWorkflowExternal WorkflowAuto PII TaggingSample DataWhat are TiersBest Practices for ClassificationDomains & Data ProductMetricsColumn Bulk OperationsOn this pageAuto Classification Workflow ConfigurationPipeline Configuration ParametersKey Parameters ExplainedenableAutoClassificationconfidencestoreSampleDatauseFqnForFilteringAuto Classification Workflow Execution1. Install the Required Python Package2. Define and Execute the Python WorkflowSample Auto Classification Workflow yaml3. Expected OutcomeAuto Classification1. Define the YAML Config2. Run with the CLIWorkflow ExecutionTo Execute the Auto Classification Workflow:Expected OutcomesDocumentation IndexFetch the complete documentation index at: https://docs.open-metadata.org/llms.txtUse this file to discover all available pages before exploring further.​Auto Classification Workflow Configuration

The Auto Classification Workflow enables automatic tagging of sensitive information within databases. Below are the configuration parameters available in the Service Classification Pipeline JSON.

​Pipeline Configuration Parameters

ParameterDescriptionTypeDefault ValuetypeSpecifies the pipeline type.StringAutoClassificationclassificationFilterPatternRegex to compute metrics for tables matching specific tags, tiers, or glossary patterns.ObjectN/AschemaFilterPatternRegex to fetch schemas matching the specified pattern.ObjectN/AtableFilterPatternRegex to exclude tables matching the specified pattern.ObjectN/AdatabaseFilterPatternRegex to fetch databases matching the specified pattern.ObjectN/AincludeViewsOption to include or exclude views during metadata ingestion.BooleantrueuseFqnForFilteringDetermines whether filtering is applied to the Fully Qualified Name (FQN) instead of raw names.BooleanfalsestoreSampleDataOption to enable or disable storing sample data for each table.BooleantrueenableAutoClassificationEnables automatic tagging of columns that might contain sensitive information.BooleanfalseconfidenceConfidence level for tagging columns as sensitive. Value ranges from 0 to 100.Number80sampleDataCountNumber of sample rows to ingest when Store Sample Data is enabled.Integer50

​Key Parameters Explained

​enableAutoClassification

Set this to true to enable automatic detection of sensitive columns (e.g., PII).

Applies pattern recognition and tagging based on predefined criteria.

​confidence

Confidence level for tagging sensitive columns:

A higher confidence value (e.g., 90) reduces false positives but may miss some sensitive data.

A lower confidence value (e.g., 70) identifies more sensitive columns but may result in false positives.

​storeSampleData

Controls whether sample rows are stored during ingestion.

If enabled, the specified number of rows (sampleDataCount) will be fetched for each table.

​useFqnForFiltering

When set to true, filtering patterns will be applied to the Fully Qualified Name of a table (e.g., service_name.db_name.schema_name.table_name).

When set to false, filtering applies only to raw table names.

​Auto Classification Workflow Execution

To execute the Auto Classification Workflow, follow the steps below:

​1. Install the Required Python Package

Ensure you have the correct OpenMetadata ingestion package installed, including the PII Processor module:

pip install "openmetadata-ingestion[pii-processor]"

​2. Define and Execute the Python Workflow

Instead of using a YAML configuration, use the AutoClassificationWorkflow from OpenMetadata to trigger the ingestion process programmatically.

​Sample Auto Classification Workflow yaml

source:

type: bigquery

serviceName: local_bigquery

serviceConnection:

config:

type: BigQuery

credentials:

gcpConfig:

type: service_account

projectId: my-project-id-1234

privateKeyId: privateKeyID

privateKey: "-----BEGIN PRIVATE KEY-----\nmySuperSecurePrivateKey==\n-----END PRIVATE KEY-----\n"

clientEmail: client@email.secure

clientId: "1234567890"

authUri: https://accounts.google.com/o/oauth2/auth

tokenUri: https://oauth2.googleapis.com/token

authProviderX509CertUrl: https://www.googleapis.com/oauth2/v1/certs

clientX509CertUrl: https://www.googleapis.com/oauth2/v1/certs

sourceConfig:

config:

type: AutoClassification

storeSampleData: true

enableAutoClassification: true

databaseFilterPattern:

includes:

- hello-world-1234

schemaFilterPattern:

includes:

- super_schema

tableFilterPattern:

includes:

- abc

processor:

type: "orm-profiler"

config:

tableConfig:

- fullyQualifiedName: local_bigquery.hello-world-1234.super_schema.abc

profileSample: 85

partitionConfig:

partitionQueryDuration: 180

columnConfig:

excludeColumns:

- a

- b

sink:

type: metadata-rest

config: {}

workflowConfig:

#  loggerLevel: INFO # DEBUG, INFO, WARN or ERROR

openMetadataServerConfig:

hostPort: http://localhost:8585/api

authProvider: openmetadata

securityConfig:

jwtToken: "eyJraWQiOiJHYjM4OWEtOWY3Ni1nZGpzLWE5MmotMDI0MmJrOTQzNTYiLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJhZG1pbiIsImlzQm90IjpmYWxzZSwiaXNzIjoib3Blbi1tZXRhZGF0YS5vcmciLCJpYXQiOjE2NjM5Mzg0NjIsImVtYWlsIjoiYWRtaW5Ab3Blbm1ldGFkYXRhLm9yZyJ9.tS8um_5DKu7HgzGBzS1VTA5uUjKWOCU0B_j08WXBiEC0mr0zNREkqVfwFDD-d24HlNEbrqioLsBuFRiwIWKc1m_ZlVQbG7P36RUxhuv2vbSp80FKyNM-Tj93FDzq91jsyNmsQhyNv_fNr3TXfzzSPjHt8Go0FMMP66weoKMgW2PbXlhVKwEuXUHyakLLzewm9UMeQaEiRzhiTMU3UkLXcKbYEJJvfNFcLwSl9W8JCO_l0Yj3ud-qt_nQYEZwqW6u5nfdQllN133iikV4fM5QZsMCnm8Rq1mvLR0y9bmJiD7fwM1tmJ791TUWqmKaTnP49U493VanKpUAfzIiOiIbhg"

​3. Expected Outcome

Automatically classifies and tags sensitive data based on predefined patterns and confidence levels.

Improves metadata enrichment and enhances data governance practices.

Provides visibility into sensitive data across databases.

This approach ensures that the Auto Classification Workflow is executed correctly using the appropriate OpenMetadata ingestion framework.

​Auto Classification

The Auto Classification workflow will be using the orm-profiler processor.

After running a Metadata Ingestion workflow, we can run the Auto Classification workflow.

While the serviceName will be the same to that was used in Metadata Ingestion, so the ingestion bot can get the serviceConnection details from the server.

​1. Define the YAML Config

This is a sample config for the Auto Classification Workflow:

​2. Run with the CLI

After saving the YAML config, we will run the command the same way we did for the metadata ingestion:

metadata classify -c <path-to-yaml>

Now instead of running ingest, we are using the classify command to select the Auto Classification workflow.

​Workflow Execution

​To Execute the Auto Classification Workflow:

Create a Pipeline

Configure the Auto Classification JSON as demonstrated in the provided configuration example.

Run the Ingestion Pipeline

Use OpenMetadata or an external scheduler like Argo to trigger the pipeline execution.

Validate Results

Verify the metadata and tags applied to sensitive columns in the OpenMetadata UI.

​Expected Outcomes

Automatic Tagging:

Columns containing sensitive information (e.g., names, emails, SSNs) are automatically tagged based on predefined confidence levels.

Enhanced Visibility:

Gain improved visibility and classification of sensitive data within your databases.

Sample Data Integration:

Store sample data to provide better insights during profiling and testing workflows.

Was this page helpful?YesNoSuggest editsRaise issueAdding Auto Classification Workflow through UIPreviousAuto Pii Tagging Guide | Official DocumentationNext⌘I
