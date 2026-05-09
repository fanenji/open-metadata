type: concept
title: Unified Data Infrastructure Architecture
created: 2026-04-29
updated: 2026-04-29
tags: [architecture, data-infrastructure, reference-architecture, lifecycle]
related: [data-lifecycle-stages, modern-business-intelligence-blueprint, multimodal-data-processing-blueprint, ai-ml-blueprint, data-lakehouse, elt-pattern, feature-store-architecture]
sources: ["Data-Report-Martin-Inline-Graphics-R8-1.pdf"]
---
# Unified Data Infrastructure Architecture

A comprehensive reference architecture framework that covers the full data lifecycle from sources to output. The framework organizes the modern data infrastructure landscape into a unified model with six lifecycle stages and three common blueprints.

## Lifecycle Stages

The architecture is organized around six stages:
1. **Sources** — Operational systems, applications, logs, and third-party APIs that generate business data
2. **Ingestion and Transformation** — Extract data from operational systems (E), deliver to storage aligning schemas (L), transform data for analysis (T)
3. **Storage** — Data warehouses, data lakes, and file/object storage optimized for low cost, scalability, and analytic workloads
4. **Historical** — Describe what happened in the past; provide an interface for analysts and data scientists to derive insights via query and processing
5. **Predictive** — Predict what will happen in the future; build data-driven/ML applications
6. **Output** — Present results to internal and external users; embed data models into operational systems

Cross-cutting concerns include workflow orchestration, data quality, metadata management, entitlements/security, and observability.

## Three Common Blueprints

The framework identifies three common architectural patterns:
- **[[modern-business-intelligence-blueprint]]** — Traditional BI pipeline
- **[[multimodal-data-processing-blueprint]]** — Batch, streaming, and interactive query workloads
- **[[ai-ml-blueprint]]** — ML lifecycle infrastructure

## Relationship to Existing Wiki Concepts

This framework provides a higher-level organizational lens that contextualizes many existing wiki concepts:
- [[data-lakehouse]] fits within the Storage stage
- [[elt-pattern]] aligns with the Ingestion and Transformation stage
- [[feature-store-architecture]] is a component of the AI/ML Blueprint
- [[dbt]] appears as the primary data modeling tool across all blueprints
- [[great-expectations-for-data-contracts]] and [[datahub]] appear in the cross-cutting quality and metadata layers