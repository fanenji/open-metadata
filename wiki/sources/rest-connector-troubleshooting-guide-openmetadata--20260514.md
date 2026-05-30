---
type: source
title: REST Connector Troubleshooting Guide | OpenMetadata Support
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, rest-connector, troubleshooting, ingestion]
related: [rest-api-connector, rest-connector-troubleshooting, ingestion-pipeline-troubleshooting, metadata-ingestion-workflow, openmetadata-connectors]
sources: ["rest-connector-troubleshooting-guide-openmetadata--20260514.md"]
---

# REST Connector Troubleshooting Guide | OpenMetadata Support

This source is the official troubleshooting documentation for the REST API Connector (Beta) in OpenMetadata v1.12.x. It covers three troubleshooting scenarios: Workflow Deployment Error, enabling debug logging for any ingestion, and a generic reference to permission issues.

## Key Content

- **Workflow Deployment Error**: If errors occur during workflow deployment, the Ingestion Pipeline Entity is created but no workflow runs in the container. The fix is to edit the Ingestion Pipeline and re-deploy it. The Service can also be edited from the Connection tab.
- **Debug Logging**: A UI procedure to enable verbose logging for any ingestion workflow. Steps: Settings > Services > Service Type > Select Service > Ingestion tab > three-dot menu > Edit > Enable Debug Log > Next > Schedule > Submit.
- **Permission Issues**: A placeholder section that directs users to connector-specific documentation for prerequisites and access configurations.

## Limitations

- No specific error messages, log patterns, or root causes are provided for the Workflow Deployment Error.
- The Permission Issues section offers no actionable guidance beyond a redirect.
- The guide is purely procedural with no diagnostic depth.

## Relevance

This source directly extends the [[rest-api-connector]] page with a dedicated troubleshooting subsection. It also relates to [[ingestion-pipeline-troubleshooting]] (general K8s-native ingestion troubleshooting) and [[metadata-ingestion-workflow]] (the 8-step UI process). The debug logging procedure is the most actionable content and applies to all connectors, not just REST.