---
type: entity
title: Service Insights
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, data-insights, analytics, service]
related: [openmetadata-insights, data-insights-pipeline, metadata-ingestion-workflow, auto-classification, auto-tiering-pipeline, data-quality, usage-pipeline, openmetadata-ai-application, data-insights-application-troubleshooting]
sources: ["service-insights-overview-official-documentation---20260514.md"]
---
# Service Insights

Service Insights is a UI tab within OpenMetadata that displays per-service analytics. Unlike the global [[openmetadata-insights|Data Insights]] report, which provides an overview of the entire data estate, Service Insights scopes its analytics to individual services (e.g., a specific database service, dashboard service, or messaging service).

## Available Charts and Tables

Service Insights provides 11 charts and tables, each with specific prerequisite pipelines:

### Total Data Assets
Displays the total number of data assets within a service, categorized by asset type (e.g., tables, databases, schemas, stored procedures for a database service). Requires successful execution of the [[metadata-ingestion-workflow|Metadata Ingestion Pipeline]].

### Description Coverage
Shows the percentage of data assets with a populated description field. Requires both the Metadata Ingestion Pipeline and the [[data-insights-pipeline|Data Insights Pipeline]].

### PII Coverage
Displays the percentage of data assets containing columns tagged with PII tags. Requires both the [[auto-classification|Auto Classification Pipeline]] and the Data Insights Pipeline.

### Tier Coverage
Shows the percentage of data assets with a populated tier classification. Requires both the [[auto-tiering-pipeline|Auto Tiering Pipeline]] and the Data Insights Pipeline.

### Ownership Coverage
Displays the percentage of data assets with a populated owner field. Requires both the Metadata Ingestion Pipeline and the Data Insights Pipeline.

### Generated Data with OpenMetadata AI (OpenMetadata Only)
A table showing a breakdown of metadata populated by the OpenMetadata AI agent versus metadata populated manually. Requires the Auto Classification Pipeline, Auto Data Quality (DQ) Pipeline, Auto Tiering Pipeline, [[openmetadata-ai-application|OpenMetadata AI Application]], and Data Insights Application.

### PII Distribution
A table showing a breakdown of data assets categorized by their associated PII tags. Requires both the Auto Classification Pipeline and the Data Insights Application.

### Tier Distribution
A table showing a breakdown of data assets based on their assigned Tier classification. Requires both the Auto Tiering Pipeline and the Data Insights Application.

### Most Used Data Assets
Displays the top five most frequently accessed data assets, determined by usage percentile. Requires the [[usage-pipeline|Usage Pipeline]].

### Most Expensive Queries
Displays the top queries based on query execution cost. Requires the Usage Pipeline. **Note:** Not all connectors support extracting query cost — verify that your connector supports this feature.

### Data Quality
Shows the percentage of data assets with one or more data quality tests configured. Requires both the [[data-quality|Data Quality Pipeline]] and the Data Insights Pipeline.

## Troubleshooting

If any chart or table shows no data, verify that all prerequisite pipelines listed for that specific chart have been executed successfully. See [[data-insights-application-troubleshooting]] for general Data Insights troubleshooting.

## Relationship to Data Insights

Service Insights is a complementary view to the global [[openmetadata-insights|Data Insights]] report. While Data Insights provides organization-wide metrics, Service Insights drills down into individual services, enabling service owners to monitor the health and completeness of their specific data assets.