---
type: entity
title: GeoServices REST Specification
created: 2026-04-04
updated: 2026-04-04
tags: [geospatial, standard, esri, api]
related: [koop-js, bill-dollins, cloud-native-geospatial-workflow]
sources: ["Producing GeoJSON from SQL (DuckDB Geoparquet).md"]
---
# GeoServices REST Specification

The GeoServices REST Specification is ESRI's standard for exposing geospatial feature services over HTTP. It defines a RESTful API for querying, editing, and serving geographic features.

[[Bill Dollins]] is working toward building a [[Koop]] provider that serves [[GeoParquet]] data through this specification, using [[DuckDB]] as a proxy layer. This would enable cloud-native geospatial formats to be consumed by legacy systems that require GeoServices-compatible feature services.