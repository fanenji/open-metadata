---
type: entity
title: dbt Agent Skills
created: 2026-05-09
updated: 2026-05-09
tags: [dbt, ai-agents, mcp, open-source]
related: [dbt-mcp-server, model-context-protocol, dbt-agent-skills-benchmark, dbt-semantic-layer-syntax-drift, abhishek-kumar-gupta]
sources: ["dbt-agent-skills-the-playbook-that-makes-ai-actual-20260509.md"]
---
# dbt Agent Skills

An open-source collection of structured Markdown instructions that encode expert dbt workflows for AI coding agents. Maintained by [[dbt Labs]], the skills transform generalist AI assistants into specialized dbt practitioners by teaching correct iteration patterns, validation steps, and governance checks.

## Architecture

- **MCP + Agent Skills Layered Architecture**: MCP provides tool access (models, lineage, CLI); Agent Skills provide the knowledge layer (when to call tools, in what order, what to check).
- Skills are plain Markdown files loaded as system prompts or custom instructions.
- Built on an open standard written and donated by Anthropic, adopted by 30+ AI agents/platforms.

## Skill Categories

1. **Analytics Engineering** — Core iterative dbt development workflow: explore upstream context, build incrementally, validate at each step, never ship without tests.
2. **Semantic Layer** — Correct MetricFlow syntax and governed metric querying, addressing [[dbt-semantic-layer-syntax-drift]].
3. **Platform Operations** — Infrastructure and operational tasks.
4. **Migration** — Multi-step migration playbooks (e.g., migrating to dbt Fusion).

## Setup

Clone the [dbt-labs/dbt-agent-skills](https://github.com/dbt-labs/dbt-agent-skills) repo and load skills via agent-specific mechanisms (e.g., `claude skills add`, `.cursor/rules`, Copilot Custom Instructions). Pair with the [[dbt-mcp-server]] for full context.

## Relationship to Existing Wiki

- Complements [[dbt-mcp-server]] by providing the knowledge layer that makes MCP useful for production work.
- Extends [[model-context-protocol]] by showing how MCP is operationalized with a knowledge layer.
- Related to [[dbt-osmosis-llm-module]] (both address AI-assisted dbt work, but Agent Skills focus on workflow behavior while dbt-osmosis focuses on documentation generation).
- Related to [[dbt-data-contract-implementation]] and [[dbt-observability-implementation]] (both encode governance and validation patterns).