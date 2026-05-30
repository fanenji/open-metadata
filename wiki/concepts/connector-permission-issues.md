---
type: concept
title: "Connector Permission Issues"
created: 2026-05-30
updated: 2026-05-30
tags: []
related: []
---

type: concept
title: Connector Permission Issues
created: 2026-05-14
updated: 2026-05-14
tags: [troubleshooting, permissions, connectors, ingestion]
related: [superset-connector, oracle-connector, postgresql-connector, service-connection, debug-logging-ingestion, hybrid-rbac-abac-model]
sources: ["superset-troubleshooting-guide-openmetadata-suppor-20260514.md"]
---

# Connector Permission Issues

Permission issues are the most common root cause of ingestion failures in OpenMetadata. They arise when the credentials or access configurations provided in the [[service-connection]] do not have sufficient privileges to read metadata from the source system.

## Common Patterns

- **Missing Read Access**: The connector user lacks `SELECT` or equivalent read permissions on the source database or API.
- **Insufficient API Scope**: For dashboard connectors like [[superset-connector]], the API token may not have the required scopes.
- **Network Restrictions**: Firewall rules or IP allowlists blocking the ingestion container from reaching the source.
- **Authentication Failures**: Expired passwords, revoked tokens, or misconfigured SSL/TLS settings.

## Diagnosis

1. Enable [[debug-logging-ingestion|debug logging]] on the ingestion pipeline to capture the exact error message.
2. Review the ingestion container logs for HTTP status codes (e.g., 401 Unauthorized, 403 Forbidden).
3. Verify the connector-specific prerequisites documented for each source.

## Resolution

- Refer to the connector-specific documentation for required permissions:
  - [[superset-connector]] — API and database extraction permissions.
  - [[oracle-connector]] — Schema-level SELECT limitation and workarounds.
  - [[postgresql-connector]] — SSL modes, IAM authentication, and `pg_stat_statements` requirements.
- Regenerate or update credentials in the service connection.
- Test connectivity from the ingestion container using CLI tools or curl.

## Related

- [[service-connection]] — The configured link between OpenMetadata and the source.
- [[debug-logging-ingestion]] — Procedure to enable verbose logging for diagnosis.
- [[hybrid-rbac-abac-model]] — OpenMetadata's internal authorization framework.