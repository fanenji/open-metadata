---
type: clip
title: "DataFrame Chunk-Based Validation - OpenMetadata Documentation"
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/data-quality-observability/quality/data-quality-as-code/dataframe-validation-chunking"
clipped: 2026-05-14
origin: web-clip
sources: []
tags: [web-clip]
---

# DataFrame Chunk-Based Validation - OpenMetadata Documentation

Source: https://docs.open-metadata.org/v1.12.x/how-to-guides/data-quality-observability/quality/data-quality-as-code/dataframe-validation-chunking

Skip to main contentOpenMetadata Documentation home pagev1.12.xSearch...⌘KSearch...NavigationData Quality as CodeDataFrame Chunk-Based ValidationHomeQuickstartDeploymentConnectorsHow-to GuidesMCPAdmin GuideGuide for Data UsersData DiscoveryData ContractsData CollaborationData Quality and ObservabilityData Quality and ProfilerData Quality ObservabilityData LineageData InsightsData GovernanceReleasesDevelopersSDK & APIsData Quality and ObservabilityOverviewData QualityOverviewConfigure Data QualityTests - YAML ConfigColumn Tests - YAML ConfigTests - UI ConfigDimensional ValidationData Quality as CodeOverviewGetting Started with Data Quality as CodeTest RunnerDataFrame ValidationChunk-Based ValidationTest Definitions ReferenceAdvanced UsagePublishing & Best PracticesCustom TestsTest LibraryData ProfilerAlerts & NotificationsIncident ManagerOn this pageChunk-Based ValidationMethod 1: Manual Chunk ValidationMethod 2: Using the run() MethodTransaction-Safe Chunk ProcessingFailure ModesWorking with Validation ResultsAccessing Test ResultsMerging Results from Multiple ChunksPublishing Results to OpenMetadataImportant Considerations for Chunk-Based ValidationTests That Require Full TableRecommended ApproachBest PracticesError HandlingNext StepsDocumentation IndexFetch the complete documentation index at: https://docs.open-metadata.org/llms.txtUse this file to discover all available pages before exploring further.​Chunk-Based Validation

For large datasets that don’t fit in memory, validate data in chunks:

​Method 1: Manual Chunk Validation

import pandas as pd

from metadata.sdk.data_quality.dataframes.dataframe_validator import DataFrameValidator, ValidationResult

validator = DataFrameValidator()

validator.add_openmetadata_table_tests("Postgres.warehouse.staging.transactions")

results = []

# Process file in chunks

for chunk in pd.read_csv("large_file.csv", chunksize=10000):

# Validate chunk

result = validator.validate(chunk)

results.append(result)

# Load if valid, otherwise stop

if result.success:

load_chunk_to_database(chunk)

else:

print(f"Validation failed on chunk")

rollback_all_chunks()

break

# Merge all results

final_result = ValidationResult.merge(*results)

# Publish aggregated results

final_result.publish("Postgres.warehouse.staging.transactions")

​Method 2: Using the run() Method

The run() method provides a cleaner approach with automatic chunk handling:

from metadata.sdk.data_quality.dataframes.dataframe_validator import DataFrameValidator

import pandas as pd

from sqlalchemy import create_engine, Table, MetaData, insert, delete

# Configure validator

validator = DataFrameValidator()

validator.add_openmetadata_table_tests("Postgres.warehouse.staging.orders")

# Setup database connection

engine = create_engine("postgresql://user:pass@localhost/warehouse")

# Define success and failure handlers

def load_chunk(df, validation_result):

"""Load validated chunk to database"""

with engine.connect() as conn:

table = Table("orders", MetaData(), autoload_with=conn)

conn.execute(insert(table).values(), df.to_dict(orient="records"))

def handle_failure(df, validation_result):

"""Rollback on validation failure"""

with engine.connect() as conn:

table = Table("orders", MetaData(), autoload_with=conn)

conn.execute(delete(table))

print(f"Validation failed: {validation_result}")

# Run validation on chunks

result = validator.run(

pd.read_csv("orders.csv", chunksize=5000),

on_success=load_chunk,

on_failure=handle_failure

)

# Publish results

if result.success:

print("✓ All chunks validated and loaded successfully")

else:

print("✗ Validation failed - transaction rolled back")

result.publish("Postgres.warehouse.staging.orders")

​Transaction-Safe Chunk Processing

Use a context manager to ensure atomic transactions:

from metadata.sdk.data_quality.dataframes.dataframe_validator import DataFrameValidator

import pandas as pd

from sqlalchemy import create_engine, MetaData, Table, insert

class DatabaseSession:

def __init__(self, connection_string, table_name):

self.engine = create_engine(connection_string)

self.table_name = table_name

self._conn = None

def __enter__(self):

self._conn = self.engine.connect()

self._trans = self._conn.begin()

self.table = Table(self.table_name, MetaData(), autoload_with=self._conn)

return self

def __exit__(self, exc_type, exc_val, exc_tb):

if exc_type is not None:

self._trans.rollback()

else:

self._trans.commit()

self._conn.close()

def load_chunk(self, df, validation_result):

"""Load chunk to database"""

self._conn.execute(

insert(self.table).values(),

df.to_dict(orient="records")

)

def rollback(self, df, validation_result):

"""Rollback transaction"""

self._trans.rollback()

# Use in validation workflow

validator = DataFrameValidator()

validator.add_openmetadata_table_tests("Postgres.warehouse.staging.sales")

with DatabaseSession("postgresql://user:pass@localhost/warehouse", "sales") as session:

result = validator.run(

pd.read_csv("sales_data.csv", chunksize=10000),

on_success=session.load_chunk,

on_failure=session.rollback

)

print(f"Validation {'succeeded' if result.success else 'failed'}")

​Failure Modes

As of version 1.11.0.0 of the SDK, DataFrameValidator supports only one failure mode: short circuit.

from metadata.sdk.data_quality.dataframes import FailureMode

# SHORT_CIRCUIT (default): Stop on first test failure

result = validator.validate(df, mode=FailureMode.SHORT_CIRCUIT)

# In chunk-based processing, SHORT_CIRCUIT stops processing additional chunks

result = validator.run(

data_chunks,

on_success=load_chunk,

on_failure=rollback,

mode=FailureMode.SHORT_CIRCUIT  # Stop on first failed chunk

)

Future versions will include additional modes to report back failing rows or skipping failing batches.

​Working with Validation Results

​Accessing Test Results

result = validator.validate(df)

# Check overall success

if result.success:

print("All tests passed")

# Iterate through individual test results

for test_case, test_result in result.test_cases_and_results:

print(f"Test: {test_case.name.root}")

print(f"Status: {test_result.testCaseStatus}")

print(f"Details: {test_result.result}")

​Merging Results from Multiple Chunks

from metadata.sdk.data_quality.dataframes import ValidationResult

results = []

for chunk in data_chunks:

result = validator.validate(chunk)

results.append(result)

# Merge all chunk results

merged_result = ValidationResult.merge(*results)

# Merged result contains aggregated information

print(f"Overall success: {merged_result.success}")

​Publishing Results to OpenMetadata

After validation, publish results back to OpenMetadata for tracking and alerting:

result = validator.validate(df)

# Publish results to OpenMetadata

result.publish("Postgres.warehouse.staging.customer_data")

This enables:

Historical tracking of data quality trends

Alerting on validation failures

Visualization in OpenMetadata UI

Centralized data quality reporting

​Important Considerations for Chunk-Based Validation

When using chunk-based validation, be aware of tests that require the full dataset:

​Tests That Require Full Table

Some tests analyze the entire dataset and may produce incorrect results when run on chunks:

TableRowCountToBeBetween: Counts rows in each chunk, not the full dataset

TableRowCountToEqual: Validates chunk size, not full dataset size

ColumnValuesSumToBeBetween: Sums values per chunk, not across all data

The SDK will issue a warning when such tests are detected:

WholeTableTestsWarning: Running tests that require the whole table on chunks

could lead to false positives. For example, a DataFrame with 200 rows split

in chunks of 50 could pass tests expecting DataFrames to contain max 100 rows.

The following tests could have unexpected results:

- tableRowCountToBeBetween

- columnValuesSumToBeBetween

​Recommended Approach

For datasets that don’t fit in memory and require full-table tests:

Use TestRunner to validate after loading

Focus DataFrame validation on column-level tests that do not require aggregation

Split validation into two phases:

During ETL: Validate column-level quality with DataFrameValidator

After loading: Validate table-level metrics with TestRunner

Example two-phase approach:

# Phase 1: Validate chunks during ETL (column-level only)

chunk_validator = DataFrameValidator()

chunk_validator.add_tests(

ColumnValuesToBeNotNull(column="id"),

ColumnValuesToBeUnique(column="id"),

ColumnValuesToBeBetween(column="amount", min_value=0)

)

result = chunk_validator.run(

pd.read_csv("data.csv", chunksize=10000),

on_success=load_chunk,

on_failure=rollback

)

# Phase 2: Validate table metrics after loading (table-level)

if result.success:

from metadata.sdk.data_quality import TestRunner

table_validator = TestRunner.for_table("Postgres.warehouse.staging.transactions")

table_validator.add_tests(

TableRowCountToBeBetween(min_count=10000),

ColumnValuesSumToBeBetween(column="amount", min_value=1000000)

)

# Automatically publishes results for table tests only

table_results = table_validator.run()

​Best Practices

Validate before loading: Catch issues before contaminating your warehouse

result = validator.validate(transformed_df)

if result.success:

load_to_warehouse(df)

Use transactional chunk processing: Ensure atomic all-or-nothing behavior

with database_transaction():

result = validator.run(chunks, on_success=load, on_failure=rollback)

Leverage OpenMetadata tests: Let data stewards define quality criteria

validator.add_openmetadata_table_tests("Table.FQN")

Publish results: Enable tracking and alerting

result.publish("Table.FQN")

Handle failures gracefully: Don’t silently fail

if not result.success:

alert_team()

rollback_transaction()

raise DataQualityError(result)

Use appropriate tests for chunks: Avoid full-table tests when processing chunks

​Error Handling

Handle validation errors appropriately:

from metadata.sdk.data_quality.dataframes.dataframe_validator import DataFrameValidator

try:

validator = DataFrameValidator()

validator.add_openmetadata_table_tests("Postgres.warehouse.staging.orders")

result = validator.validate(df)

if not result.success:

# Handle validation failure

log_validation_failures(result)

raise ValueError("Data quality checks failed")

except ValueError as e:

print(f"Configuration error: {e}")

# Table not found in OpenMetadata

except Exception as e:

print(f"Validation error: {e}")

# Other errors during validation

​Next Steps

Review the Test Definitions Reference for all available tests

Learn about TestRunner for validating tables after loading

Explore Advanced Usage patterns and configurations

Was this page helpful?YesNoSuggest editsRaise issueDataFrame ValidationPreviousTest Definitions ReferenceNext⌘I
