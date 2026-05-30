---
type: entity
title: "Failure Mode"
created: 2026-05-30
updated: 2026-05-30
tags: []
related: []
---

type: entity
title: FailureMode
created: 2026-05-14
updated: 2026-05-14
tags: [sdk, python, data-quality, validation]
related: [dataframe-validator, dataframe-chunk-based-validation, data-quality]
sources: ["dataframe-chunk-based-validation---openmetadata-do-20260514.md"]
---
# FailureMode

`FailureMode` is an enum in the OpenMetadata Python SDK (`metadata.sdk.data_quality.dataframes`) that controls the behavior of [[dataframe-validator]] when a validation test fails.

## Supported Values

- **`SHORT_CIRCUIT`** (default) — Stop validation on the first test failure. In chunk-based processing, this stops processing additional chunks.

## Usage

```python
from metadata.sdk.data_quality.dataframes import FailureMode

result = validator.run(
    data_chunks,
    on_success=load_chunk,
    on_failure=rollback,
    mode=FailureMode.SHORT_CIRCUIT
)
```

## Limitations

As of SDK v1.11.0.0, only `SHORT_CIRCUIT` is supported. Future versions are expected to add additional modes such as reporting failing rows or skipping failing batches.

## Connections

- Used by [[dataframe-validator]] methods `validate()` and `run()`.
- Relevant to [[dataframe-chunk-based-validation]] for controlling chunk processing behavior.