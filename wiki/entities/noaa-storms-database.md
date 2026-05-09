---
type: entity
title: NOAA Historical Storms Database
created: 2026-05-07
updated: 2026-05-07
tags: [noaa, storms, geospatial, dataset, weather]
related: [postgis, duckdb, dbt, modern-geospatial-data-stack]
sources: ["spatial-sql-the-modern-data-stack-and-postgis.md"]
---
# NOAA Historical Storms Database

A publicly available dataset from the National Oceanic and Atmospheric Administration (NOAA) containing historical storm event data from 1950 to present. The dataset is hosted on an FTP server as multiple gzipped CSV files, one per year.

## Data Structure

The database contains three main "tables":
1. **Storm details** — Event type, location, start/end coordinates, dates
2. **Fatalities** — Information about storm-related deaths
3. **Storm events** — Detailed event narratives describing what happened

## Key Characteristics

- **Format**: Gzipped CSV files, one per year (1950–present, with some breaks)
- **Access**: FTP server, files updated regularly
- **Rich text data**: Event narratives provide detailed descriptions useful for text-based classification
- **Challenge**: Files are updated frequently (timestamps change), making manual tracking difficult

## Use in Modern Geospatial Stack

As demonstrated by [[Matt Forrest]] in his talk, this dataset is ideal for demonstrating the modern geospatial data stack:
1. DuckDB reads remote gzipped CSVs directly (auto-detects schema and compression)
2. PostgreSQL Full-Text Search classifies flash flood events from narratives
3. PostGIS performs spatial joins against FEMA flood zones
4. dbt automates the pipeline for regular updates

## Related

- [[postgis]] — Used for spatial analysis of storm data
- [[duckdb]] — Used for bulk CSV processing
- [[dbt]] — Used for pipeline automation