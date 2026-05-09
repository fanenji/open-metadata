---
type: source
title: How to manage and schedule dbt
created: 2026-04-29
updated: 2026-04-29
tags: [dbt, management, scheduling, devops, data-engineering]
related: [dbt-cloud, dbt-core, dbt-project-organization-strategies, dbt-developer-experience, dbt-alternatives-to-cloud, dbt-mesh, dbt-project-scaffolding, dbt-git-branching-strategies]
sources: ["How to manage and schedule dbt.md"]
authors: [blef-fr]
year: 2022
url: "https://www.blef.fr/manage-and-schedule-dbt"
venue: "blef.fr"
---
# How to manage and schedule dbt

A comprehensive guide by Christophe Blefari (blef.fr) covering the organizational and technical aspects of managing and scheduling dbt projects in production. The article was motivated by dbt Labs' 2022 pricing changes for dbt Cloud (100% increase to $100/month/dev, 8-dev team limit, opaque Enterprise pricing), but focuses on the broader questions of dbt management and scheduling regardless of platform choice.

## Key Topics

- **dbt Management**: Git repository structure (monorepo vs. multirepo), development experience (DevEx), CI/CD, deployment, alerting, and monitoring.
- **dbt Scheduling**: Where dbt runs (server), triggers, and the observation that dbt scheduling is "tricky but not complicated" because dbt only sends SQL queries to warehouses (low compute needs).
- **Project Organization**: Mono-project vs. multi-project, exposures vs. packages for cross-project interfaces, folder structure recommendations.
- **Developer Experience**: User personas (data engineers, analytics engineers, data analysts, management, stakeholders) and levers for empowering analytics teams.
- **Ownership**: Recommendation that analytics teams should own dbt repos, with data engineers focusing on DevEx and foundational layers.

## Key Recommendations

- Start with one repo, one project for small teams.
- Analytics team should own dbt repos, not data engineering.
- Data engineers should empower analytics teams through DevEx.
- Use exposures for cross-project interfaces rather than packages.
- One YAML per model file, sources at schema/database level.

## Connections

This source strengthens existing wiki coverage of [[dbt-cloud]] pricing, [[dbt-project-scaffolding]], [[dbt-git-branching-strategies]], and [[dbt-mesh]] (multi-project patterns). It extends dbt management beyond CI/CD to include DevEx and user personas. The source is opinion-based (not empirical) but provides practical, experience-driven guidance.