---
type: entity
title: DBT Dragons
created: 2026-04-04
updated: 2026-05-07
tags: ["team", "blablacar", "dbt", "data-mesh", "scaling"]
related: ["blablacar", "dbt-migration-strategy", "data-mesh", "thibault-ambard", "tushar-bhasin", "dbt-scaling-patterns", "dbt-project-governance"]
sources: ["One Thousands and One dbt Models How BlaBlaCar Moved to dbt in 12 months.md", "One Thousands and One dbt Models How BlaBlaCar Moved to dbt in 12 months - Summary.md"]
---
# DBT Dragons

The **DBT Dragons** were an internal expert group at [[blablacar]] formed to scale dbt knowledge across a ~50-person data team during their 12-month dbt migration. The group was part of BlaBlaCar's animal-themed team naming convention and consisted of domain champions embedded within a [[data-mesh]] organization.

## Structure

- **~8-10 domain champions** identified from each domain team who showed high engagement during early training
- Served as the go-to contacts for dbt questions within their respective domains
- Attended deeper technical sessions beyond the onboarding workshops offered to regular ICs
- Embedded in squads, enabling decentralized support in a data-mesh setup

## Responsibilities

The DBT Dragons model was created to avoid a bottleneck on the 2 core dbt authors who initially led the migration. By distributing expertise across domain teams, BlaBlaCar achieved:

- Building onboarding for the rest of the data services (50+ ICs)
- Supporting migration in a decentralized manner across squads
- Developing additional features for the dbt framework (DAG generator, dev environment)
- Taking feedback from users and identifying improvements
- Reduced centralized support burden
- Faster feedback cycles within domain teams
- More context-aware support (domain experts understand both dbt and their team's business logic)

## Related Patterns

The DBT Dragons model is a practical implementation of the [[dbt-scaling-patterns]] concept, specifically addressing the knowledge distribution challenge when scaling dbt adoption across a large organization, and aligns with data-mesh principles for decentralized ownership.