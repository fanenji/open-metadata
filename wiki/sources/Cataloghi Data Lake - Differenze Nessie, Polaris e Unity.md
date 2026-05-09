---
type: source
title: "Cataloghi Data Lake - Differenze Nessie, Polaris e Unity"
authors: []
year: 2026
url: "https://aistudio.google.com/u/1/prompts/1Ya8xYB80bvxzBoEe0f7WWRtwS6PEKLj"
venue: "AI Studio Conversation"
tags: [nessie, iceberg, catalog, gemini, tools]
related: [nessie, apache-iceberg, data-lakehouse, unbundled-data-architecture]
created: 2026-02-13
updated: 2026-02-13
sources: ["Cataloghi Data Lake - Differenze Nessie, Polaris e Unity.md"]
---
# Cataloghi Data Lake - Differenze Nessie, Polaris e Unity

A comparative analysis of three distinct approaches to metadata management in Data Lake and Data Lakehouse architectures: Nessie Catalog, Polaris Catalog, and Unity Catalog.

## Summary of Approaches

1. **Nessie Catalog (Project Nessie)**
   - **Focus**: Git-like transactional semantics (branching, merging, tagging) for Apache Iceberg.
   - **Primary Use Case**: DataOps, CI/CD for data, and isolated experimentation.
   - **Key Features**: Multi-table ACID transactions, time travel, and rollback.

2. **Polaris Catalog**
   - **Focus**: API Standardization and Interoperability.
   - **Primary Use Case**: Preventing vendor lock-in by providing a universal REST API for Apache Iceberg engines.
   - **Key Features**: Open-source specification supported by major industry players (Apple, Netflix, Adobe).

3. **Unity Catalog (Databricks)**
   - **Focus**: Unified Governance and Security.
   - **Primary Use Case**: Centralized "control tower" for organizations heavily invested in the Databricks ecosystem.
   - **Key Features**: Fine-grained access control (row/column level), automated lineage, and centralized auditing.
