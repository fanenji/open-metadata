---
type: entity
title: OpenMetadata Data Quality Test Library
created: 2026-02-26
updated: 2026-02-26
tags: [data-quality, testing, governance, no-code]
related: [dbt, openmetadata-1.12-release-notes, data-governance]
sources: ["Annaching OpenMetadata 1.12.md"]
---
# OpenMetadata Data Quality Test Library

The **Data Quality Test Library** is a feature introduced in OpenMetadata 1.12 that allows for the creation of reusable, parameterized, SQL-based test templates.

## Core Functionality
Unlike traditional testing methods that require writing custom SQL for every table, this library allows administrators to define a template once (e.g., an "ARR validation" rule) and apply it across multiple assets via a GUI.

## Key Features
- **Reusable Templates**: Parameterized SQL definitions that can be applied to various tables without rewriting code.
- **GUI-Driven Experience**: A "no-code" interface for end-users to apply tests via simple forms, while administrators maintain centralized control.
- **Centralized Governance**: Ensures that critical business rules are applied consistently across the organization, preventing "fragmented" testing logic.

## Comparison with dbt
While [[dbt]] relies on a **code-first, YAML-based** approach that requires technical expertise, the OpenMetadata Test Library offers a **no-code, GUI-based** alternative that empowers non-technical business users to enforce quality standards.