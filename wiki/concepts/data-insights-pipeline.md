---
type: concept
title: Data Insights Pipeline
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, data-insights, pipeline, analytics]
related: [service-insights, openmetadata-insights, backfill-configuration, recreate-data-insights-index, data-insights-application-troubleshooting]
sources: ["service-insights-overview-official-documentation---20260514.md"]
---
# Data Insights Pipeline

The Data Insights Pipeline is a core pipeline in OpenMetadata that processes and populates all Data Insights charts, including the per-service charts in [[service-insights|Service Insights]]. It is a prerequisite for most Service Insights charts.

## Purpose

The Data Insights Pipeline aggregates metadata from various sources and computes the metrics displayed in the Data Insights report and Service Insights charts. Without successful execution of this pipeline, most Service Insights charts will show no data.

## Prerequisite Charts

The following Service Insights charts require the Data Insights Pipeline:
- [[service-insights|Description Coverage]]
- [[service-insights|PII Coverage]]
- [[service-insights|Tier Coverage]]
- [[service-insights|Ownership Coverage]]
- [[service-insights|Data Quality]]

The following Service Insights tables require the Data Insights Application (which includes the Data Insights Pipeline):
- [[service-insights|Generated Data with OpenMetadata AI]]
- [[service-insights|PII Distribution]]
- [[service-insights|Tier Distribution]]

## Troubleshooting

If Service Insights charts show no data, verify that the Data Insights Pipeline has been executed successfully. See [[data-insights-application-troubleshooting]] for general troubleshooting steps, including [[backfill-configuration]] and [[recreate-data-insights-index]].