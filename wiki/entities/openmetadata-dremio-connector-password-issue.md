---
type: entity
title: OpenMetadata Dremio Connector Password Issue
created: 2026-02-23
updated: 2026-02-23
tags: [security, openmetadata, dremio, connector, vulnerability]
related: [gestione-secrets, secrets-management-strategy, custom-connector-openmetadata, openmetadata-dremio-connector, dremio]
sources: ["Gestione Secrets.md"]
---
# OpenMetadata Dremio Connector Password Issue

A known security vulnerability in the custom [[openmetadata-dremio-connector]]: the Dremio password is stored in plaintext, violating the Data Platform's [[secrets-management-strategy]] which mandates that all secrets be stored exclusively as GitLab CI/CD variables.

## Problem Description

The custom OpenMetadata connector for Dremio, hosted by [[tiki-institut]], stores the Dremio password in plaintext — presumably in configuration files or within the connector code itself. This bypasses the platform's canonical secrets management approach and represents a significant security gap.

## Impact

- **Security risk**: Plaintext credentials can be exposed through code repositories, logs, or configuration dumps.
- **Policy violation**: Directly contradicts the [[secrets-management-strategy]] mandate.
- **Production blocker**: May prevent production deployment until resolved.

## Resolution Options

1. **Refactor the connector** to read the Dremio password from a GitLab CI/CD variable at runtime.
2. **Implement OAuth-based authentication** between OpenMetadata and Dremio, eliminating the need for a stored password.
3. **Use a secrets vault** (e.g., HashiCorp Vault) as an intermediary, though this adds complexity.
4. **Accept the risk** with a documented workaround and mitigation plan (e.g., restricted access, encryption at rest).

## Related Pages

- [[gestione-secrets]] — The source note flagging this issue
- [[secrets-management-strategy]] — The canonical secrets management approach
- [[custom-connector-openmetadata]] — Pattern for building custom OpenMetadata connectors
- [[openmetadata-dremio-connector]] — The specific connector with the password issue
- [[dremio]] — The data lakehouse engine being connected to