---
type: concept
title: Subprocess Execution Pattern
created: 2026-05-07
updated: 2026-05-07
tags: [subprocess, python, script-execution, etl, geospatial]
related: [fastapi-background-tasks-pattern, celery-integration-pattern, geoscript-rest-api-architecture, legacy-geospatial-etl-pipeline]
sources: ["GEOSCRIPTS - REST API.md"]
---
# Subprocess Execution Pattern

The subprocess execution pattern involves using Python's `subprocess.Popen` to launch external scripts from within a web service. This pattern bridges existing Python scripts with a REST API layer without requiring script refactoring.

## How It Works

1. The FastAPI endpoint receives a request with a script name and optional arguments
2. The script name is mapped to a secure path via a hardcoded dictionary
3. A command is constructed using the `/srv/geoscript/run` shell script to ensure the correct virtual environment
4. `subprocess.Popen` launches the command as a separate process
5. `process.communicate()` waits for completion and captures stdout/stderr

## Example

```python
command = f"/srv/geoscript/run dp/ora_to_pg.py --id 56"
process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = process.communicate()
```

## Advantages

- **No script refactoring**: Existing scripts work without modification
- **Environment isolation**: Scripts run in their own process with the correct virtual environment
- **Familiar pattern**: Simple and well-understood

## Disadvantages

- **Architectural debt**: Scripts were not designed for programmatic reuse
- **No direct error propagation**: Errors are captured as strings, not exceptions
- **Security risks**: Shell injection and path traversal vulnerabilities must be carefully mitigated
- **Resource management**: Each subprocess consumes system resources

## Security Considerations

- Always validate script names against a hardcoded dictionary
- Use `shlex.quote()` for argument quoting to prevent shell injection
- Avoid constructing commands from user input directly

## Related Pages

- [[fastapi-background-tasks-pattern]] — Uses subprocess in background tasks
- [[celery-integration-pattern]] — Uses subprocess in Celery tasks
- [[geoscript-rest-api-architecture]] — Overall architecture context