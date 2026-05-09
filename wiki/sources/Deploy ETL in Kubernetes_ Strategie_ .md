---
type: source
title: "Deploy ETL in Kubernetes: Strategies"
created: 2026-02-13
updated: 2026-02-13
tags: [kubernetes, etl, devops, container-strategy]
related: [kubernetes-etl-deployment-strategies, container-image-strategy-for-data-pipelines, elt-pattern, data-ingestion-architectural-patterns]
sources: ["Deploy ETL in Kubernetes_ Strategie_ .md"]
---
# Deploy ETL in Kubernetes: Strategies

A Gemini conversation analyzing deployment strategies for an ETL system in Kubernetes. The system runs both Python scripts (batch) and a FastAPI application (service) from a shared codebase. The analysis compares two approaches: a single Docker image used for both Jobs/CronJobs and Services, versus two separate images optimized for each workload type.

**Key recommendation:** Two separate images is the best practice for production systems, aligned with Kubernetes principles of focused containers, resource efficiency, and independent scalability. The single-image approach is acceptable for small projects or prototyping.

**Topics covered:**
- Single Responsibility Principle for containers
- Separation of concerns between batch and API workloads
- Image size optimization and attack surface reduction
- Resource allocation granularity for bursty jobs vs. steady services
- Shared code management strategies (internal Python packages, shared directories)
- Trade-offs between simplicity and long-term maintainability