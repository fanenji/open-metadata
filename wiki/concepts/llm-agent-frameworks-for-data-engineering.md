---
type: concept
title: LLM Agent Frameworks for Data Engineering
created: 2026-04-29
updated: 2026-04-29
tags: [ai, llm, agents, frameworks, data-engineering]
related: [ai-augmented-data-engineering, self-healing-data-pipelines, text2sql-patterns, ritam-mukherjee]
sources: ["Integrating LLMs and AI Agents into Data Engineering Workflows.md"]
---
# LLM Agent Frameworks for Data Engineering

Frameworks for building LLM-based workflows and AI agents that can automate data engineering tasks. These frameworks provide the architectural pattern of chaining prompts, LLM calls, and actions together to create semi-autonomous agents.

## Key Frameworks

- **LangChain/LangGraph**: Popular framework for chaining LLM tasks. Used in the article's log analysis example with `ChatOpenAI`, `PromptTemplate`, and `StrOutputParser`.
- **CrewAI**: Framework for multi-agent setups where multiple AI agents collaborate on complex tasks.

## Agent Chain Pattern

The basic architectural pattern is: Prompt → LLM → Output Parser → Action. This can be scaled with tools for querying databases, alerting Slack, or triggering pipeline actions.

## Integration Points

- **dbt**: AI beta for code generation
- **Airflow**: Custom operators to embed agents
- **Databricks**: Lakehouse AI for built-in LLM support
- **Observability**: WhyLabs or Great Expectations with LLM plugins

## Connection to Existing Wiki

This concept provides the tooling layer for [[ai-augmented-data-engineering]] and connects to the wiki's existing coverage of [[text2sql-patterns]] and [[model-context-protocol]].