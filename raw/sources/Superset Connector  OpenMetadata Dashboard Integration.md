---
title: "Superset Connector | OpenMetadata Dashboard Integration"
source: "https://docs.open-metadata.org/v1.12.x/connectors/dashboard/superset"
author:
published:
created: 2026-05-14
description: "Learn how to connect Apache Superset dashboards to OpenMetadata with our comprehensive connector guide. Setup instructions, configuration, and metadata integration."
tags:
  - "clippings"
topic:
type: "note"
---
## Superset

PROD

In this section, we provide guides and references to use the Superset connector. Configure and schedule Superset metadata and profiler workflows from the OpenMetadata UI:

## Requirements

The ingestion also works with Superset 2.0.0 🎉 **API Connection**: To extract metadata from Superset via API, user must have at least `can read on Chart` & `can read on Dashboard` permissions. **Database Connection**: To extract metadata from Superset via MySQL or Postgres database, database user must have at least `SELECT` privilege on `dashboards` & `slices` tables within superset schema.

## Metadata Ingestion

To ingest metadata from your sources, you need to create a service connection. The service connects your source system with OpenMetadata. Once you create a service, you can use it to configure your ingestion workflows.  
  
To create a service connection and ingest your metadata, follow the steps below:

## Connection Details

## Securing Superset Connection with SSL in OpenMetadata

1. To establish secure connections between OpenMetadata and Superset, navigate to the `Advanced Config` section. We need to update the `Certificate Path` and ensure that the certificates are accessible from the Airflow Server.
![Supertset API SSL Configuration](https://mintcdn.com/openmetadata/zq8wMYJ70mT1Pi3x/public/images/connectors/ssl_superset.png?w=2500&fit=max&auto=format&n=zq8wMYJ70mT1Pi3x&q=85&s=93c9e32cfacedf9c296ea7953de7a47c)

Supertset API SSL Configuration

2. To establish secure connections between OpenMetadata and Superset’s MySQL database, you need to configure SSL certificates appropriately. If you only require SSL validation, specify the `caCertificate` to use the CA certificate for validating the server’s certificate. For mutual authentication, where both client and server need to authenticate each other, you must provide all three parameters: `ssl_key` for the client’s private key, `ssl_cert` for the client’s SSL certificate, and `ssl_ca` for the CA certificate to validate the server’s certificate.
![MySQL SSL Configuration](https://mintcdn.com/openmetadata/zq8wMYJ70mT1Pi3x/public/images/connectors/ssl_superset_mysql.png?w=2500&fit=max&auto=format&n=zq8wMYJ70mT1Pi3x&q=85&s=a49aafd3f442145b0e7a42ebdcbff6cf)

MySQL SSL Configuration

3. To establish secure connections between OpenMetadata and Superset’s PostgreSQL database, you can configure SSL using different SSL modes provided by PostgreSQL, each offering varying levels of security.Under `PostgresConnection Advanced Config`, specify the SSL mode appropriate for your connection, such as `prefer`, `verify-ca`, `allow`, and others. After selecting the SSL mode, provide the CA certificate used for SSL validation (`caCertificate`). Note that PostgreSQL requires only the CA certificate for SSL validation.
![Postgres SSL Configuration](https://mintcdn.com/openmetadata/zq8wMYJ70mT1Pi3x/public/images/connectors/ssl_superset_postgres.png?w=2500&fit=max&auto=format&n=zq8wMYJ70mT1Pi3x&q=85&s=4c9408ae0875819e98b851cdbbfcb20f)

Postgres SSL Configuration

## Lineage

To establish lineage from your **database tables to dashboards**, you must add the corresponding **database service name**.

![lineage in dashboard](https://mintcdn.com/openmetadata/9SXjaLbGROaofLQU/public/images/connectors/dashboard-lineage.png?w=2500&fit=max&auto=format&n=9SXjaLbGROaofLQU&q=85&s=b2d2afcf3b0d32c40971e7f6b3a95297)

lineage in dashboard