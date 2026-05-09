---
type: entity
title: Postholer
created: 2026-04-29
updated: 2026-04-29
tags: [organization, hiking, geospatial, cloud-native]
related: [scott-parks, cloud-optimized-geotiff-cog, flatgeobuf-fgb, serverless-geospatial-architecture, legacy-geospatial-etl-pipeline]
sources: ["How Postholer Went Serverless Using Cloud-Native Geospatial Data.md"]
---
# Postholer

A hiking resource founded by [[scott-parks]] that features interactive trail maps with 87 raster/vector layers. Postholer provides data on snow conditions, climate, weather, wildfires, fauna, and other topics relevant to hikers, particularly those on the Pacific Crest Trail.

## Architecture

Postholer's maps are built on a fully serverless architecture using [[cloud-optimized-geotiff-cog]] for raster data and [[flatgeobuf-fgb]] for vector data, served directly from S3 to a Leaflet-based web client. This replaced a traditional OGC tile server stack (PostgreSQL/PostGIS, MapServer, MapCache on EC2).

## Data Sources

- CDEC (California Data Exchange Center)
- SnoTEL (Snow Telemetry)
- SNODAS (Snow Data Assimilation System)
- Various climate, weather, and wildfire data sources