---
type: entity
title: AutoPilot
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, automation, ingestion, workflow]
related: [postgresql-connector, metadata-ingestion-workflow, ingestion-scheduling, data-lineage, data-profiling]
sources: ["postgresql-connector-openmetadata-database-integra-20260514.md"]
---

# AutoPilot

AutoPilot is an OpenMetadata feature that automatically handles workflows such as usage tracking, data lineage, and similar tasks without requiring users to set up or manage them manually. When enabled, AutoPilot takes care of these processes in the system.

## Overview

AutoPilot simplifies the operational overhead of managing ingestion pipelines by automating routine metadata workflows. Instead of manually configuring and scheduling separate pipelines for usage and lineage, users can rely on AutoPilot to handle these tasks automatically.

## Key Characteristics

- **Automatic Workflow Management**: Usage tracking, data lineage, and similar workflows are handled automatically.
- **No Manual Setup Required**: Users do not need to create or manage separate ingestion pipelines for these workflows.
- **System-Managed**: AutoPilot operates within the OpenMetadata system, orchestrating the necessary processes.

## Relationship to Existing Features

AutoPilot appears to be an additional layer on top of the existing [[metadata-ingestion-workflow]] and [[ingestion-scheduling]] mechanisms. It is mentioned in the context of the [[postgresql-connector]] documentation, suggesting it is a general connector feature rather than PostgreSQL-specific.

## Open Questions

- Does AutoPilot replace the need for separate usage/lineage pipeline configuration, or is it an additional layer that works alongside manual configuration?
- What is the exact relationship between AutoPilot and the existing ingestion scheduling mechanism?
- How is AutoPilot enabled or disabled? Is it a per-service toggle or a global setting?
- What is the scope of workflows that AutoPilot manages beyond usage tracking and data lineage?

## Related Pages

- [[postgresql-connector]] — PostgreSQL connector documentation where AutoPilot is mentioned.
- [[metadata-ingestion-workflow]] — The canonical UI-driven process for ingesting metadata.
- [[ingestion-scheduling]] — Mechanism for running metadata agent pipelines on recurring schedules.
- [[data-lineage]] — Tracking the origin and transformation of data.
- [[data-profiling]] — Analyzing data to understand its structure, content, and quality.