---
type: concept
title: Kubernetes Jobs and CronJobs
created: 2026-03-15
updated: 2026-03-15
tags: [kubernetes, batch-processing, etl, scheduling, cron]
related: [kubernetes, kubernetes-secrets-management, kubernetes-probes, helm-for-data-platforms, kubernetes-etl-deployment-strategies, container-image-strategy-for-data-pipelines]
sources: ["Kubernetes Development on macOS Guide.md"]
---
# Kubernetes Jobs and CronJobs

Kubernetes Jobs and CronJobs are workload types for running batch processing tasks, such as ETL scripts. They are the core deployment pattern for data pipeline workloads on Kubernetes.

## Jobs

- **Purpose**: Run ETL tasks once or on demand.
- **Behavior**: Creates one or more Pods and ensures they complete successfully.
- **Restart Policy**: Set `spec.template.spec.restartPolicy` to `Never` or `OnFailure`.
- **Completion**: Job is complete when a specified number of Pods terminate successfully.
- **Backoff Limit**: `spec.backoffLimit` controls retry attempts before marking the Job as failed.

## CronJobs

- **Purpose**: Scheduled tasks (e.g., nightly data processing).
- **Schedule**: `spec.schedule` uses standard cron syntax (e.g., `"0 2 * * *"` for 2 AM daily).
- **Job Template**: `spec.jobTemplate` contains the template for Jobs the CronJob controller creates.
- **Concurrency Policy**: `spec.concurrencyPolicy` controls overlapping runs (`Allow`, `Forbid`, `Replace`). `Forbid` is often useful for ETL jobs.
- **History Limits**: `spec.successfulJobsHistoryLimit` / `spec.failedJobsHistoryLimit` control retention of completed/failed Job instances (keep low, e.g., 1-3).
- **Starting Deadline**: `spec.startingDeadlineSeconds` sets maximum time for a job to start after its scheduled time if missed.

## Example: Geospatial ETL CronJob

A typical CronJob for a nightly geospatial ETL process includes:
- Container image with GDAL/GeoPandas dependencies.
- Volume mounts for database credentials (Kubernetes Secrets).
- Resource requests/limits (memory-intensive for geospatial tasks).
- `concurrencyPolicy: Forbid` to prevent overlapping runs.
- `restartPolicy: OnFailure` for automatic retries.

## Best Practices

- Use `Forbid` concurrency policy for ETL jobs to prevent overlapping runs.
- Set appropriate resource requests and limits (geospatial tasks are memory-intensive).
- Mount database credentials as Kubernetes Secrets (volume mounts).
- Keep history limits low to avoid cluttering the cluster.
- Use `startingDeadlineSeconds` to handle missed schedules after cluster downtime.