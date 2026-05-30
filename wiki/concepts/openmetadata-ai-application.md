---
type: concept
title: OpenMetadata AI Application
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, ai, metadata-generation, automation]
related: [service-insights, auto-classification, auto-tiering-pipeline, data-quality, application-framework]
sources: ["service-insights-overview-official-documentation---20260514.md"]
---
# OpenMetadata AI Application

The OpenMetadata AI Application is an AI agent within OpenMetadata that generates metadata for data assets. It is referenced in the [[service-insights|Service Insights]] documentation as a prerequisite for the "Generated Data with OpenMetadata AI" table, which distinguishes metadata created by the AI agent from metadata created manually.

## Purpose

The OpenMetadata AI Application automates the creation of metadata, such as descriptions, tags, and other annotations, reducing the manual effort required for metadata enrichment. It is part of the [[application-framework|Application Framework]] and is listed as "OpenMetadata Only" in the official documentation.

## Relationship to Other Pipelines

The OpenMetadata AI Application works alongside the [[auto-classification|Auto Classification Pipeline]], [[auto-tiering-pipeline|Auto Tiering Pipeline]], and Auto Data Quality (DQ) Pipeline to populate the "Generated Data with OpenMetadata AI" table in Service Insights.

## Open Questions

- Does the OpenMetadata AI Application require a specific license or deployment mode?
- What types of metadata does the AI agent generate (e.g., descriptions, tags, glossary terms)?
- How is the AI agent configured and trained?