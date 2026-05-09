---
type: entity
title: dbt-osmosis LLM Module
created: 2026-04-29
updated: 2026-05-07
tags: [dbt-osmosis, llm, documentation, code-module, dbt, documentation-generation]
related: [dbt-osmosis, dbt-llm-documentation-generation, dbt-osmosis-custom-prompt-guide, dbt-osmosis-benchmarking]
sources: ["dbt-osmosis synthetize.md", "DBT-OSMOSIS.md"]
---
# dbt-osmosis LLM Module

The `llm.py` module is the core component of [[dbt-osmosis]] responsible for LLM-powered documentation generation. It interfaces with multiple LLM providers via OpenAI-compatible API endpoints to generate table and column descriptions from dbt SQL model definitions. The module is invoked with the `--synthesize` flag.

## Architecture

The module connects to a configurable LLM backend via an OpenAI-compatible API. It accepts a batch of dbt SQL model definitions and returns generated YAML documentation with table and column descriptions. The module preserves any existing manually written descriptions, only generating descriptions for undocumented elements.

The exact processing flow involves:

1. Parsing dbt SQL model files
2. Extracting table and column metadata
3. Constructing prompts for the LLM backend
4. Sending requests to the configured API endpoint
5. Parsing and merging generated descriptions into YAML output

## Supported Providers and Configuration

The module supports multiple LLM providers. Configuration is done via environment variables, which are not documented in the official dbt-osmosis documentation but can be found in the source code (`src/dbt_osmosis/core/llm.py`).

| Provider | Required Environment Variables |
|----------|-------------------------------|
| `openai` | `OPENAI_API_KEY` |
| `azure-openai` | `AZURE_OPENAI_BASE_URL`, `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_DEPLOYMENT_NAME` |
| `lm-studio` | `LM_STUDIO_BASE_URL`, `LM_STUDIO_API_KEY` |
| `ollama` | `OLLAMA_BASE_URL`, `OLLAMA_API_KEY` |
| `google-gemini` | `GOOGLE_GEMINI_API_KEY` |
| `anthropic` | `ANTHROPIC_API_KEY` |

Both Ollama and LM Studio backends are tested and known to work:

- **Ollama** — tested at http://10.11.9.76:11434/v1
- **LM Studio** — tested at http://127.0.0.1:1234/v1

All backends use the OpenAI-compatible API format, making the module backend-agnostic.

Example configuration for Ollama:

```bash
export LLM_PROVIDER=ollama
export OLLAMA_BASE_URL=http://10.11.9.76:11434
export OLLAMA_API_KEY=ollama
export OLLAMA_MODEL='qwen2.5-coder:14b-instruct-q4_K_M'
```

## Usage

```bash
dbt-osmosis yaml refactor --synthesize
```

## Key Behaviors

- Generates descriptions in English by default.
- Preserves existing descriptions — does not overwrite manual edits.
- Quality degrades with larger batch sizes; generating fewer descriptions yields better, more detailed results.
- The quality of generated documentation also depends heavily on the LLM model and prompt configuration.

## Customization Points

- **Custom prompt templates**: The module supports using a custom prompt file to guide the LLM's behavior (see [[dbt-osmosis-custom-prompt-guide]]), superseding earlier limitations.
- **Language**: Currently only English is supported; Italian language descriptions are a planned feature.
- **Detail level**: Configurable detail levels are not yet implemented.

## Known Limitations

- Configuration is not documented in the official dbt-osmosis documentation; users must read the source code to discover required environment variables.
- The quality of generated documentation depends heavily on the LLM model and prompt configuration.
- Larger batch sizes can degrade output quality.

## Related

- [[dbt-osmosis]] — Central tool
- [[dbt-llm-documentation-generation]] — Related documentation generation patterns
- [[dbt-osmosis-custom-prompt-guide]] — Custom prompt configuration
- [[dbt-osmosis-benchmarking]] — LLM model benchmarking plans