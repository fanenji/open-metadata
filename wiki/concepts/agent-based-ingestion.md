---
type: concept
title: Agent-Based Ingestion
created: 2026-05-14
updated: 2026-05-14
tags: [architecture, ingestion, agent, automation, scheduling]
related: [metadata-agent, auto-classification, metadata-ingestion-workflow, ingestion-scheduling]
sources: ["adding-auto-classification-workflow-through-ui---o-20260514.md"]
---
# Agent-Based Ingestion

Agent-Based Ingestion is an architectural pattern in OpenMetadata where configurable, schedulable agents perform specific tasks against connected data sources. Originally developed for metadata extraction via [[metadata-agent|metadata agents]], the pattern has been extended to governance automation with the [[auto-classification|Auto Classification Agent]].

## Core Characteristics

- **Per-service configuration**: Each agent instance is tied to a specific service connection (e.g., a database).
- **Scheduled execution**: Agents run on configurable time intervals, from hourly to custom cron expressions (see [[ingestion-scheduling]]).
- **UI-driven setup**: Agents are configured through a tabbed interface within the service details page, following the [[metadata-ingestion-workflow]] pattern.
- **Toggleable features**: Agents expose configuration toggles (e.g., sample data storage for auto-classification) to control behavior and resource usage.

## Agent Types

| Agent Type | Purpose | Configured In |
|------------|---------|---------------|
| Metadata Agent | Extract schema, lineage, profiling, and quality metadata | Services > [type] > Ingestion tab |
| Auto Classification Agent | Detect and tag sensitive data automatically | Services > Databases > Agents tab |

The agent pattern provides a consistent operational model: users familiar with configuring metadata ingestion can apply the same mental model to governance automation tasks.