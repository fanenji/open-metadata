---
type: concept
title: Data Incident Management
created: 2026-05-06
updated: 2026-05-06
tags: [data-observability, incident-management, lineage, alerting]
related: [data-root-cause-analysis, full-data-stack-observability, data-observability-three-pillars, data-observability-definition]
sources: ["Data Quality Monitoring is dead. Say Hello to Full Data Stack Observability.md"]
---
# Data Incident Management

Data incident management is the process of assessing the impact of data anomalies and coordinating response across stakeholders. It is a key application of [[full-data-stack-observability]], enabled by the combination of anomaly detection and [[data-observability-three-pillars|lineage]].

When an anomaly is detected, incident management involves:
- **Impact assessment** — Determining which dashboards, charts, ML models, or downstream consumers are affected.
- **Stakeholder notification** — Alerting relevant data consumers and teams whose workflows may be impacted.
- **Root cause analysis** — Tracing upstream dependencies to identify the origin of the issue (see [[data-root-cause-analysis]]).
- **Post-mortem analysis** — Learning from incidents to shift from firefighting to fire prevention.

Lineage with column-level detail is essential for effective incident management, as it provides the context needed to understand the blast radius of a data issue.
