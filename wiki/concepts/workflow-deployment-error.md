---
type: concept
title: Workflow Deployment Error
created: 2026-05-14
updated: 2026-05-15
tags: [troubleshooting, ingestion, pipeline, error, deployment, pipelines, openmetadata, error-pattern]
related: [ingestion-pipeline-troubleshooting, metadata-ingestion-workflow, powerbi-connector, debug-logging-ingestion, metadata-agent, service-connection, superset-connector, rest-connector-troubleshooting, postgresql-connector-troubleshooting, oracle-connector, debug-logging]
sources: [powerbi-dashboard-troubleshooting-guide-openmetada-20260514.md, superset-troubleshooting-guide-openmetadata-suppor-20260514.md, rest-connector-troubleshooting-guide-openmetadata--20260514.md, powerbi-dashboard-troubleshooting-guide-openmetada-20260514-2.md, postgresql-connector-troubleshooting---openmetadat-20260514.md, oracle-troubleshooting-guide-openmetadata-support--20260514.md]
---

# Workflow Deployment Error

A Workflow Deployment Error is a partial failure mode during metadata ingestion pipeline deployment in [[OpenMetadata]]. The [[metadata-agent|Ingestion Pipeline Entity]] is successfully created in the metadata catalog, but the actual workflow (the running process that extracts and ingests metadata) fails to deploy in the ingestion container. As a result, the pipeline appears in the UI but never executes any workflow runs, creating an orphan entity with no active ingestion. This is a recoverable condition. This pattern is documented for the [[oracle-connector]] but applies to all connectors.

## Symptoms

- An Ingestion Pipeline Entity appears in the UI for the service.
- No workflow runs are visible in the Ingestion tab.
- No logs are generated for the pipeline run.
- The pipeline status may show as "Queued" or "Failed" without any execution history.
- The pipeline remains in a non-functional state.
- No workflow is present in the ingestion container (e.g., no Kubernetes Job or Airflow DAG is created).
- Metadata is not being ingested.

## Root Causes

- Transient network or infrastructure issues during deployment (e.g., connectivity between OpenMetadata and the ingestion container, or between OpenMetadata and the source system).
- Invalid, expired, or malformed credentials in the [[service-connection]].
- Resource constraints in the ingestion container (e.g., insufficient memory or CPU) preventing workflow startup.
- Configuration errors in the pipeline definition.
- Configuration validation errors that are not caught during entity creation.

## Prevention

- Enable [[debug-logging-ingestion|debug logging]] before deployment to capture detailed error information.
- Verify [[service-connection]] prerequisites and all necessary permissions before creating the pipeline.
- Monitor ingestion container health and resource usage (e.g., Kubernetes Job or Airflow worker) and ensure sufficient memory and CPU.

## Resolution

1. Navigate to **Settings > Services**, select the affected service, and go to the **Ingestion** tab.
2. Click the three-dot menu on the affected pipeline and select **Edit**.
3. Review and correct any configuration issues:
   - Check connection details, credentials, and pipeline definition.
   - If needed, from the **Connection** tab, edit the service configuration.
4. Click **Deploy** to redeploy the workflow.
5. If the issue persists, verify the service connection from the **Connection** tab and address any problems.

The condition is fully recoverable; re-deploying the pipeline after correcting the underlying cause will re-create the workflow in the ingestion container.

## Importance

This is a subtle failure mode — users may not realize a pipeline entity exists without a running workflow. It is documented in the troubleshooting guides for multiple connectors but is applicable to any connector.

## Known Occurrences

This pattern has been documented for:
- [[postgresql-connector-troubleshooting]] — PostgreSQL connector
- [[powerbi-connector]] — PowerBI dashboard connector
- [[superset-connector]] — Apache Superset connector
- [[rest-connector-troubleshooting]] — REST connector
- [[oracle-connector]] — Oracle connector

It is a general behavior of the ingestion framework and may occur with any connector.

## Related Concepts

- [[ingestion-pipeline-troubleshooting]] — General troubleshooting framework for pipeline failures.
- [[metadata-ingestion-workflow]] — The canonical ingestion process.
- [[metadata-agent]] — The configurable pipeline that performs ingestion.
- [[debug-logging-ingestion]] — Enabling debug logs to diagnose root causes.
- [[service-connection]] — Connection configuration that can cause deployment issues.
- [[rest-connector-troubleshooting]] — REST connector-specific troubleshooting, including this error pattern.
- [[powerbi-connector]] — PowerBI-specific connector page where this error is documented.
- [[superset-connector]] — Superset-specific connector page where this error is documented.
- [[postgresql-connector-troubleshooting]] — PostgreSQL connector page where this error is documented.
- [[oracle-connector]] — Oracle connector page where this error is documented.