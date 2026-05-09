---
type: entity
title: OpenMetadata AI Assistant
created: 2026-03-19
updated: 2026-03-19
tags: [openmetadata, ai, data-quality, llm]
related: [openmetadata, openmetadata-data-quality, ollama-integration-pattern, llm-model-selection-for-dq, mistral-small-4]
sources: ["Suggested Data Quality Tools.md"]
---
# OpenMetadata AI Assistant

The OpenMetadata AI Assistant is a native feature that integrates with local LLMs via **Ollama** to suggest data quality tests and descriptions from table schemas and metadata. It scans table schemas and metadata, then proposes tests such as "Column A should not be null" or "Column B values should be between 1-100" without data leaving the infrastructure.

## Key Capabilities

- **Schema-driven suggestions**: Analyzes column names, data types, and metadata to propose relevant quality tests
- **Local LLM integration**: Connects directly to Ollama via UI settings — no custom middleware or `llm.py` required
- **On-premise deployment**: All processing stays within the infrastructure
- **Click-to-confirm workflow**: Users review and confirm suggested tests in the UI

## Integration

The AI Assistant is configured through OpenMetadata's UI settings, where users specify the Ollama endpoint and model. Recommended models include [[mistral-small-4]] for DQ suggestions and [[qwen3.5-122b-a10b]] for documentation generation.

## Relationship to Existing Stack

The AI Assistant is part of [[openmetadata]]'s Data Quality module, which also includes the [[openmetadata-dq-dashboard]] for visualization and alerting. It complements [[dbt-expectations]] by providing AI-driven test suggestions rather than requiring manual test definition.