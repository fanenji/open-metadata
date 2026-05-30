---
type: concept
title: Hybrid Ingestion Runner Secret Management
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, ingestion, security, secrets, hybrid]
related: [postgresql-connector, service-connection, cli-ingestion-with-basic-auth, bot-authentication]
sources: ["postgresql-connector-openmetadata-database-integra-20260514.md"]
---

# Hybrid Ingestion Runner Secret Management

When using a Hybrid Ingestion Runner in OpenMetadata, sensitive credential fields—such as passwords, API keys, or private keys—must reference secrets using a specific format. This ensures that credentials are not stored in plaintext in pipeline configurations.

## Secret Reference Format

Sensitive fields in the connection configuration must use the following format:

```
password: secret:/my/database/password
```

This format applies only to fields marked as secrets in the connection form. These fields typically mask input and show a visibility toggle icon in the UI.

## Scope

The secret reference format is required for:

- Passwords
- API keys
- Private keys
- Any other field marked as a secret in the connection form

## Related Concepts

- [[service-connection]] — The configured link between OpenMetadata and an external data source.
- [[cli-ingestion-with-basic-auth]] — Alternative ingestion method using JWT token authentication.
- [[bot-authentication]] — Mechanism by which automated applications authenticate using JWT tokens.
- [[postgresql-connector]] — PostgreSQL connector documentation where this format is documented.

## Notes

- This is a general connector feature, not specific to PostgreSQL.
- For a complete guide on managing secrets in hybrid setups, refer to the official Hybrid Ingestion Runner Secret Management Guide.