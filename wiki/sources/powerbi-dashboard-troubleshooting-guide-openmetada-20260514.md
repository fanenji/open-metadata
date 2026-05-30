---
type: source
title: PowerBI Dashboard Troubleshooting Guide | OpenMetadata Support
created: 2026-05-14
updated: 2026-05-14
tags: [powerbi, troubleshooting, ingestion, connectors]
related: [powerbi-connector, workflow-deployment-error, debug-logging-ingestion, ingestion-pipeline-troubleshooting, openmetadata-connectors]
sources: ["powerbi-dashboard-troubleshooting-guide-openmetada-20260514.md"]
---

# PowerBI Dashboard Troubleshooting Guide | OpenMetadata Support

This is the official OpenMetadata v1.12.x troubleshooting guide for the PowerBI dashboard connector. It documents three troubleshooting scenarios: Workflow Deployment Error (orphan Ingestion Pipeline Entity creation), enabling debug logging for any ingestion workflow, and permission issues that require connector-specific prerequisite verification.

## Key Topics

- **Workflow Deployment Error**: A partial failure mode where the Ingestion Pipeline Entity is created but no workflow runs. Resolution involves editing and redeploying the pipeline.
- **Debug Logging**: A 5-step UI procedure (Services → Select → Ingestion tab → Edit → Enable Debug Log) applicable to any ingestion workflow.
- **Permission Issues**: Errors requiring verification of connector-specific prerequisites and access configurations.

## Connections

- Extends the general [[ingestion-pipeline-troubleshooting]] framework with PowerBI-specific context.
- References the broader [[openmetadata-connectors]] library.
- Defers to connector-specific documentation for permission details.
