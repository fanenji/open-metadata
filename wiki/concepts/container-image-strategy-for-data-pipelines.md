---
type: concept
title: Container Image Strategy for Data Pipelines
created: 2026-02-13
updated: 2026-02-13
tags: [docker, container, data-pipelines, devops, security]
related: [kubernetes-etl-deployment-strategies, elt-pattern, data-ingestion-architectural-patterns, kubernetes]
sources: ["Deploy ETL in Kubernetes_ Strategie_ .md"]
---
# Container Image Strategy for Data Pipelines

Design principles and best practices for building Docker images for data pipeline workloads, covering the trade-offs between monolithic and focused images.

## Core Principles

### Single Responsibility Principle for Containers
Each container should focus on one task. For data pipelines, this means separating:
- **Batch execution images** — Contain only the runtime and libraries needed to run scripts.
- **Service images** — Contain the runtime, web framework, and API-specific dependencies.

### Separation of Concerns
Decoupling batch and service workloads into distinct images allows:
- Independent evolution of each component.
- Targeted security scanning and patching.
- Different base images optimized for each workload type.

### Image Size Optimization
Smaller images provide:
- Reduced attack surface (fewer packages, less code).
- Faster deployment and scaling.
- Lower storage costs in registries and node storage.
- Reduced network transfer time during pod startup.

### Resource Allocation Granularity
Different workloads benefit from independently tuned resource profiles:
- **Bursty batch jobs:** High CPU/memory for short durations.
- **Steady API services:** Moderate resources with horizontal scaling.

## Decision Framework

| Factor | Single Image | Separate Images |
|--------|-------------|-----------------|
| Complexity | Low | Higher |
| Resource efficiency | Lower | Higher |
| Security posture | Weaker | Stronger |
| Maintainability | Simpler initially | Better long-term |
| Shared code management | Trivial | Requires strategy |

## Security Considerations

- Removing web server code from batch images reduces the theoretical attack surface if a Job pod is compromised.
- Smaller images have fewer CVEs to track and patch.
- Separate images allow different security scanning policies for batch vs. service workloads.

## Relationship to Data Architecture

Container image strategy is an operational concern that supports [[elt-pattern]] and [[data-ingestion-architectural-patterns]] by providing the infrastructure for reliable, efficient pipeline execution.