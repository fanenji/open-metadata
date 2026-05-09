---
type: source
title: Claude code is already scarily good at data engineering
authors: [Hugo Lu]
year: 2026
url: "https://medium.com/@hugolu87/claude-code-is-already-scarily/2b238d8ee573"
venue: "Medium"
tags: [ai, data-engineering, agentic-workflows, claude]
related: [agentic-skills-pattern, human-in-the-loop-agent-patterns, agentic-debugging-workflow]
sources: ["claude-code-is-already-scarily-good-at-data-engineering.md"]
---
# Claude code is already scarily good at data engineering

An article by Hugo Lu demonstrating how AI agents (specifically Claude Code) can be used to autonomously debug, fix, and test data engineering pipelines using metadata, CLI tools, and structured "skills."

The author argues that for an agent to be effective, the architecture must provide:
1. **Metadata and Lineage**: Task durations, error messages, and asset history.
2. **Code Access**: Ability to read and write to repositories.
3. **CLI/API Interfaces**: Preferring CLI tools over MCP for token efficiency.
4. **Governance**: Structured instructions (skills) and human-in-the-loop (HITL) patterns.

The article also introduces the **Pause/Continue** pattern using FastAPI to handle agent interactivity and reliability.