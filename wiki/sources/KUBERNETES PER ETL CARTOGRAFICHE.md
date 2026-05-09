---
type: source
title: "Source: KUBERNETES PER ETL CARTOGRAFICHE.md"
created: 2026-05-07
updated: 2026-05-07
sources: ["KUBERNETES PER ETL CARTOGRAFICHE.md"]
tags: []
related: []
---

# Source: KUBERNETES PER ETL CARTOGRAFICHE.md

# Structured Analysis: KUBERNETES PER ETL CARTOGRAFICHE.md

## Key Entities

| Name | Type | Role | In Wiki? |
|------|------|------|----------|
| Orbstack | Tool/Platform | Central — proposed local Kubernetes environment for Mac | No |
| Kubernetes | Platform | Central — target deployment environment | Yes ([[kubernetes]]) |
| FastAPI | Framework | Central — API service layer for ETL scripts | Yes ([[fastapi]]) |
| Python/DuckDB/GeoPandas/GDAL | Stack | Central — ETL script technology stack | Partial ([[duckdb]] exists) |
| Airflow/Prefect | Orchestration | Central — workflow orchestration | No |
| Oracle/PostGIS | Database | Peripheral — remote data sources | Partial ([[oracle-to-postgresql-gdal-etl]]) |
| k3s | Kubernetes Distribution | Implicit — Orbstack's underlying K8s engine | No |
| Job/CronJob | Kubernetes Resource | Central — execution pattern for ETL scripts | No |
| Service/Ingress | Kubernetes Resource | Central — API exposure pattern | No |

## Key Concepts

| Concept | Definition | Importance | In Wiki? |
|---------|------------|------------|----------|
| Job/CronJob execution pattern | Running containerized scripts as Kubernetes Jobs (one-off) or CronJobs (scheduled) rather than interactive exec | Core architectural decision for ETL deployment | No |
| Service/Ingress exposure pattern | Exposing FastAPI endpoints via Kubernetes Service (internal) and Ingress (external) | Core architectural decision for API deployment | No |
| Local K8s development environment | Running a lightweight Kubernetes cluster locally for development/testing | Central to the document's purpose | No |

## Main Arguments & Findings

1. **Core Claims:**
   - Kubernetes Jobs/CronJobs are the correct execution model for ETL scripts, not interactive container exec
   - FastAPI endpoints should be exposed via Kubernetes Service (internal) and Ingress (external)
   - Orbstack provides a k3s-based Kubernetes environment suitable for local development on Mac

2. **Evidence:**
   - Document is prescriptive/opinion-based, not empirical
   - References standard Kubernetes patterns (Job, CronJob, Service, Ingress)
   - Links to a Gemini conversation for further context

3. **Strength of Evidence:**
   - Low — document is a brief architectural recommendation, not a rigorous analysis
   - No benchmarks, comparisons, or real-world validation

## Connections to Existing Wiki

- **Strengthens:** [[kubernetes-etl-deployment-strategies]] — provides concrete execution patterns (Job/CronJob) and exposure patterns (Service/Ingress) for the containerized ETL approach
- **Extends:** [[fastapi]] — adds Kubernetes-specific deployment guidance
- **Related but not directly linked:** [[container-image-strategy-for-data-pipelines]], [[legacy-geospatial-etl-pipeline]]

## Contradictions & Tensions

- **Internal tension:** The document recommends Jobs/CronJobs for automated execution but acknowledges `kubectl exec` for interactive use — no guidance on when to use which in a development wo
