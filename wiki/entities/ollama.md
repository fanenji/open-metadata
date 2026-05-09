---
type: entity
title: Ollama
created: 2026-04-04
updated: 2026-05-07
tags:
  - tool
  - llm
  - open-source
  - local
  - local-inference
  - serving
  - privacy
  - runtime
  - deployment
related:
  - ai-copilot-for-data-engineering
  - langchain
  - local-llm-openmetadata-extension
  - openmetadata
  - data-discovery-tools
  - privacy-by-design
  - local-llm-for-bi-development
  - model-context-protocol
  - opencode
  - qwen-models
  - Ritam Mukherjee
  - llm-model-selection-for-data-quality
  - qwen-2-5-coder
sources: ["Suggested Models (Gemini) - OLD.md", "Integrating LLMs and AI Agents into Data Engineering Workflows 1.md", "fully-local-power-bi-development-opencode-qwen-power-bi-mcp.md", "Local LLM for OpenMetadata - Visual Studio Marketplace.md"]
---
# Ollama

Ollama is an open-source platform for serving large language models (LLMs) locally on your hardware. It provides a simple command‑line interface and API for downloading, managing, and running a wide variety of open‑source models, including Meta's Llama family, Qwen models, Mistral, CodeLlama, and codestral. Exposed via an OpenAI‑compatible API (`http://localhost:11434/v1`), Ollama is a go‑to solution for local inference and privacy‑preserving AI deployments. It is 100% local, free to use, and works offline, requiring no internet connectivity or per‑token costs.

As highlighted in the article *Integrating LLMs and AI Agents into Data Engineering Workflows* by [[Ritam Mukherjee]], using Ollama addresses security concerns about feeding sensitive data into third‑party APIs, because models run entirely on local infrastructure. This aligns with the recommendation to use fine‑tuned, self‑hosted models when possible. In data discovery contexts, Ollama powers the [[local-llm-openmetadata-extension]] for [[openmetadata]], enabling [[privacy-by-design]] workflows that keep sensitive metadata on‑premises. It is also the assumed runtime in the [[Suggested Models (Gemini) - OLD.md]] source, which recommends models for use with [[OpenMetadata]] in data quality pipelines.

## Features

- **Local inference:** Runs models entirely on the user's hardware, ensuring data privacy. No internet connection required.
- **Free and open source:** No per‑token costs or API subscriptions.
- **OpenAI‑compatible API:** Exposes models at `http://localhost:11434/v1`, making it drop‑in compatible with many applications, including [[OpenMetadata]] and custom tools.
- **Wide model support:** Access to hundreds of open‑source models — pull and run models such as Llama, Qwen, Mistral, CodeLlama, codestral, and more with a single CLI command.
- **Model management:** Easily download, run, and manage model variants via CLI.
- **Context window configuration:** Supports custom `num_ctx` parameter for extended context windows (default 4K).
- **Quantization support:** Run quantized versions of models to fit in limited VRAM.
- **Security & privacy:** Models run locally, eliminating the need to send sensitive data to external APIs.

## Installation & Setup

- **Install Ollama:** Download from [ollama.com/download](https://ollama.com/download) or use Homebrew on macOS.
- **Pull a model:** `ollama pull llama2` (or any supported model).
- **Configure endpoint:** The default local endpoint `http://localhost:11434` works immediately; for remote clients, set `OLLAMA_HOST="0.0.0.0"`.

## Configuration

### Context Window

Ollama defaults to a 4K context window, which silently breaks tool calling for MCP‑based workflows (e.g., with [[opencode]]). The context must be explicitly expanded:

```bash
ollama run qwen3.5:35b-a3b
/set parameter num_ctx 32768
/save qwen3.5:35b-a3b-32k
/bye
```

### Mac VM Networking

When running Ollama on macOS with other components in a Windows VM:
1. Set `OLLAMA_HOST="0.0.0.0"` to listen on all interfaces.
2. Find the Mac's gateway IP on the virtual network (e.g., `192.168.xxx.2`).
3. Update the [[opencode]] config's `baseURL` to point to that IP.

## Usage

Run models directly from the CLI:

```bash
ollama run qwen2.5-coder
ollama run llama3.1
ollama run codestral
```

After pulling a model and configuring the endpoint, applications that support the OpenAI API format (including [[langchain]], [[opencode]], and [[openmetadata]]) can target `http://localhost:11434/v1` for inference.

## Use Cases

### Data Engineering Workflows

Used alongside [[ai-copilot-for-data-engineering]], [[langchain]], and [[opencode]], Ollama provides a secure, local LLM backend for building AI agents without exposing proprietary data. For example, it is the inference engine in the [[local-llm-for-bi-development]] pattern, enabling fully local Power BI development with tools like [[qwen-models]].

### Data Discovery & Governance

As one of three supported providers in the [[local-llm-openmetadata-extension]] for [[openmetadata]], Ollama enables [[privacy-by-design]] workflows for exploring sensitive metadata. By relying on a local model, teams can leverage LLMs for data discovery without sending metadata to cloud providers, supporting [[data-governance]] and [[data-masking-techniques]].

### Data Quality

Ollama serves as the deployment platform for running LLMs locally to power automated test generation and data quality analysis. It is the assumed runtime in the [[Suggested Models (Gemini) - OLD.md]] source, which recommends models (e.g., from [[llm-model-selection-for-data-quality]]) for use with [[OpenMetadata]] data quality workflows.

## See Also

- [[ai-copilot-for-data-engineering]]
- [[data-discovery-tools]]
- [[data-governance]]
- [[data-masking-techniques]]
- [[langchain]]
- [[local-llm-for-bi-development]]
- [[local-llm-openmetadata-extension]]
- [[model-context-protocol]]
- [[opencode]]
- [[openmetadata]]
- [[privacy-by-design]]
- [[qwen-models]]
- [[Ritam Mukherjee]]
- [[llm-model-selection-for-data-quality]]
- [[qwen-2-5-coder]]