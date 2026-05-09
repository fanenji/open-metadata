---
type: concept
title: Dashboards-as-Code
created: 2026-04-08
updated: 2026-04-08
tags: [bi, ci-cd, version-control, analytics]
related: [lightdash, agentic-bi, ci-cd-for-data-pipelines, dbt-project-scaffolding, dbt]
sources: ["Lightdash  Build Intelligence, not just dashboards..md"]
---
# Dashboards-as-Code

**Dashboards-as-Code** is the practice of managing Business Intelligence dashboards through version-controlled code, enabling software engineering workflows (CI/CD, code review, automated testing) to be applied to analytics.

## Key Principles

- **Version Control:** Dashboards are defined in code (e.g., YAML, JSON) and stored in Git, allowing for change tracking, rollbacks, and collaboration.
- **CI/CD for Analytics:** Changes to dashboards go through automated testing and deployment pipelines, similar to application code.
- **Reusability:** Metric definitions are defined once (e.g., in [[dbt]]) and reused across dashboards, ensuring consistency.
- **Automation:** Tools like [[Lightdash]] enable AI-driven dashboard creation and modification, treating dashboards as code artifacts.

## Relationship to Existing Concepts

- **Extends [[CI-CD-for-data-pipelines]]:** The CI/CD paradigm is extended from data transformation pipelines to the BI reporting layer.
- **Related to [[dbt-project-scaffolding]]:** Both concepts emphasize code-driven, automated workflows for data and analytics.
- **Enables [[agentic-bi]]:** Dashboards-as-Code provides the version-controlled foundation that allows AI agents to autonomously build and refactor analytics.

## Benefits

- Eliminates manual dashboard creation and "final_final_dashboard_v3" confusion.
- Enables automated testing of dashboard changes before deployment.
- Facilitates collaboration through code review and branching strategies.
- Provides a clear audit trail of who changed what and when.