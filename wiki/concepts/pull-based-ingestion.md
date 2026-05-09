type: concept
title: Pull-based Ingestion
created: 2026-02-13
updated: 2026-02-13
tags: [etl, metadata, data-engineering]
related: [openmetadata]
sources: ["Cosa è Openmetadata Unified Knowledge Graph_.md"]
---
# Pull-based Ingestion

**Pull-based Ingestion** is a mechanism where a central platform or service actively reaches out to various data sources to retrieve and ingest metadata or data, rather than waiting for the sources to "push" updates.

In metadata management platforms like [[openmetadata]], this pattern is used to ensure high reliability and consistency.

## Characteristics
- **Consistency**: By actively polling or scheduled retrieval, the platform ensures the metadata reflects the actual state of the underlying databases, pipelines, and dashboards.
- **Reliability**: The platform controls the ingestion logic, making it easier to manage error handling, retries, and scheduling.
- **Centralized Control**: The central system manages the frequency and scope of the ingestion process via connectors.

## Comparison with Push-based Ingestion
While **push-based** (or event-driven) ingestion (e.g., using [[kafka]]) is excellent for real-time updates, it requires the source systems to be "aware" of the metadata platform and capable of sending notifications. **Pull-based** ingestion is often easier to implement in heterogeneous environments where legacy systems cannot easily trigger outbound events.

---END EXPLANATION ---

---FILE: wiki/index.md---
# Wiki Index

## Entities
- [[regione-liguiia]] — The owner and stakeholder of the Data Platform.
- [[dremio]] — Data virtualization engine and semantic layer provider.
- [[trino]] — A primary alternative to Dremio for federated queries.
- [[kubernetes]] — Kubernetes container orchestration platform.
- [[nessie]] — Data catalog providing Git-empty versioning.
- [[gemini]] — AI model used for architectural analysis.
- [[kafka]] — Distributed event streaming platform for ingestion.
- [[elementary]] — dbt observability package and CLI.
- [[langchain]] — Framework for building LLM-powered applications.
- [[autogpt]] — Autonomous AI agent framework.
- [[great-expectations]] — Data validation and profiling library.
- [[dvc]] — Data Version Control for datasets and ML pipelines.
- [[data-world]] — Organization responsible for KG/LLM accuracy research.
- [[gpt-4]] — LLM used as the primary engine for Text-to-SQL/SPARQL benchmarks.
- [[apache-sedona]] — Distributed spatial computing engine for Apache Spark.
- [[proj4j]] — Lightweight Java port of PROJ.4 used by Sedona.
- [[wherobots-cloud]] — Managed geospatial notebook environment.
- [[geopandas]] — Python library for manipulating geospatial data.
- [[matplotlib]] — Python library for creating static visualizations.
- [[sedonapydeck]] — Package for interactive geospatial visualizations.
- [[openmetadata-ai-cdk]] — Tool for programmatic access to metadata intelligence.
- [[open-data-contract-standard-odcs]] — Standard for data contract interoperability.
- [[sqlglot]] — SQL parser used for lineage parsing in OpenMetadata.
- [[openmetadata]] — Open-source semantic context layer for AI-ready data teams.
- [[collate]] — Managed enterprise version of Openjava OpenMetadata.
- [[minio]] — S3-compatible object storage for the physical data layer.
- [[apache-iceberg]] — Open table format providing ACID transactions and schema evolution.
- [[superset]] — Modern, open-source data exploration and dashboarding.
- [[opensearch]] — Suite for search, log analysis, and observability.
- [[architectkb]] — A complementary "knowledge vault" for persistent architectural knowledge.
- [[arc-kit-commands]] — A reference page listing the 50+ slash commands in ArcKit.
- [[leo-godin]] — Senior Data Engineer at Shopify and author of observability insights.
- [[omg-p-c-data-model]] — Enterprise insurance schema used in KG/LLM benchmarks.
- [[turkel]] — Author of the article on dbt best practices.
- [[dbt-labs]] — The creators of dbt.
- [[abhishek-kubarr-gupta]] — Author and expert in AI, Cloud, and Data Engineering.
- [[duckdb]] — In-process SQL OLAP engine for high-performance analytics.
- [[motherduck]] — Serverless, cloud-based extension of DuckDB.
- [[kestra]] — Open-source orchestration platform for automated workflows.
- [[geoscript]] — Legacy ETL system for SDI, currently being modernized.
- [[viscarto]] — PostGIS database used for spatial staging and analysis.
- [[dbt-workbench]] — A self-hosted, open-source UI for dbt projects.
- [[mcp-toolbox]] — An open-source tool empowering AI agents to run code/tests with data understanding.
- [[looker]] — BI/Dashboarding tool used as a target for metadata synchronization.
- [[gemini-cli]] — Interface for interacting with MCP servers and executing agentic workflows.
- [[mahdi-karabiben]] — Author and proponent of context-centric semantic layers.
- [[polaris-catalog]] — Open-source API standard for Iceberg interoperability.
- [[unity-catalog]] — Databricks governance platform.
- [[expedia-group]] — Organization demonstrating the WAP pattern efficiency.
- [[dbt-creator-tool]] — Automation script for bootstrapping dbt projects and Kestra flows.
- [[dremio-mcp-server]] — Implementation of MCP for Dremio.
- [[uv]] — Fast Python package manager.
- [[personal-access-token]] — Authentication credential for Dremio.
- [[nexar]] — Dashcam company using massive GPS/vision datasets.
- [[h3]] — Hierarchical hexagonal grid system.
- [[openstreetmap]] — Authoritative source for road network topology.
- [[whos-on-flags]] — Gazetteer for unambiguous place identification.
- [[python]] — Target language for modernizing ETL pipelines.
- [[postgis]] — Spatial extension for PostgreSQL used for spatial data storage.
- [[oracle]] — Source system for spatial data.
- [[ogr2ogr]] — CLI tool for spatial data transformation.
- [[pytest]] — Testing framework for Python-based pipelines.
- [[docker]] — Containerization tool for ephemeral test environments.
- [[pyproj]] — Python interface to the PROJ library.
- [[proj]] — The underlying C library for coordinate transformations.

## Concepts
- [[data-virtualization-layer]] — Unified SQL interface and abstraction layer.
- [[data-lakehouse]] — Architecture combining object storage with ACID transactions.
- [[infrastructure-architecture]] — High-level K8s, GitLab, and Kestra deployment strategy.
- [[data-storage-layer]] — Configuration of Dremio, Nessie, and Minio.
- [[nessie-versioning-api]] — Comparison of Folder-based vs. Branch-based isolation.
- [[containerized-development-empty]] — Reproducible, Docker-based workspace.
- [[declarative-yaml-orchestration]] — Workflow definition via configuration files.
- [[orchestration-decompling-patterns]] — Strategy for separating execution flow from business logic.
- [[software-defined-assets]] — Paradigm focusing on data objects rather as versioned assets.
- [[kafka-ingelse-layer]] — Data movement via streaming.
- [[geospatial-data-stack]] — Specialized workflow for geographic datasets.
- [[opensearch-monitoring]] — Logging and observability strategy.
- [[geospiatial-analysis-techniques]] — Methods for spatial visualization and statistical binting.
- [[knowledge-graph]] — Unifying technical and business metadata in a graph.
- [[ontology-explorer]] — Visual tool for navigating business ontologias.
- [[semantic-context-layer]] — The layer providing meaning to metadata for AI agents.
- [[data-lakehouse-on-permise-architecture]] — Integration of MinIO, Ice/Iceberg, and Nessie for local sovereignty.
- [[unbundled-data-architecture]] — Strategic decoupling of storage and compute.
- [[knowledge-compounding-in-architecture]] — How structured documentation creates long-term organizational value.
- [[metadata-mart]] — Structured database for storing dbt artifacts.
- [[anomaly-detection]] — Using statistical methods to identify pipeline deviations.
- [[ai-driven-rag-data-api]] — Using autonomous agents to automate DQ detection.
- [[data-quality-dimensions]] — Framework of metrics (Compleintess, Accuracy, etc.) for data health.
- [[benchmark-kg-llm-accuracy]] — Empirical study on KG impact on LLM SQL accuracy.
- [[spatial-pre-processing-pattern]] — Strategy for handling unsupported spatial transformations.
- [[dbt-best-flags]] — Industry-standard patterns for dbt modeling and workflow management.
- [[spatial-join-patterns]] — Pattern of joining attribute-only CSVs with geometry-rich Shapefiles.
- [[spatial-rdd-and-spatial-dataframe]] — Core data structures in Apache Sedona.
- [[open-data-contract-standard-odcs]] — Standard for data contract interoperability.
- [[model-context-protocol]] — Standard for AI agents to interact with data landscapes.
- [[data-sovereignty-strategy]] — Importance of on-premise/open-source for NIS2/DORA compliance.
- [[data-lakehouse-on-premise-pattern]] — A dedicated page detailing the integration of MinIO, Iceberg, and Nessie.
- [[unbundled-data-schema]] — To formalize the decision-making process regarding the decoupling of storage and compute.
- [[constrained-generation-skills]] — Using templates to ensure AI output follows strict structures.
- [[automated-safety-chunks-hooks]] — Local scripts to enforce security and integrity in AI workflows.
- [[text-to-sparql-for-prime-enterprise]] — Methodology of using R2RML and OWL to bridge the gap between relational data and LLMs.
- [[dbt-environment-management]] — Configuration of dev vs prod targets and conditional logic.
- [[dbt-modeling-layers]] — Formalizing the Staging $\rightarrow$ Intermediate $\rightarrow$ Marts architecture.
- [[dbt-advanced-patterns]] — Summary of advanced dbt techniques for production-grade pipelines.
- [[dbt-slim-ci-strategy]] — Technical deep-dive into implementing `state:modified` workflows.
- [[hybrid-execution-pattern]] — Architecture of querying local and cloud data in a single session.
- [[event-driven-etl]] — Data pipelines triggered by external events.
- [[data-masking]] — Protecting PII during the ETL process.
- [[kestra-blueprints]] — Reusable workflow templates for rapid deployment.
- [[sdi-dp-integration-lagic]] — Strategy for integrating SDI with the Data Platform.
- [[artifact-driven-ui]] — A UI that parses existing JSON metadata produced by a tool.
- [[semantic-intelligence-layer]] — A layer providing AI agents with the meaning behind raw data.
- [[ai-ready-data]] — Data enriched with semantic context for autonomous agents.
- [[what-why-who-how-framework]] — A multidimensional approach to metadata for AI agents.
- [[etl-bias]] — The organizational risk of centralized data engineering.
- [[data-downtime]] — The period of unusable or inaccurate data.
- [[data-catalog-comparison]] — Comparison of Nessie, Polaris, and Unity catalogs.
- [[write-audit-publish-pattern]] — A data validation workflow (Write $\rightarrow$ Audit $\rightarrow$ Publish).
- [[kestra-promotion-strategy]] — Namespace-switching and renaming logic used during MRs.
- [[environment-promotion-workflow]] — The dev $\rightarrow$ test $\rightarrow$ stage $\rightarrow$ prod lifecycle.
- [[agentic-skills-pattern]] — Using markdown-based instructions to define deterministic agent behaviors.
- [[human-in-the-loop-agent-patterns]] — Using Pause/Continue and Session-based models for production AI.
- [[agentic-debugging-workflow]] — Using metadata and CLI tools for autonomous pipeline remediation.
- [[collate-ai]] — Agentic metadata management suite.
- [[reverse-metadata]] — Bidragional metadata synchronization.
- [[self-hosted-mcp-deployment]] — Running MCP servers in private infrastructure.
- [[dremioai-configuration-mode]] — Configuration profile for Dremio connection parameters.
- [[h3-spatial-indexing]] — Using hexagonal grids to optimize spatial queries.
- [[spatial-to-integer-conversion]] — Replacing geometry with integer IDs.
- [[dbt-python-models-support]] — Reference for which adapters support .py models.
- [[organizationally-aware-ai]] — AI that understands business context and governance.
- [[groovy-to-python-migration]] — Refactoring legacy Groovy ETL to Python.
- [[integration-testing-without-mocking]] — Using real containers for high-fidelity spatial testing.
- [[process-wrapper-pattern]] — Controlling external CLI dependencies via wrapper scripts.
- [[environment-based-configuration]] — Using `.env` files for standardized configuration.
- [[automated-geometry-validation]] — Using PostGIS to validate and repair geometries.
- [[gsb-files]] — Specialized files used by PROJ for high-accuracy coordinate transformations.
- [[grid-shift-transformation]] — Technique using .gsb files to account for local distortions.
- [[metadata-federation]] — The ability to perform cross-catalog queries and create a unified lineage view.
- [[pull-based-ingestion]] — A mechanism where the platform actively retrieves metadata from sources.
