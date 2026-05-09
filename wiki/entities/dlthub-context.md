---
type: entity
title: dltHub Context
created: 2026-04-29
updated: 2026-04-29
tags: [ai-native, context-assets, llm, pipeline-generation]
related: [dlthub-platform, dlt-data-load-tool, ai-native-pipeline-generation, model-context-protocol]
sources: ["dltHub ELT as Python Code.md"]
---
# dltHub Context

**dltHub Context** is an AI-native hub of context assets that enables LLMs to generate production-ready [[dlt-data-load-tool]] pipeline code from any REST API specification. It supports 10,100+ sources and aims to scale to hundreds of thousands.

## Components

- **Skills**: Pre-built capabilities for common data source patterns
- **Commands**: Instructions for LLMs to generate specific pipeline code
- **Hooks**: Integration points for custom logic
- **AGENT.md**: Context files that guide LLM behavior

## Workflow

1. User provides a REST API specification
2. LLM uses dltHub Context assets to generate dlt pipeline code
3. Pipeline code is executed to ingest data
4. Reports are delivered via Notebooks — all in one flow

## Significance

dltHub Context represents a shift toward LLM-driven data engineering, where AI agents can autonomously create data pipelines from API documentation. This dramatically reduces the time from source identification to live data — from days to minutes.

## Connections

- Conceptually similar to [[dbt-mcp-server]] in providing AI-native tooling for data pipelines
- Related to [[model-context-protocol]] as a pattern for AI-agent interaction with data tools
- Enables [[ai-native-pipeline-generation]] as a practical implementation