type: concept
title: dbt Scaling Patterns
created: 2026-04-04
updated: 2026-04-04
tags: [dbt, scaling, data-mesh, onboarding, governance]
related: [dbt-dragons, dbt-dev-datasets, dbt-project-governance, double-run-validation, dbt-dry-run, blablacar]
sources: ["One Thousands and One dbt Models How BlaBlaCar Moved to dbt in 12 months - Summary.md"]
---
# dbt Scaling Patterns

**dbt scaling patterns** are a collection of practices developed by [[blablacar]] to onboard a ~50-person data team to dbt over 12 months, migrating ~1,200 models.

## Core Patterns

### 1. DBT Dragons (Knowledge Distribution)
- Identify domain champions (~8-10 people) who become go-to dbt contacts in their teams
- Reduces central team bottleneck; enables faster feedback cycles
- See [[dbt-dragons]]

### 2. Dev Datasets (Development Isolation)
- Each engineer works in a personal BigQuery dataset
- Enables safe parallel development without interference
- See [[dbt-dev-datasets]]

### 3. Double-Run Validation (Migration Safety)
- Run old and new models in parallel during migration
- Compare outputs before cutover to ensure zero regressions
- See [[double-run-validation]]

### 4. dbt-dry-run CI Gate (Pre-Execution Validation)
- Mandatory syntax and cost validation before merging
- Catches errors early at zero cost
- See [[dbt-dry-run]]

### 5. Onboarding Tooling
- CLI setup scripts for one-command environment configuration
- Query generator for scaffolding new dbt models
- Data quality module for automated double-run validation

### 6. Project Governance
- Define criteria for creating new dbt projects vs. new folders
- Prevent cross-project lineage and CI maintenance problems
- See [[dbt-project-governance]]

### 7. Git Training
- Foundational git skills training for analysts new to version control
- Addresses the unexpected onboarding bottleneck of git complexity

## Key Insight

dbt's opinionated framework enforces consistency across 50 engineers without requiring constant governance policing. The combination of tooling, training, and organizational patterns (DBT Dragons) enabled BlaBlaCar to scale dbt adoption while maintaining data quality and developer productivity.