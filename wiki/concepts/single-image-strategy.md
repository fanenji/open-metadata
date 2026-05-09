---
type: concept
title: Single Image Strategy
created: 2026-04-29
updated: 2026-04-29
tags: [kubernetes, deployment, docker, etl]
related: [kubernetes-etl-deployment-strategies, two-image-strategy, container-image-strategy-for-data-pipelines]
sources: ["GEOSCRIPTS - DEPLOY KUBERNETS.md"]
---
# Single Image Strategy

A deployment strategy for Kubernetes where one Docker image serves multiple workload types (e.g., batch scripts and a web API), differentiated only by the container command.

## How It Works

- A single Docker image contains all code and dependencies for both scripts and the API.
- For Job/CronJob pods, the container command runs the script directly (e.g., `python /app/scripts/etl.py`).
- For Deployment/Service pods, the container command starts the web server (e.g., `uvicorn main:app`).

## Trade-offs

**Pros:** Simpler image management, consistent environment, faster initial setup.

**Cons:** Larger image size, wasted dependencies in each pod, less precise resource allocation, slightly larger attack surface.

## When to Use

- Small projects or prototypes
- When code sharing overhead for two images is excessive
- During initial development phases

## Related

- [[two-image-strategy]] — The recommended alternative
- [[kubernetes-etl-deployment-strategies]] — Decision framework
- [[container-image-strategy-for-data-pipelines]] — General principles