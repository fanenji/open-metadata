---
type: concept
title: Auto Tiering Pipeline
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, data-insights, tiering, automation, pipeline]
related: [tiers, service-insights, data-insights-pipeline, auto-classification, openmetadata-ai-application]
sources: ["service-insights-overview-official-documentation---20260514.md"]
---
# Auto Tiering Pipeline

The Auto Tiering Pipeline is an automated pipeline in OpenMetadata that assigns tier classifications to data assets. It is referenced as a prerequisite for the [[service-insights|Service Insights]] Tier Coverage and Tier Distribution charts, and for the Generated Data with OpenMetadata AI table.

## Purpose

The Auto Tiering Pipeline automates the process of assigning [[tiers|Tier]] classifications (Tier 1 through Tier 5) to data assets, reducing the manual effort required for tier-based governance. It is distinct from the [[auto-classification|Auto Classification Pipeline]], which handles PII tagging.

## Prerequisites

The Auto Tiering Pipeline is listed as "OpenMetadata Only" in the official documentation, suggesting it may be available only in specific deployment modes or license tiers.

## Relationship to Other Pipelines

The Auto Tiering Pipeline works in conjunction with the [[data-insights-pipeline|Data Insights Pipeline]] to populate tier-related charts in Service Insights. It is also one of several pipelines required for the Generated Data with OpenMetadata AI table, which tracks metadata created by automated agents versus manual input.

## Open Questions

- Is the Auto Tiering Pipeline a separate feature from the Auto Classification Pipeline, or is it a sub-component? The official documentation lists them separately.
- What is the exact configuration and scheduling mechanism for the Auto Tiering Pipeline?
- Is it available in all OpenMetadata deployments or only in specific editions?