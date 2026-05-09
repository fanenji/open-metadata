---
type: source
title: "Sintesi Architettura (Claude)"
created: 2026-03-08
updated: 2026-03-08
tags: [architecture, data-platform, modern-data-stack, elt, data-lakehouse, governance]
related: [minio, apache-iceberg, project-nessie, dremio, dbt, kestra, openmetadata, apache-superset, jupyter, opensearch, gitlab-ci-cd-data-platform, ckan-portal, wso2-api-gateway, stack-cartografico, bronze-silver-gold-architecture, dremio-reflections, dremio-vds-pds, dremio-row-column-security, dcat-ap-agid-compliance, pdnd-interoperability, elt-pattern, data-lakehouse, data-virtualization-pattern, nessie-catalog-versioning, iceberg-table-versioning, dbt-dremio-adapter]
sources: ["Sintesi Architettura (Claude).md"]
---
# Sintesi Architettura (Claude)

Documento di riferimento LD23GPS-PA7665-002 v1 per la Data Platform Regionale di Liguria Digitale / Regione Liguria. Presenta l'architettura sintetica della piattaforma con componenti adottati, schema per livelli logici, pipeline ELT, e scelte tecnologiche rispetto al documento originale.

## Key Points

- **Architecture Pattern**: Classic Modern Data Stack with object storage (MinIO), table format (Iceberg), catalog (Nessie), virtualization (Dremio), transformations (dbt), orchestration (Kestra), governance (OpenMetadata), and multiple consumption interfaces.
- **ELT Pipeline**: Data flows from sources through Kestra orchestration into the Data Lake (MinIO + Iceberg), then transformed via dbt + Dremio through Bronze → Silver → Gold layers, served to consumers (Superset, Power BI, Jupyter, CKAN, API).
- **Dremio as Central Hub**: Dremio serves as the unified SQL access layer with VDS/PDS, Reflections cache, Semantic Layer, and Row/Column Security.
- **Key Decisions**: OpenMetadata over DataHub, Kestra over Airflow/Mage/NiFi, Jupyter over Zeppelin. No Kafka (direct ingestion via Kestra), no Spark (processing delegated to Dremio Reflections and dbt).
- **Infrastructure**: Single GitLab instance for all environments (dev/test/prod), MinIO cluster (4 nodes, ~32 TB usable), Dremio cluster (1 coordinator + 3 executors), Nessie (1 node).
- **Compliance**: DCAT-AP, AGID, PDND standards for open data and interoperability.

## Architecture Layers

1. **Sources Layer**: Oracle DB, SQL Server, Postgres, MySQL, API, FTP, File, Elastic, MongoDB
2. **Core Layer**: MinIO, Iceberg, Nessie, Dremio, dbt, Kestra
3. **Consumption Layer**: Apache Superset, Power BI, Jupyter, CKAN Portal, WSO2 API Gateway, Stack Cartografico
4. **Cross-cutting Layer**: OpenMetadata, OpenSearch, GitLab, LDAP/Identity

## Component Specifications

- **MinIO**: 4 nodes, 16 CPU / 32 GB RAM / 4×1 TB flash per node, erasure coding
- **Dremio**: 1 coordinator (16 CPU / 32 GB) + 3 executors (16 CPU / 128 GB each)
- **Nessie**: 1 node, 2 CPU / 8 GB RAM / 50 GB storage
- **OpenSearch**: Metricbeat agents for log/metric collection, ML anomaly detection
- **Superset**: Connects to Dremio via sqlalchemy_dremio (ODBC port 31010 / Arrow Flight port 32010)

## Decision Rationale

- **OpenMetadata > DataHub**: Simpler architecture, pull-based ingestion, native dbt integration, SSO/SAML support
- **Kestra > Airflow/Mage/NiFi**: Modern UI, declarative YAML paradigm, ELT-native design
- **Jupyter > Zeppelin**: Complete Python stack with geospatial support (GeoPandas, Leafmap)
- **No Kafka**: Direct ingestion via Kestra instead of message broker
- **No Spark**: Processing delegated to Dremio (Reflections) and dbt