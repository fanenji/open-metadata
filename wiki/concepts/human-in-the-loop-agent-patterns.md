---
type: concept
title: Human-in-the-loop Agent Patterns
created: 2026-04-21
updated: 2026-04-21
tags: [ai, reliability, governance, software-engineering]
related: [agentic-skills-pattern, data-observability]
sources: ["claude-code-is-already-scarily-good-at-data-engineering.md"]
---
# Human-in-the-loop Agent Patterns

As AI agents move from "one-shot" generators to autonomous operators in production environments, the **Human-in-the-loop (HITL)** pattern becomes critical for maintaining trust and reliability.

### The Pause/Continue Pattern
Rather than treating an agent as a black box that executes a task and returns a result, the **Pause/Continue** pattern treats the agent like an "intern." The agent is empowered to perform the bulk of a task but is explicitly programmed to trigger a `pause_for_human` tool when it encounters:
- Ambiguity or lack of information.
- High-risk operations (e.g., deleting a production branch).
- The need for explicit approval.

### Implementation via Sessions
This pattern is best implemented using **Agent Sessions**. A session maintains the state, history, and context of an interaction. Using frameworks like FastAPI, an agent can:
1. **Pause**: Save a checkpoint and return a `status: "paused"` response to the caller.
2. **Wait**: The system waits for a human to provide feedback or a "continue" command.
3. **Resume**: The agent resumes from the saved checkpoint, incorporating the new human input into its context.

### Importance for Data Engineering
In data engineering, where a single incorrect SQL command can corrupt downstream tables, HITL patterns ensure that autonomous remediation (e.g., fixing a broken dbt model) is subject to human oversight before being merged into production.