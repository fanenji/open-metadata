---
type: source
title: Custom Tests | OpenMetadata Quality Testing Guide
created: 2026-05-14
updated: 2026-05-14
tags: [data-quality, custom-tests, testing, openmetadata]
related: [data-quality, custom-tests, test-definition, test-suite, test-case, test-case-result, ingestion-framework]
sources: ["custom-tests-openmetadata-quality-testing-guide----20260514.md"]
authors: [OpenMetadata]
year: 2026
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/data-quality-observability/quality/custom-tests"
venue: "OpenMetadata Documentation"
---

# Custom Tests | OpenMetadata Quality Testing Guide

This official guide explains how to extend OpenMetadata's data quality testing with custom tests. It covers two pathways: an API-only approach for writing results from external test tools, and a UI-executable approach using the Python SDK and namespace packages.

## Key Content

- **Step 1: Creating a TestDefinition** — POST to `/api/v1/dataQuality/testDefinitions` with description, entityType (TABLE or COLUMN), name, testPlatforms, and parameterDefinition.
- **Step 2: Creating a TestSuite** — POST to `/api/v1/dataQuality/testSuites/executable` with name, description, and executableEntityReference.
- **Step 3: Creating a TestCase** — POST to `/api/v1/dataQuality/testCases` with entityLink, testDefinition reference, testSuite reference, and parameterValues.
- **Step 4: Writing TestCaseResults** — PUT to `/api/v1/dataQuality/testCases/{testFQN}/testCaseResult` with result, testCaseStatus, timestamp, and testResultValue.
- **Step 5: Making Custom Tests UI-Executable** — Requires a namespace package under `metadata/data_quality/validations/table/sqlalchemy/` or `column/sqlalchemy/`, a class inheriting from `BaseTestValidator` (optionally `SQAValidatorMixin`), and `pip install` of the package.

## Key Requirements

- The `testPlatforms` field must include `OpenMetadata` for UI execution.
- The Python file name must match the TestDefinition name.
- Every `__init__.py` in the namespace package must include `__path__ = __import__('pkgutil').extend_path(__path__, __name__)`.
- The validator class must implement `run_validation()` returning a `TestCaseResult` object.

## Connections

- Directly extends the [[data-quality]] concept with custom test creation.
- Uses the [[ingestion-framework]] Python SDK.
- Introduces the [[custom-tests]], [[test-definition]], [[test-suite]], [[test-case]], and [[test-case-result]] entities.