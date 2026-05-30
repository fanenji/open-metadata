---
type: concept
title: BaseTestValidator
created: 2026-05-14
updated: 2026-05-14
tags: [data-quality, testing, python-sdk, openmetadata]
related: [custom-tests, test-definition, test-case, test-case-result, ingestion-framework]
sources: ["custom-tests-openmetadata-quality-testing-guide----20260514.md"]
---

# BaseTestValidator

`BaseTestValidator` is the base Python class for implementing custom test logic in OpenMetadata's UI-executable pathway. Custom test classes must inherit from this class and implement the `run_validation()` method.

## Usage

```python
from metadata.data_quality.validations.base_test_handler import BaseTestValidator

class MyCustomTestValidator(BaseTestValidator):
    """Implements custom test validator for OpenMetadata."""

    def run_validation(self) -> TestCaseResult:
        """Run test validation and return a TestCaseResult."""
        # Custom logic here
        pass
```

## SQAValidatorMixin

For SQLAlchemy sources, the `SQAValidatorMixin` can be used alongside `BaseTestValidator` to gain access to additional out-of-the-box methods.

## Key Requirements

- The class name must follow the pattern `<YourTest>Validator` where `<YourTest>` matches the TestDefinition name.
- The `run_validation()` method must return a [[test-case-result|TestCaseResult]] object.
- The Python file must be placed in the correct namespace package directory.

## Related

- [[custom-tests]] — Overview of the custom test creation process.
- [[test-definition]] — The schema/definition of a custom test.
- [[test-case]] — A specific instance of a test definition applied to an entity.
- [[test-case-result]] — The result/status of a test execution.
- [[ingestion-framework]] — The Python SDK used for custom test creation.