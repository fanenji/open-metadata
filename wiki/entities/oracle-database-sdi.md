---
type: entity
title: Oracle Database SDI
created: 2026-02-13
updated: 2026-02-13
tags: [sdi, oracle, database, geospatial]
related: [sdi-regione-liguria, geoscript-system, postgis-viscarto, legacy-geospatial-etl-pipeline]
sources: ["Integrazione SDI_DP_ Analisi e Proposte_ .md"]
---
# Oracle Database SDI

The Oracle database is the source management database for geospatial data within the SDI of Regione Liguria. It serves as the origin of data flows in both integration hypotheses.

## Role in Integration

- **Hypothesis 1**: Oracle → PostGIS (via Geoscript) → DP. Oracle data is first copied to PostGIS using existing procedures, then ingested into the DP.
- **Hypothesis 2**: Oracle → DP (directly from Geoscript). A parallel process in Geoscript writes data directly to the DP's object storage.

## Connection to Legacy Pipeline

The Oracle-to-PostGIS phase in Hypothesis 1 directly matches the existing [[oracle-to-postgresql-gdal-etl]] pattern documented in the wiki.