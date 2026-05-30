---
type: entity
title: Test Case
created: 2026-05-14
updated: 2026-05-15
tags: ["data-quality", "testing", "condition", "test-case", "openmetadata"]
related: ["test-definition", "test-suite", "data-quality", "custom-tests", "test-case-result"]
sources:
  - "configure-data-quality-official-documentation---op-20260514.md"
  - "custom-tests-openmetadata-quality-testing-guide----20260514.md"
---

# Test Case

A **Test Case** is a specific instance of a [[test-definition|Test Definition]] applied to a table or column entity in OpenMetadata. It defines a concrete condition that the Test Definition must meet to be considered successful, making it the runnable unit of data quality testing. For example, a Test Case might define `max=n` as the pass/fail threshold for a column value test.

## Relationship to Other Concepts

- **[[test-definition|Test Definition]]**: A Test Case instantiates a Test Definition with specific pass/fail criteria. Each Test Case is linked to exactly one Test Definition, but a single Test Definition can be reused across multiple Test Cases with different parameters.
- **[[test-suite|Test Suite]]**: Test Cases are grouped into Test Suites for consolidated management and alerting.
- **[[data-quality]]**: Test Cases are the executable unit within the data quality framework.
- **[[custom-tests]]**: Custom tests follow the same Test Case model, enabling user‑defined validation logic.
- **[[test-case-result]]**: The result or status of a test execution is captured as a TestCaseResult.

## API Endpoint

`POST /api/v1/dataQuality/testCases`

## Required Fields

| Field | Type | Description |
|-------|------|-------------|
| `entityLink` | string | Link to the entity: `<#E::table::fqn>` or `<#E::table::fqn::columns::column name>` |
| `name` | string | Unique name for the test case |
| `testDefinition` | object | Reference to the TestDefinition (FQN or id + type) |
| `testSuite` | object | Reference to the TestSuite (FQN or id + type) |
| `parameterValues` | array | List of parameter objects with `name` and `value` |

## Important Notes

- The `entityLink` must include the starting and ending `<>` characters.
- For column-level tests, use the `::columns::column name` suffix.
- The response includes a UUID required for writing [[test-case-result|TestCaseResults]].

## Example

```json
{
  "entityLink": "<#E::table::local_redshift.dev.dbt_jaffle.customers>",
  "name": "custom_test_Case",
  "testDefinition": {
    "id": "1f3ce6f5-67be-45db-8314-2ee42d73239f",
    "type": "testDefinition"
  },
  "testSuite": {
    "id": "3192ed9b-5907-475d-a623-1b3a1ef4a2f6",
    "type": "testSuite"
  },
  "parameterValues": [
    {"name": "colName", "value": 10}
  ]
}
```