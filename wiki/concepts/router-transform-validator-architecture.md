---
type: concept
title: Router-Transform-Validator Architecture
created: 2026-04-29
updated: 2026-04-29
tags: [architecture, ai, agents, etl, data-pipeline]
related: [agent-based-etl-pipeline, llm-agent-guardrails, elt-pattern, dbt-testing-patterns, prem-chandak]
sources: ["I Replaced a Production Data Pipeline with AI Agents — Here’s What Actually Happened.md"]
---
# Router-Transform-Validator Architecture

A three-agent architectural pattern for [[agent-based-etl-pipeline]] design. Each agent has a specific responsibility, and the power of the system comes from how they work together.

## Agent Roles

### Router Agent
- Analyzes incoming data characteristics
- Selects the best processing path (standard, flexible, or custom)
- Maintains routing history to learn which paths work best
- Average decision time: ~145ms

### Transform Agent
- Writes and executes transformation code at runtime
- Builds a library of successful transformation patterns
- Handles edge cases and format variations autonomously
- Subject to [[llm-agent-guardrails]] including batch size limits and execution timeouts
- Average success rate: 99.9% (with retries)

### Validator Agent
- Checks output correctness against target schema
- Validates data quality dimensions (accuracy, completeness, consistency)
- Rejects invalid transformations for retry
- Average validation time: ~89ms
- Rejection rate: ~0.08%

## Data Flow

```
Data Source
    ↓
Router Agent ──→ [Path A] Transform Agent → Validator → Output
    ├─→ [Path B] Transform Agent → Validator → Output  
    └─→ [Path C] Transform Agent → Validator → Output
         ↓
    [Learns from failures]
```

## Key Design Principles

1. **Simplicity**: Each agent has a single, well-defined responsibility
2. **Context Sharing**: Agents maintain and share context (routing history, successful transforms, validation criteria)
3. **Self-healing**: On failure, the Router can retry with an alternative path
4. **Observability**: All decisions, reasoning, and outcomes are logged for transparency

## Relationship to Existing Concepts

- **[[elt-pattern]]**: Represents a dynamic, runtime-generated alternative to predefined ELT transformations
- **[[dbt-testing-patterns]]**: The Validator agent parallels dbt's test patterns but uses LLM reasoning instead of SQL assertions
- **[[data-quality-dimensions]]**: The Validator checks multiple quality dimensions simultaneously
