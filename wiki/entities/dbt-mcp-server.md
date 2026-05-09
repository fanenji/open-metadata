---
type: entity
title: dbt MCP Server
created: 2026-04-04
updated: 2026-05-07
tags: ["dbt", "mcp", "ai", "data-governance", "tool"]
related: ["model-context-protocol", "dbt-semantic-layer", "dbt-fusion", "dbt-cloud", "dbt-core", "dbt-labs", "dbt-mcp-server-deployment-modes", "dbt-mcp-server-tools-reference", "dbt-mcp-server-setup-guide", "dbt-mcp-server-agentic-patterns", "dbt-mcp-server-credit-management", "dbt-catalog", "dbt-lsp"]
sources: ["the-dbt-mcp-server-how-ai-finally-gets-to-talk-to-your-data-the-right-way.md", "dbt-labsdbt-mcp A MCP (Model Context Protocol) server for interacting with dbt..md"]
---
# dbt MCP Server

The **dbt MCP Server** is an official, production-ready [[model-context-protocol]] (MCP) server developed by [[dbt-labs]]. It provides a structured, standardized bridge for AI agents (such as Claude, Cursor, VS Code Copilot) to interact with dbt projects across [[dbt-core]], [[dbt-fusion]], and dbt Platform. It enables governed access to models, metrics, lineage, freshness signals, and CLI operations.

## Architecture

The server supports two deployment modes:

- **Local MCP Server**: Runs on the developer's machine with full dbt CLI access (`run`, `test`, `build`, `compile`, `docs`, `show`, `list`, `parse`), code generation capabilities, column-level lineage via the [[dbt-fusion]] engine, and optional [[dbt-cloud]] API access.
- **Remote MCP Server**: Hosted by dbt, requires zero local installation, connects via HTTP. Provides Semantic Layer queries, SQL execution, metadata discovery, and administrative API access for data consumers.

An architecture diagram is available in the [official repository](https://github.com/dbt-labs/dbt-mcp).

## Tool Categories

The server exposes 40+ tools across the following categories:

### dbt CLI Tools (local only)
- `build`, `compile`, `docs`, `get_lineage_dev`, `get_node_details_dev`, `list`, `parse`, `run`, `show`, `test`

### Semantic Layer Tools (local + remote)
- `get_dimensions`, `get_entities`, `get_metrics_compiled_sql`, `list_metrics`, `list_saved_queries`, `query_metrics`
- Query and explore the [[dbt Semantic Layer]].

### Discovery Tools (local + remote)
- Retrieve models, sources, exposures, lineage, macros, seeds, snapshots, tests, and model health/performance via the [[dbt Discovery API]].

### SQL Tools (local + remote)
- `execute_sql`: Executes SQL on dbt Platform infrastructure with Semantic Layer support.
- `text_to_sql`: Generates SQL from natural language using project context.

### Codegen Tools (local only)
- `generate_model_yaml`, `generate_source`, `generate_staging_model`: Automate boilerplate code generation.

### Administrative API Tools (requires connection to dbt Cloud)
- `cancel_job_run`, `get_job_details`, `get_job_run_artifact`, `get_job_run_details`, `get_job_run_error`, `get_project_details`, `list_job_run_artifacts`, `list_jobs`, `list_jobs_runs`, `list_projects`, `retry_job_run`, `trigger_job_run`
- Manage dbt Platform jobs and projects via the [[dbt Administrative API]].

### Fusion Tools (local + remote)
- `fusion.compile_sql`, `fusion.get_column_lineage`, `get_column_lineage`: Leverage the Fusion engine for advanced SQL compilation and column-level lineage analysis.

### Product Docs (local + remote)
- `get_product_doc_pages`, `search_product_docs`: Search and fetch content from docs.getdbt.com.

### MCP Server Metadata
- `get_mcp_server_branch`, `get_mcp_server_version`: Return information about the running server.

### Experimental MCP Bundle
An experimental Model Context Protocol Bundle (`dbt-mcp.mcpb`) is published with each release, enabling MCPB-aware clients to import the server without additional setup.

## Key Use Cases

- **Conversational data access**: Non-technical users query governed metrics via natural language.
- **Agentic dbt automation**: LLM-orchestrated migration, debugging, and CI/CD workflows.
- **AI-accelerated IDE development**: Context-aware assistance in Cursor, VS Code, or Claude Code.

## Security & Operational Considerations

- The dbt CLI tools can modify data models, sources, and warehouse objects. The server documentation explicitly warns: "Proceed only if you trust the client and understand the potential impact." In production consumption setups, use `DISABLE_DBT_CLI=true` to prevent warehouse modification.
- `text_to_sql` is the only tool consuming dbt Copilot credits; credit exhaustion blocks all tools.
- Pin `dbt-mcp` versions in production to avoid breaking changes from `uvx dbt-mcp` defaulting to the latest version.
- Store sensitive environment variables in `.env` files referenced via `--env-file`.

## Dependencies

Dependencies are pinned to specific versions. Only security-related updates are submitted via automated pull requests.

## Setup

Three deployment paths are available:
- **Local MCP + dbt Platform** (recommended for engineers)
- **Local MCP without dbt Cloud** (for dbt Core users)
- **Remote MCP** (zero-install for analysts and consumers)

See [[dbt-mcp-server-setup-guide]] for detailed instructions.

## Feedback

Community feedback is welcome via GitHub Issues or the `#tools-dbt-mcp` channel in the [dbt Community Slack](https://www.getdbt.com/community/join-the-community).