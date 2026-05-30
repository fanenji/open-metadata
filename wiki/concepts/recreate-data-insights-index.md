---
type: concept
title: Recreate DataInsights DataAssets Index
created: 2026-05-14
updated: 2026-05-14
tags: [data-insights, indexing, troubleshooting, openmetadata]
related: [data-insights-application-troubleshooting, reindexing-search, backfill-configuration, openmetadata-insights]
sources: ["resolving-data-insights-and-kpi-display-issues-in--20260514.md"]
---
# Recreate DataInsights DataAssets Index

A targeted index rebuild operation specific to the Data Insights Application's data assets within OpenMetadata. It is exposed as a toggle — **Recreate DataInsights DataAssets Index** — in the Data Insights Application configuration panel.

## Distinction from General Reindexing

This operation is distinct from the general [[reindexing-search]] operation documented in the administration guide. While general reindexing rebuilds the entire Elasticsearch/OpenSearch index for all metadata entities (with nine configurable parameters and significant performance considerations), the Recreate DataInsights DataAssets Index targets only the indices used by the Data Insights Application for rendering charts, KPIs, and reports. It is an application-specific, lighter-weight operation.

## Role in Troubleshooting

Enabling this toggle is the third step in the [[data-insights-application-troubleshooting]] workflow, paired with [[backfill-configuration]]. When KPI charts do not display or the insights menu returns no results despite the application being installed and executed, a stale or corrupted Data Insights index is a probable cause. Recreating it forces a fresh index build from the underlying data.

## Production Considerations

Although lighter in scope than full reindexing, this operation still consumes computational resources and may impact Elasticsearch/OpenSearch cluster performance during execution. Administrators should schedule it during maintenance windows or low-usage periods in production environments.
