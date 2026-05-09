---
type: concept
title: dbt Exposures
created: 2026-04-29
updated: 2026-05-07
tags: [dbt, lineage, data-governance, documentation]
related: [dbt-core, dbt-project-scaffolding, data-lineage, dbt-catalog, dbt-observability-implementation, data-contract-observability, dbt-cloud, elementary-dbt-package, downstream-lineage, impact-analysis]
sources: ["How to get started with dbt.md", "Why aren’t you using dbt Exposures?.md", "Why aren't you using dbt Exposures?.md"]
---

# dbt Exposures

dbt Exposures are a YAML-based documentation entity within [[dbt Core]] projects that explicitly define downstream consumption of data models — such as dashboards, reports, notebooks, ML models, and applications. By declaring exposures, users extend the dbt DAG beyond the warehouse to include business-relevant assets, enabling full lineage tracking from raw sources through transformations to final outputs.

## YAML Syntax

Exposures are defined in a YAML file (commonly named `exposures.yml`) inside a dbt project. Below is a typical example:

```yaml
exposures:
  - name: executive_revenue_dashboard
    type: dashboard
    maturity: high
    url: https://looker.yourcompany.com/dashboards/executive_revenue_dashboard
    description: |
      Executive-facing dashboard showing monthly revenue KPIs.
    depends_on:
      - ref('fct_revenue')
      - ref('dim_date')
    owner:
      name: Joe Analyst
      email: joe.analyst@company.com
```

Each exposure can optionally include `type`, `maturity`, `url`, `description`, `depends_on` (list of model refs), and `owner` information.

## Supported Types

| Type            | Description                                      |
|-----------------|--------------------------------------------------|
| `dashboard`     | BI dashboards (Looker, Mode, Tableau, etc.)      |
| `notebook`      | Data science notebooks                           |
| `analysis`      | Ad‑hoc analyses                                  |
| `ml`            | Machine learning models                          |
| `application`   | Downstream applications                          |

## Maturity Levels

The optional `maturity` field indicates the criticality of the downstream asset:

- `low`
- `medium`
- `high`

This helps prioritise communication and effort when upstream changes occur.

## Benefits

- **Explicit downstream connections** — Documents where data ends up, reducing the “black box” of data warehouses.
- **Business-relevant lineage** — Extends the DAG from technical models to business value, reframing it as a data supply chain.
- **Proactive change management** — Enables informed communication with stakeholders before breaking changes are made.
- **Improved impact analysis** — Shows which business assets depend on which models, allowing you to assess the blast radius of modifications.
- **Data governance** — Captures ownership, criticality, and usage context, strengthening accountability.
- **Model review facilitation** — Answers questions about model purpose, ownership, and continued relevance, making model reviews more productive.

## Implementation Options

- **Manual** — Write exposure YAML by hand. Simple but does not scale well.
- **Scripted** — Use BI tool APIs to auto‑generate exposure files from dashboards, reports, etc.
- **dbt Cloud Integration** — Native integrations with tools like Tableau can create and maintain exposures automatically.

## Relationship to Other Concepts

- [[dbt-catalog]] — Exposures extend the catalog with downstream usage metadata.
- [[dbt-observability-implementation]] — Exposures complement run and test monitoring for full observability.
- [[data-contract-observability]] — Exposures can serve as the “consumer side” of data contracts.
- [[downstream-lineage]] — Exposures are the primary mechanism for documenting downstream lineage in dbt.
- [[impact-analysis]] — Exposures enable impact analysis by showing which business assets depend on which models.

By defining exposures, teams move from a narrow warehouse‑centric view to a broader data‑supply‑chain perspective, improving trust and collaboration around data assets.