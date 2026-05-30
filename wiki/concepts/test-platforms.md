---
type: concept
title: Test Platforms
created: 2026-05-14
updated: 2026-05-14
tags: [data-quality, test-library, openmetadata]
related: [test-library, custom-sql-test-definitions, data-quality]
sources: ["test-library-custom-sql-based-data-quality-tests---20260514.md"]
---
# Test Platforms

The Test Platforms field is a required configuration when creating a custom test definition in the [[test-library|Test Library]]. It specifies which execution environments can run the test.

## Critical Distinction

- **OpenMetadata**: Selecting this platform means the test will be executed natively by OpenMetadata's data quality engine. This is the only option that triggers automatic execution.
- **dbt, Soda, GreatExpectations**: These platforms are for **tracking results only**. Selecting them does not cause OpenMetadata to execute the test in those tools. Users must run the tests externally and then import or report results back to OpenMetadata.

## Implications

- If you want the test to run automatically as part of OpenMetadata's data quality workflow, you **must** include "OpenMetadata" in the Test Platforms field.
- Tests configured with external platforms only are intended for organizations that already use dbt, Soda, or GreatExpectations and want to centralize result tracking in OpenMetadata.
- Multiple platforms can be selected simultaneously.

## Usage

When creating a test definition, the Test Platforms field appears in the configuration form alongside Name, Description, Entity Type, SQL Expression, Supported Data Sources, and Parameters.