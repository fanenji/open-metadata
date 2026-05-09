---
type: concept
title: Context Engineering
created: 2026-04-04
updated: 2026-04-04
tags: [context, ai, data-engineering, metadata]
related: [context-architect-role, context-store, context-propagation, contextualize-pipeline, ECL-framework, active-metadata-management, agent-friendly-api-design]
sources: ["The 2026 Data Engineering Roadmap Building Data Systems for the Agentic AI Era.md"]
---
# Context Engineering

Context engineering is the practice of designing data systems that embed rich, machine-readable context alongside the data itself. It is identified as the most critical emerging skill for data engineers in the agentic AI era, as AI agents need context — not just data — to discover, understand, and utilize information without human intervention.

## Dimensions of Context

- **Semantic Context**: Business meaning, nuances, and edge cases of data. Captures distinctions that AI systems can reason about (e.g., "customer" in one system vs. another).
- **Temporal Context**: When data was created, last updated, and the state of the world at capture time. Crucial for AI agents making decisions based on historical data.
- **Relational Context**: How data relates to other datasets, dependencies, and meaningful joins.
- **Quality Context**: Reliability, known issues, limitations, and trustworthiness of data.
- **Provenance Context**: Origin, transformations, and systems that have touched the data.

## Relationship to Existing Wiki Concepts

Context engineering provides a unifying framework for several existing wiki concepts:
- [[context-architect-role]] — The role that practices context engineering.
- [[context-store]] — The infrastructure that stores context.
- [[context-propagation]] — How context travels through pipelines.
- [[contextualize-pipeline]] — The pipeline that infers and stores context.
- [[ECL-framework]] — The Extract, Contextualize, Link framework, which context engineering operationalizes.

## Key Insight

AI agents lack the institutional knowledge that human analysts bring. Context engineering explicitly encodes this knowledge into data systems, enabling autonomous agents to make intelligent decisions about data usage.
