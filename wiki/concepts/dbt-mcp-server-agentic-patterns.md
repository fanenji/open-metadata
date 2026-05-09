---
type: concept
title: dbt MCP Server Agentic Patterns
created: 2026-05-07
updated: 2026-05-07
tags: [dbt, mcp, ai, automation, agentic]
related: [dbt-mcp-server, dbt-mcp-server-tools-reference, dbt-mcp-server-deployment-modes]
sources: ["the-dbt-mcp-server-how-ai-finally-gets-to-talk-to-your-data-the-right-way.md"]
---
# dbt MCP Server Agentic Patterns

The [[dbt-mcp-server]] enables LLM-orchestrated automation of dbt workflows. This page documents the key agentic patterns.

## Migration Agent Pattern

Indicium, a data consulting company, built a migration agent using the dbt MCP server that automates legacy-to-dbt migrations. They reported cutting migration timelines by up to 90%.

**Workflow:**
1. Agent calls `get_all_sources` to understand available raw data
2. Agent calls `generate_staging_model` to scaffold initial SQL
3. Agent calls `generate_model_yaml` to create documentation and tests
4. Agent calls `compile` to validate Jinja/SQL
5. Agent calls `run` to materialize the model
6. Agent calls `test` to validate data integrity
7. Agent calls `get_model_health` to confirm the model is healthy

All steps orchestrated by an LLM using governed dbt context.

## Debugging Agent Pattern

When a model fails, the AI assistant can:
1. Call `get_job_run_error` to fetch the actual run error
2. Analyze the error in context of the model's lineage
3. Suggest or apply fixes
4. Re-run and validate

## CI/CD Agent Pattern

In automated pipelines, the agent can:
1. Detect changed models via state comparison
2. Generate and validate YAML for new models
3. Run tests on affected models only
4. Report results and health status

## Conversational Data Access Pattern

Non-technical users interact via natural language:
1. User asks a business question (e.g., "What was week-over-week growth in signups?")
2. Agent calls `list_metrics` to find governed metrics
3. Agent calls `query_metrics` with appropriate dimensions and time grains
4. Returns consistent answer grounded in organizational business logic

## Key Considerations

- Full CLI access enables powerful automation but carries warehouse modification risk
- Use `DISABLE_DBT_CLI=true` in production consumption setups
- Monitor Copilot credit consumption — `text_to_sql` is the only credit-consuming tool
- Pin `dbt-mcp` versions to avoid breaking changes in automated workflows