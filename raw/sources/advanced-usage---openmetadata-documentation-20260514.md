---
type: clip
title: "Advanced Usage - OpenMetadata Documentation"
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/data-quality-observability/quality/data-quality-as-code/advanced-usage"
clipped: 2026-05-14
origin: web-clip
sources: []
tags: [web-clip]
---

# Advanced Usage - OpenMetadata Documentation

Source: https://docs.open-metadata.org/v1.12.x/how-to-guides/data-quality-observability/quality/data-quality-as-code/advanced-usage

Skip to main contentOpenMetadata Documentation home pagev1.12.xSearch...⌘KSearch...NavigationData Quality as CodeAdvanced UsageHomeQuickstartDeploymentConnectorsHow-to GuidesMCPAdmin GuideGuide for Data UsersData DiscoveryData ContractsData CollaborationData Quality and ObservabilityData Quality and ProfilerData Quality ObservabilityData LineageData InsightsData GovernanceReleasesDevelopersSDK & APIsData Quality and ObservabilityOverviewData QualityOverviewConfigure Data QualityTests - YAML ConfigColumn Tests - YAML ConfigTests - UI ConfigDimensional ValidationData Quality as CodeOverviewGetting Started with Data Quality as CodeTest RunnerDataFrame ValidationChunk-Based ValidationTest Definitions ReferenceAdvanced UsagePublishing & Best PracticesCustom TestsTest LibraryData ProfilerAlerts & NotificationsIncident ManagerOn this pageAdvanced UsageLoading Tests from YAMLBasic YAML LoadingUsing OpenMetadata Connection from YAMLYAML File StructureAdvanced TestRunner ConfigurationCustomizing Workflow BehaviorAccessing Test DefinitionsNext StepsDocumentation IndexFetch the complete documentation index at: https://docs.open-metadata.org/llms.txtUse this file to discover all available pages before exploring further.​Advanced Usage

This guide covers advanced patterns and configurations for Data Quality as Code, including loading tests from YAML files, customizing workflow configurations, and integrating with production systems.

​Loading Tests from YAML

You can load test definitions from YAML workflow files, enabling version-controlled test configurations:

​Basic YAML Loading

from metadata.sdk.data_quality import TestRunner

# Load from YAML file

runner = TestRunner.from_yaml(file_path="tests/customer_quality.yaml")

# Or from YAML string

yaml_config = """

source:

type: TestSuite

serviceName: local_postgres

sourceConfig:

config:

type: TestSuite

entityFullyQualifiedName: Postgres.warehouse.public.customers

processor:

type: orm-test-runner

config:

testCases:

- name: customer_email_not_null

testDefinitionName: columnValuesToBeNotNull

columnName: email

- name: customer_id_unique

testDefinitionName: columnValuesToBeUnique

columnName: customer_id

workflowConfig:

openMetadataServerConfig:

hostPort: http://localhost:8585/api

authProvider: openmetadata

securityConfig:

jwtToken: your-token-here

"""

runner = TestRunner.from_yaml(yaml_string=yaml_config)

# Run the loaded tests

results = runner.run()

​Using OpenMetadata Connection from YAML

By default, from_yaml() uses the connection configured via configure(). To use the connection from the YAML file:

runner = TestRunner.from_yaml(

file_path="tests/config.yaml",

use_connection_from_yaml=True

)

​YAML File Structure

A complete YAML configuration includes:

source:

type: TestSuite

serviceName: postgres_production

sourceConfig:

config:

type: TestSuite

entityFullyQualifiedName: Postgres.analytics.public.user_events

processor:

type: orm-test-runner

config:

forceUpdate: false

testCases:

# Table-level tests

- name: table_row_count_validation

testDefinitionName: tableRowCountToBeBetween

parameterValues:

- name: minValue

value: "10000"

- name: maxValue

value: "1000000"

# Column-level tests

- name: user_id_not_null

testDefinitionName: columnValuesToBeNotNull

columnName: user_id

- name: event_timestamp_format

testDefinitionName: columnValuesToMatchRegex

columnName: event_timestamp

parameterValues:

- name: regex

value: "^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}Z$"

workflowConfig:

loggerLevel: INFO

openMetadataServerConfig:

hostPort: http://localhost:8585/api

authProvider: openmetadata

securityConfig:

jwtToken: ${OPENMETADATA_JWT_TOKEN}

​Advanced TestRunner Configuration

​Customizing Workflow Behavior

from metadata.sdk.data_quality import TestRunner

from metadata.generated.schema.metadataIngestion.workflow import LogLevels

runner = TestRunner.for_table("BigQuery.analytics.events.user_sessions")

# Configure detailed settings

runner.setup(

force_test_update=True,           # Update existing test definitions

log_level=LogLevels.DEBUG,        # Enable debug logging

raise_on_error=False,             # Continue on errors

success_threshold=95,             # Require 95% success rate

enable_streamable_logs=True       # Stream logs in real-time

)

# Add tests and run

runner.add_test(TableRowCountToBeBetween(min_count=1000))

results = runner.run()

​Accessing Test Definitions

Inspect configured tests before running:

runner = TestRunner.for_table("MySQL.ecommerce.public.orders")

runner.add_tests(

TableRowCountToBeBetween(min_count=100),

ColumnValuesToBeNotNull(column="order_id")

)

# Access test definitions

for test_def in runner.test_definitions:

print(f"Test: {test_def.testDefinitionName}")

print(f"Parameters: {test_def.parameterValues}")

​Next Steps

Publishing Results & Best PracticesPublish results to OpenMetadata, implement error handling, generate tests dynamically, and apply production best practices.Was this page helpful?YesNoSuggest editsRaise issueTest Definitions ReferencePreviousPublishing Results & Best PracticesNext⌘I
