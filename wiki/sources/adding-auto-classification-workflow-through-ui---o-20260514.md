---
type: source
title: "Adding Auto Classification Workflow through UI - OpenMetadata Documentation"
created: 2026-05-14
updated: 2026-05-14
tags: [auto-classification, data-governance, classification, ui-workflow, agent]
related: [auto-classification, classification-tags, metadata-agent, metadata-ingestion-workflow, pii-sample-data-masking]
sources: ["adding-auto-classification-workflow-through-ui---o-20260514.md"]
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/data-governance/classification/auto-classification/workflow"
authors: ["OpenMetadata Documentation Team"]
year: 2026
---
# Adding Auto Classification Workflow through UI - OpenMetadata Documentation

Official procedural guide for configuring the Auto Classification Agent through the OpenMetadata UI (v1.12.x). The document describes a 5-step workflow: navigate to the database service, access the Agents tab, configure auto-classification details (including a sample data storage toggle), set the schedule, and activate the agent. The Auto Classification Agent is configured per-database service and runs on a configurable schedule to automatically identify and tag sensitive data.

Key points:
- The agent is accessed via **Settings > Services > Databases > [select database] > Agents tab**.
- A **store sample data** option is enabled by default; disabling it prevents sample data ingestion during scheduled runs.
- The workflow mirrors the [[metadata-ingestion-workflow]] pattern, extending the agent paradigm from metadata ingestion to governance automation.
- This feature complements the manual [[classification-tags]] application and the collaborative [[tag-request-workflow]].