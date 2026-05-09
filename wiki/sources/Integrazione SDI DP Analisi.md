---
type: source
title: Integrazione SDI DP Analisi
created: 2026-02-13
updated: 2026-02-13
tags: [sdi, data-platform, integration, geospatial, etl]
related: [sdi-regione-liguria, geoscript-etl-system, postgis-viscarto, sdi-dp-integration-strategies, raster-ingestion-cog-pipeline, geospatial-streaming-kafka-geomesa, legacy-geospatial-etl-pipeline, oracle-to-postgresql-gdal-etl, geospatial-etl-pipeline-iceberg, cloud-native-geospatial-workflow]
sources: ["Integrazione SDI DP Analisi.md"]
---
# Integrazione SDI DP Analisi

This document is a conversation output analyzing the integration of the existing Spatial Data Infrastructure (SDI) of Regione Liguria with the new Data Platform (DP). It describes the current Geoscript ETL system (Groovy/GDAL on Windows Server 2019), proposes two hypotheses for vector data ingestion (two-phase Oracle→PostGIS→DP and single-phase Oracle→DP via Geoscript), and outlines raster ingestion via GDAL→COG. The analysis evaluates trade-offs between reuse of existing processes, latency, orchestration complexity, and scalability. Alternative proposals include direct Oracle→Iceberg ingestion via Spark/Dremio, streaming geospatial with Kafka+GeoMesa, and serverless GDAL processing.

## Key Points

- The SDI and DP have overlapping ETL and analytical database functions, creating integration complexity.
- Hypothesis 1 (two-phase) reuses existing PostGIS processes but introduces latency and dual orchestration.
- Hypothesis 2 (single-phase) reduces latency but increases dependency on legacy Geoscript and requires full migration to Python/Ubuntu.
- Raster ingestion is straightforward but scalability-limited on a single VM.
- Alternative proposals (direct Iceberg, streaming, serverless) offer better scalability but require significant new development.

## Related Pages

- [[sdi-regione-liguria]] — The existing Spatial Data Infrastructure
- [[geoscript-etl-system]] — The legacy Groovy/GDAL ETL system
- [[postgis-viscarto]] — The PostGIS analytical database in SDI
- [[sdi-dp-integration-strategies]] — Comparison of integration hypotheses
- [[raster-ingestion-cog-pipeline]] — Raster ingestion pattern
- [[geospatial-streaming-kafka-geomesa]] — Streaming alternative
- [[legacy-geospatial-etl-pipeline]] — Related legacy pipeline documentation
- [[oracle-to-postgresql-gdal-etl]] — Related ETL workflow pattern
- [[geospatial-etl-pipeline-iceberg]] — Related Iceberg ingestion pattern
- [[cloud-native-geospatial-workflow]] — Related cloud-native workflow