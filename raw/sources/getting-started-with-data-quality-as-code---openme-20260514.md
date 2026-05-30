---
type: clip
title: "Getting Started with Data Quality as Code - OpenMetadata Documentation"
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/data-quality-observability/quality/data-quality-as-code/getting-started"
clipped: 2026-05-14
origin: web-clip
sources: []
tags: [web-clip]
---

# Getting Started with Data Quality as Code - OpenMetadata Documentation

Source: https://docs.open-metadata.org/v1.12.x/how-to-guides/data-quality-observability/quality/data-quality-as-code/getting-started

Skip to main contentOpenMetadata Documentation home pagev1.12.xSearch...⌘KSearch...NavigationData Quality as CodeGetting Started with Data Quality as CodeHomeQuickstartDeploymentConnectorsHow-to GuidesMCPAdmin GuideGuide for Data UsersData DiscoveryData ContractsData CollaborationData Quality and ObservabilityData Quality and ProfilerData Quality ObservabilityData LineageData InsightsData GovernanceReleasesDevelopersSDK & APIsData Quality and ObservabilityOverviewData QualityOverviewConfigure Data QualityTests - YAML ConfigColumn Tests - YAML ConfigTests - UI ConfigDimensional ValidationData Quality as CodeOverviewGetting Started with Data Quality as CodeTest RunnerDataFrame ValidationChunk-Based ValidationTest Definitions ReferenceAdvanced UsagePublishing & Best PracticesCustom TestsTest LibraryData ProfilerAlerts & NotificationsIncident ManagerOn this pageGetting Started with Data Quality as CodePrerequisitesInstallationBasic InstallationInstallation with Database ConnectorsInstallation with DataFrame SupportInstallation with Multiple FeaturesAuthenticationGetting a JWT TokenOption 1: Using an Existing Bot TokenOption 2: Creating a Custom BotConfiguring the SDKUsing Environment VariablesConfiguration ParametersVerify InstallationYour First Data Quality TestCommon Installation IssuesConnection TimeoutImport ErrorsNext StepsAdditional ResourcesDocumentation IndexFetch the complete documentation index at: https://docs.open-metadata.org/llms.txtUse this file to discover all available pages before exploring further.​Getting Started with Data Quality as Code

This guide will help you install the OpenMetadata Python SDK and configure authentication to start running data quality tests programmatically.

​Prerequisites

Before you begin, ensure you have:

Python 3.10 or higher installed

pip package manager

Access to an OpenMetadata instance (version 1.11.0 or later)

A JWT token for authentication (see Authentication below)

​Installation

Install the openmetadata-ingestion package with the necessary extras for your use case:

​Basic Installation

pip install "openmetadata-ingestion>=1.12.0.0"

​Installation with Database Connectors

Install additional dependencies based on the databases you’ll be testing:

# For PostgreSQL

pip install "openmetadata-ingestion[postgres]>=1.12.0.0"

# For MySQL

pip install "openmetadata-ingestion[mysql]>=1.12.0.0"

# For BigQuery

pip install "openmetadata-ingestion[bigquery]>=1.12.0.0"

# For multiple databases

pip install "openmetadata-ingestion[postgres,mysql,bigquery]>=1.12.0.0"

​Installation with DataFrame Support

If you plan to use DataFrame validation features:

pip install "openmetadata-ingestion[pandas]>=1.12.0.0"

​Installation with Multiple Features

Combine multiple extras as needed:

# For DataFrame validation with Postgres support

pip install "openmetadata-ingestion[pandas,postgres]>=1.12.0.0"

# For comprehensive ETL support

pip install "openmetadata-ingestion[pandas,postgres,pyarrow]>=1.12.0.0"

​Authentication

Data Quality as Code requires authentication with your OpenMetadata instance. The SDK supports JWT token authentication.

​Getting a JWT Token

You can obtain a JWT token in two ways:

​Option 1: Using an Existing Bot Token

OpenMetadata provides pre-configured bots like the ingestion-bot:

Log in to your OpenMetadata instance

Navigate to Settings > Bots

Find the ingestion-bot (or create a new bot)

Copy the JWT token

​Option 2: Creating a Custom Bot

For production use, create a dedicated bot with specific permissions:

Go to Settings > Bots

Click Add Bot

Provide a name and description

Assign appropriate roles (typically DefaultBotPolicy and Ingestion Bot Policy)

Copy the generated JWT token

​Configuring the SDK

Once you have a JWT token, configure the SDK in your Python code:

from metadata.sdk import configure

configure(

host="http://localhost:8585/api",  # Your OpenMetadata API URL

jwt_token="your-jwt-token-here"

)

​Using Environment Variables

For better security, let configure pick them up from environment variables:

from metadata.sdk import configure

configure()

Set the environment variable before running your script:

export OPENMETADATA_HOST="http://localhost:8585/api"

export OPENMETADATA_JWT_TOKEN="your-jwt-token-here"

python your_script.py

​Configuration Parameters

The configure() function accepts the following parameters:

ParameterTypeRequiredDescriptionEnvironment VariablehoststrNoOpenMetadata API URL (e.g., http://localhost:8585/api)OPENMETADATA_HOSTjwt_tokenstrNoJWT authentication tokenOPENMETADATA_JWT_TOKEN

​Verify Installation

Create a simple test to verify your setup:

from metadata.sdk import configure

from metadata.sdk.data_quality import TestRunner

# Configure SDK

configure(

host="http://localhost:8585/api",

jwt_token="your-jwt-token-here"

)

# Test connection by creating a runner

try:

runner = TestRunner.for_table("your_service.database.schema.table")

print("✓ SDK configured successfully!")

except Exception as e:

print(f"✗ Configuration failed: {e}")

Replace "your_service.database.schema.table" with the fully qualified name of an actual table in your OpenMetadata instance.

​Your First Data Quality Test

Now that you’re set up, let’s run your first data quality test:

from metadata.sdk import configure

from metadata.sdk.data_quality import TestRunner, TableRowCountToBeBetween

# Configure SDK

configure(

host="http://localhost:8585/api",

jwt_token="your-jwt-token-here"

)

# Create a test runner for a specific table

runner = TestRunner.for_table("MySQL.ecommerce.public.customers")

# Add a test to verify row count is within expected range

runner.add_test(

TableRowCountToBeBetween(min_count=1000, max_count=100000)

)

# Run the tests

results = runner.run()

# Print results

for result in results:

test_case = result.testCase

test_result = result.testCaseResult

print(f"Test: {test_case.name.root}")

print(f"Status: {test_result.testCaseStatus}")

print(f"Result: {test_result.result}")

​Common Installation Issues

​Connection Timeout

If you experience connection timeouts, verify:

OpenMetadata instance is running and accessible

API URL is correct (should end with /api)

Network connectivity between your script and OpenMetadata

Firewall rules allow the connection

​Import Errors

If you encounter import errors:

ModuleNotFoundError: No module named 'metadata'

Verify the package is installed correctly:

pip list | grep openmetadata

If not listed, reinstall:

pip install --upgrade "openmetadata-ingestion>=1.12.0.0"

​Next Steps

Now that you have the SDK installed and configured:

Learn how to run table-level tests using the TestRunner API

Explore DataFrame validation for ETL pipelines

Review the complete test definitions reference

​Additional Resources

OpenMetadata Python SDK Documentation

Data Quality Overview

Authentication & Authorization

Examples and Tutorials

Was this page helpful?YesNoSuggest editsRaise issueData Quality as CodePreviousTestRunner - Running Table-Level TestsNext⌘I
