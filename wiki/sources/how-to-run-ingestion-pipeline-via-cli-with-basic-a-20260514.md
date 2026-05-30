---
type: source
title: "How To Run Ingestion Pipeline Via CLI with Basic Auth - OpenMetadata Documentation"
created: 2026-05-14
updated: 2026-05-14
tags: [ingestion, cli, authentication, jwt, basic-auth]
related: [cli-ingestion-with-basic-auth, bot-authentication, ingestion-framework, metadata-ingestion-workflow, security-config]
sources: ["how-to-run-ingestion-pipeline-via-cli-with-basic-a-20260514.md"]
authors: ["OpenMetadata"]
year: 2026
url: "https://docs.open-metadata.org/v1.12.x/how-to-guides/admin-guide/cli-ingestion-with-basic-auth"
venue: "OpenMetadata Documentation v1.12.x"
---

# How To Run Ingestion Pipeline Via CLI with Basic Auth - OpenMetadata Documentation

Official procedural guide for running ingestion pipelines from the command line using JWT-based authentication. Covers obtaining the JWT token from the ingestion-bot, configuring the `securityConfig` block in the pipeline YAML, and executing the pipeline via the `metadata ingest` command.

## Key Points

- OpenMetadata switched from no-auth to Basic Auth starting in version 0.12.1, making authentication mandatory for CLI ingestion.
- The `securityConfig` block in the pipeline workflow YAML must contain a `jwtToken` and specify `authProvider: openmetadata`.
- The JWT token is obtained from the pre-configured **ingestion-bot** via Settings > Bots.
- The pipeline is executed with: `metadata ingest -c ./pipeline_name.yaml`