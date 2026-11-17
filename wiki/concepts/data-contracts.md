---
type: concept
title: Data Contracts
created: 2026-07-15
sources: ["https://blog.open-metadata.org/end-the-2-am-pipeline-fixes-openmetadatas-collaborative-actionable-data-contracts-stop-breaks-df34adb27125"]
tags: [data-contracts, data-quality, data-governance, schema-management]
related: [data-quality, data-observability-alerts, openmetadata-collaboration, data-asset-ownership, glossary-terms, tag-request-workflow, announcements, classification-tiers, data-products]
updated: 2026-07-07
---
# Data Contracts

A **Data Contract** is a formal, versioned agreement between **data producers** (backend engineers, service owners) and **data consumers** (analysts, data scientists, ML engineers) that specifies the schema, semantics (business rules), and quality expectations for a data asset. In [[OpenMetadata]], data contracts represent a shift from passive metadata documentation to active, enforceable agreements, bringing software-engineering discipline — SLAs, change management, automated monitoring — to the data layer.

Data contracts unify three dimensions of data governance:

- **Schema** — Which columns are included and their expected types.
- **Semantics** — Business rules: Owners, Tags, Domain, Tier, Glossary Terms, descriptions.
- **Quality** — Data Quality Tests that enforce reliability.

## The Problem They Solve

In a **schema-last world**, data producers ship changes without warning, and consumers build pipelines, dashboards, and ML models on assumptions. The result: broken dashboards at 2 AM, failing models, and frantic Slack messages asking "Why did this column disappear?" Informal agreements — hallway conversations, outdated Confluence pages — don't scale: they become obsolete immediately and carry no enforcement.

## Two Critical Gaps in Data Contract Solutions

### Collaboration Gap

Most contract solutions force a false choice:
- **YAML-only systems** — technically rigorous but exclude business users who understand how data is actually used
- **UI-only documents** — business-accessible but lack technical rigor and actionable content

OpenMetadata bridges this gap with a **dual YAML + UI approach**, enabling technical and business stakeholders to collaborate as equals. When only engineers participate, contracts miss critical business requirements; when only business users define them, contracts become wish lists that ignore technical realities.

### Actionability Gap

Static contracts (YAML files, Confluence pages) are "painted-on locks" — they provide a false sense of security but anyone can ignore them. Without continuous validation and automated monitoring, contracts become outdated documentation referenced only after problems arise.

OpenMetadata addresses this through **integrated validation**: contracts are continuously checked, violations auto-create incidents with stakeholder notifications via existing channels (Slack, Teams, GChat, Email, webhooks), and historical SLA tracking reveals trends. Violations become collaborative problem-solving moments rather than silent failures.

## OpenMetadata Data Contracts Capabilities

### Granular Schema Contracts

Instead of all-or-nothing table contracts, contract only **critical columns**. If a table has 20 columns but you depend on 5, contract those 5 while allowing complete freedom to evolve the other 15 — balancing stability with innovation.

### Semantic Validation

Enforces **metadata requirements** (ownership, description, tags) as part of contracts. Prevents data that is technically correct but functionally unusable due to lost tribal knowledge — ensuring data products remain usable long after the original creators have moved on.

### Data Quality & Observability Validation

Transforms monitoring from reactive alerts to **active prevention**. Choose specific table- and column-level quality tests to enforce as part of contracts: uniqueness constraints, null validations, referential integrity checks, and custom business rules.

### Integrated Alerting

When a contract breaks, stakeholders are notified through their existing channels. This transforms contract violations from silent failures into collaborative problem-solving moments, turning governance from reactive firefighting into active data stewardship.

### Approval Workflows

Every contract must be **reviewed, approved, and governed** before enforcement, ensuring contracts are genuine agreements with buy-in, not unilateral declarations. This connects with the broader [[tag-request-workflow]] pattern in OpenMetadata's governance model.

### Continuous SLA Validation with Historical Tracking

Automated daily checks and on-demand validation runs produce **time-series health charts**, enabling teams to identify patterns in contract violations and address systemic issues before they cascade downstream.

## Current Implementation (UI Workflow)

As of the latest release, OpenMetadata provides a structured UI workflow for creating data contracts on tables. The process follows a **6-step wizard**:

1. **Contract Details** — Name, optional Owners, description.
2. **Schema** — Select columns.
3. **Semantics** — Define business rules (Owners, Tags, Domain, Tier, Glossary Terms, etc.).
4. **Quality** — Add Data Quality Tests.
5. **Save** — Finalize.
6. **Run** — Execute on demand.

This implementation focuses on schema and semantics aspects with integrated data quality tests.

## Origins and Roadmap

Data contracts were first described as a future concept in the OpenMetadata 1.2.0 community meeting, aligning with the [[data-mesh-openmetadata|data mesh]] framework. In data mesh, [[data-products|data products]] are provided to consumers with guarantees; data contracts formalise those guarantees, making them explicit, measurable, and enforceable.

The feature was released in **OpenMetadata 1.9** (September 2025). Future enhancements planned include: more data asset types, additional guarantee types (SLAs, freshness guarantees), enforcement models with versioning, a programmatic API, and further customization options. The existing [[glossary-approval-workflow]] and [[data-quality]] features are foundational building blocks.

## Current Limitations

- Available only for tables.
- No documented enforcement model (blocking vs. documentary).
- No documented versioning or update mechanism.
- No API for programmatic management.

## Relationship to OpenMetadata Concepts

- **[[data-quality]]** — Contracts incorporate Data Quality Tests as enforceable guarantees.
- **[[data-observability-alerts]]** — Contract violations trigger alerts through the observability infrastructure.
- **[[data-asset-ownership]]** — Owners are a semantic rule enforced by contracts.
- **[[classification-tags]]** and **[[tiers]]** — Tags and tiers are semantic rules enforced by contracts.
- **[[glossary-terms]]** — Related via Tags and Domain; semantic validation requires proper business metadata.
- **[[openmetadata-collaboration]]** — The dual YAML+UI approach enables cross-team collaboration.
- **[[data-products]]** — Contracts are the formal guarantee for data products within the data mesh framework.
- **[[glossary-approval-workflow]]** and **[[tag-request-workflow]]** — Building blocks for the contract approval lifecycle.