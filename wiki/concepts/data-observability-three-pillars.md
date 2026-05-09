---
type: concept
title: Data Observability Three Pillars
created: 2026-05-06
updated: 2026-05-06
tags: [data-observability, framework, metrics, metadata, lineage]
related: [data-observability-definition, full-data-stack-observability, data-incident-management, data-root-cause-analysis]
sources: ["Data Quality Monitoring is dead. Say Hello to Full Data Stack Observability.md"]
---
# Data Observability Three Pillars

The three pillars of data observability are a framework adapted from software observability's Metrics, Traces, and Logs. They are designed to capture the critical aspects of data engineering workflows:

1. **Metrics** — Measure the quality of data, including freshness/timeliness, completeness/volume, duplication, schema changes, and accuracy.
2. **Metadata** — Access to data about the data, providing context about structure, provenance, and pipeline status.
3. **Lineage** — Knowledge of dependencies between data assets, enabling root cause analysis (upstream tracing) and impact assessment (downstream dependencies).

These pillars form the foundation of [[full-data-stack-observability]] and distinguish data observability from software observability. They complement the seven dimensions of [[data-observability-definition]] (freshness, security, redundancy, discrepancy, documentation, quality, lineage) by providing a higher-level structural framework.
