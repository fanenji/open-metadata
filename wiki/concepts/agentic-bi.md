---
type: concept
title: Agentic BI
created: 2026-04-08
updated: 2026-04-08
tags: [bi, ai, automation, analytics]
related: [lightdash, dashboards-as-code, ci-cd-for-data-pipelines, text2sql-patterns, dbt]
sources: ["Lightdash  Build Intelligence, not just dashboards..md"]
---
# Agentic BI

**Agentic BI** refers to a paradigm in Business Intelligence where AI systems can autonomously build, refactor, and ship analytics. This goes beyond traditional BI tools that require manual dashboard creation or simple natural language query interfaces.

## Characteristics

- **Autonomous Analytics:** AI agents can create, modify, and deploy dashboards without human intervention.
- **Code-Driven:** Analytics artifacts (dashboards, metrics, reports) are treated as code, enabling version control and CI/CD.
- **dbt Integration:** Agentic BI platforms like [[Lightdash]] integrate with [[dbt]] to reuse metric definitions, ensuring consistency.
- **Natural Language Interfaces:** Users can query data using natural language, but the AI handles the underlying complexity.

## Relationship to Existing Concepts

- **Extends [[text2sql-patterns]]:** Agentic BI takes natural language queries a step further by automating the entire analytics workflow, not just SQL generation.
- **Extends [[CI-CD-for-data-pipelines]]:** The concept of CI/CD is extended from data pipelines to the BI layer, enabling dashboards-as-code.
- **Related to [[dashboards-as-code]]:** Dashboards-as-code is a key enabler of Agentic BI, providing the version-controlled foundation for AI-driven changes.

## Open Questions

- How does Agentic BI ensure data governance and semantic consistency when AI agents make changes?
- What is the balance between automation and human oversight in Agentic BI workflows?
- How mature are Agentic BI platforms in production environments?