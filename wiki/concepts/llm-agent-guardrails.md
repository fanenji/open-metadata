---
type: concept
title: LLM Agent Guardrails
created: 2026-04-29
updated: 2026-04-29
tags: [ai, agents, safety, governance, data-pipeline]
related: [agent-based-etl-pipeline, router-transform-validator-architecture, data-observability-definition, data-incident-management, prem-chandak]
sources: ["I Replaced a Production Data Pipeline with AI Agents — Here’s What Actually Happened.md"]
---
# LLM Agent Guardrails

Safety patterns and constraints for autonomous AI agents operating in production data pipelines. These guardrails are essential to prevent agents from making harmful decisions while preserving their ability to handle unpredictable situations effectively.

## Core Principles

1. **Explicit Boundaries**: Define clear lists of what agents can and cannot do autonomously
2. **Human-in-the-loop Approval**: Require human authorization for high-risk actions
3. **Observability**: Track all agent decisions, reasoning, and outcomes transparently
4. **Fail-safe Recovery**: Agents should retry with alternative approaches on failure

## Boundary Categories

### Allowed (Tactical Decisions)
- Write transformation code
- Choose processing paths
- Retry failed operations
- Adapt to format changes

### Prohibited (Strategic Decisions)
- Change data schemas
- Delete data
- Modify access controls
- Reprocess historical data without approval

## Approval Gate Pattern

When an agent detects a high-risk action is needed, it sends a Slack message with:
- Action type and scope
- Risk level assessment
- Reasoning for the action
- Timeout for human response (e.g., 5 minutes)

The agent waits for explicit approval before proceeding.

## Observability Dashboard

A production guardrail system includes a real-time dashboard showing:
- Agent decisions per time period
- Path distribution (standard vs. flexible vs. custom)
- Average decision and validation times
- Success/failure rates
- Code reuse percentage
- Rejection rate

## Relationship to Existing Concepts

- **[[data-observability-definition]]**: Agent observability extends observability principles to AI decision-making
- **[[data-incident-management]]**: Guardrails prevent incidents by constraining agent autonomy
- **[[data-contract-implementation]]**: Guardrails can serve as runtime enforcement of data contracts
