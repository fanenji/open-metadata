---
type: entity
title: Data Asset Details Page
created: 2026-05-14
updated: 2026-05-14
tags: [ui, data-discovery, openmetadata]
related: [data-lineage, data-profiling, data-quality, custom-properties, activity-feed, announcements, glossary-terms, classification-tags, schema-tab, sample-data-tab, queries-tab, data-observability-tab, lineage-tab, custom-properties-tab, config-tab, details-tab, executions-tab, features-tab, children-tab]
sources: ["detailed-view-of-the-data-assets---openmetadata-do-20260514.md"]
---

# Data Asset Details Page

The data asset details page is the primary UI view for inspecting a single data asset in OpenMetadata. It aggregates all metadata, lineage, quality, and collaboration features into a single page organized by tabs.

## Top Panel

The top panel displays:
- **Source** — The service or connector from which the asset was ingested.
- **Owner** — The Team or User responsible for the asset.
- **Tier** — Importance classification (Tier 1–5).
- **Type** — The asset type (Table, Topic, Dashboard, Pipeline, ML Model, Container).
- **Usage** — Usage frequency or popularity metrics.
- **Description** — A textual description of the asset.

## Top-Right Controls

- **Tasks** — Circular icon showing the number of open tasks.
- **Version History** — Clock icon showing major/minor version changes.
- **Follow** — Star icon showing the number of followers.
- **Share** — Link sharing capability.
- **Announcements** — Accessible via the ⋮ menu.
- **Rename** — Accessible via the ⋮ menu.
- **Delete** — Accessible via the ⋮ menu.

## Tab-Based Organization

The details page is divided into tabs whose availability depends on the asset type. The following table summarizes which tabs are available for each asset type:

| Tab | Table | Topic | Dashboard | Pipeline | ML Model | Container |
|-----|-------|-------|-----------|----------|----------|-----------|
| Schema | ✓ | ✓ | | | | ✓ |
| Activity Feeds & Tasks | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Sample Data | ✓ | ✓ | | | | |
| Queries | ✓ | | | | | |
| Data Observability | ✓ | | | | | |
| Lineage | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Custom Properties | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Config | | ✓ | | | | |
| Details | | | ✓ | | ✓ | |
| Executions | | | | ✓ | | |
| Features | | | | | ✓ | |
| Children | | | | | | ✓ |

## Tab Descriptions

- **Schema Tab** — Displays columns, types, descriptions, tags, glossary terms, and frequently joined tables. Available for Tables, Topics, and Containers.
- **Activity Feeds & Tasks Tab** — Shows all tasks and mentions for the asset. Available for all asset types.
- **Sample Data Tab** — Shows ingested sample data. Available for Tables and Topics.
- **Queries Tab** — Shows SQL queries run against the table, including duration and usage by other tables. Users can add new queries. Available for Tables only.
- **Data Observability Tab** — Contains three sub-tabs: Table Profile, Column Profile, and Data Quality. Available for Tables only.
- **Lineage Tab** — Shows end-to-end lineage at table and column levels, with configurable upstream/downstream layers and a no-code manual lineage editor. Available for all asset types.
- **Custom Properties Tab** — Allows viewing and editing custom property values. Available for all asset types.
- **Config Tab** — Shows topic configuration. Available for Topics only.
- **Details Tab** — For Dashboards: chart name, type, description, and tags. For ML Models: Hyper Parameters and Model Store details.
- **Executions Tab** — Shows pipeline execution status (Success, Failure, Pending, Aborted) as a chronological list or tree, with filtering by status and date. Available for Pipelines only.
- **Features Tab** — Shows ML Model features with type, algorithm, description, sources, glossary terms, and tags. Available for ML Models only.
- **Children Tab** — Shows container contents. Available for Containers only.

## Related Pages

- [[data-lineage]] — End-to-end lineage traceability and manual editing.
- [[data-profiling]] — Table and column profiling in the Data Observability tab.
- [[data-quality]] — Data quality tests in the Data Observability tab.
- [[custom-properties]] — Extending metadata models with custom attributes.
- [[activity-feed]] — Activity feeds and tasks on asset details pages.
- [[announcements]] — Creating announcements from the details page.
- [[glossary-terms]] — Business metadata displayed in Schema and Features tabs.
- [[classification-tags]] — Tags displayed in Schema, Details, and Features tabs.