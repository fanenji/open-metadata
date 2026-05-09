---
type: concept
title: Downstream Lineage
created: 2026-04-04
updated: 2026-04-04
tags: [lineage, dbt, data-governance]
related: [dbt-exposures, impact-analysis, dbt-catalog, dbt-dag-generator]
sources: ["Why aren’t you using dbt Exposures?.md"]
---
# Downstream Lineage

Downstream lineage extends the data lineage graph beyond final data models to include business-relevant downstream assets such as BI dashboards, reports, notebooks, ML models, and applications. In dbt projects, [[dbt-exposures]] are the primary mechanism for documenting this downstream lineage.

## Importance

- Transforms the DAG from a technical artifact into a value chain visible to business stakeholders.
- Enables [[impact-analysis]] by showing which business assets depend on which models.
- Reduces the "break something" anxiety during model changes.
- Facilitates proactive communication with downstream consumers.

## Relationship to Technical Lineage

The wiki already documents technical lineage concepts ([[dbt-dag-generator]], column-level lineage via dbt-fusion). Downstream lineage adds the *business* dimension, connecting technical artifacts to their business impact.