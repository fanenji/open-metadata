---
type: source
title: "Defining Data Quality: The Foundation of Modern Data Architecture"
created: 2026-04-29
updated: 2026-04-29
tags: [data-quality, data-governance, data-architecture]
related: [data-quality-dimensions, data-quality-score, shift-left-data-quality, engineering-led-data-quality, data-quality-certification-vs-usability-certification, data-observability-definition, environmental-data-quality-hierarchy]
sources: ["Defining Data Quality The Foundation of Modern Data Architecture.md"]
authors: [Naidu Rongali]
year: 2025
url: "https://medium.com/towards-data-engineering/defining-data-quality-the-foundation-of-modern-data-architecture-9dc356b182e4"
venue: "Towards Data Engineering (Medium)"
---
# Defining Data Quality: The Foundation of Modern Data Architecture

This article by Naidu Rongali, Sr Data & AI Engineer at Amazon, provides a foundational definition of Data Quality (DQ) for modern distributed data architectures. It argues that DQ must be defined through measurable dimensions and enforced programmatically, removing subjectivity from the term.

The core contribution is a framework of seven DQ dimensions: Accuracy, Completeness, Consistency, Uniqueness, Integrity, Validity, and Availability/Timeliness. The article proposes a quantifiable **Data Quality Score** — the percentage of passed DQ rules per dataset — as a consistent, scalable metric for governance dashboards.

Key enforcement strategies include the **Shift-Left Approach** (moving validation as close to the source as possible) and **Layered Validation** (redundant checks at every system handoff). The article argues for **Engineering-Led Enforcement** as the default, with dedicated DQ platforms justified only for compliance or enterprise-wide visibility needs. It also distinguishes **Data Quality Certification** (how good is the data?) from **Data Usability Certification** (how ready is the data for use?).

The source aligns with existing wiki content on [[data-observability-definition]], [[environmental-data-quality-hierarchy]], and [[dbt-testing-patterns]], providing a complementary DQ dimension framework to the observability dimensions already documented.