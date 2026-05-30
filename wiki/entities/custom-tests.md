---
type: entity
title: Custom Tests
created: 2026-05-14
updated: 2026-05-14
tags: [data-quality, testing, custom-tests, openmetadata]
related: [data-quality, test-definition, test-suite, test-case, test-case-result, ingestion-framework, base-test-validator]
sources: ["custom-tests-openmetadata-quality-testing-guide----20260514.md"]
---

# Custom Tests

Custom Tests are user-defined data quality tests that extend OpenMetadata's built-in test library. They allow organizations to implement quality rules specific to their data and domain.

## Two Pathways

1. **API-only**: Create a [[test-definition|TestDefinition]], [[test-suite|TestSuite]], and [[test-case|TestCase]] via the REST API, then write [[test-case-result|TestCaseResults]] directly. This pathway is for external test tools (Soda, dbt, Great Expectations, etc.) and does not require Python packaging.

2. **UI-executable**: Same API steps plus a Python namespace package containing a validator class. The test becomes available in the OpenMetadata UI for scheduling and execution. Requires `testPlatforms` to include `OpenMetadata`.

## Workflow Summary

1. Create a [[test-definition|TestDefinition]] via `POST /api/v1/dataQuality/testDefinitions`.
2. Create a [[test-suite|TestSuite]] via `POST /api/v1/dataQuality/testSuites/executable`.
3. Create a [[test-case|TestCase]] via `POST /api/v1/dataQuality/testCases`.
4. (Optional) Write [[test-case-result|TestCaseResults]] via `PUT /api/v1/dataQuality/testCases/{testFQN}/testCaseResult`.
5. (Optional) Create a namespace package with a [[base-test-validator|BaseTestValidator]] subclass and `pip install` it.

## Key Requirements for UI-Executable Tests

- The Python file name must match the TestDefinition `name`.
- The namespace package structure: `metadata/data_quality/validations/{table|column}/sqlalchemy/<yourTest>.py`.
- Every `__init__.py` must include `__path__ = __import__('pkgutil').extend_path(__path__, __name__)`.
- The validator class must inherit from `BaseTestValidator` and implement `run_validation()` returning a `TestCaseResult`.

## Related

- [[data-quality]] — The overarching concept of data quality in OpenMetadata.
- [[test-definition]] — The schema/definition of a custom test.
- [[test-suite]] — A logical grouping of test cases.
- [[test-case]] — A specific instance of a test definition applied to an entity.
- [[test-case-result]] — The result/status of a test execution.
- [[base-test-validator]] — The base Python class for custom test logic.
- [[ingestion-framework]] — The Python SDK used for custom test creation.