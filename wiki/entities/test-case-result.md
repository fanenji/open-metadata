---
type: entity
title: TestCaseResult
created: 2026-05-14
updated: 2026-05-14
tags: [data-quality, testing, test-case-result, openmetadata]
related: [custom-tests, test-definition, test-suite, test-case, data-quality]
sources: ["custom-tests-openmetadata-quality-testing-guide----20260514.md"]
---

# TestCaseResult

A TestCaseResult represents the outcome of a [[test-case|TestCase]] execution in OpenMetadata. It is written via the API and is visible in the Test Suite or on the table entity page.

## API Endpoint

`PUT /api/v1/dataQuality/testCases/{testFQN}/testCaseResult`

## Required Fields

| Field | Type | Description |
|-------|------|-------------|
| `result` | string | Result message describing the outcome |
| `testCaseStatus` | string | One of: `Success`, `Failed`, `Aborted` |
| `timestamp` | integer | Unix timestamp in milliseconds |
| `testResultValue` | array | List of result value objects with `value` field |

## Example

```json
{
  "result": "found 1 values expected n",
  "testCaseStatus": "Success",
  "timestamp": 1662129151000,
  "testResultValue": [{"value": "10"}]
}
```

## Notes

- Writing TestCaseResults is optional if the test is executed through the OpenMetadata UI (the UI writes results automatically).
- This endpoint is primarily for the API-only pathway where external test tools write their results.

## Related

- [[custom-tests]] — Overview of the custom test creation process.
- [[test-definition]] — The schema/definition of a custom test.
- [[test-suite]] — Container for test cases.
- [[test-case]] — A specific instance of a test definition applied to an entity.