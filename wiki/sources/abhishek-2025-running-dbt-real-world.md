---
type: source
title: "Running dbt in the Real World: Cost Control, Governance, and Team Practices at Scale"
created: 2026-05-06
updated: 2026-05-06
tags: [dbt, cost-control, governance, team-practices, operating-model]
related: [dbt-cost-control, dbt-query-tagging, dbt-runbooks, dbt-minimum-model-standards, dbt-job-design-by-layer, dbt-slim-ci, write-audit-publish-pattern, dbt-observability-implementation, data-contract-observability, data-domain-governance, abhishek-kumar-gupta]
sources: ["Running dbt in the Real World Cost Control, Governance, and Team Practices at Scale.md"]
authors: [Abhishek Kumar Gupta]
year: 2025
url: "https://medium.com/tech-with-abhishek/running-dbt-in-the-real-world-cost-control-governance-and-team-practices-at-scale-3699f3693fed"
venue: "Medium (Tech with Abhishek)"
---
# Running dbt in the Real World: Cost Control, Governance, and Team Practices at Scale

This article by [[Abhishek Kumar Gupta]] (published December 29, 2025) addresses the operational challenges of running dbt at scale in organizations with many engineers, domains, and stakeholders. The core thesis is that success depends on building a system around models — cost control, governance, and team workflows — not just writing SQL.

## Key Contributions

1. **Cost-Aware dbt**: Practical levers for controlling warehouse spend, including incremental models, Slim CI (`state:modified`), job grouping by layer, and off-peak scheduling.
2. **Query Tagging for Cost Attribution**: A pattern for setting warehouse query tags from dbt config to attribute cost to projects, jobs, environments, and domains, enabling cost-back conversations.
3. **Governance Role Model**: Clear separation of responsibilities between Platform/Data Infra Team, Domain/Data Product Owners, and Analytics Engineers/Contributors.
4. **Minimum Model Standards**: Codified rules requiring tests (`not_null`, `unique`, relationships), enforced contracts, and documentation for production-facing models.
5. **Team Workflows**: Small focused PRs, local dev with `dbt build --select <model>+`, CI with `state:modified+`, and the Write–Audit–Publish (WAP) promotion pattern.
6. **Operational Maturity**: Cost dashboards, reliability/quality dashboards, and runbooks for incident response.

## Connections to Existing Wiki

This article strengthens existing concepts like [[dbt-slim-ci]], [[write-audit-publish-pattern]], [[dbt-observability-implementation]], and [[data-contract-observability]]. It introduces new concepts including [[dbt-cost-control]], [[dbt-query-tagging]], [[dbt-runbooks]], [[dbt-minimum-model-standards]], and [[dbt-job-design-by-layer]].