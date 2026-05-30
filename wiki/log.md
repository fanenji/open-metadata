# Research Log

- 2026-05-30 — wiki-lint: 66 warning, 379 info (--fix applicato: 52 frontmatter aggiunti, 1 created field aggiunto, lint.py allineato a schema.md; --no-semantic --no-qmd)

## 2026-05-13

- Project created


## 2024-05-24

- Ingested source document: OpenMetadata Architecture Overview (sources.md)
- Created entity pages: openmetadata, ingestion-framework
- Created concept pages: data-profiling, data-lineage, data-quality, glossary-tags
- Updated wiki/index.md with new entries
- Updated wiki/overview.md to reflect new source

## 2026-05-14

- Ingested source: "OMD - Getting Started.md" — Official OpenMetadata getting started guide.
- Created entity page: [[openmetadata]] — Updated with feature summary and user roles.
- Created concept pages: [[unified-metadata-graph]], [[openmetadata-connectors]], [[openmetadata-features]], [[openmetadata-collaboration]], [[openmetadata-insights]].
- Updated wiki/index.md with new entries.
- Updated wiki/overview.md to reflect new source and concepts.

## 2026-05-14 ingest | Kubernetes Native Orchestrator

- Ingested source: **OMD - Kubernetes Native Orchestrator.md** (official OpenMetadata v1.12.x documentation)
- Created entity pages: [[omjob-operator]], [[pipeline-service-client]]
- Created concept page: [[kubernetes-native-orchestrator]]
- Updated [[index.md]] with new entries under Entities, Concepts, and Sources
- Updated [[overview.md]] to reflect the new K8s-native ingestion architecture
- Key findings: v1.12 introduces two K8s orchestration modes; OMJob Operator provides exit handler guarantee and failure diagnostics not available with native Jobs

## 2026-05-14 ingest | OMD - Kubernetes On Premises

- Ingested official OpenMetadata documentation on deploying to on-premises Kubernetes clusters.
- Created entity pages: [[kubernetes]], [[helm-charts]], [[nfs-subdir-external-provisioner]].
- Created concept pages: [[on-premises-kubernetes-deployment]], [[external-dependencies-configuration]], [[airflow-storage-requirements]].
- Updated [[kubernetes-native-orchestrator]] with cross-reference to the Airflow-dependent deployment model.
- Noted tension between Airflow-dependent Helm deployment and the Airflow-free K8s-native orchestrator.

## 2026-05-14 ingest | OMD - Kubernetes Orchestrator Operations & Troubleshooting

- Ingested official OpenMetadata v1.12.x operations and troubleshooting guide for the Kubernetes native orchestrator.
- Created concept pages: [[airflow-to-kubernetes-migration]], [[ingestion-pipeline-troubleshooting]], [[exit-handler-guarantee]].
- Updated [[wiki/index.md]] with new entries under Concepts and Sources.
- Key findings: OMJob Operator provides guaranteed exit handlers (vs. best-effort in plain K8s mode); migration from Airflow is manual and does not auto-transfer schedules; common failure modes include Queued state, OOMKilled, RBAC errors, and CronJob scheduling issues.

## 2026-05-14 ingest | REST API Connector Documentation

- Ingested source: `rest-api-connector-openmetadata-integration-docume-20260514.md` — official OpenMetadata v1.12.x documentation for the REST API Connector (Beta).
- Created entity page: [[rest-api-connector]] — documents the Beta connector's features, requirements (OpenAPI Schema URL + optional Token), connection workflow, and AutoPilot integration.
- Created concept page: [[openapi-specification]] — explains the OpenAPI Specification standard and its role as the schema format enabling the REST API Connector.
- Updated [[openmetadata-connectors]] index entry to include the REST API Connector.
- Flagged AutoPilot as a potential future concept page; not yet documented in the wiki.

## 2026-05-14

- **ingest** | Research: Production Namespace Best Practices — Added source page and three new concept pages: [[kubernetes-namespaces]], [[resource-quotas-limit-ranges]], and [[namespace-rbac]]. Updated [[kubernetes]] and [[omjob-operator]] pages with namespace governance cross-references. Updated index and overview.

## 2026-05-14

- Ingested source: Understand Code Layout - OpenMetadata Documentation (v1.12.x developer guide)
- Created entity page: [[openmetadata-code-layout]] — repository structure, build tooling, and architectural components
- Created concept page: [[schema-first-approach]] — JSON Schema as source of truth driving Java/Python code generation
- Created concept page: [[change-events-system]] — event capture via ContainerResponseFilter, dual storage in DB and Elasticsearch
- Created concept page: [[pull-based-ingestion-model]] — active pull vs. push for metadata extraction
- Created entity pages for peripheral tools: [[dropwizard]], [[flyway]], [[swagger]], [[google-oauth]]
- Updated [[ingestion-framework]] with specific directory paths for Source, Processor, Sink, Stage, BulkSink
- Updated [[openmetadata-connectors]] with exact source directory locations for connector development
- Updated [[unified-metadata-graph]] with confirmation of entity types and event-driven update mechanism
- Updated [[external-dependencies-configuration]] with confirmation of MySQL/Postgres and Elasticsearch roles
- Updated [[airflow-to-kubernetes-migration]] with context on Airflow DAG definitions in the codebase
- Updated wiki/index.md and wiki/overview.md to reflect all new pages

## 2026-05-14

- Ingested source: [[openmetadata-system-architecture-developer-guide---20260514]] — Official developer guide to the OpenMetadata v1.12.x system architecture and core dependencies.
- Created concept page: [[openmetadata-system-architecture]] — High-level architecture overview identifying the four core dependencies: JSON Schemas, Dropwizard/Jetty, MySQL 8.x, and ElasticSearch 7.x.
- Created entity page: [[mysql-8x]] — Relational database used as the primary transactional metadata store.
- Created entity page: [[elasticsearch-7x]] — Search engine used to index metadata and power full-text search.
- Created entity page: [[jsonschemas]] — JSON Schema definitions that serve as the single source of truth for metadata entity structures.
- Updated [[external-dependencies-configuration]] cross-reference: noted version-specific ElasticSearch 7.x reference vs. broader ElasticSearch/OpenSearch support.
- Updated [[index]] and [[overview]] to include new pages.

## 2026-05-14 ingest | OpenMetadata System Architecture Developer Guide (v2)

- Ingested source: `openmetadata-system-architecture-developer-guide---20260514-2.md` — a terse official developer guide page listing the four core dependencies (JSON Schemas, Dropwizard/Jetty, MySQL 8.x, ElasticSearch 7.x).
- Created entity page for [[jetty]] to document its role as the embedded HTTP server within Dropwizard.
- Updated [[openmetadata-system-architecture]] concept page to explicitly include Jetty alongside Dropwizard and to cross-reference the [[change-events-system]] and [[pull-based-ingestion-model]].
- Added new source entry and Jetty entity to the wiki index.

---
type: overview
title: Wiki Log
tags: []
related: []
---

## 2026-05-14

- Ingested admin-guide-openmetadata-administration-documentat-20260514.md — Official OpenMetadata v1.12.x Administration Guide covering Roles & Policies, Teams & Users, Data Observability Alerts, Custom Properties, Data Insights, Audit Logs, Permission Debugger, Persona customization, Reindexing Search, and CLI Ingestion with Basic Auth. Created concept pages for openmetadata-administration, roles-and-policies, teams-and-users, data-observability-alerts, custom-properties, audit-logs, permission-debugger, persona-and-landing-page-customization, reindexing-search, and cli-ingestion-with-basic-auth. Updated index.md and overview.md.

## 2026-05-14 ingest | Customizable Landing Page with Pluggable Panels

- Ingested source: `customizable-landing-page-with-pluggable-panels----20260514.md` (official OpenMetadata v1.12.x documentation on persona-based landing page customization).
- Created concept page: [[pluggable-panels]] — documents the modular UI widget system, current panel catalog, configuration mechanism, persona switching, and future roadmap.
- Created entity page: [[persona]] — defines Persona as a named role profile with landing page customization, switching, and default persona capabilities.
- Updated [[wiki/index.md]] with new entity (Persona), concept (Pluggable Panels), and source entries.
- Updated [[wiki/overview.md]] to reflect the new customization and persona management capabilities.
- Noted minor tension: the general panel list omits "Pipeline Status" but the Data Engineer use case references it; flagged for clarification.

## [2026-05-14] ingest | How to Define Personas in OpenMetadata

- Ingested source: **how-to-define-personas-in-openmetadata---openmetad-20260514.md** (Official OpenMetadata v1.12.x documentation on defining Personas).
- Updated entity page: [[persona]] — expanded from stub with full definition, purpose, creation steps, examples (Data Engineer, Data Steward, Data Scientist), and relationship to Roles/Policies.
- Created concept page: [[role-based-ui-customization]] — new page exploring the mechanism of UI customization based on organizational roles, distinguishing it from access control.
- Updated index: added [[role-based-ui-customization]] to Concepts, added source entry.
- Updated overview: reflected new Persona definition details and role-based UI customization concept.
- Open questions identified: full set of UI elements controllable by Persona, interaction with Roles/Policies, multi-Persona assignment behavior.

## [2026-05-14] ingest | How to Delete a Service Connection

Ingested official documentation source: "How to Delete a Service Connection" from OpenMetadata v1.12.x Admin Guide. Created source page [[how-to-delete-a-service-connection-official-docume-20260514]] and concept page [[delete-service-connection]] documenting the UI deletion procedure, the two-step DELETE confirmation safeguard, and important considerations about downstream effects on ingested metadata, lineage, and ingestion pipelines. Updated [[wiki/index.md]] with new entries. Noted ambiguity in the source where the confirmation prompt conflates "delete the database" with "delete the service connection."

## 2026-05-14 ingest | Manage Teams and Users - OpenMetadata Documentation

- Ingested source: [[manage-teams-and-users---openmetadata-documentatio-20260514]] (official v1.12.x Admin Guide page on Teams and Users).
- Updated [[teams-and-users]] concept page to explicitly include the multi-Admin model and team types.
- Created new concept page [[multi-admin-model]] documenting decentralized administration architecture.
- Created new concept page [[team-types]] documenting team classifications and flagging open questions about available types and change effects.
- Updated [[wiki/index.md]] with new entries for multi-admin-model and team-types.

## 2026-05-14 ingest | Team Structure in OpenMetadata Official Documentation

- Ingested source: `team-structure-in-openmetadata-official-documentat-20260514.md` — official v1.12.x documentation on team hierarchy.
- Created concept page: [[team-hierarchy-rules]] — complete parent-child matrix, data asset ownership rules, Group immutability, and open questions.
- Updated entity page: [[team-types]] — resolved open questions about available types, added definitive hierarchy constraints and ownership rules.
- Updated [[wiki/index.md]] — added [[team-types]] to Entities, [[team-hierarchy-rules]] to Concepts, and the source to Sources.
- Updated [[wiki/overview.md]] — added team hierarchy and governance details to the administration section.
- Flagged open question: Can BusinessUnit, Division, or Department types be changed after creation? Only Group immutability is explicitly documented.

## [2026-05-14] ingest | How to Add a Team | OpenMetadata Admin Guide

- Ingested source: **how-to-add-a-team-openmetadata-admin-guide---openm-20260514.md** — official OpenMetadata v1.12.x documentation for the Add Team UI workflow.
- Created concept page: [[how-to-add-a-team]] — step-by-step procedure with emphasis on Group immutability and data asset ownership constraints.
- Created concept page: [[public-team]] — documents the Public Team toggle for open collaboration.
- Updated [[wiki/index.md]] with new entries under Concepts and Sources.
- Updated [[wiki/overview.md]] to reflect the new team creation procedure and Public Team concept.
- Cross-referenced existing pages: [[team-types]], [[team-hierarchy-rules]], [[teams-and-users]], [[multi-admin-model]].
- Flagged open question: Can non-Group team types (BusinessUnit, Division, Department) be changed after creation? The "How to Change the Team Type" page is referenced in navigation but not yet ingested.

## 2026-05-14

- Ingested source: How to Add Users to Teams - OpenMetadata Documentation (v1.12.x). Created procedural concept page [[how-to-add-users-to-teams]] documenting the two workflows for adding users to teams (during invitation and for existing users), role inheritance from teams, and multi-team membership capability. Created [[multi-team-membership]] concept page to capture the implications and open questions around users belonging to multiple teams. Updated index with new entries.

## [2026-05-14] ingest | How to Change the Team Type Official Documentation

Ingested official OpenMetadata v1.12.x documentation on changing team types via the UI. Created source page and [[how-to-change-team-type]] concept page documenting the procedure, known constraints, and critical warnings about Group immutability, hierarchy validity, and impact on child teams. Identified significant gaps in the official documentation regarding validation of hierarchy rules during type changes and the interaction with Group immutability constraints from [[how-to-add-a-team]]. Flagged open questions for further investigation.

## 2026-05-14 ingest | Advanced Guide for Roles and Policies - OpenMetadata Documentation

- Ingested source: `advanced-guide-for-roles-and-policies---openmetada-20260514.md`
- Created concept pages: [[hybrid-rbac-abac-model]], [[viewbasic-viewall-operations]], [[bot-authentication]], [[resource-attributes]]
- Updated [[roles-and-policies]] with cross-references to new concept pages
- Updated [[wiki/index.md]] with new entries
- Updated [[wiki/overview.md]] to reflect expanded authorization and authentication coverage
- Flagged: The source references subsequent pages ("Building Blocks of Authorization - Rules, Policies, and Roles" and "Use Cases - Creating Roles & Policies in OpenMetadata") that are not yet ingested. These should be located and analyzed to complete the authorization picture.

## 2026-05-14 ingest | Building Blocks of Authorization - Rules, Policies, and Roles

- Ingested source: `building-blocks-of-authorization---rules-policies--20260514.md` (OpenMetadata v1.12.x official documentation)
- Created concept pages: `authorization-rules`, `authorization-policies`, `spel-conditions`, `search-rbac`, `default-organization-policy`
- Created source summary page: `building-blocks-of-authorization---rules-policies--20260514`
- Updated `wiki/index.md` with new entries under Concepts and Sources
- Updated `wiki/overview.md` to reflect the expanded authorization framework documentation
- Key findings: Three-tier architecture (Rules → Policies → Roles) with SpEL-based conditions as the ABAC implementation; Deny precedence for conflict resolution; policy inheritance flows top-down through team hierarchy; Search RBAC is opt-in and disabled by default; default Organization Policy provides baseline ownership governance
- Cross-references established with existing pages: `roles-and-policies`, `hybrid-rbac-abac-model`, `resource-attributes`, `viewbasic-viewall-operations`, `teams-and-users`, `team-hierarchy-rules`

## 2026-05-14

- **ingest** | Use Cases - Creating Roles & Policies in OpenMetadata — Ingested official documentation covering four practical policy design patterns: ServiceOwner role for ingestion delegation, Data Steward role for governance, team-owned data access restriction, and tag-based PII protection. Created entity pages for Data Steward Role, ServiceOwner Role, and Data Consumer Role; concept page for Tag-Based Access Control; synthesis page for Policy Use Cases. Updated index and overview.

## 2026-05-14 ingest | How To Run Ingestion Pipeline Via CLI with Basic Auth

- Ingested official OpenMetadata v1.12.x documentation on CLI-based ingestion with Basic Auth.
- Created source page: [[how-to-run-ingestion-pipeline-via-cli-with-basic-a-20260514]]
- Created concept page: [[security-config]] — YAML configuration block for JWT token and authProvider.
- Created entity page: [[metadata-cli]] — The `metadata` command-line tool for ingestion.
- Updated concept page: [[cli-ingestion-with-basic-auth]] — Enriched with full procedural steps, terminology clarification (JWT-based, not HTTP Basic Auth), and comparison with other ingestion methods.
- Updated index with new entries.
- Flagged open questions: Can bots other than ingestion-bot be used? How does CLI ingestion interact with the K8s orchestrator?

## 2026-05-14

- **Ingest** | Reindexing Search — OpenMetadata Documentation: Ingested the official v1.12.x documentation for the Reindexing Search administrative operation. Updated the [[reindexing-search]] concept page from a stub to a full operational reference covering the symptom checklist, UI procedure, Recreate Indexes toggle, all nine configuration parameters with defaults and best practices, a high-performance starting configuration, and the ambiguous re-installation fallback. Added the source page at [[reindexing-search---openmetadata-documentation-20260514]]. Updated [[wiki/index.md]] with the new source entry and expanded concept description.

## 2026-05-14 ingest | Resolving Data Insights and KPI Display Issues in OpenMetadata

Ingested official OpenMetadata v1.12.x troubleshooting documentation for Data Insights Application display failures. Created concept pages: [[data-insights-application-troubleshooting]] (three-step diagnostic workflow covering four symptom patterns), [[backfill-configuration]] (historical data processing toggle), and [[recreate-data-insights-index]] (application-specific index rebuild distinct from general [[reindexing-search]]). Added source page and updated wiki/index.md with new entries. Updated overview.md to reflect the new Data Insights troubleshooting domain.

## 2026-05-14

- Ingested source: Permission Debugger | Analyze and Troubleshoot User Access - OpenMetadata Documentation (permission-debugger-analyze-and-troubleshoot-user--20260514.md)
- Created/updated entity page: [[permission-debugger]] with full workflow, resource types, operations, evaluation summary metrics, and worked examples
- Created concept page: [[resource-types-permission-debugger]] documenting the complete enumerable list of resource types available in the debugger
- Created concept page: [[evaluation-summary-permission-debugger]] documenting the quantitative metrics output and their diagnostic interpretation
- Updated [[wiki/index.md]] with new entity, concepts, and source entries
- Updated [[wiki/overview.md]] to reflect expanded Permission Debugger documentation

## 2026-05-14 ingest | Persona and Landing Page Customization in OpenMetadata

- Ingested source: `persona-and-landing-page-customization-in-openmeta-20260514.md` — official overview page from OpenMetadata v1.12.x Administration Guide.
- Updated [[persona]] entity page: added multi-persona switching capability, design philosophy, and open questions about interaction with RBAC-ABAC.
- Updated [[persona-and-landing-page-customization]] concept page: clarified hierarchical relationship (Persona → Landing Page → Pluggable Panels), added benefit statements, and distinguished presentation layer from authorization layer.
- Updated [[role-based-ui-customization]] concept page: strengthened link to Personas as implementation mechanism, added multi-persona flexibility as key differentiator.
- Updated [[wiki/index.md]]: added new source entry, updated descriptions for persona, persona-and-landing-page-customization, and role-based-ui-customization.
- Updated [[wiki/overview.md]]: integrated persona and landing page customization into the administration and user experience narrative.

## 2026-05-14 ingest | MCP Server - OpenMetadata Documentation

- Ingested official documentation for the OpenMetadata MCP Server (v1.12.x).
- Created entity page: [[mcp-server]] — built-in application exposing the unified metadata graph to AI assistants via MCP.
- Created concept page: [[model-context-protocol]] — the open standard enabling uniform AI-to-data-system connections.
- Created source page: [[mcp-server---openmetadata-documentation-20260514]].
- Updated [[wiki/index.md]] with new entries for MCP Server (entity) and Model Context Protocol (concept).
- Updated [[wiki/overview.md]] to reflect AI-powered metadata interaction as a new platform capability.
- Identified open governance question: best practices for dedicated bot users/scoped roles for MCP Server PAT access versus reusing personal PATs.

## 2026-05-14

- Ingested source: dbt Workflow | OpenMetadata Data Build Tool Integration — official documentation for the dbt connector covering artifact requirements (manifest.json, catalog.json, run_results.json), dbt Core storage configuration, dbt Cloud API integration, and ten categories of ingested metadata including lineage, tests, tags, and governance attributes.

## 2026-05-14 ingest | Embedding an MCP Server into OpenMetadata

- Ingested community meetup presentation on embedding MCP server into OpenMetadata.
- Created entity pages: [[application-framework]], [[personal-access-token]].
- Created concept pages: [[agentic-ai]], [[bottom-up-top-down-enrichment]].
- Updated [[mcp-server]] with embedded architecture rationale, identity-preserving auth, and use cases.
- Updated [[unified-metadata-graph]] with bottom-up + top-down enrichment concept.
- Updated [[hybrid-rbac-abac-model]] with PAT-based MCP permission propagation.
- Updated index and overview to reflect new AI/agentic capabilities.

---
type: overview
title: Wiki Log
tags: []
related: []
---
## 2026-05-14

- Ingested source: OpenMetadata Community Meeting Oct 2023 Release 1.2.0 — documented domains, data products, glossary approval workflow, cost analysis, knowledge center, personas, metadata applications framework, search indexes, stored procedures, Chrome extension, Collate Inc., and data mesh concepts.

## 2026-05-14 ingest | Oracle Connector | OpenMetadata Enterprise Database Guide

- Created source page: [[Oracle Connector  OpenMetadata Enterprise Database Guide]]
- Created entity page: [[oracle-connector]] — Turnkey connector for Oracle databases (12c–21c), covering permission models, `python-oracledb` driver, and supported workflows.
- Created concept page: [[oracle-schema-select-limitation]] — Documents Oracle's lack of native schema-level `SELECT` grant and workarounds for Profiler/Data Quality.
- Updated index: added Oracle Connector source, entity, and concept entries.
- Updated overview: added Oracle connector coverage to the project overview.

## 2026-05-14 ingest | PostgreSQL Connector  OpenMetadata Database Integration

- Ingested official PostgreSQL connector documentation (v1.12.x).
- Created entity page: [[postgresql-connector]] — covers requirements, SSL, IAM, stored procedure lineage, and `pg_stat_statements` dependency.
- Created concept page: [[pg-stat-statements]] — documents critical limitations (eviction, normalization, no timestamps), mitigation strategies, and custom query source alternative.
- Created concept page: [[stored-procedure-lineage]] — configuration requirements for capturing lineage from PostgreSQL stored procedures.
- Created concept page: [[postgresql-ssl-modes]] — SSL connection modes and CA certificate configuration.
- Created concept page: [[postgresql-iam-authentication]] — AWS RDS IAM authentication setup with IAM policy requirements.
- Updated [[index]] with new entity and concept entries.
- Updated [[overview]] to reflect PostgreSQL connector and `pg_stat_statements` limitations.

## 2026-05-14

- Ingested source: How to Classify Data Assets | Official Documentation — procedural guide for applying classification tags, usage tracking, Tiers, System Classification, and tag request workflow.
- Created concept pages: [[classification-tags]], [[tiers]], [[system-classification]], [[tag-request-workflow]].
- Updated index with new entries under Concepts and Sources.

## 2026-05-14

- Ingested source: How to Request for Classification Tags | Official Documentation — documented the Task-based tag request workflow (three-tab interface, Accept/Edit Accept resolution) and tag-specific conversation threads (@mentions, #mentions, replies, reactions).
- Created concept page: [[tag-request-workflow]] — enriched with procedural details from the official source (entry point via ? icon, three-tab tag interface, assignee actions).
- Created concept page: [[conversations-around-classification]] — documented the tag-level conversation feature, its capabilities, and distinction from the request workflow.
- Updated index with new source and concept entries.

## 2026-05-14

- Ingested source: Sample Data Handling Using PII Tags - OpenMetadata Documentation (v1.12.x). Created concept pages for [[pii-sample-data-masking]] and [[tag-inheritance-for-masking]]. Updated [[wiki/index.md]] with new entries. Identified open questions regarding API-level masking scope and complete PII tag list.

## 2026-05-14 ingest | Adding Auto Classification Workflow through UI - OpenMetadata Documentation

- Ingested source: [[adding-auto-classification-workflow-through-ui---o-20260514]]
- Created concept pages: [[auto-classification]], [[agent-based-ingestion]], [[sample-data-storage-toggle]]
- Updated index with new entries under Concepts and Sources
- Key findings: Auto Classification extends the agent-based ingestion pattern to governance automation; configured per-database service with a sample data storage toggle; complements manual classification and tag request workflows
- Open questions flagged: relationship between Auto Classification and Auto PII Tagging; detection methods used by the agent

## 2026-05-14 ingest | External Storage for Sample Data

- Ingested source: [[external-storage-for-sample-data---openmetadata-do-20260514]] — Official documentation for external sample data storage (v1.2.1+).
- Created concept page: [[sample-data-external-storage]] — Covers S3/Parquet export capability, three-tier credential hierarchy, configurable sampling parameters, and the UI 50-row limit vs. Parquet row count distinction.
- Created concept page: [[order-of-precedence-storage-credentials]] — Documents the Schema > Database > Service resolution hierarchy for storage credentials.
- Created concept page: [[openmetadata-storage-config]] — Documents the opt-out mechanism for skipping sample data upload at specific schema/database levels.
- Updated index with new entries under Concepts and Sources.
- Updated overview to reflect external storage capability and its relationship to auto-classification and profiling workflows.

## 2026-05-14

- Ingested source: **What are Tiers | OpenMetadata Classification Tiers Guide** — Official documentation for the five-tier importance-based classification system in OpenMetadata v1.12.x. Expanded the `[[tiers]]` concept page with the complete tier structure, impact/usage matrix, "start with extremes" methodology, Tier 5 decluttering practice, and UI application procedure. Added source page and updated index.

## 2026-05-14 ingest | Superset Connector: OpenMetadata Dashboard Integration

- Ingested official Superset connector documentation (v1.12.x).
- Created entity page: [[superset-connector]] — turnkey dashboard connector for Apache Superset 2.0.0+.
- Created concept page: [[dashboard-connectors]] — new connector category distinct from database connectors.
- Created concept page: [[dashboard-lineage]] — traceability from dashboards to database tables.
- Updated [[openmetadata-connectors]] index entry to reflect dashboard connector category.
- Updated [[data-lineage]] cross-references to include dashboard lineage.
- Updated [[postgresql-ssl-modes]] cross-references for dashboard connector SSL context.
- Noted Airflow dependency in SSL configuration; open question on K8s-native orchestrator compatibility.

## [2026-05-14] ingest | How to Assign or Change Data Ownership - OpenMetadata Documentation

## 2026-05-14

- Ingested [[how-to-request-for-tags-official-documentation---o-20260514]] — Official documentation for requesting classification tags and conversations around tags in OpenMetadata v1.12.x.
- Updated [[tag-request-workflow]] concept page with the `?` icon entry point, three-tab diff interface (Current, New, Difference), and Task-based workflow details.
- Updated [[conversations-around-classification]] concept page with the Conversation icon entry point, @mentions, #mentions, replies, reactions, editing, and deletion.

## [2026-05-14] ingest | How to Add Glossary Terms | Official Documentation

- Ingested source: [[how-to-add-glossary-terms-official-documentation---20260514]]
- Created entity page: [[glossary-terms]] — documents Glossary Terms as a named entity with tag propagation behavior
- Created concept page: [[how-to-add-glossary-terms]] — step-by-step UI procedure for applying Glossary Terms to data assets
- Updated [[glossary-tags]] concept page to include tag propagation section
- Updated [[classification-tags]] concept page to cross-reference glossary term tag propagation
- Updated [[tag-inheritance-for-masking]] concept page to note similarity with glossary term propagation
## [2026-05-15] external batch delete | 16 source files

Deleted 16 source files and 0 wiki pages.

Sources:
- column-tests---yaml-config-openmetadata-quality-co-20260514-10.md
- column-tests---yaml-config-openmetadata-quality-co-20260514-11.md
- column-tests---yaml-config-openmetadata-quality-co-20260514-12.md
- column-tests---yaml-config-openmetadata-quality-co-20260514-13.md
- column-tests---yaml-config-openmetadata-quality-co-20260514-14.md
- column-tests---yaml-config-openmetadata-quality-co-20260514-15.md
- column-tests---yaml-config-openmetadata-quality-co-20260514-16.md
- column-tests---yaml-config-openmetadata-quality-co-20260514-17.md
- column-tests---yaml-config-openmetadata-quality-co-20260514-2.md
- column-tests---yaml-config-openmetadata-quality-co-20260514-3.md
- column-tests---yaml-config-openmetadata-quality-co-20260514-4.md
- column-tests---yaml-config-openmetadata-quality-co-20260514-5.md
- column-tests---yaml-config-openmetadata-quality-co-20260514-6.md
- column-tests---yaml-config-openmetadata-quality-co-20260514-7.md
- column-tests---yaml-config-openmetadata-quality-co-20260514-8.md
- column-tests---yaml-config-openmetadata-quality-co-20260514-9.md
## [2026-05-15] external delete | bulk-export-data-assets-via-csv-in-openmetadata----20260514-2.md

Deleted 1 source file and 0 wiki pages.
## [2026-05-15] external delete | bulk-import-data-assets-via-csv-in-openmetadata----20260514-2.md

Deleted 1 source file and 0 wiki pages.


## [2026-05-14] ingest | How to Customize OpenMetadata

- Ingested source: [[how-to-customize-openmetadata---openmetadata-docum-20260514]]
- Created concept page: [[theme-customization]] — Global UI customization with company branding and custom colors.
- Updated [[persona-and-landing-page-customization]] to note the distinction between global theme customization and per-user persona customization.
- Updated [[openmetadata-administration]] to reference theme customization under Settings > Preferences.

---
type: overview
title: Activity Log
tags: []
related: []
---

# Activity Log

## 2026-05-14

- Ingested [[overview-of-announcements-official-documentation---20260514]] — Official documentation for the Announcements feature in OpenMetadata v1.12.x.
- Created [[announcements]] concept page — Scheduled, time-bound notifications about upcoming changes to data assets.
- Created [[activity-feed]] concept page — Central UI component displaying real-time updates about data assets.
- Updated [[openmetadata-collaboration]] — Added Announcements as a collaboration feature.
- Updated [[data-observability-alerts]] — Added note about alerts for announcements.
- Updated [[openmetadata-features]] — Added Announcements under collaboration features.
- Updated [[wiki/index.md]] — Added new entries for announcements and activity-feed concepts.
- Updated [[wiki/overview.md]] — Added Announcements and Activity Feed to the project overview.

## 2026-05-14 ingest | REST API Connector (Duplicate Source)

- Ingested duplicate source `rest-api-connector-openmetadata-integration-docume-20260514-2.md` — official REST API Connector (Beta) documentation.
- No new pages created; content is already covered by existing [[rest-api-connector]] page.
- Added source page at `wiki/sources/rest-api-connector-openmetadata-integration-docume-20260514-2.md`.
- Updated `wiki/index.md` to include the new source entry.
- Noted open questions: Beta limitations, AutoPilot definition, performance characteristics.

## 2026-05-14 ingest | PowerBI Dashboard Troubleshooting Guide

- Ingested [[powerbi-dashboard-troubleshooting-guide-openmetada-20260514-2]] — official troubleshooting guide for the PowerBI dashboard connector (v1.12.x).
- Created [[powerbi-connector]] entity page — turnkey dashboard connector for Microsoft Power BI.
- Created [[workflow-deployment-error]] concept page — partial failure state during ingestion pipeline deployment.
- Updated [[index]] — added new entity and concept entries.
- Updated [[overview]] — added PowerBI connector and Workflow Deployment Error to the summary.

## 2026-05-14

- Ingested [[guide-to-searching-data-using-hierarchical-view----20260514]] — Official guide for searching data using the Hierarchy View in OpenMetadata v1.12.x. Created [[hierarchy-view]] entity page and [[hierarchical-data-discovery]] concept page. Updated [[data-discovery]] to reference the Hierarchy View as an alternative discovery method.

## [2026-05-14] ingest | Conversation Threads | OpenMetadata Collaboration Guide

## 2026-05-14

- Ingested [[overview-of-announcements-official-documentation---20260514-2]] — Official documentation for the Announcements feature in OpenMetadata v1.12.x. Updated [[announcements]] entity page with details on banner display, landing page placement, emoji reactions, replies, and integration with Alerts for external notifications.

## [2026-05-14] ingest | What is Tiering | OpenMetadata Data Tiering Guide
- 2026-05-22: Saved query page `thinkwe-need-to-answer-the-question-explain-in-det-2026-05-22-061312.md`
- 2026-05-25: Saved query page `thinkwe-need-to-answer-how-can-i-ingest-custom-pro-2026-05-25-140121.md`

- 2026-05-29 12:00 — query: "Configurare su OpenMetadata un utente che ha i diritti di lettura dei metadati di tutti i servizi di tipo database" → 14 pagine consultate


- 2026-05-29 12:10 — query aggiornata: "Configurare utente read-only su metadati servizi database" — aggiunta sezione service account e autenticazione JWT (PAT vs Bot)

