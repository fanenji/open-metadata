---
type: concept
title: dbt Migration Strategy
created: 2026-05-06
updated: 2026-05-06
tags: [dbt, migration, strategy, blablacar]
related: [blablacar, dbt-dag-generator, dbt-dry-run, dbt-developer-experience, dbt-dragons, data-mesh, kristoff, double-run-migration, migration-fatigue-management]
sources: ["One Thousands and One dbt Models How BlaBlaCar Moved to dbt in 12 months.md"]
---
# dbt Migration Strategy

A set of organizational and technical patterns for migrating large-scale data pipelines to dbt, derived from [[BlaBlaCar]]'s 12-month migration of 1,000+ models.

## Key Patterns

### Expert Hiring
Hiring an external dbt expert ([[Kristoff]]) was critical for informed decision-making, future problem scoping, and avoiding pitfalls. The team had zero prior dbt knowledge.

### Start with the Most Complex Pipeline
BlaBlaCar started with their most complex, highest-ROI pipeline ("spaghetti" — 120 models) rather than a simple one. This maximized learning and impact early.

### Double Run Migration
Running old and new pipelines in parallel with data quality checks for 3-4 days before cutover. A data quality module was built to compare outputs and ensure correctness.

### Query Generator
An internal script that converts standard BigQuery SQL to dbt format (refs, sources, tests). Also preserved schema definitions by adding tests.

### CLI Setup Tool
A lightweight CLI for standardized dbt project and profile creation across 50+ users, reducing repetitive setup overhead.

### Migration Fatigue Management
- Rotating teams in alternative sprints (two teams of 3 engineers each)
- Handover rituals and share-and-learn sessions
- Automatic reporting for project progress and delay detection
- Heavy investment in communication and documentation

### Decentralized Migration via Expert Groups
After the initial centralized migration of 120 models, the [[DBT Dragons]] group was formed to support decentralized migration across squads in a [[data-mesh]] organization.

### Technical Debt Acknowledgment
The "don't change business logic" rule during migration created technical debt (pre/post hooks) that requires post-migration cleanup.

## Lessons Learned
- Abstraction (easy onboarding) vs. flexibility (power users) is a key trade-off
- Multi-project design (one per DAG) leads to management overhead; consolidation via `--selector` flags is preferred
- Developer experience (VS Code, git, cheat sheets) requires significant investment
- dbt Cloud was rejected initially but is being reconsidered as features improve