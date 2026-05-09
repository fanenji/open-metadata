---
type: entity
title: Airflow
created: 2026-04-05
updated: 2026-05-07
tags: [airflow, orchestration, pipeline, openmetadata, workflow, python, kubernetes]
related: [openmetadata, openmetadata-ingestion-framework, openmetadata-lineage, kestra, kubernetes, prefect, orchestration-system-comparison, orchestration-code-portability, orchestration-authn-authz, dbt, dremio, datahub]
sources: ["OpenMetadata - The Complete Guide Every Data Engineer Needs to Read.md", "Orchestratori Data Platform_ Analisi Comparativa 1.md"]
---
# Apache Airflow

Apache Airflow is a mature, open-source workflow orchestration platform for scheduling and monitoring data pipelines. It uses Directed Acyclic Graphs (DAGs) defined in Python to program, schedule, and monitor workflows, and is considered a de facto standard for complex workflow orchestration. In the context of [[OpenMetadata]], Airflow serves two key roles:

1. **Ingestion Framework Host** — The OpenMetadata Ingestion Framework can run as Airflow DAGs, enabling scheduled metadata extraction from connected sources.
2. **Pipeline Metadata Source** — OpenMetadata integrates with Airflow to capture pipeline metadata automatically, including lineage information.

## Architecture

Airflow's architecture consists of several key components:
- **Scheduler**: Triggers workflows and submits tasks to executors.
- **Executor**: Runs tasks. The `KubernetesExecutor` runs each task as a separate Kubernetes pod.
- **Webserver**: Provides the UI for monitoring and managing DAGs and tasks.
- **Worker**: Executes tasks (when using the CeleryExecutor or similar).
- **DAG (Directed Acyclic Graph)**: The core workflow definition structure, written in Python.

## Kubernetes Deployment

Airflow offers excellent Kubernetes support:
- **KubernetesExecutor**: Native executor that runs each task as a separate Kubernetes pod, enabling job execution external to the control plane.
- **KubernetesPodOperator**: Provides fine-grained control over pod definition for specific tasks.
- Official and community-maintained Helm charts simplify deployment on Kubernetes, OpenShift, and Rancher.

## Integration

Airflow integrates with numerous tools and platforms.

### dbt
Excellent integration via specific providers (e.g., `apache-airflow-providers-dbt-cloud`) or custom operators for dbt Core.

### Dremio
Good integration via Python client, JDBC/ODBC operators.

### DataHub
Strong native integration with official providers for lineage and metadata tracking.

### OpenMetadata
As described above, Airflow acts as both the host for the Ingestion Framework and a source of pipeline metadata. The following example shows how to use the OpenMetadata Airflow provider:

```python
from airflow_provider_openmetadata.hooks.openmetadata import OpenMetadataHook

hook = OpenMetadataHook(openmetadata_conn_id="openmetadata_default")
metadata = hook.get_conn()
# Lineage is captured automatically when DAGs run
```

## Authentication and Authorization

Airflow 2.x includes a built-in Role-Based Access Control (RBAC) system for the UI. It supports integration with OAuth, LDAP, and OpenID Connect providers. The system is extensible and customizable.

## Code Portability

Migrating Airflow DAGs to other orchestration systems requires significant rewriting, as the logic is tightly coupled to Airflow's operators and abstractions. Similarly, porting workflows from other systems to Airflow requires translation into its Python DAG structure.

## Pros and Cons

**Pros:**
- Most mature system with vast community, extensive documentation, and rich ecosystem of providers.
- Maximum flexibility with Python-defined DAGs.
- Good horizontal scalability with Kubernetes integration.
- Feature-rich UI for monitoring, log viewing, and task re-execution.

**Cons:**
- Steeper learning curve for DAG definition and architecture understanding.
- Complex Python dependency management across DAGs and tasks (mitigated by `KubernetesPodOperator`).
- Dynamic DAG generation can be cumbersome.
- Scheduler has historically been a performance and resilience bottleneck in very large installations.