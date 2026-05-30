---
type: concept
title: Debug Logging
created: 2026-05-14
updated: 2026-05-14
tags: [troubleshooting, ingestion, logging, diagnostics]
related: [oracle-connector, ingestion-pipeline-troubleshooting, workflow-deployment-error]
sources: ["oracle-troubleshooting-guide-openmetadata-support--20260514.md"]
---

# Debug Logging

Debug Logging is a diagnostic technique for ingestion pipelines in OpenMetadata. It enables verbose logging output that helps identify the root cause of failures during metadata ingestion.

## Procedure

The debug logging procedure is connector-agnostic and applies to any ingestion workflow:

1. Navigate to **Settings > Services** in the OpenMetadata UI.
2. Select the service type (e.g., Database) and then the specific service.
3. Go to the **Ingestion** tab.
4. Click the three-dot menu on the right-hand side of the ingestion type and select **Edit**.
5. In the configuration dialog, enable the **Debug Log** option.
6. Click **Next**, configure the schedule if needed, and click **Submit** to apply the changes.

## Usage

Enable debug logging when:
- An ingestion pipeline fails with an unclear error message.
- A [[workflow-deployment-error]] occurs and the pipeline entity is created but no workflow runs.
- Permission-related errors are encountered during connector setup or metadata ingestion.

After resolving the issue, consider disabling debug logging to reduce log volume.