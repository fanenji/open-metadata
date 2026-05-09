---
type: entity
title: Apache Airflow
created: 2026-04-04
updated: 2026-05-07
tags: ["orchestrator", "python", "workflow", "industry-standard", "orchestration", "open-source", "kubernetes", "security"]
related: ["kestra", "separation-of-orchestration-and-business-logic", "task-based-orchestration", "sensors", "orchestration-decoupling-patterns", "maxime-beauchemin", "functional-data-engineering", "pure-task", "mage", "declarative-yaml-orchestration", "event-driven-orchestration", "kubernetes-etl-deployment-strategies", "dbt-dag-generator", "flask-appbuilder", "kubernetes", "reverse-proxy-authentication-pattern", "dagster", "prefect", "argo-workflows"]
sources: ["Airflow vs Dagster vs Kestra.md", "Airflow vs Kestra.md", "Functional Data Engineering — a modern paradigm for batch data processing.md", "Kestra vs Airflow (Video).md", "Orchestrazione Data Platform - Analisi Comparativa.md"]
---
# Apache Airflow

**Apache Airflow** is an open-source workflow orchestration platform originally created by [[Maxime Beauchemin]] at Airbnb. It is a mature, industry-standard, Python-based platform used to programmatically author, schedule, and monitor complex data pipelines and workflows via Directed Acyclic Graphs (DAGs). It is widely used for ETL pipelines, ML model training, and infrastructure task automation. Airflow was designed with [[functional-data-engineering]] principles in mind, providing a framework for orchestrating idempotent, pure tasks at scale. Airflow is the primary comparison baseline for [[Kestra]] and other modern orchestration tools.

## Design and Paradigm

Airflow represents workflows as DAGs of tasks. The paradigm is task-based, imperative orchestration defined using Python code and operators. In the functional data engineering paradigm, each task corresponds to a table, and each task instance corresponds to a partition. This mapping makes it easy to track lineage, re-run failed tasks safely, and parallelize backfills.

Key characteristics of Airflow's design:

- **Python-First**: Workflows are defined as Python DAGs, requiring programming knowledge and boilerplate.
- **Schedule-First**: Primarily cron-based scheduling, with event-driven "Asset Watchers" added in version 3.
- **UI**: Primarily observability-focused rather than authoring-focused; includes a tree view visualization showing task instances over time.

Features aligned with functional data engineering include:
- Support for idempotent task execution
- Clear mapping between task instances and output partitions
- Tree view visualization showing task instances over time
- Safe re-execution of any task instance

## Architecture

Airflow has a distributed architecture with several key components:

- **Scheduler**: Monitors all tasks and DAGs, triggers tasks when dependencies are satisfied.
- **Webserver**: Flask-based UI (using [[Flask-AppBuilder]]) for monitoring and managing DAGs.
- **Metadata Database**: Relational database (PostgreSQL/MySQL) storing task state, connections, variables.
- **Executor**: Defines how tasks are executed (e.g., KubernetesExecutor for K8s environments). Also configures the execution model for workers.
- **Workers**: Pods or processes that execute task logic.
- **DAG Processor**: Parses DAG files and serializes them into the metadata database.
- **Triggerer**: Optional high-availability service for deferred tasks.

## Security

Airflow has the most mature native authentication and authorization among open-source orchestrators, powered by Flask AppBuilder (FAB):

- **Native Auth**: Database-based authentication, RBAC with predefined roles (Admin, User, Viewer, Op, Public), granular DAG-level access control.
- **Fernet Key Encryption**: Sensitive data encrypted in the metadata database.
- **LDAP Integration**: Supported via FAB's LDAP backend.
- **OAuth/OIDC**: Supported via FAB configuration.
- **SAML**: Possible through OIDC bridge or custom security manager.
- **Kerberos**: Native support for Kerberized services.

## Deployment

### General Deployment

Production requires a multi-service setup coordinating a webserver, scheduler/DAG processor, metadata database, and executor. Managed services such as Amazon MWAA and Google Cloud Composer are available. Also see [[kubernetes-etl-deployment-strategies]] for typical deployment patterns.

### Kubernetes Deployment

The official Helm chart is the primary deployment method on Kubernetes. Using the KubernetesExecutor is standard practice, launching each task as an independent K8s pod. Critical considerations include DAG file synchronization, log persistence, metadata database connectivity, and resource management. For more, see [[kubernetes]].

## Ecosystem and Integrations

Airflow boasts an extensive community base and a vast ecosystem of operators and providers, including the widest range of available connectors, particularly for AWS services. A robust plugin system further extends functionality. The large operator library covers many data tools and services.

## Scalability

Airflow has proven capability to manage massive-scale deployments, including thousands of concurrent DAGs running at high frequency in large-scale production environments.

## Complexity and Best Practices

While Airflow's high flexibility is a strength, it can lead to unmanageable codebases without strict engineering discipline. A notable risk is "dependency hell" when Python business logic is executed directly within the Airflow environment. To mitigate these issues, it is recommended to adopt the [[separation-of-orchestration-and-business-logic]] (also known as [[orchestration-decoupling-patterns]]). Business logic should be encapsulated in separate Python repositories and packaged into Docker images, which Airflow then orchestrates. Following functional data engineering principles—such as keeping tasks idempotent and stateless—further reduces complexity and enhances maintainability.

## Comparison with Kestra

Airflow is often compared with [[Kestra]]. The following table highlights key differences:

| Feature | Airflow | Kestra |
|---------|---------|--------|
| Language | Python-first | Multi-language YAML |
| Triggers | Schedule + add-ons | Native event-driven |
| Deployment | Multi-service | Single Docker Compose |
| UI Self-Service | Observability-focused | Editor + Apps |
| Plugins | Python operators | 500+ containerized |

### When to Choose Airflow
- Team is deeply invested in Python and existing DAGs/operators
- Using managed offerings like MWAA or Cloud Composer
- Primarily needs scheduled batch data pipelines
- Happy with current Airflow setup — no need to migrate

## Pros and Cons

**Pros**: Mature and widely adopted, large community, extensive integrations, Python-native flexibility, scalable with KubernetesExecutor.

**Cons**: Steep learning curve, complex setup and management on-premise, scheduler can become a bottleneck, UI less intuitive than modern tools, XComs data passing limitations.

## Related Pages

- [[kestra]] — Primary alternative to Airflow
- [[dagster]] — Asset-centric alternative
- [[prefect]] — Pythonic dynamic workflow alternative
- [[mage]] — Code-centric ETL/ELT alternative
- [[argo-workflows]] — K8s-native alternative
- [[dbt-dag-generator]] — Middleware that generates Airflow DAGs from dbt projects
- [[kubernetes-etl-deployment-strategies]] — Airflow's multi-service deployment model
- [[separation-of-orchestration-and-business-logic]] and [[orchestration-decoupling-patterns]] — Best practices for managing Airflow complexity
- [[functional-data-engineering]] — The design paradigm underlying Airflow
- [[task-based-orchestration]] — Core concept of Airflow's DAGs
- [[sensors]] — Event-driven capabilities in Airflow
- [[pure-task]] — Principle of idempotent tasks
- [[maxime-beauchemin]] — Creator of Airflow
- [[declarative-yaml-orchestration]] — Contrast with Airflow's Python approach
- [[event-driven-orchestration]] — Contrast with Airflow's schedule-first model
- [[flask-appbuilder]] — Authentication/RBAC framework used by Airflow
- [[kubernetes]] — Target deployment environment
- [[reverse-proxy-authentication-pattern]] — Alternative auth approach