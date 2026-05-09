---
type: concept
title: Geospatial Streaming with Kafka and GeoMesa
created: 2026-04-29
updated: 2026-04-29
tags: [streaming, kafka, geomesa, geospatial, near-real-time]
related: [sdi-dp-integration-strategies, sdi-regione-liguria, cloud-native-geospatial-workflow]
sources: ["Integrazione SDI DP Analisi.md"]
---
# Geospatial Streaming with Kafka and GeoMesa

This concept page documents the alternative approach of using Kafka and GeoMesa for near-real-time geospatial data ingestion from Oracle to the Data Platform.

## Architecture

1. **Change Data Capture**: Every modification in Oracle is published to a Kafka topic
2. **Stream Processing**: GeoMesa consumes the Kafka topic and processes geospatial data
3. **Storage**: GeoMesa populates a distributed catalog (HBase/Cassandra) and produces GeoParquet files in S3
4. **Query**: OGC-standard queries via GeoServer on GeoMesa

## Advantages

- Near-real-time updates with low latency
- Horizontal scalability for large data volumes
- OGC-standard query capabilities via GeoServer integration
- Decouples source system changes from target updates

## Disadvantages

- High setup and tuning complexity for GeoMesa
- Significant learning curve and new skill requirements
- Additional infrastructure components to manage (Kafka, GeoMesa, distributed storage)
- Overkill if batch updates are sufficient for requirements

## When to Consider

- Requirements for sub-minute data freshness
- High-frequency update patterns in Oracle
- Need for horizontal scalability beyond single-node GDAL processing
- Team has or can acquire Kafka and GeoMesa expertise

## Related Pages

- [[sdi-dp-integration-strategies]] — Alternative integration strategies
- [[sdi-regione-liguria]] — The source SDI system
- [[cloud-native-geospatial-workflow]] — Related cloud-native patterns