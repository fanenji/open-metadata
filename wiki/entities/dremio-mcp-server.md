---
type: entity
title: Dremio MCP Server
created: 2026-02-13
updated: 2026-05-09
tags:
  - dremio
  - mcp
  - self-hosted
  - ai-integration
  - ai-tools
  - ai-agents
  - open-source
  - production-readiness
related:
  - model-context-protocol
  - dremio
  - claude
  - uv
  - agentic-skills-pattern
  - dremio-cloud-edition
  - dbt-mcp-server
  - ai-agent-integration-risk-framework
sources:
  - Come installare il server mcp di Dremio-20260507.md
  - Come installare il server mcp di Dremio.md
  - research-the-source-does-not-clarify-whether-the-dremio-mcp-2026-05-09.md
---
# Dremio MCP Server

The **Dremio MCP Server** is an open-source project that implements the [[model-context-protocol]] (MCP) to expose [[dremio]]'s data virtualization and data lakehouse capabilities to AI agents and LLM clients (such as [[claude]]). It acts as a bridge between the Dremio engine and MCP‑compatible AI clients, allowing agents to execute SQL queries, explore data patterns, and perform system performance analysis through natural language interfaces. Launched in May 2025, it is a key enabler of Dremio's "Agentic Lakehouse" vision. The server is designed to be run in self‑hosted environments (Docker or Kubernetes) using the [[uv]] package manager.

## Prerequisites

- **[[uv]]**: A fast Python package manager.
- **Dremio URI**: The endpoint for the Dremio deployment (e.g., `http://localhost:9047/`).
- **Personal Access Token (PAT)**: Generated from Dremio credentials for secure authentication.
- **MCP Client**: An AI client like Claude.

## Installation

1. Clone the official repository:
   ```bash
   git clone https://github.com/dremio/dremio-mcp
   cd dremio-mcp
   ```
2. (Optional) Verify the installation:
   ```bash
   uv run dremio-mcp-server --help
   ```

## Configuration

Create a Dremio connection profile and configure the AI client:

1. Create a `dremioai` profile with the URI and PAT:
   ```bash
   uv run dremio-mcp-server config create dremioai --uri <your-uri> --pat <your-pat>
   ```
2. Create the client‑specific configuration (e.g., for Claude):
   ```bash
   uv run dremio-mcp-server config create claude
   ```
3. List existing configurations:
   ```bash
   uv run dremio-mcp-server config list --type dremioai
   uv run dremio-mcp-server config list --type claude
   ```

## Operational Modes

The server supports two specialized modes to tailor the agent's capabilities:

- **`FOR_DATA_PATTERNS`**: Optimized for natural‑language to SQL translation and data exploration.
- **`FOR_SS_SELF`**: Optimized for infrastructure performance analysis and system monitoring.

## Usage

Start the server:
```bash
uv run dremio-mcp-server run
```

Authentication is handled via the Personal Access Token (PAT) provided during configuration. Jobs executed through the MCP server are visible in the Dremio console under the **"External Tools"** filter.

## Production Readiness

Production readiness depends entirely on the deployment model.

### Self-Managed (Open Source) — Experimental / Pre-Production

- **Support:** Explicitly excluded from Dremio Support Policies. Community support only via GitHub issues and forums.
- **Stability:** Default configuration has `enable_experimental: false`, but lack of vendor support makes it high-risk for production.
- **Security:** Data is shared with the AI service; responses may be affected by LLM hallucination.
- **Verdict:** Suitable for proof-of-concepts and development environments only.

### Cloud-Hosted (Dremio Cloud) — Conditionally Production-Ready

- **Support:** Managed by Dremio as part of the [[dremio-cloud-edition]].
- **Integration:** Configured via endpoint and OAuth client; operations appear as regular Dremio jobs.
- **Maturity:** Brand new — described as "just the beginning" in launch materials.
- **Verdict:** More architecturally sound for production, but should be phased in cautiously.

## Comparison

Compared to the [[dbt-mcp-server]] (official dbt Labs), the Dremio MCP Server is much newer. The dbt MCP Server has a more established community and is built on the mature dbt Cloud/Rest API.

## Governance Gaps

- No detailed guardrails for destructive agent actions (e.g., `DROP TABLE`, massive `SELECT *` scans).
- No specified query cost limits or row-level security integration for agentic workflows.
- No official benchmarks, rate limits, concurrency limits, or uptime SLAs.