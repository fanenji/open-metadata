---
type: concept
title: "Either Stacktrace Error"
created: 2026-05-30
updated: 2026-05-30
tags: []
related: []
---

type: concept
title: Either/StackTraceError Pattern
created: 2026-05-14
updated: 2026-05-14
tags: [error-handling, ingestion, python-sdk]
related: [custom-connectors, custom-connector-deployment, ingestion-framework]
sources: ["custom-connectors-build-extend-openmetadata-easily-20260514.md"]
---

# Either/StackTraceError Pattern

The `Either`/`StackTraceError` pattern is a structured error handling mechanism used in OpenMetadata's ingestion framework, particularly in custom connectors. It wraps the execution state of yielded data to ensure errors are tracked and logged rather than silently failing.

## Components

### Either

A class from `metadata.ingestion.api.models` that wraps execution state:

- `Either.right` — contains a successful `CreateEntityRequest`
- `Either.left` — contains a `StackTraceError` for failed operations

### StackTraceError

A class from `metadata.ingestion.api.models` that captures error details:

- `name` — a descriptive name for the error
- `error` — a human-readable error message
- `stack_trace` — the full Python traceback

## Usage Example

```python
from metadata.ingestion.api.models import Either, StackTraceError

try:
    1 / 0
except Exception:
    yield Either(
        left=StackTraceError(
            name="My Error",
            error="Demoing one error",
            stack_trace=traceback.format_exc(),
        )
    )

for row in self.data:
    yield Either(
        right=CreateTableRequest(...)
    )
```

## Output

Errors are logged in a summary table at the end of execution:

```
+--------+---------------+-------------------+----------------------------------------------------------+
| From   | Entity Name   | Message           | Stack Trace                                              |
+========+===============+===================+==========================================================+
| Source | My Error      | Demoing one error | Traceback (most recent call last):                       |
|        |               |                   |   File "...", line 182, in yield_data                    |
|        |               |                   |     1 / 0                                                |
|        |               |                   | ZeroDivisionError: division by zero                      |
+--------+---------------+-------------------+----------------------------------------------------------+
```

## Importance

This pattern is critical for production custom connectors. Without it, errors in the `_iter` generator would cause the entire ingestion pipeline to fail without clear diagnostics. The structured format enables both logging and potential programmatic error handling.

## Open Questions

- Does this pattern apply to built-in connectors as well, or only custom ones?
- Are there any security considerations (e.g., code injection risks) when allowing custom Python classes to be loaded?