---
type: concept
title: Service Account Authentication
created: 2026-05-06
updated: 2026-05-06
tags: [security, authentication, jwt, automation]
related: [openmetadata, @modelcontextprotocol/server-openmetadata]
sources: ["Configurare Claude con server MCP di OpenMetadata.md"]
---
# Service Account Authentication

**Service Account Authentication** is the practice of using dedicated, non-human identities to facilitate programmatic access to enterprise systems.

## Role in AI Agents
In the context of the "AI Stack," service accounts are critical for allowing autonomous agents (via [[model-context-protocol]]) to interact with data platforms without requiring human user credentials.

## Implementation via JWT
In platforms like [[openmetadata]], this is typically implemented using **JSON Web Tokens (JWT)**:
1. A **Service Account** or **Bot** is created within the platform.
2. A unique **JWT** is generated for that account.
3. This token is then injected into the environment variables of the MCP server, providing a secure, revocable, and scoped method of authentication for the AI agent.

---END $\text{END FILE}$---

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
- [[collate]] — Managed enterprise version of OpenMetadata.
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
- [[abhishek-kubar-gupta]] — Author and expert in AI, Cloud, and Data Engineering.
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
- [[claude-code]] — CLI-based interface for Claude, designed for agentic tasks.
- [[claude-desktop-mcp-config]] — Configuration guide for Claude Desktop MCP integration.
- [[@modelcontextprotocol/server-openmetadata]] — MCP server implementation for OpenMetadata.

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
- [[ontology-explorer]] — Visual tool for navigating business ontologies.
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
- [[reverse-metadata]] — Bidirectional metadata synchronization.
- [[self-hosted-mcp-deployment]] — Running MCP servers in private infrastructure.
- [[dremioai-configuration-mode]] — Configuration profile for Dremio connection parameters.
- [[h3-spatial-indexing]] — Using hexagonal grids to optimize spatial queries.
- [[spatial-to-integer-conversion]] — Replacing geometry with integer IDs.
- [[mcp-server-configuration]] — Process of defining environment variables and execution commands for MCP.
- [[service-account-authentication]] — Using dedicated identities (JWT) for automated tool access.

- [[announcing-openmetadata-1.12]] — Release announcement for OpenMetadata 1.12.
- [[announcing-openmetadata-1-13.md]] — Release announcement for OpenMetadata 1.13.
- [[collate-vs-openmetadata-managed-service]] — Comparison of Collate's managed service vs OpenMetadata open source.
---

## Queries
(No new queries)

## Syntheses
(No new syntheses)
---

---FILE: wiki/log.md---
---
type: log
title: Log
created: 2026-05-06
updated: 2026-05-06
tags: [log]
sources: []
---
# Log

## 2026-05-06

- Ingested "Complex geospatial analytics with dbt - Summary.md"
- Added entities: [[nexar]], [[h3]], [[openstreetmap]], [[whos-on-flags]]
- Added concepts: [[h3-spatial-indexing]], [[spatial-to-integer-conversion]]
- Updated [[dbt-best-practices]] with large-scale data patterns.
- Updated [[geospatial-data-stack]] with H3 optimization paradigm.
- Added source: [[assaf-lavi-2022-complex-geospatial-analytics-with-dbt]

## 2026-05-06

- Ingested "Configurare Claude con server MCP di OpenMetadata.md"
- Added entities: [[claude-code]], [[claude-desktop-mcp-config]], [[@modelcontextprotocol/server-openmetadata]]
- Added concepts: [[mcp-server-configuration]], [[service-account-authentication]]
- Updated [[model-context-protocol]] with OpenMetadata implementation use case.
- Updated [[openmetadata]] with Agentic Access (JWT/Service Accounts) details.

---

## Current Overview (update this to reflect the new source)
---
type: overview
title: Project Overview
tags: []
related: [Airflow vs Kstra.md, ai-sdk Bring Semintics to your An AI Agents via the Open May OpenMetadata & Collab AI SDK.md]
sources: ["Airflow vs Kstra.md", "ai-sdk Bring Semintics to your An AI Agents via the Open May OpenMetadata & Collab AI SDK.md", "Ambiente sviluppo su Container.md", "Apache Sedona Coordinate Transform.md", "best-abilities-for-workflows-a-guide-to-effective-dbt-use.md", "analyizing-real-estate-data-with-apache-sedona-20260506.md", "Announcing OpenMetadata 1.12-20260506.md", "announcing-openmetadata-1-13-20template-20260506.md", "architetture-open-source-simili-20260506.md", "ArcKit — AI Toolkit for Solution & Enterprise Architects-20260506.md", "leo-2023-elementary-dbt.md", "Automate Data Quality Checks with AI Agents-20260506.md", "benchmark-kg-llm-accuracy-2023", "best-practices-for-whorks-a-scale-guide-to-effective-dbt-use-20260506.md", "beyond-troing-data-how-to-use-duckdb-motherduck-and-kestra-for-etl.md", "BRAINSTOR - Integrazione della Spatial Data Infrastructure (SDI) con la Data Platform (DP).md", "building-a-dbt-ui-i-wish-existed.md", "building-a-semantic-intelligence-layer-for-the-ai-data-stack", "building-a-semantic-layer-for-the-ai-era-beyond-sql-generation", "building-blocks-of-semantics-ontologies-knowledge-graphs-metrics-layers", "building-data-platforms-the-etl-bias.md", "Cataloghi Data Lake - Differenze Nessie, Polaris e Unity.md", "chill-your-data-with-iceberg-write-audit-publish.md", "claude-code-is_already_scarily_good_at_data_engineering.md", "Collate vs OpenMetadata Managed Service for Data Teams at $\text{Scale.md}$", "Come installare il server mcp di Dremio.md", "assaf-lavi-2022-complex-geospatial-analytics-with-dbt", "Configurare Claude con server MCP di OpenMetadata.md"]
---
# Overview

This wiki contains all the material regarding the Data Platform system of "Regione Liguria". It contains project-related notes (meetings, architectural documents, diagrams, decisions) and documents (articles, videos, etc.) collected from various web sources.

The scope of this wiki covers the evolution of the Modern Data Stack into the "AI Stack". It explores the critical role of data engineering in supporting Generative AI through technologies like [[retrieint-augmented-api]] and [[vector-databases]]. A central focus is placed on ensuring the reliability of AI through [[data-observability]] and [[data-lineage]], emphasizing that the success of Large Language Models depends fundamentally on the quality, security, and governance of the underlying data pipelines. Recent advancements include [[ai-driven-data-quality]], which leverages LLMs and autonomous agents for automated rule generation, anomaly detection, and predictive failure detection.

The integration of semantic context is a key frontier. Through tools like [[openmetadata-ai-scale]], the platform is highly focused on "Active Governance," where AI agents can leverage [[model-context-protocol]] to access business glossaries, lineage, and even perform [[catalog-mutates]] to curate metadata. This is supported by platforms like [[collate-ai-studio]], which allow the deployment of specialized, purpose-built agents. The introduction of the **Semantic Context Layer** in [[open-metadata]] (v1.13) marks a shift from standardizing metadata to standardizing *meaning* via the **Knowledge Graph** and **Ontology Explorer**. Recent research, such as the [[benchmark-kg-llm-accuracy]], provides empirical evidence that using a Knowledge Graph (via [[text-to-sparql-for-enterprise]]) significantly improves LLM accuracy in complex enterprise environments where direct Text-to-SQL fails.

A major recent development is the implementation of a **Semantic Intelligence Layer**. By combining a semantic catalog (like [[openmetadata]]) with an action-oriented toolset (like [[mcp-toolbox]]), organizations can bridge the "semantic gap." This allows AI agents, using interfaces like [[gemini-int]], to perform high-ability tasks such as **Automated Tag Synchronization** (propagating metadata from [[openmetadata]] to [[looker]]) and **Generating Custom Metadata Insights** (extracting stats from catalogs into databases like [[postgres]] for BI visualization). This architecture ensures that data is not just clean, but truly **AI-Ready**. This evolution is further driven by the need to move beyond simple SQL generation to a framework that captures the **What, Why, and How** of data, providing the business intent necessary for autonomous agents to act reliably.

The wiki also details robust engineering practices for scaling and maintaining data infrastructure. This includes the implementation of [[data-contracts]] and [[data-governance]] to ensure stability. Recent explorations focus on the "Low-Ops Lakehouse" paradigm, which leverages the combination of [[duckdb]] for high-performance compute and [[apache-iceberg]] for scalable, governed storage. This approach emphasizes minimizing operational complexity through patterns like "Stage Then Commit" ingestion, efficient [[compintion-patterns]], and metadata hygiene. A key architectural strategy discussed is [[unbundled-data-architecture]], which decoupts storage from compute to optimize costs and prevent vendor lock-in. This is further enhanced by the [[hybrid-execution-pattern]] provided by [[motherduck]], allowing for seamless querying across local and cloud datasets.

A critical advancement in data reliability is the **Write-Audit-Publish (WAP)** pattern, particularly when implemented via **Apache Iceberg**'s branching and tagging features. This pattern allows for writing data to isolated branches, performing rigorous audits, and atomically publishing to production via metadata-for-only operations. As demonstrated by **Expedia Group**, this approach can drastically reduce both storage consumption and release costs by eliminating the need for redundant ETL runs and physical data duplication.

The wiki also incorporates best practices for dbt workflow management, emphasizing the importance of version control, environment separation (dev vs prod), and modular modeling. By adopting layered architectures (Staging $\rightarrow$ Intermediate $\rightarrow$ Marts) and utilizing features like Slim CI and source freshness, analytics teams can ensure highly maintainable and efficient pipelines. For environments where cloud-native tools like dbt Cloud introduce friction, tools like [[dbt-workbench]] provide an **artifact-driven** alternative, allowing for lineage and SQL inspection in air-gapped or on-premise setups.

The implementation of a **CI/CD Git Flow** provides the operational backbone for these pipelines. By utilizing a **Unified Repository Pattern**, the platform ensures that Kestra orchestration flows are versioned alongside dbt transformation code. Through a structured **Environment Promotion Workflow** (`dev` $\rightarrow$ `test` $\rightarrow$ `stage` $\rightarrow$ `prod`), the platform automates the deployment of both code and orchestration logic, using GitLab CI/CD to handle namespace switching and flow renaming across different Kubernetes clusters.

Additionally, the wiki explores specialized workflows for geospatial science, moving away from monolithic environments like Conda toward modular stacks using [[pyenv]] and [[poetry]]. This includes the use [[duckdb]] for in-process analytical queries and [[geoparquet]] for optimized, and cloud-native geospatial storage, alongside [[juniper]] for SQL-driven data science and visualization. For large-scale spatial analytics, [[apache-sedona]] is utilized, though users must be aware of its CRS transformation limitations (specifically the lack of `.gsb` support) and should implement a [[spatial-pre-handling-pattern]] using tools like [[geopandas]] or GDAL when high precision is required.

The integration of the **Spatial Data Infrastructure (SDI)** into the **Data Platform (DP)** is a critical architectural milestone. This involves a complex pipeline to ingest vector and raster data from legacy systems (Oracle/PostGIS) into the modern Lakehouse (MinIO/Iceberg). A key focus is the **Hybrid Optimized Architecture**, which uses the existing PostGIS (`viscarto`) as a robust staging and transformation layer to handle complex regional coordinate transformations (EPSpi:7tro) before final ingestion into the DP via Spark.

The architecture is moving toward the **Agentic Enterprise**, where the semantic layer acts as the "trust fabric." This involves a fundamental shift from **descriptive** semantics (explinting the past) to **prescriptive** semantics (governing the future). This is achieved through a system of four building blocks: the **Data Substrate** (execution), **Ontologies** (meaning), **Knowledge Graphs** (context), and **Metrics Layers** (executable truth via semantic contracts). This evolution is further supported by the emergence of **Agentic Debugging Workabilities**, where agents use metadata, code access, and CLI tools to autonomously remediate pipeline failures using structured **Agentic Skills**.

Finally, the platform is expanding its interoperability with AI agents through the **Model Context Protocol (MCP)**. Recent implementations, such as the [[dremio-mcp-server]], demonstrate how the virtualization layer can be exposed to LLMs like Claude. By using tools like [[uv]] for deployment and configuring specialized modes like `FOR_DATA_PRE_PATTERNS`, the platform enables autonomous agents to perform complex data exploration and infrastructure monitoring directly through the Dremio engine.
