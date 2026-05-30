---
type: entity
title: REST Connector Troubleshooting
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, rest-connector, troubleshooting, ingestion]
related: [rest-api-connector, ingestion-pipeline-troubleshooting, metadata-ingestion-workflow, openmetadata-connectors, rest-connector-troubleshooting-guide-openmetadata--20260514]
sources: ["rest-connector-troubleshooting-guide-openmetadata--20260514.md"]
---

# REST Connector Troubleshooting

This page consolidates troubleshooting guidance for the [[rest-api-connector|REST API Connector]] (Beta) in OpenMetadata. It covers common issues, diagnostic procedures, and known limitations.

## Workflow Deployment Error

If errors occur during the workflow deployment process, the Ingestion Pipeline Entity will still be created, but no workflow will be present in the Ingestion container.

**Resolution:**
1. Navigate to the Ingestion Pipeline for the affected service.
2. Click the three-dot menu and select **Edit**.
3. Re-configure the pipeline settings if needed.
4. Click **Deploy** to re-deploy the workflow.
5. From the **Connection tab**, you can also edit the Service if the connection configuration is incorrect.

**Note:** This error pattern may apply to all connectors, not just REST. See [[ingestion-pipeline-troubleshooting]] for general pipeline failure diagnostics.

## Debug Logging

Enabling debug logging is the primary diagnostic tool for any ingestion workflow. It provides verbose logs that help identify the root cause of failures.

**Procedure:**
1. Go to **Settings > Services** in the OpenMetadata UI.
2. Select the service type (e.g., Database) and then the specific service.
3. Open the **Ingestion** tab.
4. Click the three-dot menu on the right-hand side of the ingestion type and select **Edit**.
5. In the configuration dialog, enable the **Debug Log** option.
6. Click **Next**, configure the schedule if needed, and click **Submit**.

This procedure applies to all connectors, not just REST. For general ingestion workflow context, see [[metadata-ingestion-workflow]].

## Permission Issues

If you encounter permission-related errors during connector setup or metadata ingestion, ensure that all prerequisites and access configurations specified for the connector are properly implemented. Refer to the connector-specific documentation to verify the required permissions.

For the REST API Connector, common permission-related issues may include:
- Invalid or expired API keys/tokens.
- Insufficient API endpoint scopes.
- OpenAPI specification validation failures.
- Network/firewall restrictions blocking endpoint access.
- Authentication header format mismatches.

See the [[rest-api-connector]] page for connector-specific prerequisites and configuration details.

## Related Pages

- [[rest-api-connector]] — The REST API Connector entity page.
- [[ingestion-pipeline-troubleshooting]] — General ingestion pipeline troubleshooting for K8s-native mode.
- [[metadata-ingestion-workflow]] — The canonical 8-step UI-driven ingestion process.
- [[openmetadata-connectors]] — The library of 90+ turnkey connectors.