---
type: concept
title: External Dependencies Configuration
created: 2026-05-14
updated: 2026-05-14
tags: [openmetadata, kubernetes, configuration, database, elasticsearch, opensearch]
related: [on-premises-kubernetes-deployment, openmetadata, kubernetes]
sources: ["OMD - Kubernetes On Premises.md"]
---

# External Dependencies Configuration

The practice of configuring OpenMetadata to use separately managed database and search engine instances instead of the bundled dependencies included in the Helm Chart. This is a critical requirement for production on-premises Kubernetes deployments.

## Supported External Services

| Component | Supported Engines | Minimum Version |
|-----------|-------------------|-----------------|
| Database | MySQL | 8 |
| Database | PostgreSQL | 12 |
| Search Engine | ElasticSearch | 9.0.0 |
| Search Engine | OpenSearch | 3.0.0 |

## Configuration

External dependencies are configured through the `openmetadata-values.prod.yaml` file. Key configuration sections include:

### Database Connection

```yaml
openmetadata:
  config:
    database:
      host: <DATABASE_SQL_ENDPOINT>
      port: 3306
      driverClass: com.mysql.cj.jdbc.Driver
      dbScheme: mysql
      dbUseSSL: true
      databaseName: <DATABASE_SQL_DATABASE_NAME>
      auth:
        username: <DATABASE_SQL_DATABASE_USERNAME>
        password:
          secretRef: mysql-secrets
          secretKey: openmetadata-mysql-password
```

### Search Engine Connection

```yaml
openmetadata:
  config:
    elasticsearch:
      host: <SEARCH_ENGINE_ENDPOINT_WITHOUT_HTTPS>
      searchType: elasticsearch  # or 'opensearch'
      port: 443
      scheme: https
      auth:
        enabled: true
        username: <SEARCH_ENGINE_CLOUD_USERNAME>
        password:
          secretRef: elasticsearch-secrets
          secretKey: openmetadata-elasticsearch-password
```

## Kubernetes Secrets

Credentials must be created as Kubernetes Secrets before deploying the Helm Chart. The secrets are referenced by `secretRef` and `secretKey` in the values file.

## Disabling Bundled Dependencies

When using external services, the bundled MySQL and ElasticSearch dependencies in the OpenMetadata Helm Chart must be explicitly disabled to prevent unnecessary resource consumption and potential conflicts.