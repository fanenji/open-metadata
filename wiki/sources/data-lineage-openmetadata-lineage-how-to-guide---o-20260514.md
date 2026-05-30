---
type: source
title: "Source: data-lineage-openmetadata-lineage-how-to-guide---o-20260514.md"
created: 2026-05-15
updated: 2026-05-15
sources: ["data-lineage-openmetadata-lineage-how-to-guide---o-20260514.md"]
tags: []
related: []
---

# Source: data-lineage-openmetadata-lineage-how-to-guide---o-20260514.md

## Analysis of: Data Lineage | OpenMetadata Lineage How-To Guide

### Key Entities

| Name | Type | Role | In Wiki? |
|------|------|------|----------|
| OpenMetadata | Platform | Central (the system being documented) | Yes |
| Snowflake | Data Warehouse | Peripheral (example source) | Yes |
| Metabase | Dashboard Service | Peripheral (example source) | Yes |
| Python SDK | Tool | Peripheral (programmatic lineage creation) | Yes (implied via code-layout) |

### Key Concepts

| Name | Definition | Why It Matters | In Wiki? |
|------|------------|----------------|----------|
| **Data Lineage** | Tracking how data moves through organizational systems, showing transformations and usage | Core feature for traceability and impact analysis | Yes ([[data-lineage]]) |
| **Lineage Workflow** | Configured ingestion pipeline that automatically extracts lineage from sources | Primary method for lineage population | Partially (implied in [[metadata-ingestion-workflow]]) |
| **Column-Level Lineage** | Granular lineage showing transformations at the column level | Enables detailed impact analysis and debugging | No (only general lineage exists) |
| **Manual Lineage** | User-driven editing of table and column-level lineage relationships | Allows correction and enrichment of auto-extracted lineage | No |
| **Dashboard Lineage** | Traceability from dashboards/charts back to underlying database tables | Connects BI layer to data sources | Yes ([[dashboard-lineage]]) |

### Main Arguments & Findings

- **Core claim**: OpenMetadata provides comprehensive lineage tracking across Database, Dashboard, and Pipeline assets.
- **Supported capabilities**: Automatic extraction from data warehouses (Snowflake) and dashboards (Metabase), programmatic creation via Python SDK, and manual editing.
- **Evidence strength**: This is official documentation — authoritative but introductory. No technical depth, performance data, or troubleshooting guidance is provided.

### Connections to Existing Wiki

- **Strengthens**: [[data-lineage]] — provides official categorization (Database, Dashboard, Pipeline) and confirms the lineage workflow configuration from UI.
- **Extends**: [[dashboard-lineage]] — confirms dashboard lineage as a supported category.
- **Related but not directly linked**: [[metadata-ingestion-workflow]], [[dbt-lineage-ingestion]], [[stored-procedure-lineage]], [[data-profiling]], [[data-quality]].

### Contradictions & Tensions

- **No contradictions** with existing wiki content.
- **Internal tension**: The page lists four sub-topics (Lineage Workflow, Explore Lineage, Column-Level Lineage, Manual Lineage) but provides no detail on any of them — it's purely a navigation index. This creates a gap between the claimed feature set and the documented depth.

### Recommendations

**Pages to create:**
1. **[[lineage-workflow]]** — Dedicated page covering the UI-based lineage workflow configuration, including source selection, scheduling, and troubleshooting.
2. **[[column-level
