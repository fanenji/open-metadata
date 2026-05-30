---
type: entity
title: Test Library
created: 2026-05-14
updated: 2026-05-14
tags: [data-quality, test-library, openmetadata]
related: [custom-sql-test-definitions, test-platforms, data-quality, data-profiling]
sources: ["test-library-custom-sql-based-data-quality-tests---20260514.md"]
---
# Test Library

The Test Library is an OpenMetadata feature accessible to administrators through the Observability menu (Observability > Test Library). It enables the creation of reusable, parameterized SQL-based data quality test definitions without writing custom code. The Test Library supports both table-level and column-level validations, dynamic parameter resolution, and the ability to enable/disable test definitions to control their availability.

## Key Features

- **SQL-Based Test Definitions**: Write custom validation logic using SQL queries.
- **Dynamic Parameters**: Use reserved parameters (`{{ table_name }}`, `{{ column_name }}`) and user-defined parameters that are resolved at runtime.
- **Reusable Tests**: Create test definitions once and apply them across multiple tables and columns.
- **Enable/Disable**: Control which test definitions are available for creating new test cases. Disabled definitions do not affect existing test cases.
- **Test Platforms**: Select the execution platform (OpenMetadata, dbt, Soda, GreatExpectations). Only "OpenMetadata" triggers native execution; other platforms are for tracking results from external frameworks.

## Accessing the Test Library

Navigate to **Observability > Test Library** in the OpenMetadata UI. This page is restricted to administrators.

## Creating a Custom Test Definition

1. Click **Add Test Definition**.
2. Configure fields: Name (required), Description (required), Entity Type (TABLE or COLUMN), SQL Expression (required), Supported Data Sources, Test Platforms (required), Parameters (optional).
3. Write the SQL expression following the fail-on-rows semantics: the test fails if the query returns one or more rows; an empty result set means the test passes.
4. Define user-defined parameters (if any) by clicking **Add Parameter** and entering the parameter name and optional description.
5. Select supported data sources to ensure SQL syntax compatibility.
6. Click **Save**.

## Managing Test Definitions

- **Edit**: Click on a test definition row to open the edit form.
- **Enable/Disable**: Use the toggle switch to control availability. Disabled definitions are hidden from the test case creation flow but existing test cases continue to work.
- **Delete**: Click the delete icon. A test definition cannot be deleted if it has associated test cases.

## Using Custom Test Definitions

Once created, custom test definitions appear in the test case creation flow. To create a test case:

1. Navigate to the table or column.
2. Go to the **Data Quality** tab.
3. Click **Add Test**.
4. Select the custom test definition.
5. Provide values for user-defined parameters.
6. Save the test case.

The test executes as part of the data quality workflow, with the SQL expression evaluated using the actual table/column names and parameter values.

## Permissions

| Action | Required Role |
|--------|---------------|
| View Test Library | Admin |
| Create Test Definition | Admin |
| Edit Test Definition | Admin |
| Delete Test Definition | Admin |
| Enable/Disable Test Definition | Admin |

Regular users can use enabled test definitions when creating test cases but cannot modify the definitions themselves.

## Best Practices

- **Return failing rows**: Structure queries to return rows that fail validation. Empty result = pass.
- **Be specific**: Write targeted queries checking one condition.
- **Consider performance**: Use appropriate WHERE clauses; avoid full table scans.
- **Test your SQL**: Validate manually before creating the test definition.
- **Naming conventions**: Use descriptive names (e.g., `columnValuesInRange`, `noOrphanedRecords`).
- **Documentation**: Provide clear descriptions and examples of expected parameter values.