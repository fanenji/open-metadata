---
type: concept
title: Debug Logging for Ingestion
created: 2026-05-14
updated: 2026-05-15
tags: [troubleshooting, ingestion, logging, debugging, connectors, openmetadata]
related: [ingestion-pipeline-troubleshooting, workflow-deployment-error, metadata-ingestion-workflow, powerbi-connector, superset-connector, service-connection, metadata-agent, rest-connector-troubleshooting]
sources: [powerbi-dashboard-troubleshooting-guide-openmetada-20260514.md, superset-troubleshooting-guide-openmetadata-suppor-20260514.md, rest-connector-troubleshooting-guide-openmetadata--20260514.md]
---

# Debug Logging for Ingestion

Debug logging is a diagnostic feature in OpenMetadata that enables verbose logging for any ingestion workflow. When enabled, the ingestion pipeline produces detailed logs that reveal information about the extraction, transformation, and loading process. It is the primary tool for diagnosing connector-specific issues and troubleshooting ingestion failures.

## Procedure

1. Navigate to **Settings > Services** in the OpenMetadata UI.
2. Select the service type (e.g., Database, Dashboard, API) and then the specific service.
3. Go to the **Ingestion** tab and click the three-dot menu on the right-hand side of the ingestion type.
4. Select **Edit**, then enable the **Debug Log** toggle/option.
5. Click **Next**, configure the schedule if needed, and click **Submit** (or **Next/Submit** depending on the workflow).

This procedure works for any ingestion workflow, whether it is a database, dashboard, API, or other connector.

## Scope and Applicability

- Debug logging can be enabled on a per-ingestion basis.
- It applies to all connector types, not just the [[rest-api-connector|REST API Connector]].
- The setting persists across pipeline runs until disabled.
- This technique is documented in the [[powerbi-connector]], [[superset-connector]], and [[rest-connector-troubleshooting]] guides, but is applicable universally.

## Best Practices

- Enable debug logging only during active troubleshooting to avoid log volume.
- Review logs in the ingestion container or Kubernetes pod logs.
- Disable debug logging after the issue is resolved to reduce resource consumption.

## Use Cases

- Diagnosing [[connector-permission-issues|permission issues]] during metadata extraction.
- Identifying API version mismatches, authentication failures, or authorization failures.
- Tracing the exact data being ingested for [[filter-patterns]] validation.
- Debugging [[workflow-deployment-error|workflow deployment errors]] where the pipeline entity exists but no workflow runs.
- Tracing data extraction and transformation steps.
- Debugging schema discovery issues.

## Related

- [[ingestion-pipeline-troubleshooting]] — General troubleshooting framework for common pipeline failures.
- [[workflow-deployment-error]] — A common scenario diagnosed with debug logging.
- [[metadata-ingestion-workflow]] — The 8-step UI process for setting up ingestion (the canonical ingestion process).
- [[powerbi-connector]] — Specific connector that this technique applies to.
- [[superset-connector]] — Specific connector that this technique applies to.
- [[service-connection]] — Connection configuration details.
- [[metadata-agent]] — The configurable pipeline (agent) that performs metadata extraction.
- [[rest-connector-troubleshooting]] — REST connector-specific troubleshooting.