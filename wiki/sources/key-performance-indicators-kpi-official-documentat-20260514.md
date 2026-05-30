---
type: source
title: "Source: key-performance-indicators-kpi-official-documentat-20260514.md"
created: 2026-05-15
updated: 2026-05-15
sources: ["key-performance-indicators-kpi-official-documentat-20260514.md"]
tags: []
related: []
---

# Source: key-performance-indicators-kpi-official-documentat-20260514.md

## Analysis of: Key Performance Indicators (KPI) | Official Documentation - OpenMetadata Documentation

### Key Entities

- **Admin** (Role) — Central actor; only Admins can define KPIs. Already exists in wiki ([[openmetadata-administration]]).
- **OpenMetadata** (Platform) — The system where KPIs are defined and tracked. Already exists in wiki ([[openmetadata]]).
- **Data Assets** (Entity) — The objects being measured (tables, topics, etc.). Already exists in wiki ([[data-asset-ownership]]).
- **Data Insights** (Feature) — The subsystem that powers KPI tracking and reporting. Already exists in wiki ([[openmetadata-insights]], [[data-insights-application-troubleshooting]]).

### Key Concepts

- **Key Performance Indicators (KPI)** — Measurable goals (Completed Description, Completed Ownership) set by Admins to track documentation, ownership, and tiering coverage of data assets. Central to the source.
- **KPI Categories** — Two supported types: Completed Description (description coverage) and Completed Ownership (ownership coverage). Both can be absolute (number) or relative (percentage). Core concept.
- **Metric Type** — Choice between Percentage or Number for KPI targets. Important for goal configuration.
- **Data Insights Report** — The output/report that provides a quick glance of coverage metrics. Already exists in wiki ([[data-insights-application-troubleshooting]]).

### Main Arguments & Findings

- **Core Claim:** KPIs enable organizations to decentralize documentation and ownership by setting measurable, time-bound goals.
- **Evidence:** The source describes the UI workflow for adding KPIs (chart selection, metric type, start/end date, description) and the line graph visualization showing daily progress, days left, and current coverage.
- **Evidence Strength:** Low — this is official documentation describing a feature, not empirical research. No data on effectiveness or adoption.

### Connections to Existing Wiki

- **Strengthens:** [[openmetadata-insights]] — KPIs are a core component of Data Insights.
- **Extends:** [[data-asset-ownership]] and [[classification-tags]] — KPIs measure ownership and description coverage, providing a governance feedback loop.
- **Related:** [[tiers]] — Tiering is mentioned as a KPI target alongside documentation and ownership.
- **Related:** [[data-steward-role]] — The Data Steward role is likely the primary actor responsible for meeting KPI targets.

### Contradictions & Tensions

- **Missing KPI Category:** The source mentions "Completed Description" and "Completed Ownership" but does not include "Completed Tiering" despite the introductory paragraph stating KPIs target "documentation, ownership, and tiering." This is either an omission in the documentation or a feature gap.
- **No Tiering KPI:** The "KPI Categories" section lists only two categories, contradicting the three mentioned in the introduction. This is a significant internal tension.

### Recommendations

- **Create New Page:** [[kpi-categories
