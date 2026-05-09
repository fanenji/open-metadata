---
type: concept
title: Augmentative vs Autonomous Adoption
created: 2026-04-04
updated: 2026-04-04
tags: [ai-adoption, governance, data-engineering, llm, risk-management]
related: [ai-copilot-for-data-engineering, llm-generated-dbt-tests, CI-CD-for-data-pipelines, data-quality-dimensions]
sources: ["Integrating LLMs and AI Agents into Data Engineering Workflows 1.md"]
---
# Augmentative vs Autonomous Adoption

Augmentative vs Autonomous Adoption is a decision framework for integrating LLMs and AI agents into data engineering workflows. The article by [[Ritam Mukherjee]] argues that current best practice is **augmentative** — AI acts as a copilot assisting humans, not replacing them.

## Augmentative Approach (Recommended)

- AI generates drafts, humans review and approve
- Human-in-the-loop for all production deployments
- AI handles 30-40% of repetitive, mechanical work
- Humans focus on logic, architecture, and edge cases

## Autonomous Approach (Future Goal)

- AI detects issues and deploys fixes automatically
- Self-healing pipelines with no human intervention
- Requires high reliability and trust in AI outputs
- Not yet production-ready for most organizations

## Mitigation Strategies

1. **Always review outputs** before deployment
2. **Use fine-tuned or self-hosted models** (e.g., via [[Ollama]]) for sensitive data
3. **Add unit tests** with human-in-the-loop approvals
4. **Monitor the AI agent** itself for reliability

## Connections to Existing Wiki

- Aligns with [[CI-CD-for-data-pipelines]] human-in-the-loop approval patterns
- Informs governance decisions for [[ai-copilot-for-data-engineering]]
- Relevant to risk assessment for [[llm-generated-dbt-tests]]