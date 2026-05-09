---
type: entity
title: Koop.js
created: 2026-04-04
updated: 2026-04-04
tags: [geospatial, framework, nodejs, provider]
related: [bill-dollins, duckdb, geoparquet, geoservices-rest-specification, cloud-native-geospatial-workflow]
sources: ["Producing GeoJSON from SQL (DuckDB Geoparquet).md"]
---
# Koop.js

Koop is an open-source Node.js framework for transforming geospatial data between formats and APIs. It uses a provider architecture where data sources can be connected to output formats like the [[GeoServices REST Specification]].

[[Bill Dollins]] is working on a Koop provider that uses [[DuckDB]] as a proxy layer to serve [[GeoParquet]] data through the GeoServices REST Specification. The provider would push column selections and WHERE clauses down to DuckDB for performance, acting as a pass-through layer.

Koop enables the bridging of cloud-native geospatial formats (like GeoParquet) with legacy systems that require feature services.