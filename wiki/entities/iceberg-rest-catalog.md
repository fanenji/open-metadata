---
type: entity
title: Iceberg REST Catalog
created: 2026-04-29
updated: 2026-04-29
tags: [iceberg, catalog, governance, interoperability]
related: [iceberg-v3-geo-types, data-lakehouse, foursquare-geospatial-architecture, polaris, nessie-catalog-versioning, data-catalog-critique]
sources: ["Geospatial Tables in the Open Lakehouse A New Era for Iceberg & Parquet - Summary.md"]
---
# Iceberg REST Catalog

The Iceberg REST Catalog is a modern API-first catalog specification for Apache Iceberg tables. It replaces legacy catalog implementations (like Hive Metastore) with a standardized interface for table discovery, access control, and governance.

## Role in the Open Lakehouse

The panel identified catalog standardization as the **critical remaining missing piece** for a complete open geospatial lakehouse. With a standardized catalog:

- **Compute engines discover tables** without engine-specific configuration
- **Access control and governance** can be enforced at the catalog level (via implementations like Polaris, Unity Catalog)
- **Observability** — which rows, columns, and files were accessed, by whom, and at what frequency — can be captured centrally
- **Data providers gain visibility**: instead of losing control after data is copied, they can track usage patterns and manage access via catalog policies

## Relationship to Other Catalog Implementations

The Iceberg REST Catalog is a specification, not an implementation. Implementations include:
- **Polaris** (open-source catalog from Snowflake)
- **Unity Catalog** (Databricks)
- **Nessie** (Git-for-data catalog-level versioning)
- **Custom implementations** (any system implementing the REST API)

## Importance for Geospatial Workloads

For geospatial data providers (e.g., governments, satellite companies), the catalog layer enables:
- Publishing data once on object storage in Iceberg format
- Controlling who accesses which spatial regions or layers
- Tracking usage patterns for billing or impact analysis
- Revoking access without data migration
