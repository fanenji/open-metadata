---
type: entity
title: Lightdash
created: 2026-04-08
updated: 2026-04-08
tags: [bi, open-source, ai-native, dbt, analytics]
related: [agentic-bi, dashboards-as-code, dbt-cloud, dbt, looker, ci-cd-for-data-pipelines, text2sql-patterns]
sources: ["Lightdash  Build Intelligence, not just dashboards..md"]
---
# Lightdash

**Lightdash** is an open-source, AI-native Business Intelligence (BI) platform designed for modern data teams. It integrates directly with [[dbt]] to define metrics once and provide instant, trustworthy insights across an organization.

## Key Features

- **Agentic BI:** AI can build, refactor, and ship analytics autonomously, reducing manual dashboard creation.
- **Dashboards-as-Code:** Dashboards are managed through version-controlled code, enabling [[CI-CD-for-data-pipelines]] for analytics.
- **dbt Integration:** Connects to dbt projects to reuse metric definitions, ensuring consistency between transformation and reporting.
- **Unlimited User Seats:** Pricing model that avoids per-user licensing costs, positioning it as an alternative to [[Looker]].
- **Natural Language Queries:** Improves data discoverability and governance.
- **Usage Analytics:** Tracks BI adoption within the organization.
- **Developer Workflows:** CLI and code-based tools for data teams.
- **Enterprise Security:** SOC2 Type II and HIPAA compliant.

## Positioning

Lightdash is positioned as a cheaper, more developer-friendly alternative to Looker. It competes with or complements [[dbt-cloud]]'s built-in catalog and discovery features. The platform targets teams that want to move from manual analytics to automated, code-driven workflows.

## Open Questions

- How does Lightdash's "Agentic BI" handle data governance and semantic consistency compared to a governed dbt project?
- Is Lightdash a viable replacement for dbt Cloud's built-in catalog, or is it complementary?
- What is the actual maturity and adoption of Lightdash in production environments?