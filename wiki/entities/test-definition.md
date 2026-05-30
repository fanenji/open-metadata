---
type: entity
title: Test Definition
created: 2026-05-14
updated: 2026-05-15
tags: ["data-quality", "testing", "template", "test-definition", "openmetadata", "custom-tests"]
related: [test-case, test-suite, data-quality, custom-tests, test-case-result]
sources: ["configure-data-quality-official-documentation---op-20260514.md", "custom-tests-openmetadata-quality-testing-guide----20260514.md"]
---
# Test Definition

A **Test Definition** (also referred to as `TestDefinition` in the API) is a generic template in OpenMetadata that specifies the structural elements of a quality check. It describes the test's metadata, including its name, description, entity type (`TABLE` or `COLUMN`), supported platforms, and parameters. Test Definitions serve as reusable templates from which specific [[test-case|Test Cases]] are created. One Test Definition can be linked to multiple Test Cases, each with its own pass/fail conditions.

## Structure / Fields

A Test Definition is defined by the following fields:

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | Unique name for the test definition. Must match the Python file name for UI‑executable tests. |
| `description` | string | Description of the test. |
| `entityType` | string | `TABLE` or `COLUMN` — indicates whether the test is applied at the table or column level. For column-level tests, the target column is specified as a parameter. |
| `testPlatforms` | array | Platforms that support the test: `OpenMetadata`, `GreatExpectations`, `dbt`, `Deequ`, `Soda`, `Other`. |
| `parameterDefinition` | array | List of parameter objects, each with a `name` field. Parameters typically include the column name (for column‑level tests) and optionally the expected data type. |

## API Endpoint

`POST /api/v1/dataQuality/testDefinitions`

## Important Notes

- The `name` must match the Python file name for UI‑executable tests.
- For UI execution, `testPlatforms` must include `OpenMetadata`.
- The response includes a UUID that is required when creating a [[test-case|TestCase]].

## Relationship to Other Concepts

- A Test Definition is instantiated by one or more [[test-case|Test Cases]].
- Test Cases belong to a [[test-suite|Test Suite]].
- Test Definitions are a foundational component of the [[data-quality]] framework.
- For custom tests, see [[custom-tests]].
- Test execution results are represented by [[test-case-result]].

## Example

```json
{
  "description": "A demo custom test",
  "entityType": "TABLE",
  "name": "demo_test_definition",
  "testPlatforms": ["Soda", "dbt"],
  "parameterDefinition": [{"name": "ColumnOne"}]
}
```