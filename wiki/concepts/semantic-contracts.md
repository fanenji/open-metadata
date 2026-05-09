---
type: concept
title: Semantic Contracts
created: 2026-04-07
updated: 2026-04-07
tags: [governance, metrics, ai-readiness, data-quality]
related: [metrics-layer, ai-ready-data, data-governance]
sources: ["Building Blocks of Semantics Ontologies, Knowledge Graphs & Metrics Layers.md"]
pattern: [metrics-layer]
---
# Semantic Contracts

A **Semantic Contract** is an evolution of the traditional metric definition. While a standard metric might simply be a SQL aggregation, a semantic contract encodes the business intent, constraints, and valid contexts required for autonomous agents to act on data.

## Components of a Semantic Contract
To be "agent-ready," a metric must define:
*   **Grain**: The level of aggregation (e.g., per supplier, per region).
*   **Filters**: The logic for what is included or excluded (e.g., excluding tax or one-time capital expenditures).
*   **Valid Contexts**: The specific business scenarios where this metric is applicable (e.g., "Valid for Sourcing Strategy, but invalid for Financial Reporting").
*   **Policy Constraints**: The boundaries of action (e.g., "This metric can inform a negotiation, but cannot authorize a payment").
*   **Business Intent**: The underlying "why" behind the calculation.

## Importance in the Agentic Enterprise
Without semantic contracts, different agents or teams may calculate the same metric (e.g., "Addressable Spend") using different logic, leading to conflicting actions and a breakdown in organizational trust. Semantic contracts ensure that **agents act on metrics, not just data.**

---END EXPLANATION ---

---FILE: wiki/index.md---
# Wiki Index

## Entities
*(No new entities from this source)*

## Concepts
- [[data-virtualization-layer]] — Unified SQL interface and abstraction layer.
- [[data-lakehouse]] — Architecture combining object storage with ACID transactions.
- [[infrastructure-architecture]] — High-level K8s, GitLab, and Kestra deployment strategy.
- [[data-storage-layer]] — Configuration of Dremio, Nessie, and Minio.
- [[nessie-versioning-strategy]] — Comparison of Folder-based vs. Branch-based isolation.
- [[containerized-development-empty]] — Reproducible, Docker-based workspace.
- [[declarative-yaml-orchestration]] — Workflow definition via configuration files.
- [[orchestration-decompling-patterns]] — Strategy for separating execution flow from business logic.
- [[software-defined-assets]] — Paradigm focusing on data objects rather as versioned assets.
- [[kafka-ingelse-layer]] — Data movement via streaming.
- [[geospatial-data-stack]] — Specialized workflow for geographic datasets.
- [[opensearch-monitoring]] — Logging and observability strategy.
- [[geospiatial-analysis-techniques]] — Methods for spatial visualization and statistical binting.
- [[knowledge-graph]] — Unifying technical and business metadata in a graph.
- [[ontology-explorer]] — Visual tool for navigating business ontologies.
- [[semantic-context-layer]] — The layer providing meaning to metadata for AI agents.
- [[data-lakehouse-on-permise-architecture]] — Integration of MinIO, Ice/Iceberg, and Nessie for local sovereignty.
- [[unbundled-data-architecture]] — Strategic decoupling of storage and compute.
- [[knowledge-compounding-in-architecture]] — How structured documentation creates long-term organizational value.
- [[metadata-mart]] — Structured database for storing dbt artifacts.
- [[anomaly-detection]] — Using statistical methods to identify pipeline deviations.
- [[ai-driven-data-quality]] — Using autonomous agents to automate DQ detection.
- [[data-quality-dimensions]] — Framework of metrics (Compleintess, Accuracy, etc.) for data health.
- [[benchmark-kg-llm-accuracy]] — Empirical study on KG impact on LLM SQL accuracy.
- [[spatial-pre-processing-pattern]] — Strategy for handling unsupported spatial transformations.
- [[dbt-best-practices]] — Industry-standard patterns for dbt modeling and workflow management.
- [[spatial-join-patterns]] — Pattern of joining attribute-only CSVs with geometry-rich Shapefiles.
- [[spatial-rdd-and-spatial-dataframe]] — Core data structures in Apache Sedona.
- [[open-data-contract-standard-odcs]] — Standard for data contract interoperability.
- [[model-context-protocol]] — Standard for AI agents to interact with data landscapes.
- [[data-sovereignty-strategy]] — Importance of on-premise/open-source for NIS2/DORA compliance.
- [[data-lakehouse-on-premise-pattern]] — A dedicated page detailing the integration of MinIO, Iceberg, and Nessie.
- [[unbundled-data-architecture]] — To formalize the decision-making process regarding the decoupling of storage and compute.
- [[constrained-generation-skills]] — Using templates to ensure AI output follows strict structures.
- [[automated-safety-chunks-hooks]] — Local scripts to enforce security and integrity in AI workflows.
- [[text-to-sparql-for-enterprise]] — Methodology of using R2RML and OWL to bridge the gap between relational data and LLMs.
- [[dbt-environment-management]] — Configuration of dev vs prod targets and conditional logic.
- [[dbt-modeling-layers]] — Formalizing the Staging $\rightarrow$ Intermediate $\rightarrow$ Marts architecture.
- [[dbt-advanced-patterns]] — Summary of advanced dbt techniques for production-grade pipelines.
- [[dbt-slim-ci-strategy]] — Technical deep-dive into implementing `state:modified` workflows.
- [[hybrid-execution-pattern]] — Architecture of querying local and cloud data in a single session.
- [[event-driven-etl]] — Data pipelines triggered by external events.
- [[data-masking]] — Protecting PII during the ETL process.
- [[kestra-blueprints]] — Reusable workflow templates for rapid deployment.
- [[sdi-dp-integration-strategy]] — Strategy for integrating SDI with the Data Platform.
- [[artifact-driven-ui]] — A UI that parses existing JSON metadata produced by a tool.
- [[semantic-intelligence-layer]] — A layer providing AI agents with the meaning behind raw data.
- [[ai-ready-data]] — Data enriched with semantic context for autonomous agents.
- [[what-why-who-how-framework]] — A multidimensional approach to metadata for AI agents.
- [[the-agentic-enterprise-architecture]] — The shift from data pipelines to decision pipelines.
- [[semantic-contracts]] — Defining requirements for metrics layers (grain, filters, business intent).
- [[embeddings-vs-knowledge-graphs]] — Comparison of discovery (embeddings) vs. explanation (graphs).

## Sources
- [[analisi-architettura-data-platform-regionally]] — Architectural review of the Regional Data Platform.
- [[Airflow vs Dagster vs Kstra]] — Comparative analysis of orchestration tools.
- [[ambiente-svagupp/su-conatiner]] — Documentation for the containerized dev environment.
- [[airflow-vs-kestra]] — Reddit discussion on trade-offs and real-world usage.
- [[AMBIENTI.md]] — Environment and Infrastructure Strategy.
- [[analisi-architettura]] — Architectural review of the Regional Data Platform.
- [[analyzing-real-estate-data-with-apache-sedona]] — Tutorial on spatial analysis with Sedona and Wherobots.
- [[announcing-openmetadata-1.12]] — Release announcement for OpenMetadata 1.12.
- [[announcing-openmetadata-1-13.md]] — Release announcement for Opentro OpenMetadata 1.13.
- [[architettures-open-source-simili.md]] — Research on on-premise open-source architectures.
- [[arc-kit-ai-toolkit-for-solution-enterprise-architects]] — ArcKit — AI Toolkit for Solution & Enterprise Architects.
- [[leo-202rad-elementary-dbt]] — Are You Using Elementary for DBT?
- [[automate-data-quality-checks-with-ai-agents]] — Automating DQ checks with AI agents.
- [[benchmark-kg-llm-accuracy]] — Benchmark of KG impact on LLM SQL accuracy.
- [[Apache Sedona Coordinate Transform.md]] — Technical discussion on Sedona CRS limitations.
- [[best-practices-for-whorks-a-guide-to-effective-dbt-use.md]] — A guide to effective dbt usage and workflow management.
- [[analyzing-real-estate-data-with-apache-sedona-20260506.md]] — Tutorial on analyzing Zillow real estate data using Sedona.
- [[announcing-openmetadata-1.12-20260506.md]] — Release announcement for OpenMetadata 1.12.
- [[announcing-openmetadata-1-13-20rab-20260506.md]] — Release announcement for OpenMetadata 1.13.
- [[architetture-open-source-simili-20260506.md]] — Research on on-premise open-source architectures.
- [[benchmark-kg-llm-accuracy-202rad-elementary-dbt]] — Benchmark of KG impact on LLM SQL accuracy.
- [[best-practices-for-whorks-a-guide-to-effective-dbt-use-20260506.md]] — A guide to effective dbt usage and workflow management.
- [[beyond-basics-7-advanced-dbt-patterns-for-production-grade-pipelines.md]] — Advanced dbt patterns for production-grade pipelines.
- [[beyond-storing-data-how-to-use-duckdb-motherduck-and-kestra-for-etl.md]] — Using DuckDB, MotherDuck, and Kestra for efficient ETL.
- [[BRAINSTOR - Integrazione della Spatial Data Infrastructure (SDI) con la Data Platform (DP).md]] — Brainstorming on SDI/DP integration.
- [[building-a-dbt-ui-i-whish-existed.md]] — Discussion on building an artifact-driven dbt UI.
- [[building-a-semantic-intelligence-layer-for-the-ai-data-stack]] — Implementing a semantic layer using OpenMetadata and MCP.
- [[building-a-semantic-layer-for-the-ai-era-beyond-sql-generation]] — Moving from SQL generation to business context.
- [[building-blocks-of-semantics-ontologies-knowledge-graphs-metrics-layers]] — The four building blocks of the semantic layer.
