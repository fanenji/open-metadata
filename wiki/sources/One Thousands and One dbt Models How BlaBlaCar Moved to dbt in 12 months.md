---
type: source
title: "One Thousands and One dbt Models: How BlaBlaCar Moved to dbt in 12 months"
created: 2026-05-06
updated: 2026-05-06
tags: [dbt, migration, data-mesh, blablacar, data-engineering]
related: [blablacar, dbt-dag-generator, dbt-migration-strategy, dbt-dry-run, dbt-developer-experience, data-mesh, dbt-cloud, kristoff, dbt-dragons, thibault-ambard, tushar-bhasin]
sources: ["One Thousands and One dbt Models How BlaBlaCar Moved to dbt in 12 months.md"]
---
# One Thousands and One dbt Models: How BlaBlaCar Moved to dbt in 12 months

A talk by Thibault Ambard (Data Engineering Manager) and Tushar Bhasin (Senior Data Engineer / Data Engineering Lead) at BlaBlaCar, presented at Forward Data Conference 2024. The talk details BlaBlaCar's 12-month journey migrating 1,000+ data models to dbt, covering decision-making, tooling, migration execution, and organizational patterns.

## Key Topics

- **Decision to adopt dbt:** No benchmarking, expert hiring (Kristoff), choosing Core over Cloud.
- **Enablers:** dbt DAG generator, orchestration decisions (Airflow, graph view, multiple projects), developer onboarding.
- **Migration execution:** Starting with the most complex pipeline ("spaghetti"), double-run data quality checks, query generator, CLI setup tool, gamification, migration fatigue management.
- **Organizational patterns:** DBT Dragons expert group, decentralized migration in a data mesh, cheat sheets, documentation.
- **Lessons learned:** Flexibility vs. abstraction trade-off, multi-project consolidation, technical debt from "don't change business logic" rule, future plans for dbt Cloud and dbt tests.

## Key Metrics

- 1,200 models migrated after 18 months
- 120 models in the first complex pipeline, 10 weeks, 6 engineers
- ~2 tables/day/engineer (rough estimate)
- 50+ data professionals onboarded
- 50+ dbt projects (being consolidated)

## Key Quotes

> "We made a technical choice without looking at competition. No benchmark, nothing. We said okay, we want a data transformation tool, there's one name that comes over and over again is dbt, so let's go with dbt."

> "The first page that we received as a contribution to our docs was a cheat sheet... on git, not on dbt."

## Relevance

This source provides concrete, real-world implementation details for dbt migration at scale, complementing the wiki's existing coverage of [[blablacar]], [[data-mesh]], [[dbt-dag-generator]], and [[dbt-cloud]]. It introduces new concepts like [[dbt-migration-strategy]], [[dbt-dry-run]], [[dbt-developer-experience]], and the [[dbt-dragons]] organizational pattern.