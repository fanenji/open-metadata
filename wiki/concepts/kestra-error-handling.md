---
type: concept
title: Kestra Error Handling
created: 2026-05-08
updated: 2026-05-08
tags: [kestra, orchestration, error-handling, retries, monitoring]
related: [kestra, error-recovery-mechanisms, ci-cd-for-data-pipelines, data-observability-definition, prometheus]
sources: ["research-error-recovery-mechanisms-2026-05-08.md"]
---
# Kestra Error Handling

Kestra provides declarative, built-in error handling for the orchestration layer of modern [[elt-pattern]] pipelines.

## Key Features

- **The `errors` Property:** Defines a list of tasks to execute upon flow failure. Commonly used to trigger alerting (e.g., Slack, Email).
- **Global vs. Local Handlers:**
    - *Global:* Defined at the flow root for broad alerts and system-wide monitoring.
    - *Local:* Defined inside flowable tasks for targeted cleanup, retries, or recovery logic.
- **`allowFailure` and `allowWarning`:** Allow tasks to fail or emit warnings without failing the entire execution. Ideal for non-critical enrichment or optional cleanup steps.
- **Monitoring Integration:** Integrates with Prometheus and exposes health checks for monitoring the orchestration platform.
- **Troubleshooting Guides:** Official documentation addresses common infrastructure failures: tmp directory misconfigurations, Java startup resource consumption in Kubernetes, and Docker-in-Docker networking issues.

## Best Practices

- Use global handlers for system-wide alerts and local handlers for task-specific recovery.
- Configure retry policies for transient failures (network errors, resource contention).
- Combine with [[data-observability-definition]] tools like [[elementary-dbt-package]] to trigger recovery actions based on data quality test failures.
