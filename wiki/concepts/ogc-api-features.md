---
type: concept
title: OGC API-Features
created: 2026-04-29
updated: 2026-05-07
tags: [geospatial, web-api, standard, interoperability, rest, ogc, api, metadata-driven-api-configuration, api-configurator-system, geoserver, legacy-geospatial-etl-pipeline]
related: [flatgeobuf, geoparquet, apache-iceberg, geospatial-format-comparison-framework, cloud-native-geospatial-workflow, metadata-driven-api-configuration, api-configurator-system, geoserver, legacy-geospatial-etl-pipeline]
sources: ["FlatGeoBuf vs. GeoParquet vs. Apache Iceberg vs. OGC API-Features A Cloud Geospatial Comparison.md", "SISTEMA API - CONFIGURATORE API.md"]
---

# OGC API - Features

**OGC API - Features** is an Open Geospatial Consortium (OGC) standard (the modern evolution of WFS, the OGC Web Feature Service) for RESTful feature access. It provides a standard HTTP interface for querying and retrieving geospatial features, typically returning GeoJSON representations, though other formats can be offered via content negotiation. The API follows the OpenAPI 3.0 specification and defines a consistent set of endpoints.

## Standard Endpoints

The standard defines the following endpoints:

- **Landing page**: The entry point with title, description, links to SwaggerUI, dataset list, and contact info.
- **SwaggerUI**: Interactive API documentation available in HTML and JSON formats.
- **Conformance** (`/conformance`): Lists the supported OGC standards.
- **Datasets** (`/datasets`): Lists available datasets.
- **Dataset** (`/datasets/{datasetId}`): Description and metadata for a specific dataset.
- **Items** (`/datasets/{datasetId}/items`): List of features in a dataset, with query parameters such as bounding box, attribute filters, and pagination.
- **Item** (`/datasets/{datasetId}/items/{itemId}`): Single feature data.

This endpoint structure enables RESTful access to geospatial features.

## Key Characteristics

- **RESTful access**: Data is exposed as collections of features via HTTP endpoints with parameters for bounding box, attribute filters, pagination, etc.
- **Format-agnostic**: While GeoJSON is the default, servers can offer GML, CSV, FlatGeoBuf, or other formats via HTTP content negotiation.
- **On-demand queries**: Clients request only the data they need, making it ideal for interactive applications.
- **Modular parts**: Supports create, update, and delete operations via transactional extensions (part of the standard).
- **Standardized**: OGC/ISO standard ensuring broad interoperability across clients and servers.

## Scalability Considerations

- Scalability depends entirely on the backend implementation (spatial database, data lake, cloud function, etc.).
- Can be scaled horizontally with multiple instances behind a load balancer.
- Not optimized for bulk analytical scans — pulling entire datasets through the API is inefficient.
- Best suited for granular queries where users need slices of data at a time.

## Ecosystem Support

- Supported by web mapping libraries (Leaflet, OpenLayers via OGC API clients).
- Supported by desktop GIS (recent QGIS, ArcGIS).
- Designed around OpenAPI/JSON schemas for easy developer understanding.
- Increasingly adopted for modern web GIS and data sharing portals.

## Use Cases

- Interactive web mapping applications.
- System-to-system data integration.
- Federated data sharing networks.
- Real-time access to frequently updated data (e.g., live traffic, cadastral services).
- Complementing file formats by providing a query interface in front of cloud storage.
- **Data Platform foundation**: OGC API - Features is the foundation for the [[api-configurator-system]], which generates read-only APIs from metadata (database tables or JSON configurations). This enables rapid provisioning of OGC-compliant endpoints for geospatial data sharing.

## Relationship to Other Formats

OGC API - Features is complementary to file and table formats:
- A server can be backed by an [[apache-iceberg]] table or [[geoparquet]] files.
- A server can offer [[flatgeobuf]] as an output format for efficient transfer.
- Bulk downloads can be offered as GeoParquet or FGB files alongside the API.

## Related Standards

- **OpenAPI 3.0**: The API is described and documented using the OpenAPI specification.
- **GeoJSON**: The default representation format for features.
- **OGC Web Feature Service (WFS)**: The predecessor standard; OGC API - Features is its modern RESTful evolution.

## Related

- [[flatgeobuf]]
- [[geoparquet]]
- [[apache-iceberg]]
- [[geospatial-format-comparison-framework]]
- [[cloud-native-geospatial-workflow]]
- [[metadata-driven-api-configuration]]
- [[api-configurator-system]]
- [[geoserver]]
- [[legacy-geospatial-etl-pipeline]]