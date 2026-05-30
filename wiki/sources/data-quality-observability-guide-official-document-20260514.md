---
type: source
title: "Source: data-quality-observability-guide-official-document-20260514.md"
created: 2026-05-15
updated: 2026-05-15
sources: ["data-quality-observability-guide-official-document-20260514.md"]
tags: []
related: []
---

# Source: data-quality-observability-guide-official-document-20260514.md

## Analysis of: Data Quality Observability Guide

### Key Entities

| Name | Type | Role | In Wiki? |
|------|------|------|----------|
| OpenMetadata | Platform | Central — the system providing the observability features | Yes ([[openmetadata]]) |
| Data Quality | Feature | Central — core capability for setting up quality tests, alerting, triage, and incident resolution | Yes ([[data-quality]]) |
| Data Profiler | Feature | Central — profiling setup for observability | Yes ([[data-profiling]]) |
| Alerts & Notifications | Feature | Central — observability alert configuration | Yes ([[data-observability-alerts]]) |
| Incident Manager | Feature | Central — incident management within OpenMetadata | No |
| Anomaly Detection | Feature | Central — automated incident management for faster resolution | No |

### Key Concepts

| Name | Definition | Why It Matters | In Wiki? |
|------|------------|----------------|----------|
| Data Quality Observability | Unified approach combining quality tests, observability metrics, incident management, and root cause analysis | Core value proposition — positions OpenMetadata as a unified solution for discovery, governance, and observability | No (as a combined concept) |
| No Code Tests | Quality tests that can be set up without writing code | Lowers barrier to entry for data quality monitoring | No (as a named concept) |
| Root Cause Analysis | Feature for identifying the underlying cause of data issues | Differentiator — mentioned as an OpenMetadata feature for incident resolution | No |
| Real-time Monitoring | Continuous monitoring of data flows and quality in real-time | Ensures data reliability and trustworthiness | No (as a named concept) |

### Main Arguments & Findings

- **Core Claim:** OpenMetadata provides a simple, easy-to-use, unified solution for data quality and observability that combines discovery, governance, and observability in one platform.
- **Supporting Evidence:** The page lists four sub-areas (Data Quality, Data Profiler, Alerts & Notifications, Incident Manager) and mentions Anomaly Detection as an automated feature.
- **Evidence Strength:** Weak — this is a high-level overview/index page with no technical depth, implementation details, or case studies. It functions as a navigation hub to deeper documentation.

### Connections to Existing Wiki

- **Strengthens:** The existing [[data-quality]], [[data-profiling]], and [[data-observability-alerts]] pages by providing a higher-level framing of how these features work together.
- **Extends:** Introduces the concept of "Data Quality Observability" as a unified category, which is not currently captured in the wiki.
- **New Entities:** Incident Manager and Anomaly Detection are not yet documented in the wiki.

### Contradictions & Tensions

- **Internal Tension:** The page mentions "root cause analysis (OpenMetadata feature)" but the Incident Manager page (linked) may or may not fully deliver this. The parenthetical suggests it's a distinguishing 
