---
type: concept
title: FastAPI Background Tasks Pattern
created: 2026-05-07
updated: 2026-05-07
tags: [fastapi, background-tasks, async, rest-api, subprocess]
related: [fastapi, celery-integration-pattern, geoscript-rest-api-architecture, legacy-geospatial-etl-pipeline, subprocess-execution-pattern]
sources: ["GEOSCRIPTS - REST API.md"]
---
# FastAPI Background Tasks Pattern

The FastAPI BackgroundTasks pattern enables non-blocking execution of long-running operations after an HTTP response has been returned to the client. In the context of geospatial ETL, this pattern is used to execute Python scripts (`ora_to_pg.py`, `load_postgis.py`) without blocking the API endpoint.

## How It Works

1. The endpoint receives a request and immediately returns a response (e.g., `{"message": "Script execution started"}`)
2. FastAPI registers a background task function via `background_tasks.add_task()`
3. After the response is sent, FastAPI executes the registered function in a background thread
4. The background function uses `subprocess.Popen` to launch the actual script as a separate process
5. `process.communicate()` waits for the script to complete within the background thread

## Implementation Example

```python
from fastapi import FastAPI, BackgroundTasks
import subprocess

app = FastAPI()

def run_script_in_background(script_path: str):
    command = f"/srv/geoscript/run {script_path}"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    # Handle output and errors

@app.post("/run-script/{script_name}")
async def trigger_script(script_name: str, background_tasks: BackgroundTasks):
    scripts_available = {
        "ora_to_pg": "dp/ora_to_pg.py",
        "load_postgis": "rqa/load_postgis.py"
    }
    script_path = scripts_available.get(script_name)
    if not script_path:
        return {"message": "Invalid script"}
    background_tasks.add_task(run_script_in_background, script_path)
    return {"message": f"Script '{script_name}' started in background"}
```

## Limitations

- **Thread blocking**: BackgroundTasks run in the same process, so a long-running task blocks the worker thread
- **No retry mechanism**: Failed tasks are not automatically retried
- **No monitoring**: No built-in task status tracking or monitoring
- **No scalability**: Cannot distribute tasks across multiple workers or machines

## When to Use

- Short-lived background operations (seconds to minutes)
- Simple use cases where infrastructure overhead is not justified
- Development and testing environments

## Security Considerations

The source explicitly warns about path traversal vulnerabilities. Script names should be validated against a hardcoded dictionary rather than resolved dynamically from user input.

## Related Pages

- [[celery-integration-pattern]] — More robust alternative for production use
- [[geoscript-rest-api-architecture]] — Overall architecture context
- [[subprocess-execution-pattern]] — The underlying subprocess execution mechanism