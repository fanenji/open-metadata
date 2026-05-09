---
type: concept
title: SDI-DP Integration Patterns
created: 2026-03-18
updated: 2026-03-18
tags: [sdi, data-platform, integration, architecture, patterns]
related: [sdi-spatial-data-infrastructure, data-ingestion-architectural-patterns, elt-pattern, etl-pattern, data-virtualization-pattern, stream-processing-ingestion, data-lakehouse, cloud-native-geospatial-workflow]
sources: ["Integrazione SDI e Data Platform.md"]
---
# SDI-DP Integration Patterns

This concept describes the architectural patterns for integrating Spatial Data Infrastructures (SDI) with modern Data Platforms (DP). The choice of pattern depends on data characteristics, volume, velocity, latency requirements, and existing infrastructure.

## Integration Patterns

### 1. API-Based Integration
The DP queries SDI services or spatial databases on-demand via APIs (OGC API, REST, WFS, WMS).
- **Pros**: Access to up-to-date/real-time data; lightweight integration; leverages existing services
- **Cons**: Potential bottlenecks for large volumes; dependency on source service availability/performance; complexity managing many different APIs
- **Typical Use Case**: Access to dynamic data from external services (weather, traffic); integration of specific functions (geocoding)

### 2. ETL (Extract, Transform, Load)
Spatial data is extracted from SDI sources, transformed in a dedicated ETL engine, and loaded into the DP storage.
- **Pros**: Mature tools (especially for spatial ETL like FME, GeoKettle); centralized transformation control; guaranteed quality before loading
- **Cons**: Rigidity (transformations defined a priori); potential bottlenecks in ETL engine; often batch, not real-time; tool costs
- **Typical Use Case**: Batch loading of fundamental, well-structured spatial layers into a data warehouse; migration from legacy systems

### 3. ELT (Extract, Load, Transform)
Raw spatial data is extracted from SDI sources and loaded directly into the DP's scalable storage (data lake/lakehouse). Transformations are executed later within the DP using its compute power.
- **Pros**: Flexibility (transformations defined at query time); leverages cloud DP scalability; suitable for raw/diverse data; potentially faster loading
- **Cons**: Requires spatial processing capabilities in the DP; risk of "data swamp" if not governed; raw data quality may impact analyses
- **Typical Use Case**: Loading raw or semi-structured spatial data into data lakehouse for exploratory and flexible analysis; cloud-native architectures

### 4. Data Virtualization
Creates a unified logical view without physically moving or copying data.
- **Pros**: Real-time access without duplication; reduced data latency; agility in data exposure
- **Cons**: Limited performance for complex/voluminous queries on heterogeneous sources; dependency on underlying source performance; complex distributed query management (especially spatial)
- **Typical Use Case**: Providing a quick integrated view for simple queries or initial exploration; avoiding copies of sensitive data

### 5. Streaming Integration
Continuous ingestion, processing, and loading of real-time spatial data streams (IoT sensors, vehicle fleets, social feeds) into the DP.
- **Pros**: Handling high-velocity data (IoT, sensors); real-time analysis and reactions; enables dynamic use cases
- **Cons**: Infrastructure complexity (Kafka, stream processing engines); state and consistency management; potential end-to-end latency issues
- **Typical Use Case**: Integration of geolocated IoT sensor data; real-time traffic monitoring; continuous operational dashboard updates

## Hybrid Approach

Most organizations adopt a hybrid approach combining multiple patterns:
- **ELT** for massive periodic loading of fundamental geospatial layers
- **API** for real-time access to dynamic data from external SDI services
- **Streaming** for high-frequency data from geolocated IoT sensors

## Platform Choices

- **Data Lake**: Flexible ingestion of raw spatial formats; risk of data swamp
- **Data Warehouse**: Structured, high-quality spatial data; optimized for BI queries
- **Data Lakehouse**: Combines flexibility of lake with structure/performance of warehouse; ideal for SDI-DP convergence
- **Data Mesh**: Decentralized approach where a "geospatial domain" publishes spatial data products

## Related Concepts

- [[sdi-spatial-data-infrastructure]] — The system being integrated
- [[data-ingestion-architectural-patterns]] — General ingestion patterns extended to spatial data
- [[elt-pattern]] — Preferred modern pattern for spatial data
- [[etl-pattern]] — Traditional pattern still relevant for specific use cases
- [[data-virtualization-pattern]] — Virtualized query layer over multiple sources
- [[stream-processing-ingestion]] — Real-time spatial data integration
- [[data-lakehouse]] — Identified as ideal convergence architecture
- [[cloud-native-geospatial-workflow]] — Cloud-native approaches to geospatial data