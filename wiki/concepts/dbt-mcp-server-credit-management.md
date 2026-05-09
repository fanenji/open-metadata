---
type: concept
title: dbt MCP Server Credit Management
created: 2026-05-07
updated: 2026-05-07
tags: [dbt, mcp, credits, cost-management]
related: [dbt-mcp-server, dbt-mcp-server-deployment-modes, dbt-mcp-server-tools-reference]
sources: ["the-dbt-mcp-server-how-ai-finally-gets-to-talk-to-your-data-the-right-way.md"]
---
# dbt MCP Server Credit Management

The [[dbt-mcp-server]] has a critical operational constraint related to dbt Copilot credit consumption.

## Credit Consumption Model

- **Only `text_to_sql` consumes dbt Copilot credits** — all other tools (Semantic Layer queries, discovery, CLI operations, code generation) do not consume credits
- If Copilot credits run out, the **remote MCP server blocks all tools** — including those proxied from the local server
- This creates a single point of failure for production consumption setups

## Mitigation Strategies

1. **Monitor credit usage** — Track consumption if on a plan with limits
2. **Use `execute_sql` instead of `text_to_sql`** — Manually crafted queries bypass credit consumption
3. **Prefer Semantic Layer queries** — `query_metrics` does not consume credits and provides governed results
4. **Set up credit alerts** — Configure notifications before exhaustion
5. **Consider plan tier** — Higher tiers may offer more generous credit allocations

## Best Practices

- In high-usage setups, design workflows to minimize `text_to_sql` calls
- Cache common metric queries to avoid redundant credit consumption
- Document credit consumption patterns for team awareness
- Test credit impact during development before production deployment