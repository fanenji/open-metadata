---
type: entity
title: Temporal Security
created: 2026-05-07
updated: 2026-05-07
tags: [temporal, security, authentication, authorization, durable-workflows, microservices]
related: [oss-vs-cloud-security-gap, orchestration-tool-comparison, kubernetes]
sources: ["Orchestratori Data Platform_ Analisi Comparativa 2.md"]
---
# Temporal Security

Temporal is an open-source platform for durable, fault-tolerant workflow orchestration based on the "workflow-as-code" paradigm. It is not limited to data pipelines but excels at managing long-running business processes. Its security model uses a custom plugin approach.

## Architecture on K8s

- **Temporal Server**: Core service managing workflow executions, history, and visibility
- **Temporal Worker**: Application code that executes workflow and activity tasks
- **Temporal CLI**: Command-line interface for interacting with the server
- **Temporal Web**: Web UI for monitoring workflows

## Security Model

### Authentication
- **Custom Plugin Model**: Authentication is implemented via a custom plugin interface
- **JWT**: JSON Web Token-based authentication supported via plugins
- **mTLS**: Mutual TLS for secure communication between services
- No built-in OIDC, LDAP, or SAML support

### Authorization
- **Custom Authorization**: Must be implemented via the plugin interface
- No built-in RBAC

### LDAP/SAML/OIDC
- Not natively supported
- Requires custom plugin development or integration via reverse proxy

## Deployment Considerations

- Significant development effort required for custom security plugins
- Kubernetes Operator and Helm chart available for deployment
- mTLS configuration requires certificate management infrastructure

## Pros

- Excellent for long-running, fault-tolerant business processes
- Multi-language SDKs (Go, Java, Python, TypeScript)
- Durable execution guarantees
- MIT license

## Cons

- Not designed primarily for batch data pipelines
- Custom security plugin model requires development effort
- No built-in RBAC or SSO
- Different paradigm from traditional data orchestrators