---
type: entity
title: Kestra
created: 2026-04-04
updated: 2026-05-07
tags: ["orchestrator", "yaml", "declarative", "high-performance", "orchestration", "workflow", "scheduling", "data-platform", "pipeline", "infrastructure", "open-source", "kubernetes"]
related: ["apache-airflow", "declarative-yaml-orchestration", "pipeline-blueprints", "metadata-fields-definition", "data-observability-definition", "CI-CD-for-data-pipelines", "data-platform-infrastructure-sizing", "mage", "event-driven-orchestration", "kubernetes-etl-deployment-strategies", "elt-pattern", "data-mesh", "dbt-cloud", "postgresql", "elasticsearch", "airflow", "prefect", "orchestration-system-comparison", "orchestration-code-portability", "orchestration-authn-authz", "kubernetes", "dbt", "dremio", "datahub"]
sources: ["Airflow vs Dagster vs Kestra.md", "Airflow vs Kestra.md", "DEFINIZIONE METADATI.md", "Dimensionamento.md", "Kestra vs Airflow (Video).md", "Orchestratori Data Platform_ Analisi Comparativa 1.md"]
---
# Kestra

Kestra is an open-source, high-performance, declarative workflow orchestrator that uses YAML for workflow definitions. It is language-agnostic and natively cloud-native, designed for Kubernetes. Kestra is positioned as an alternative to [[Apache Airflow]], built around a "data-first" philosophy with internal strongly-typed storage for rich data exchange between tasks. It offers a strong web UI for authoring, monitoring, and managing workflows, with quick setup via a single Docker Compose file.

Within the Data Platform, Kestra serves as the primary Pipeline Orchestrator — the component responsible for scheduling, monitoring, and managing data pipeline workflows. It is referenced in the metadata definition as the system that defines the cron pattern for update frequencies.

## Architecture

Kestra's core is Java-based and can be deployed on VMs or on Kubernetes (K8s) with stateless services that scale horizontally. It integrates well with Terraform for infrastructure as code.

**Components:** The architecture includes:
- **Webserver:** Provides the UI for flow definition (with integrated YAML editor), execution, monitoring, and blueprint management.
- **Executor:** Manages workflow execution.
- **Scheduler:** Handles scheduling and event-driven triggers.
- **Worker:** Executes tasks in Docker containers (on Kubernetes, workers run as pods or jobs), providing isolation. User code for scripting tasks runs in per-task Docker containers, supporting any language (Python, R, Node, etc.). Java-based plugins run natively in the core process.

**Dependencies:** Kestra requires [[PostgreSQL]] and [[Elasticsearch]] for operation. For high throughput and scalability, the Enterprise edition uses a [[Kafka]] backend.

**Kubernetes Deployment:** Kestra can be deployed using Helm charts. Workers execute tasks as Kubernetes pods (or jobs), providing isolation. The control plane (webserver, executor, scheduler) manages orchestration while task execution is isolated on the data plane.

**Flows:** Workflows are defined as YAML files grouped into namespaces. Each flow can contain tasks, inputs, outputs, and control-flow logic such as parallel execution, switches, loops, and error handling.

**Deployment Sizing:** For the Data Platform, the recommended deployment is a single node with 2 vCPU, 8 GB RAM, and 100 GB storage. At scale, the open-source edition caps at ~1,500 executions/min before throughput drops; the Enterprise edition, with a Kafka backend, is needed for >2,000 executions/min.

## Key Features

- **Declarative YAML Orchestration:** Workflows defined as configuration rather than code, making them easy to read, version control, and accessible to non-engineers.
- **Event-Driven Triggers:** Native first-class triggers for S3, Kafka, webhooks, and database changes, enabling real‑time pipeline execution beyond schedule‑only models.
- **Data-First Storage:** Internal strongly‑typed storage allows tasks to exchange rich data, including files, without ad‑hoc glue code.
- **Universal Orchestration:** Kestra can coordinate data pipelines, infrastructure automation, AI workflows, and business processes from a single control plane.
- **Containerized Task Execution:** Multi‑language support via per‑task Docker containers, eliminating dependency conflicts. Over 500 containerized plugins are available, reducing the need for custom pip installations.
- **Rich Web UI:** In‑browser editor with validation, autocompletion, topology and lineage graphs, real‑time log inspection, and embedded plugin documentation. This provides an "out of the box" experience ideal for rapid prototyping and standard ELT/ETL tasks.
- **Developer Experience:** Quick setup via a single Docker Compose file and an intuitive UI/UX that lowers the barrier for adoption.
- **Multitenancy:** Native multitenancy via namespaces.

## Editions

- **Open‑Source Edition:** Fully featured with no limits, all plugins free. Single‑server scaling by default. Includes basic authentication (e.g., basic auth, or via Google/GitHub/Microsoft accounts if configured) and namespace-level permissions.
- **Enterprise Edition:** Adds authentication/SSO, OpenID Connect (OIDC), LDAP, secret‑manager integration, high‑availability features, and a Kafka backend for high throughput. Also offers more granular RBAC.
- **Managed SaaS:** Planned, likely more attractive for startups.

For advanced authentication in the OSS version, a reverse proxy with authentication capabilities (e.g., Keycloak) can be used.

## Integration

- **dbt:** Plugin available for executing dbt commands.
- **Dremio:** Integration via JDBC plugin or custom scripts.
- **DataHub:** Integration is possible via API calls or custom scripts.
- Additionally, Kestra works alongside dbt and other transformation tools to orchestrate end‑to‑end data pipelines.

## Role in the Data Platform

- **Scheduling:** Defines cron patterns for data refresh schedules (e.g., daily, hourly, weekly). Referenced in [[metadata-fields-definition]] for the **Update Frequency** field.
- **Monitoring:** Tracks the status of scheduled data updates, feeding into the **Last Update Status** metadata field. This supports [[data-observability-definition]] for freshness monitoring.
- **Integration:** Can be integrated into CI/CD workflows for automated pipeline deployment (see [[CI-CD-for-data-pipelines]]).

## Code Portability

Kestra YAML workflows are specific to its syntax and plugins. Migrating to code-based systems (Python) requires a complete rewrite. Translating logic from Python (Airflow/Prefect) into Kestra YAML requires mapping tasks to available plugins or custom scripts/containers.

## Advantages

### Over Airflow

- Easier setup via a single Docker Compose file.
- Simpler YAML‑based workflow definitions readable by non-developers.
- Better performance in concurrent micro‑batch processing due to its Java backend.
- Native event‑driven triggers that go beyond Airflow's schedule‑first model.
- 500+ containerized plugins eliminate pip dependency conflicts.

### General Pros

- Language-agnostic YAML definition lowers the barrier for non-Python users and facilitates cross-team collaboration.
- Simple and readable declarative flow definition, especially for linear workflows.
- Integrated UI with YAML editor, execution monitoring, and blueprint templates.
- Extensive plugin architecture for integrating diverse systems.
- Good support for event-driven triggers (Kafka, Webhook, schedule).
- Native multitenancy via namespaces.
- Designed for scalability with Kafka and Elasticsearch.

## Disadvantages and Limitations

### Performance Bottlenecks at Scale

- High execution rates (>1,000 task runs/min) cause PostgreSQL growth and query slowdowns.
- Large execution contexts (e.g., 160KB payloads) spike latency from <1s to 24‑34s.
- The OSS edition caps at ~1,500 executions/min before throughput drops.
- The Enterprise edition, with a Kafka backend, is needed for >2,000 executions/min.

### Other Limitations

- **Debugging Complexity:** Backend operator errors often result in truncated Java stack traces that obscure the root cause. Debugging issues within plugin-executed tasks may be less straightforward than in a pure Python environment.
- **Extensibility:** Requires writing custom code or operators when native connectors for specific data sources are unavailable. Deep customization of the orchestrator itself is less flexible than Airflow or Prefect.
- **Community & Security:** Smaller community and contributor pool compared to Airflow or Prefect, making troubleshooting harder. The OSS version lacks robust fine‑grained authorization and permission management.
- **Dependencies:** PostgreSQL and Elasticsearch dependencies add setup complexity compared to tools with fewer external dependencies.
- **Scaling:** The open‑source edition scales single‑server by default; enterprise features are required for high workloads.
- **Enterprise Readiness:** Limited large‑scale enterprise battle‑testing compared to more mature orchestrators.
- **Documentation:** Gaps in documentation for advanced plugins and features.
- **Skill Requirements:** Requires strong cloud/DevOps skills; not truly self‑service for non-engineers.
- **Complex Workflows:** Defining very complex workflows, advanced conditional branching, or heavy dynamic logic in YAML can become verbose and less flexible than Python.

## Positioning

Kestra is aimed at teams hitting pain points with Airflow — complex UX, Python‑only, difficult cross‑flow dependencies. Happy Airflow users need not migrate. For code‑centric ETL/ELT teams, [[Mage]] is a better fit.

## Related Concepts

- [[metadata-fields-definition]] — The **Update Frequency** field uses Kestra cron patterns.
- [[data-observability-definition]] — Kestra's execution status feeds freshness monitoring.
- [[CI-CD-for-data-pipelines]] — Kestra can be integrated into CI/CD workflows for automated pipeline deployment.
- [[event-driven-orchestration]] — Native event-driven triggers.
- [[kubernetes-etl-deployment-strategies]] — Kestra can be deployed on Kubernetes.