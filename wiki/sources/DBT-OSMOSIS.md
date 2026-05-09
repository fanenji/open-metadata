---
type: source
title: DBT-OSMOSIS.md
created: 2026-02-17
updated: 2026-02-17
tags: [dbt, dbt-osmosis, schema-synchronization, documentation-generation, llm]
related: [dbt-osmosis, dbt-osmosis-llm-module, dbt-osmosis-custom-prompt-guide, dbt-osmosis-benchmarking, dbt-schema-synchronization, dbt-project-scaffolding]
sources: ["DBT-OSMOSIS.md"]
---
# DBT-OSMOSIS.md

Internal testing notes for the dbt-osmosis tool, covering installation, configuration, YAML refactoring, the `--synthesize` LLM documentation generation feature, and known bugs. The source documents hands-on testing with a local dbt project connected to Dremio, including the correct execution order (`dbt build` → `dbt docs generate` → `dbt-osmosis yaml refactor`), the `data_type` bug in v1.14, and the undocumented LLM provider configuration via environment variables.

## Key Findings

- **Execution order matters**: `dbt-osmosis yaml refactor` must be run after `dbt build` and `dbt docs generate` to pick up schema changes.
- **Manual edits preserved**: Manual modifications to YAML files are retained across `dbt-osmosis yaml refactor` runs.
- **data_type bug (v1.14)**: Column data types are not populated due to a bug. A fix exists in an internal GitLab repository.
- **Column comments not captured**: dbt-osmosis does not read existing column comments from the database (Dremio does not expose them).
- **LLM synthesis works**: The `--synthesize` flag generates documentation using a local Ollama model (`qwen2.5-coder:14b`), but configuration is undocumented and requires reading source code.
- **Supported LLM providers**: OpenAI, Azure OpenAI, LM Studio, Ollama, Google Gemini, Anthropic — each with specific environment variables.

## Related Pages

- [[dbt-osmosis]] — Central tool page
- [[dbt-osmosis-llm-module]] — LLM-powered documentation generation component
- [[dbt-osmosis-custom-prompt-guide]] — Custom prompt configuration
- [[dbt-osmosis-benchmarking]] — LLM model benchmarking plans
- [[dbt-schema-synchronization]] — Broader concept of schema YAML synchronization
- [[dbt-project-scaffolding]] — Automated project setup