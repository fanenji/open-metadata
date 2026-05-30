---
type: source
title: "Oracle Troubleshooting Guide | OpenMetadata Support"
created: 2026-05-14
updated: 2026-05-14
tags: [oracle, connector, troubleshooting, ingestion]
related: [oracle-connector, workflow-deployment-error, ingestion-pipeline-troubleshooting, debug-logging]
sources: ["oracle-troubleshooting-guide-openmetadata-support--20260514.md"]
---

# Oracle Troubleshooting Guide | OpenMetadata Support

**URL:** https://docs.open-metadata.org/v1.12.x/connectors/database/oracle/troubleshooting

**Source Type:** Official OpenMetadata Documentation (v1.12.x)

## Summary

This is the official troubleshooting guide for the Oracle connector in OpenMetadata v1.12.x. It covers three common troubleshooting scenarios: Workflow Deployment Error, Debug Logging, and Permission Issues. The guide provides procedural steps for diagnosing and resolving each issue.

## Key Content

- **Workflow Deployment Error:** Documents the partial failure state where the Ingestion Pipeline Entity is created but no workflow runs. The recommended recovery is to Edit the Ingestion Pipeline and Deploy it again.
- **Debug Logging:** Provides a step-by-step procedure for enabling debug logging on any ingestion workflow via the UI (Settings > Services > Service > Ingestion > Edit > Enable Debug Log).
- **Permission Issues:** Generic guidance to verify connector-specific prerequisites and access configurations.

## Relevance to Wiki

This source strengthens the existing [[oracle-connector]] page by adding specific troubleshooting procedures. It confirms the [[workflow-deployment-error]] pattern applies to the Oracle connector. The Debug Logging procedure is connector-agnostic and can be generalized.