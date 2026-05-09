---
type: entity
title: Source Cooperative
created: 2026-04-04
updated: 2026-05-07
tags: [geospatial, data-hosting, platform, cloud-native, open-data]
related: [geoparquet, bill-dollins, geoparquet-ecosystem, geoparquet-data-providers, radiant-earth, cloud-native-geospatial-workflow]
sources: ["Producing GeoJSON from SQL (DuckDB Geoparquet).md", "The GeoParquet Ecosystem at 1.0.0.md"]
---
# Source Cooperative

Source Cooperative is an open data hosting platform for geospatial and other datasets, launched by [[Radiant Earth]]. It provides access to datasets in cloud-native formats like [[GeoParquet]] and has emerged as the central repository for cloud-native geospatial data. Many major data providers host their GeoParquet data on Source Cooperative.

## Key Features

- **Free hosting** for open geospatial data
- Supports **cloud-native formats** including GeoParquet, STAC, and COGs
- Provides **direct S3-compatible access** for efficient querying
- Emerging as the **de facto standard repository** for the GeoParquet ecosystem

## Datasets Hosted

Source Cooperative hosts a wide range of open geospatial datasets, including:

- Microsoft building footprints and STAC catalogs
- Planet RapidAI4EO STAC dataset
- Maxar Open Data STAC
- Ordnance Survey National Geographic Database Boundaries
- VIDA Google-Microsoft combined building footprints (also includes OSM building footprints)
- Streambatch ESA World Cereals dataset
- Chris Holmes' personal conversions (Google Buildings, Overture Maps, EuroCrops, NYC Taxi Zones)

## Usage

[[Bill Dollins]] used Source Cooperative to download the combined VIDA dataset of Google, Microsoft, and OSM building footprints for Ireland in GeoParquet 1.1.0 format for his DuckDB GeoJSON generation experiments.

## Relevance to Project

Source Cooperative is a potential hosting option for project geospatial datasets, offering free, cloud-native storage with efficient access patterns.