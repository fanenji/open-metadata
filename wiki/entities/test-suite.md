---
type: entity
title: Test Suite
created: 2026-05-14
updated: 2026-05-15
tags: ["data-quality", "testing", "governance", "test-suite", "openmetadata", "custom-tests", "test-case-result"]
related: ["test-definition", "test-case", "data-quality", "data-observability-alerts", "logical-test-suite", "executable-test-suite", "custom-tests", "test-case-result"]
sources: ["configure-data-quality-official-documentation---op-20260514.md", "custom-tests-openmetadata-quality-testing-guide----20260514.md"]
---

# Test Suite

A **Test Suite** (also referred to as a TestSuite) is a logical container in OpenMetadata that groups related [[test-case|Test Cases]] together. It can group test cases from different tables (Logical Test Suite) or be associated with a single table (Executable Test Suite). Test Suites are required for creating a [[test-case|TestCase]]. Their primary purpose is to consolidate test case alerts and reduce alerting overload by providing a unified view of related quality checks.

## Types of Test Suites

Test Suites come in two distinct types:

### Logical Test Suite

A Logical Test Suite is a collection of test cases that may pertain to different tables, grouped together under a single framework. It does **not** have an associated execution pipeline. Its purpose is to provide a consolidated view of related test cases for easier management and visualization without running them as a single unit.

### Executable Test Suite

An Executable Test Suite is specifically associated with a **single table** (or entity). All test cases within this suite are relevant to that particular table. The suite has an execution pipeline, allowing tests to be run directly on the associated table to verify data integrity and functionality.

#### API Endpoint

Executable Test Suites can be created via the following API endpoint:

`POST /api/v1/dataQuality/testSuites/executable`

#### Required Fields

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | Unique name for the test suite |
| `description` | string | Description of the test suite |
| `executableEntityReference` | string | Fully qualified name (FQN) of the entity to test |

#### Example

```json
{
  "name": "my_test_suite",
  "description": "Test suite for customer data",
  "executableEntityReference": "local_redshift.dev.dbt_jaffle.customers"
}
```

#### Usage Notes

- Existing test suites can be reused for multiple test cases.
- The API response includes a UUID that is required when creating a [[test-case|TestCase]].

## Relationship to Other Concepts

- A Test Suite contains multiple [[test-case|Test Cases]].
- Each Test Case references a [[test-definition|Test Definition]].
- Test Suites are designed to integrate with [[data-observability-alerts]] to reduce notification noise.
- Test Suites are a core component of the [[data-quality]] framework in OpenMetadata.
- [[custom-tests]] provide additional flexibility for custom validation logic.
- [[test-case-result]] records the outcome of a test execution.