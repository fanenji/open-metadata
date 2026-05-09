---
type: concept
title: Agentic Skills Pattern
created: 2026-04-21
updated: 2026-04-21
tags: [ai, agent, automation, deterministic]
related: [claude-code-is-already-scarily-good-at-data-engineering.md, model-context-protocol]
sources: ["claude-code-is-already-scarily-good-at-data-engineering.md"]
---
# Agentic Skills Pattern

The **Agentic Skills Pattern** involves using structured, markdown-based instructions (often stored in files like `SKILL.md`) to define specific, repeatable, and deterministic workflows for an AI agent.

### Purpose
Instead of relying on the agent's general reasoning to "figure out" a complex process, a "skill" provides a step-by-step directive. This prevents the agent from "breaking through the window"—performing unpredictable or destructive actions—by constraining its behavior to a known-good sequence of tool calls and logic.

### Example Workflow: `fix-and-rerun-pipeline`
A skill for pipeline remediation might include:
1. **Verification**: Check the failed task status via API.
2. **Diagnosis**: Read logs and identify if the error is code-based or infrastructure-based.
3. **Remediation**: If code-based, create a GitHub branch, apply a minimal fix, and commit.
4. **Validation**: Re-run the pipeline on the new branch and poll for completion.

### Benefits
- **Reliability**: Reduces non-deterministic behavior in critical infrastructure.
- **Token Efficiency**: Provides only the necessary instructions for a specific task rather than a massive API definition.
- **Maintainability**: Skills can be versioned and updated alongside the data pipelines they manage.