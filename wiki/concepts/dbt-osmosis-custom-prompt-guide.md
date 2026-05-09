---
type: concept
title: dbt-osmosis Custom Prompt Guide
created: 2026-04-29
updated: 2026-04-29
tags: [dbt-osmosis, llm, prompts, customization]
related: [dbt-osmosis, dbt-osmosis-llm-module, dbt-osmosis-benchmarking, dbt-llm-documentation-generation]
sources: ["dbt-osmosis synthetize.md"]
---
# dbt-osmosis Custom Prompt Guide

A guide to configuring custom prompts for [[dbt-osmosis]]'s LLM-powered documentation generation. Custom prompts enable control over language, detail level, and content of generated descriptions.

## Current Limitations

The `llm.py` module in dbt-osmosis version 1.2.2 does not natively support:
- Custom prompt templates
- Italian language descriptions
- Configurable detail levels

These features are identified as TODO items for future development.

## Requirements

A custom prompt management system should support:
- **Language Selection** — ability to specify output language (e.g., Italian, English).
- **Detail Level Control** — parameters for concise, standard, or verbose descriptions.
- **Context Injection** — ability to include business context, domain terminology, or style guidelines.
- **Template Variables** — dynamic insertion of table name, column names, data types, and model metadata.

## Proposed Prompt Structure

A typical custom prompt template might include:
- System message defining the role (e.g., "You are a data documentation expert").
- Language instruction (e.g., "Generate descriptions in Italian").
- Detail level instruction (e.g., "Provide a concise one-sentence description").
- Context block with table/column metadata.
- Output format specification (e.g., YAML).

## Implementation Considerations

- Prompts should be stored in a configuration file (e.g., YAML or JSON) for easy editing.
- Different prompts may be needed for table descriptions vs. column descriptions.
- Prompt templates should be versioned alongside the dbt project.
- Testing different prompts should be part of the [[dbt-osmosis-benchmarking]] workflow.