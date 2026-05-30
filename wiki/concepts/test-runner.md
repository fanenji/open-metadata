---
type: concept
title: TestRunner
created: 2026-05-14
updated: 2026-05-14
tags: [data-quality, execution, pipeline]
related: [data-quality, metadata-sdk-data-quality, dataframe-validation]
sources: ["test-definitions-reference---openmetadata-document-20260514.md"]
---
# TestRunner

`TestRunner` is the component that executes data quality test definitions against data sources. It is the next step after defining tests using the [[metadata-sdk-data-quality]] module.

## Overview

While the [[metadata-sdk-data-quality]] module provides the test definitions (the *what* to validate), `TestRunner` provides the execution mechanism (the *how* to run them). It takes test definitions and applies them to actual data, returning pass/fail results.

## Usage

```python
from metadata.sdk.data_quality import ColumnValuesToBeNotNull
from metadata.sdk.data_quality import TestRunner

test = ColumnValuesToBeNotNull(column="email")
runner = TestRunner()
result = runner.run(test)
```

## Related

- [[data-quality]] — The overarching data quality concept
- [[dataframe-validation]] — Applying tests to in-memory DataFrames
- [[metadata-sdk-data-quality]] — The module providing test definitions