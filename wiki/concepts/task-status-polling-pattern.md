---
type: concept
title: Task Status Polling Pattern
created: 2026-05-07
updated: 2026-05-07
tags: [celery, task-status, polling, async, rest-api]
related: [celery-integration-pattern, geoscript-rest-api-architecture, fastapi-background-tasks-pattern]
sources: ["GEOSCRIPTS - REST API.md"]
---
# Task Status Polling Pattern

The task status polling pattern enables clients to check the status of an asynchronous task by polling a REST endpoint. This is used in conjunction with Celery to provide visibility into long-running script execution.

## How It Works

1. When a task is submitted to Celery, a unique `task_id` is returned to the client
2. The client can poll a status endpoint with the `task_id` to check progress
3. The endpoint uses Celery's `AsyncResult` to retrieve the current status and result

## Implementation

```python
from celery.result import AsyncResult

@app.get("/task-status/{task_id}")
async def get_task_status(task_id: str):
    task_result = AsyncResult(task_id, app=celery_app)
    return {
        "task_id": task_id,
        "status": task_result.status,  # PENDING, STARTED, SUCCESS, FAILURE, RETRY
        "result": task_result.result   # Return value or error message
    }
```

## Status Values

- **PENDING**: Task is waiting in the queue
- **STARTED**: Task is being executed by a worker
- **SUCCESS**: Task completed successfully
- **FAILURE**: Task failed with an error
- **RETRY**: Task is being retried

## Related Pages

- [[celery-integration-pattern]] — Celery setup that enables this pattern
- [[geoscript-rest-api-architecture]] — Overall architecture context