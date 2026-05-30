---
type: source
title: Run the Superset Connector Externally - OpenMetadata Documentation
created: 2026-05-14
updated: 2026-05-14
tags: [superset, connector, yaml, cli, ingestion, external]
related: [superset-connector, superset-external-execution, metadata-cli, personal-access-token, filter-patterns, soft-deletion, postgresql-ssl-modes, mysql-8x, postgresql-connector, ingestion-framework]
sources: ["run-the-superset-connector-externally---openmetada-20260514-2.md"]
---

# Run the Superset Connector Externally - OpenMetadata Documentation

This source is the official OpenMetadata v1.12.x documentation page for running the Superset connector externally via YAML configuration and the `metadata ingest` CLI command. It covers three connection modes (Superset API, MySQL database, PostgreSQL database), comprehensive source configuration options, SSL configuration patterns, and the complete YAML workflow configuration.

## Key Content

- **Three Connection Modes**: Superset API (default, basic/ldap auth only), MySQL database (for SSO-enabled Superset), PostgreSQL database (for SSO-enabled Superset)
- **Source Config Options**: Filter patterns for dashboards, charts, data models, and projects; toggles for owners, tags, data models, soft-deletion, draft dashboards, override metadata, and override lineage
- **SSL Configuration**: Three distinct patterns for Superset API (caCertificate only), MySQL (caCertificate + optional ssl_cert + ssl_key), and PostgreSQL (sslMode + caCertificate)
- **Store Service Connection**: Toggle controlling whether sensitive connection info is stored in the database or used only at runtime
- **CLI Execution**: Complete YAML example and `metadata ingest -c <path-to-yaml>` command

## Relevance

This source extends the existing [[superset-connector]] page with external execution details, YAML configuration, and SSL patterns. It also provides concrete examples for [[filter-patterns]], [[soft-deletion]], [[postgresql-ssl-modes]], and [[metadata-cli]] usage.
