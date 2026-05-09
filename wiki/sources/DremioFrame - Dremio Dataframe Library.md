---
type: source
title: DremioFrame - Dremio Dataframe Library
created: 2026-04-29
updated: 2026-04-29
tags: [dremio, python, dataframe, data-quality, orchestration, ai-agent, iceberg, governance]
related: [dremioframe, dremioframe-data-quality-framework, dremioframe-ai-agent, dremioframe-orchestration, dremioframe-iceberg-management, dremioframe-admin-governance, dremioframe-profile-config, dremio, dremio-mcp-server, developer-advocacy-dremio]
sources: ["DremioFrame - Dremio Dataframe Library.md"]
---
# DremioFrame - Dremio Dataframe Library

## Overview

DremioFrame is a Python library (currently in alpha) that provides a dataframe builder interface for interacting with Dremio Cloud and Dremio Software. It covers the full data lifecycle including ingestion, transformation, data quality, governance, orchestration, and AI-assisted code generation.

## Key Capabilities

- **Dataframe Builder API**: Method-chaining API (`.select()`, `.filter()`, `.join()`, `.group_by()`, etc.) for constructing Dremio queries.
- **Data Quality Framework**: Built-in expectation testing (`.quality.expect_not_null()`, `.quality.expect_row_count()`).
- **AI Agent**: Embedded DremioAgent for SQL, script, and API call generation. Explicitly positioned as a code generation assist tool, not a replacement for Dremio's native agent.
- **Orchestration**: Built-in pipeline scheduling, tasks, sensors, and distributed execution.
- **Iceberg Management**: Time travel, schema evolution, incremental processing, and lakehouse management.
- **Administration & Governance**: Catalog management, reflections, UDFs, masking, row access, tags, lineage, and privileges.
- **MCP Server**: Includes an MCP server component for AI agent integration.
- **Integrations**: Airflow, notebooks, dlt, Pydantic, S3.

## Status

Alpha. Not yet production-ready.

## Source

GitHub repository: [developer-advocacy-dremio/dremio-cloud-dremioframe](https://github.com/developer-advocacy-dremio/dremio-cloud-dremioframe)