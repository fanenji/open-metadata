---
type: source
title: "Source: data-quality-openmetadata-quality-management-guide-20260514.md"
created: 2026-05-15
updated: 2026-05-15
sources: ["data-quality-openmetadata-quality-management-guide-20260514.md"]
tags: []
related: []
---

# Source: data-quality-openmetadata-quality-management-guide-20260514.md

## Analysis of: Data Quality | OpenMetadata Quality Management Guide

### Key Entities

| Name | Type | Role | In Wiki? |
|------|------|------|----------|
| OpenMetadata | Platform | Central | Yes ([[openmetadata]]) |
| Database Connectors | Component | Peripheral (supporting) | Yes ([[openmetadata-connectors]]) |
| Data Quality Workflows | Feature | Central | Yes ([[data-quality]]) |
| Alerting System | Feature | Peripheral | Yes ([[data-observability-alerts]]) |
| Health Dashboard | Feature | Peripheral | No |
| Incident Manager | Feature | Peripheral | No (mentioned in sidebar) |
| Data Profiler | Feature | Peripheral | Yes ([[data-profiling]]) |
| Test Library | Feature | Peripheral | No |

### Key Concepts

| Name | Definition | Importance | In Wiki? |
|------|------------|------------|----------|
| **Data Quality Tests** | Assertions run at table and column levels to verify data completeness, freshness, and accuracy | Core mechanism for data quality monitoring | Yes ([[data-quality]]) |
| **No-Code Test Cases** | UI-based test creation without writing code | Key differentiator for non-technical users | No |
| **YAML Config Tests** | Test configuration via YAML files | Alternative for automation/CI | No |
| **Custom Tests** | User-defined data quality tests | Extensibility feature | No |
| **Resolution Workflow** | Process to inform data consumers about test resolutions | Collaboration feature | No |
| **Dimensional Validation** | Validation across multiple dimensions | Advanced quality concept | No |

### Main Arguments & Findings

**Core Claims:**
1. OpenMetadata enables building trust in data through monitoring completeness, freshness, and accuracy
2. Data quality tests work across all supported database connectors
3. The system is extensible to adapt to organizational needs

**Evidence:**
- Reference to video demonstrations (not analyzed)
- Listing of four key workflow components (native tests, alerting, health dashboard, resolution workflow)
- Mention of table and column level testing capabilities

**Strength of Evidence:** Weak — this is a high-level overview/landing page with no technical depth, benchmarks, or case studies. It functions as a navigation hub to deeper documentation.

### Connections to Existing Wiki

**Directly Related Pages:**
- [[data-quality]] — This source is the official documentation for this concept
- [[data-profiling]] — Mentioned as related feature
- [[data-observability-alerts]] — Alerting system is a component
- [[openmetadata-connectors]] — Tests work across all connectors

**Extends Existing Knowledge:**
- Introduces the concept of "Resolution Workflow" not currently documented
- Mentions "Incident Manager" as a sidebar feature not in wiki
- References "Dimensional Validation" as a specific approach

### Contradictions & Tensions

- **No contradictions** with existing wiki content — this is a high-level overview that doesn't provide detailed technical specifications that could conflict
- **Internal tension
