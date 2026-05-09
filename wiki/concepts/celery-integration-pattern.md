---
type: concept
title: Celery Integration Pattern
created: 2026-05-07
updated: 2026-05-07
tags: [celery, distributed-tasks, task-queue, redis, async, rest-api]
related: [fastapi-background-tasks-pattern, geoscript-rest-api-architecture, fastapi, redis, subprocess-execution-pattern, task-status-polling-pattern, email-notification-pattern]
sources: ["GEOSCRIPTS - REST API.md"]
---
# Celery Integration Pattern

Celery is a distributed task queue system that provides robust, scalable background task execution for data pipeline workloads. In the context of geospatial ETL, Celery is used to execute long-running Python scripts (`ora_to_pg.py`, `load_postgis.py`) with reliability, monitoring, and scalability guarantees.

## Architecture Components

1. **Broker (Redis)**: Receives task requests from FastAPI and queues them for workers
2. **Worker**: Separate processes that consume tasks from the queue and execute them
3. **Result Backend (Redis)**: Stores task results and status for retrieval
4. **FastAPI Application**: Submits tasks to Celery and exposes status endpoints

## Implementation

### Celery Worker Configuration

```python
from celery import Celery
import subprocess
import os

CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379/0")
CELERY_RESULT_BACKEND = os.environ.get("CELERY_RESULT_BACKEND", "redis://localhost:6379/0")

celery_app = Celery("tasks", broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)

@celery_app.task(name="run_script_task")
def run_script_task(script_path: str, *args):
    run_script_path = "/srv/geoscript/run"
    command = f"{run_script_path} {script_path}"
    if args:
        command += " " + " ".join(shlex.quote(str(arg)) for arg in args)
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if process.returncode == 0:
        return {"status": "success", "output": stdout.decode()}
    else:
        return {"status": "error", "error": stderr.decode()}
```

### FastAPI Endpoint

```python
@app.post("/run-script-celery/{script_name}", status_code=202)
async def trigger_script_celery(script_name: str):
    scripts_available = {
        "ora_to_pg": "dp/ora_to_pg.py",
        "load_postgis": "rqa/load_postgis.py"
    }
    script_path = scripts_available.get(script_name)
    if not script_path:
        return {"message": "Invalid script"}
    task = run_script_task.delay(script_path)
    return {"message": f"Task for '{script_name}' submitted.", "task_id": task.id}
```

### Task Status Polling

```python
@app.get("/task-status/{task_id}")
async def get_task_status(task_id: str):
    task_result = AsyncResult(task_id, app=celery_app)
    return {
        "task_id": task_id,
        "status": task_result.status,
        "result": task_result.result
    }
```

## Advantages Over BackgroundTasks

- **Scalability**: Multiple workers can run on different machines
- **Reliability**: Automatic retry on transient failures
- **Separation**: Worker crashes don't affect the FastAPI application
- **Monitoring**: Tools like Flower provide queue and worker visibility
- **Scheduling**: Celery Beat enables periodic task execution

## Operational Requirements

- Redis (or RabbitMQ) must be running as the message broker
- Celery workers must be started as separate processes
- Flower can be deployed for monitoring

## Related Pages

- [[fastapi-background-tasks-pattern]] — Simpler alternative for lightweight use cases
- [[geoscript-rest-api-architecture]] — Overall architecture context
- [[subprocess-execution-pattern]] — The underlying subprocess execution mechanism
- [[task-status-polling-pattern]] — Pattern for checking Celery task status
- [[email-notification-pattern]] — Email notification on task completion