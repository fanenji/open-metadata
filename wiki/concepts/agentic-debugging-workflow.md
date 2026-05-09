---
type: concept
title: Agentic Debugging Workflow
created: 2026-04-21
updated: 2026-04-21
tags: [data-engineering, ai, observability, automation]
related: [data-observability, agentic-skills-pattern, agentic-debugging-workflow]
sources: ["claude-code-is-already-scarily-good-at-data-engineering.md"]
---
# Agentic Debugging Workflow

An **Agentic Debugging Workflow** is a specialized application of AI agents designed to autonomously navigate the lifecycle of a pipeline failure: from detection to remediation and verification.

### Core Requirements
For an agent to successfully execute this workflow, the underlying architecture must provide four pillars:
1. **Metadata & Lineage**: Access to task durations, error messages, and the relationship between data assets.
2. **Code Access**: The ability to read and write to the source code repositories (e.g., GitHub).
3. **Interface (CLI/API)**: Efficient tools (preferably CLI-based for token efficiency) to interact with orchestrators like [[orchestra]] or [[apache-airflow]].
4. **Governance**: Structured instructions (skills) to ensure the agent follows safe, predefined steps.

### The Workflow Lifecycle
1. **Detection**: An observability tool or orchestrator identifies a failed task.
2. **Investigation**: The agent uses the API/CLI to fetch logs and lineage, determining if the failure is due to code (e.g., a dbt test failure) or infrastructure (e.g., a connection error).
3. **Branching**: If code-based, the agent creates a new feature branch in the version control system.
4. **Remediation**: The agent applies a minimal, targeted fix to the code.
5. **Validation**: The agent triggers a pipeline run on the new branch and monitors it until completion.
6. **Promotion**: Upon success, the agent (or a human) merges the fix into the main branch.

### Relationship to Observability
This workflow transforms [[data-observability]] from a passive monitoring capability into an active, autonomous remediation capability.