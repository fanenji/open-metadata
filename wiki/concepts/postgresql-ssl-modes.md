---
type: concept
title: PostgreSQL SSL Modes
created: 2026-05-14
updated: 2026-05-14
tags: [postgresql, ssl, security, configuration]
related: [postgresql-connector, postgresql-iam-authentication]
sources: ["PostgreSQL Connector  OpenMetadata Database Integration.md"]
---
# PostgreSQL SSL Modes

To establish secure connections between OpenMetadata and a PostgreSQL database, the [[postgresql-connector]] supports SSL configuration using standard PostgreSQL SSL modes. These are configured under the **Advanced Config** section of the connection settings.

## Supported Modes

PostgreSQL SSL modes include `prefer`, `verify-ca`, `allow`, and others, each offering varying levels of security. After selecting the SSL mode, provide the **CA certificate** used for SSL validation (`caCertificate`). PostgreSQL requires only the CA certificate for SSL validation.

## IAM Authentication and SSL

For [[postgresql-iam-authentication|IAM authentication]] with AWS RDS, it is recommended to choose the `allow` mode or another SSL mode that fits your specific requirements.