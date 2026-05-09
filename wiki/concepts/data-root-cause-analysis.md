---
type: concept
title: Data Root Cause Analysis
created: 2026-05-06
updated: 2026-05-06
tags: [data-observability, lineage, troubleshooting, root-cause-analysis]
related: [data-incident-management, full-data-stack-observability, data-observability-three-pillars]
sources: ["Data Quality Monitoring is dead. Say Hello to Full Data Stack Observability.md"]
---
# Data Root Cause Analysis

Data root cause analysis (RCA) is the process of tracing upstream dependencies to identify the origin of a data issue. It is a core application of [[full-data-stack-observability]], enabled by [[data-observability-three-pillars|lineage]].

A comprehensive lineage model shows upstream dependencies — including source applications, jobs, orchestrators, and transformations — that produce an anomalous data asset. This allows data engineers to quickly pinpoint where a problem originated rather than manually tracing through complex pipelines.

Effective RCA requires lineage that extends beyond the warehouse to include ingestion pipelines, transformation jobs, and orchestration tools. This enables teams to resolve issues before they impact business decisions, dashboards, or reports.
