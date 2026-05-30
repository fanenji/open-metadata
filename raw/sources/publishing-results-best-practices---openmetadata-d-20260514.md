---
type: clip
title: "Publishing Results & Best Practices - OpenMetadata Documentation"
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/data-quality-observability/quality/data-quality-as-code/publishing-and-best-practices"
clipped: 2026-05-14
origin: web-clip
sources: []
tags: [web-clip]
---

# Publishing Results & Best Practices - OpenMetadata Documentation

Source: https://docs.open-metadata.org/v1.12.x/how-to-guides/data-quality-observability/quality/data-quality-as-code/publishing-and-best-practices

Skip to main contentOpenMetadata Documentation home pagev1.12.xSearch...⌘KSearch...NavigationData Quality as CodePublishing Results & Best PracticesHomeQuickstartDeploymentConnectorsHow-to GuidesMCPAdmin GuideGuide for Data UsersData DiscoveryData ContractsData CollaborationData Quality and ObservabilityData Quality and ProfilerData Quality ObservabilityData LineageData InsightsData GovernanceReleasesDevelopersSDK & APIsData Quality and ObservabilityOverviewData QualityOverviewConfigure Data QualityTests - YAML ConfigColumn Tests - YAML ConfigTests - UI ConfigDimensional ValidationData Quality as CodeOverviewGetting Started with Data Quality as CodeTest RunnerDataFrame ValidationChunk-Based ValidationTest Definitions ReferenceAdvanced UsagePublishing & Best PracticesCustom TestsTest LibraryData ProfilerAlerts & NotificationsIncident ManagerOn this pagePublishing Results & Best PracticesPublishing Results to OpenMetadataDataFrame Validation ResultsBenefits of Publishing ResultsError Handling and RetriesDynamic Test GenerationMulti-Table ValidationBest Practices SummaryNext StepsDocumentation IndexFetch the complete documentation index at: https://docs.open-metadata.org/llms.txtUse this file to discover all available pages before exploring further.​Publishing Results & Best Practices

​Publishing Results to OpenMetadata

Results can be published back to OpenMetadata for tracking, alerting, and visualization:

​DataFrame Validation Results

from metadata.sdk.data_quality.dataframes.dataframe_validator import DataFrameValidator

validator = DataFrameValidator()

validator.add_openmetadata_table_tests("Postgres.staging.public.customers")

result = validator.validate(df)

# Publish results to OpenMetadata

result.publish("Postgres.staging.public.customers")

​Benefits of Publishing Results

Historical tracking: View trends over time

Alerting: Trigger notifications on failures

Dashboards: Centralized data quality monitoring

Collaboration: Share results across teams

Compliance: Maintain audit trails

​Error Handling and Retries

Implement robust error handling:

import time

from metadata.sdk.data_quality import TestRunner

def run_with_retry(table_fqn, max_retries=3, backoff=2):

"""Run tests with exponential backoff retry"""

for attempt in range(max_retries):

try:

runner = TestRunner.for_table(table_fqn)

results = runner.run()

return results

except ConnectionError as e:

if attempt < max_retries - 1:

wait_time = backoff ** attempt

print(f"Connection failed, retrying in {wait_time}s...")

time.sleep(wait_time)

else:

print(f"Failed after {max_retries} attempts")

raise

except ValueError as e:

print(f"Configuration error: {e}")

raise  # Don't retry configuration errors

except Exception as e:

print(f"Unexpected error: {e}")

raise

# Usage

results = run_with_retry("Postgres.warehouse.public.customers")

​Dynamic Test Generation

Generate tests programmatically based on metadata:

from metadata.sdk import configure, client

from metadata.sdk.data_quality import (

TestRunner,

ColumnValuesToBeNotNull,

ColumnValuesToBeUnique

)

configure(host="http://localhost:8585/api", jwt_token="token")

# Get table metadata

om_client = client()

table = om_client.ometa.get_by_name(

entity=Table,

fqn="Postgres.warehouse.public.customers"

)

# Generate tests based on column types

runner = TestRunner.for_table(table.fullyQualifiedName.root)

for column in table.columns:

# Add NOT NULL tests for required columns

if column.constraint == "NOT NULL":

runner.add_test(ColumnValuesToBeNotNull(column=column.name.root))

# Add UNIQUE tests for primary keys

if column.constraint == "PRIMARY KEY":

runner.add_test(ColumnValuesToBeUnique(column=column.name.root))

results = runner.run()

​Multi-Table Validation

Validate multiple tables in a workflow:

from metadata.sdk.data_quality import TestRunner, TableRowCountToBeBetween

tables_to_validate = {

"Postgres.warehouse.public.customers": {"min_rows": 10000},

"Postgres.warehouse.public.orders": {"min_rows": 50000},

"Postgres.warehouse.public.products": {"min_rows": 1000}

}

validation_results = {}

for table_fqn, config in tables_to_validate.items():

runner = TestRunner.for_table(table_fqn)

runner.add_test(TableRowCountToBeBetween(min_count=config["min_rows"]))

results = runner.run()

validation_results[table_fqn] = {

"passed": all(r.testCaseResult.testCaseStatus == "Success" for r in results),

"details": results

}

# Generate summary

total_tables = len(validation_results)

passed_tables = sum(1 for v in validation_results.values() if v["passed"])

print(f"\n{'='*60}")

print(f"Validation Summary: {passed_tables}/{total_tables} tables passed")

print(f"{'='*60}")

for table_fqn, result in validation_results.items():

status = "✓" if result["passed"] else "✗"

print(f"{status} {table_fqn}")

​Best Practices Summary

Version control test configurations: Store YAML configs in git

Use environment variables: Never hardcode credentials

Implement retries: Handle transient failures gracefully

Publish results: Enable tracking and alerting in OpenMetadata

Monitor execution: Track metrics for test runs

Handle errors explicitly: Don’t silently swallow failures

Document tests: Use descriptive names and descriptions

Validate incrementally: Test early and often in pipelines

Separate concerns: Let data stewards define tests, engineers execute them

Test your tests: Ensure test definitions are correct

​Next Steps

Review the Test Definitions Reference

Learn about TestRunner

Explore DataFrame Validation

Return to Data Quality as Code Overview

Check our Examples and Tutorials out

Was this page helpful?YesNoSuggest editsRaise issueAdvanced UsagePreviousCustom Tests | OpenMetadata Quality Testing GuideNext⌘I
