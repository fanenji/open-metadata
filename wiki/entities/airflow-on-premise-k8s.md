---
type: entity
title: Apache Airflow On-Premise Kubernetes
created: 2026-05-07
updated: 2026-05-07
tags: [airflow, kubernetes, orchestration, deployment, security]
related: [kubernetes, orchestration-tool-comparison, oss-vs-cloud-security-gap, reverse-proxy-auth-pattern]
sources: ["Orchestratori Data Platform_ Analisi Comparativa 2.md"]
---
# Apache Airflow On-Premise Kubernetes

Apache Airflow is a mature platform for programmatically creating, scheduling, and monitoring complex workflows as Directed Acyclic Graphs (DAGs) in Python. It is the most feature-rich open-source orchestrator for on-premise Kubernetes deployment, particularly regarding native authentication and authorization.

## Architecture on K8s

- **Scheduler**: Monitors tasks and DAGs, triggers tasks when dependencies are satisfied
- **Webserver**: Flask-based UI for monitoring, managing, and configuring DAGs
- **Metadata Database**: PostgreSQL or MySQL for task state, connections, variables, execution history
- **Executor**: `KubernetesExecutor` is the standard for K8s, launching each task as a separate pod
- **Workers**: K8s pods executing task logic (with `KubernetesExecutor`)
- **DAG Processor**: Parses DAG files and serializes them to the metadata database
- **Triggerer** (optional): High-availability service for deferred tasks

## Security (Flask AppBuilder)

Airflow's security is managed by **Flask AppBuilder (FAB)**, providing:
- **Authentication**: Database-based (username/password), LDAP, OAuth/OIDC, SAML (via custom security manager or bridge)
- **Authorization (RBAC)**: Predefined roles (Admin, User, Viewer, Op, Public) and custom roles with granular permissions, including DAG-level access control
- **Secret Encryption**: Fernet key for encrypting sensitive information in the metadata database

## Deployment Considerations

- **DAG synchronization**: Use `git-sync`, Docker image inclusion, or shared persistent volumes
- **Log persistence**: Store logs on distributed file systems or external logging services
- **Metadata database**: Must be highly available and accessible from all components
- **Resource management**: Define appropriate requests and limits for worker pods
- **Fernet key management**: Must be securely managed (e.g., via Kubernetes Secrets)
- **NetworkPolicies**: Limit network access to Airflow components

## Pros

- Most mature and widely adopted orchestrator
- Largest community, extensive documentation and integrations
- Python-native DAG definition for full control and complex logic
- Good horizontal scalability with `KubernetesExecutor`

## Cons

- Steep learning curve
- Complex setup and maintenance on K8s
- Scheduler can become a bottleneck at very large scale
- UI considered less intuitive than modern alternatives
- XComs (data passing between tasks) have size and usability limitations