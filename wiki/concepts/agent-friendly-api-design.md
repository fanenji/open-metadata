---
type: concept
title: Agent-Friendly API Design
created: 2026-04-04
updated: 2026-04-04
tags: [api, ai, agents, data-engineering]
related: [context-engineering, model-context-protocol, dremio-mcp-server, dbt-mcp-server]
sources: ["The 2026 Data Engineering Roadmap Building Data Systems for the Agentic AI Era.md"]
---
# Agent-Friendly API Design

Traditional data APIs were designed for applications that knew exactly what they wanted. Agent-friendly APIs need to be more flexible and self-describing, as AI agents interact with data systems differently than humans or traditional applications.

## Key Characteristics

- **Schema discovery endpoints**: Agents need to ask "what data do you have?" and receive useful, structured responses.
- **Semantic query interfaces**: Beyond SQL, agents benefit from interfaces that allow them to express intent rather than exact queries. Natural language interfaces, semantic search, and intent-based querying become important.
- **Capability declarations**: APIs should declare their capabilities in machine-readable ways — supported query types, rate limits, freshness guarantees.
- **Actionable error handling**: When things go wrong, agent-friendly APIs provide actionable guidance, not just error codes. They suggest alternatives, explain limitations, and help agents recover gracefully.

## Agentic Workload Patterns

- **Discovery-oriented access**: Agents often don't know exactly what data exists. Systems need to support exploration, search, and self-describing data structures.
- **Iterative refinement**: Agents query, evaluate results, and refine their approach. Systems must support this iterative pattern efficiently.
- **Explanation and provenance**: Every piece of information needs clear provenance and attribution so agents can explain their reasoning.
- **Feedback loops**: Systems should learn from agent interactions, feeding success signals back into metadata and relevance rankings.

## Relationship to Existing Wiki

This concept connects to [[model-context-protocol]] as a standardization approach for agent-tool interaction. Concrete implementations like [[dremio-mcp-server]] and [[dbt-mcp-server]] are examples of agent-friendly API design in practice.
